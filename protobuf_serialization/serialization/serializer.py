from protobuf_serialization.serialization.fields import BaseField, Field, Nested
import operator


def _compile_field_to_tuple(field, name, serializer_cls=None):
    getter = field.get_getter(default_getter=serializer_cls.default_getter)
    format_value = field.format_value
    write_value = field.write_value

    return (name, getter, format_value, write_value)


def _compile_nested_field_to_tuple(field, name, serializer_cls=None):
    getter = field.get_getter(default_getter=serializer_cls.default_getter)

    serialize_value = field.get_serialize_func()
    return (name, getter, serialize_value)


class DefaultMeta:
    default_fields = None
    default_exclude_fields = None    # shorter way, exclude some fields by default


class ProtobufSerializerMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # TODO get superclass fields
        field_map = {}
        nested_field_map = {}
        field_names = []

        for key, val in attrs.items():
            if isinstance(val, BaseField):
                val._set_name(key)
                if isinstance(val, Nested):
                    nested_field_map[key] = val
                elif isinstance(val, Field):
                    field_map[key] = val
                field_names.append(key)

        if 'Meta' not in attrs:
            attrs['Meta'] = DefaultMeta

        # Make sure Meta has fields
        Meta = attrs['Meta']
        if not hasattr(Meta, 'default_fields'):
            Meta.default_fields = None
        if not hasattr(Meta, 'default_exclude_fields'):
            Meta.default_exclude_fields = None

        serializer_cls = super().__new__(cls, name, bases, attrs)

        compiled_fields = tuple(
            cls._compile_fields(field_map, serializer_cls)
        )
        compiled_nested_fields = tuple(
            cls._compile_nested_fields(nested_field_map, serializer_cls)
        )

        serializer_cls._field_map = field_map
        serializer_cls._nested_field_map = nested_field_map
        serializer_cls._compiled_fields = compiled_fields
        serializer_cls._compiled_nested_fields = compiled_nested_fields
        serializer_cls._field_names = field_names

        return serializer_cls

    @staticmethod
    def _compile_fields(fields, serializer_cls):
        field_tuples = []
        for (name, field) in fields.items():
            field_tuple = _compile_field_to_tuple(
                field, name, serializer_cls=serializer_cls
            )
            field_tuples.append(field_tuple)

        return field_tuples

    @staticmethod
    def _compile_nested_fields(fields, serializer_cls):
        field_tuples = []
        for (name, field) in fields.items():
            field_tuple = _compile_nested_field_to_tuple(
                field, name, serializer_cls=serializer_cls
            )
            field_tuples.append(field_tuple)

        return field_tuples


class ProtobufSerializer(metaclass=ProtobufSerializerMetaclass):
    default_getter = operator.attrgetter

    def __init__(self, allow_missing=False, many=False):
        """
        - allow_missing: Don't raise error if field does not exist on source
        """
        self.allow_missing = allow_missing
        self.many = many

    def serialize(
        self, instance, many=None, allow_missing=None,
        fields=None, exclude=None, extra=None, extra_proto_fields=None
    ):
        """
        - fields: only serialize these fields
        - exclude: exclude these fields
        - extra_proto_fields is to pass in additional stuff on Proto initialization. mainly for message fields
        """
        if many is None:
            many = self.many

        if allow_missing is None:
            allow_missing = self.allow_missing

        exclude = exclude or ()

        # Optionally, filter the list of fields to serialize
        default_fields = self._get_default_fields()
        filtered = bool(fields or exclude or default_fields)
        if filtered:
            if fields:
                field_names = fields
            elif default_fields:
                if extra:
                    field_names = list(default_fields) + list(extra)
                else:
                    field_names = default_fields
            else:
                field_names = self._field_names

            if exclude:
                field_names = [f for f in field_names if (f not in exclude)]

            # Filter fields
            compiled_fields = [
                (name, *rest) for (name, *rest) in self._compiled_fields if (name in field_names)
            ]
            compiled_nested_fields = [
                (name, *rest) for (name, *rest) in self._compiled_nested_fields if (name in field_names)
            ]
        else:
            compiled_fields = self._compiled_fields
            compiled_nested_fields = self._compiled_nested_fields

        common_args = dict(
            allow_missing=allow_missing,
            compiled_fields=compiled_fields,
            compiled_nested_fields=compiled_nested_fields,
            protobuf_class=self.protobuf_class,
            extra_proto_fields=extra_proto_fields,
        )

        if many:
            serialize_single = self._serialize_single
            instances = instance
            results = [serialize_single(inst, **common_args) for inst in instances]
            return results
        else:
            return self._serialize_single(instance, **common_args)

    def _serialize_single(
        self, instance, compiled_fields, compiled_nested_fields, protobuf_class,
        allow_missing=False, extra_proto_fields=None
    ):
        """
        We pass in all of the arguments to avoid repeated '.' lookups
        - extra_proto_fields: dict of additional protos.
        """
        extra_proto_fields = extra_proto_fields or {}

        for (name, getter, serialize_value) in compiled_nested_fields:
            value = None
            try:
                value = getter(instance)
            except (AttributeError, KeyError):
                if not allow_missing:
                    raise
            if value is not None:
                value = serialize_value(value)
                extra_proto_fields[name] = value

        proto = protobuf_class(**extra_proto_fields)

        for (name, getter, format_value, write_value) in compiled_fields:
            value = None
            try:
                value = getter(instance)
            except (AttributeError, KeyError):
                if not allow_missing:
                    raise

            if value is not None:
                value = format_value(value)
                write_value(proto, name, value)

        return proto

    def dump(self, instance, **kwargs):
        # Alias
        return self.serialize(instance, **kwargs)

    def _get_default_fields(self):
        default_exclude_fields = self.Meta.default_exclude_fields
        if default_exclude_fields:
            default_fields = tuple(set(self._field_names) - set(default_exclude_fields))
            return default_fields

        return self.Meta.default_fields


class ProtobufDictSerializer(ProtobufSerializer):
    default_getter = operator.itemgetter
