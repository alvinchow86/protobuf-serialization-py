# Protobuf Serialization Tools for Python

Utils to help with serialization and deserialization of Python objects into protobuf3 (e.g. for your gRPC application). Inspired by serialization libraries like marshmallow, Django rest Framework and serpy, but for protobuf3 instead of JSON.

While the Python protobuf library already has a class-based infrastructure, it can be very awkward to use, and there are a lot of operations you are restricted from doing. This library uses a familiar class-based "serializer" interface to make it easy to define how you'd like to map a Python object (such as a Django or SQLAlchemy model instance) or a source dictionary to an output, which in this case is a Python protobuf instance (rather than a dictionary object).

```
pip install protobuf-serialization
```

## Features
- Written for high serialization performance
- Uses Google's wrapper types to support "nullable" values
- Field types for common types (string, int, enum, date, datetime, JSON string)
- Supports nesting

## Examples
### Serializer Usage

```python
from protobuf_serialization.tests.compiled.example_pb2 import Foo

class FooSerializer(ProtobufSerializer):
    protobuf_class = Foo

    id = fields.Field()
    name = fields.Field()
    content = fields.WrappedStrField()
    is_active = fields.WrappedField()
    count = fields.WrappedIntField()
    created_at = fields.DateTimeField()

foo_serializer = FooSerializer()
proto = foo_serializer.dump(instance)
```

[![CircleCI](https://circleci.com/gh/alvinchow86/protobuf-serialization-py.svg?style=svg)](https://circleci.com/gh/alvinchow86/protobuf-serialization-py)
