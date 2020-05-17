import logging
from google.protobuf.descriptor import FieldDescriptor

from protobuf_serialization.constants import VALUE_TYPES
from protobuf_serialization.serialization.serializer import ProtobufSerializer, ProtobufDictSerializer
from protobuf_serialization.serialization import fields


logger = logging.getLogger(__name__)


# Map of Protobuf message name (e.g. val_client.Customer) to ProtobufSerializer instance
# This is populated by _build_serializer_cls_for_proto_cls()
serializer_registry = {}


def serialize_to_protobuf(
    data, proto_cls, allow_missing=True, extra_proto_fields=None, for_dict=True, message_proto_map=None
):
    """
    Serializer a dict to protobuf. Constructs serializer class on the fly if needed.

    Usage:
    data = serialize_to_protobuf(foo, foo_pb2.Foo)
    """
    serializer = get_serializer_for_proto_cls(proto_cls, for_dict=for_dict, message_proto_map=message_proto_map)
    return serializer.dump(data, allow_missing=allow_missing, extra_proto_fields=extra_proto_fields)


def get_serializer_for_proto_cls(proto_cls, for_dict=True, message_proto_map=None):
    """
    Create a serializer on the fly given a protobuf class. If exists, get existing one.
    """
    message_name = proto_cls.DESCRIPTOR.full_name
    serializer = serializer_registry.get(message_name)
    if serializer:
        return serializer

    serializer_cls = _build_serializer_cls_for_proto_cls(
        proto_cls, for_dict=for_dict, message_proto_map=message_proto_map
    )

    serializer = serializer_cls(allow_missing=True)

    serializer_registry[message_name] = serializer
    return serializer


def _build_serializer_cls_for_proto_cls(proto_cls, for_dict=True, message_proto_map=None):
    serializer_name = f'{proto_cls.__name__}Serializer'

    attrs = dict(protobuf_class=proto_cls)

    fields_by_name = proto_cls.DESCRIPTOR.fields_by_name
    for name, field in fields_by_name.items():
        if field.type == FieldDescriptor.TYPE_MESSAGE:
            serializer_field = None
            type_name = field.message_type.full_name
            if type_name == 'google.protobuf.Timestamp':
                serializer_field = fields.DateTimeField()
            elif type_name in VALUE_TYPES:
                serializer_field = fields.WrappedField()
            elif message_proto_map:
                is_repeated = field.label == FieldDescriptor.LABEL_REPEATED
                proto_cls = message_proto_map.get(type_name)
                if proto_cls:
                    serializer = get_serializer_for_proto_cls(proto_cls, message_proto_map=message_proto_map)
                    serializer_field = fields.Nested(serializer=serializer, many=is_repeated)
                else:   # pragma: no cover
                    logger.debug('Not sure what to do with %s, not in message_proto_map', name)
            else:   # pragma: no cover
                logger.debug('Not sure what to do with %s', name)
            if serializer_field:
                attrs[name] = serializer_field

        else:
            serializer_field = fields.Field()
            attrs[name] = fields.Field()

    if for_dict:
        base_cls = ProtobufDictSerializer
    else:
        base_cls = ProtobufSerializer

    cls = type(
        serializer_name,
        (base_cls,),
        attrs,
    )

    return cls
