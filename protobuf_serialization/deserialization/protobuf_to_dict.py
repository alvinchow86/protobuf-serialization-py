from google.protobuf.descriptor import FieldDescriptor

from protobuf_serialization.constants import VALUE_TYPES
from protobuf_serialization.deserialization.utils import proto_timestamp_to_datetime


def protobuf_to_dict(proto, dict_cls=dict, omit_keys_if_null=False, fields=None):
    if fields:
        fields = set(fields)

    result = dict_cls()
    fields_by_name = proto.DESCRIPTOR.fields_by_name
    for name, field in fields_by_name.items():
        if fields and name not in fields:
            continue

        if field.type == FieldDescriptor.TYPE_MESSAGE:
            if _is_map_field(field):
                # Map types have to be handled differently, HasField won't work.
                # For now treat as dict, which handles string->string ok
                value = dict(getattr(proto, name))
            elif field.label == FieldDescriptor.LABEL_REPEATED:
                # Run this after the map check, since map fields also have LABEL_REPEATED..
                raw_values = getattr(proto, name)
                value = [
                    convert_message_type(
                        raw_value, field.message_type.full_name,
                        extra_args=dict(omit_keys_if_null=omit_keys_if_null, dict_cls=dict_cls)
                    ) for raw_value in raw_values
                ]
            elif proto.HasField(name):
                # This only works for singular (non-repeated), non-map types
                raw_value = getattr(proto, name)
                value = convert_message_type(
                    raw_value, field.message_type.full_name,
                    extra_args=dict(omit_keys_if_null=omit_keys_if_null, dict_cls=dict_cls)
                )
            else:
                value = None
        else:
            value = getattr(proto, name)

        if not (omit_keys_if_null and value is None):
            result[name] = value

    return result


def _is_map_field(field):
    """
    Detection logic borrowed from https://github.com/kaporzhu/protobuf-to-dict/blob/master/protobuf_to_dict/convertor.py
    """
    return (
        field.type == FieldDescriptor.TYPE_MESSAGE and
        field.message_type.has_options and
        field.message_type.GetOptions().map_entry
    )


def convert_message_type(value, type_name, extra_args=None):
    extra_args = extra_args or {}

    # Assume value is not None
    if type_name == 'google.protobuf.Timestamp':
        return proto_timestamp_to_datetime(value)
    elif type_name in VALUE_TYPES:
        return value.value
    else:
        return protobuf_to_dict(value, **extra_args)
