import json
import operator
import inspect
import functools

from protobuf_serialization.utils import write_datetime_to_message


class BaseField:
    def __init__(self, attr=None, call=False):
        self.name = None     # should be set by metaclass
        self.attr = attr     # specify another path to call
        self.call = call     # call a method on instance instead

    def get_getter(self, default_getter=operator.attrgetter):
        attr_name = self.attr or self.name
        if self.call:
            return operator.methodcaller(attr_name)
        else:
            return default_getter(attr_name)

    def _set_name(self, name):
        self.name = name

    def __repr__(self):
        return f"<Field('{self.name}')>"


class Field(BaseField):
    def write_value(self, proto, name, value):
        setattr(proto, name, value)

    # Use staticmethods to override
    def format_value(self, value):
        return value


class Nested(BaseField):
    def __init__(self, serializer=None, many=False, **kwargs):
        super().__init__(**kwargs)
        self.many = many

        if inspect.isclass(serializer):
            # If serializer is a class, then instantiate it
            serializer = serializer()

        self.serializer = serializer

    def get_serialize_func(self):
        if self.many:
            return functools.partial(self.serializer.serialize, many=True)
        else:
            return self.serializer.serialize


class StrMixin:
    format_value = staticmethod(str)


class IntMixin:
    format_value = staticmethod(int)


class EnumMixin:
    @staticmethod
    def format_value(value):
        return value.value


class DateMixin(StrMixin):
    @staticmethod
    def format_value(value):
        return value.isoformat()


class JSONStrMixin:
    """
    Handle fields that are Strings but source is JSON
    """
    @staticmethod
    def format_value(value):
        return json.dumps(value)


class WrappedField(Field):
    @staticmethod
    def write_value(proto, name, value):
        message = getattr(proto, name)
        setattr(message, 'value', value)


class DateTimeField(Field):
    @staticmethod
    def write_value(proto, name, value):
        message = getattr(proto, name)
        write_datetime_to_message(message, value)


class DictField(Field):
    def __init__(self, fields, *args, **kwargs):
        self.fields = fields
        super().__init__(*args, **kwargs)

    def write_value(self, proto, name, value):
        message = getattr(proto, name)
        for field in self.fields:
            val = value.get(field)
            if val is not None:
                setattr(message, field, val)


class WrappedStrField(StrMixin, WrappedField):
    pass


class WrappedIntField(IntMixin, WrappedField):
    pass


class WrappedEnumField(EnumMixin, WrappedField):
    pass


class WrappedDecimalField(StrMixin, WrappedField):
    pass


class WrappedJSONStrField(JSONStrMixin, WrappedField):
    pass


class WrappedDateField(DateMixin, WrappedField):
    pass
