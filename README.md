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
- Supports nested serializers
- Allows defining custom fields
- Convenience functions for serialization and deserialization 

## Usage
The core base class for the serializer is `ProtobufSerializer`. There is also `ProtobufDictSerializer` to handle dict-like objects instead.

This library also comes with a cool utility called `serialize_to_protobuf()`, which will basically take a dictionary and output a protobuf. Underneath the hood it will introspect the protobuf class and dynamically generate a `ProtobufSerializer`

There is also a function `protobuf_to_dict()` which does the reverse operation - it takes a protobuf and turns it into a dict. It's similar to https://github.com/kaporzhu/protobuf-to-dict but with some simplications, plus some better support for things like datetimes.

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

### `serialize_to_protobuf`

```python
from protobuf_serialization.tests.compiled.example_pb2 import Foo
source = dict(
    id=1,
    name='val',
    content='stuff',
    is_active=True,
    count=12,
    created_at=created_at
)
data = serialize_to_protobuf(source, Foo)
```

[![CircleCI](https://circleci.com/gh/alvinchow86/protobuf-serialization-py.svg?style=svg)](https://circleci.com/gh/alvinchow86/protobuf-serialization-py)
