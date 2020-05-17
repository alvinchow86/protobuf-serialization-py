import pytest

from datetime import datetime, date
from enum import Enum
import json

from dateutil.tz import UTC

from protobuf_serialization.tests.compiled.example_pb2 import Foo, Bar, Parent, Child, Category, Coin
from protobuf_serialization.serialization import ProtobufSerializer, ProtobufDictSerializer, fields


class FooSerializer(ProtobufSerializer):
    protobuf_class = Foo

    id = fields.Field()
    name = fields.Field()
    content = fields.WrappedStrField()
    is_active = fields.WrappedField()
    count = fields.WrappedIntField()
    created_at = fields.DateTimeField()


class FooDictSerializer(ProtobufDictSerializer):
    protobuf_class = Foo

    name = fields.Field()
    content = fields.WrappedStrField()


class CategorySerializer(ProtobufSerializer):
    protobuf_class = Category
    name = fields.Field()
    type = fields.Field()


class ChildSerializer(ProtobufSerializer):
    protobuf_class = Child
    name = fields.Field()
    label = fields.WrappedField()
    category = fields.Nested(CategorySerializer)


class ParentSerializer(ProtobufSerializer):
    protobuf_class = Parent

    name = fields.Field()
    label = fields.WrappedField()
    child = fields.Nested(ChildSerializer)


class CoinSerializer(ProtobufSerializer):
    protobuf_class = Coin

    categories = fields.Nested(CategorySerializer, many=True)


class Model:
    def __init__(self, **fields):
        for k, v in fields.items():
            setattr(self, k, v)


def test_serializer_basic():
    id = 123
    name = 'Foo'
    content = 'stuff'
    is_active = True
    count = 501
    created_at = datetime(2019, 1, 1, 12, 0, tzinfo=UTC)

    instance = Model()
    instance.id = id
    instance.name = name
    instance.content = content
    instance.is_active = is_active
    instance.count = count
    instance.created_at = created_at

    foo_serializer = FooSerializer()
    proto = foo_serializer.dump(instance)
    assert proto.id == id
    assert proto.name == name
    assert proto.content.value == content
    assert proto.is_active.value == is_active
    assert proto.count.value == count
    assert proto.created_at.ToDatetime() == datetime(2019, 1, 1, 12, 0)

    # Check aliased
    proto2 = foo_serializer.serialize(instance)
    assert proto2 == proto

    # Check __repr__
    print(FooSerializer.name)


def test_dict_serializer():
    name = 'Foo'
    content = 'stuff'

    instance = dict(
        name=name,
        content=content,
    )

    foo_serializer = FooDictSerializer()
    proto = foo_serializer.dump(instance)
    assert proto.name == name
    assert proto.content.value == content


def test_optional_fields():
    child = Model(name='child', label='ch', category=Model(name='foo', type='bar'))
    parent = Model(name='parent', label='boss', child=child)
    serializer = ParentSerializer()

    # fields
    proto = serializer.dump(parent, fields=['name', 'label'])
    assert proto.name
    assert proto.label.value
    assert not proto.HasField('child')

    proto = serializer.dump(parent, fields=['name'])
    assert proto.name
    assert not proto.HasField('label')
    assert not proto.HasField('child')

    # exclude
    proto = serializer.dump(parent, exclude=['name'])
    assert proto.name == ''
    assert proto.label.value
    assert proto.HasField('child')


def test_serializer_default_fields():
    class FooSerializer(ProtobufSerializer):
        protobuf_class = Foo

        id = fields.Field()
        name = fields.Field()

        class Meta:
            default_fields = ('id',)

    foo = Model(id=1, name='foo', content='FOO')
    serializer = FooSerializer()
    result = serializer.dump(foo)
    assert result.id == 1
    assert not result.name

    # Override
    result = serializer.dump(foo, fields=('id', 'name'))
    assert result.id == 1
    assert result.name == 'foo'

    result = serializer.dump(foo, extra=('name',))
    assert result.id == 1
    assert result.name == 'foo'


def test_serializer_default_exclude_fields():
    class FooSerializer(ProtobufSerializer):
        protobuf_class = Foo

        id = fields.Field()
        name = fields.Field()

        class Meta:
            default_exclude_fields = ('name',)

    foo = Model(id=1, name='foo')
    serializer = FooSerializer()
    assert serializer._get_default_fields() == ('id',)
    result = serializer.dump(foo)
    assert result.id == 1
    assert not result.name

    # Override
    result = serializer.dump(foo, extra=('name',))
    assert result.id == 1
    assert result.name == 'foo'


def test_serialize_many():
    foos = [
        Model(id=1, name='foo', content='FOO'),
        Model(id=2, name='bar', content='BAR'),
    ]
    results = FooSerializer(allow_missing=True).dump(foos, many=True)
    assert len(results) == 2
    assert isinstance(results[0], Foo)
    assert results[0].id == 1
    assert results[0].name == 'foo'
    assert results[0].content.value == 'FOO'

    # Alternatively set many=True on serializer class
    results = FooSerializer(allow_missing=True, many=True).dump(foos)
    assert len(results) == 2


def test_nested_serializer():
    category = Model(name='cool', type='beans')
    child = Model(name='child', label='ok', category=category)
    parent = Model(name='parent', label='boss', child=child)

    parent_serializer = ParentSerializer()
    proto = parent_serializer.dump(parent)

    assert proto.name == 'parent'
    assert proto.child.name == 'child'
    assert proto.child.label.value == 'ok'
    assert proto.child.category.name == 'cool'

    # Test nested with missing
    parent = Model(name='parent')
    with pytest.raises(AttributeError):
        parent_serializer.dump(parent)


def test_nested_repeated_serializer():
    category1 = Model(name='foo', type='FOO')
    category2 = Model(name='bar', type='BAR')
    categories = [category1, category2]
    coin = Model(categories=categories)

    coin_serializer = CoinSerializer()
    proto = coin_serializer.dump(coin)
    assert len(proto.categories) == 2
    assert proto.categories[0].name == 'foo'
    assert proto.categories[0].type == 'FOO'
    assert proto.categories[1].name == 'bar'
    assert proto.categories[1].type == 'BAR'


def test_allow_missing():
    serializer = FooDictSerializer()
    with pytest.raises(KeyError):
        serializer.dump(dict(name='Foo'))

    proto = serializer.dump(dict(name='Foo'), allow_missing=True)
    assert proto.name == 'Foo'
    assert proto.content.value == ''

    serializer = FooDictSerializer(allow_missing=True)
    proto = serializer.dump(dict(name='Foo'))
    assert proto.name == 'Foo'
    assert proto.content.value == ''


def test_method_call():
    class FooModel:
        def name(self):
            return 'foo'

    instance = FooModel()

    class FooSerializer(ProtobufSerializer):
        protobuf_class = Foo
        name = fields.Field(call=True)

    foo_serializer = FooSerializer()
    proto = foo_serializer.dump(instance)
    assert proto.name == 'foo'


def test_date_field():
    instance = Model(birth_date=date(2010, 5, 15))

    class FooSerializer(ProtobufSerializer):
        protobuf_class = Foo
        content = fields.WrappedDateField(attr='birth_date')

    foo_serializer = FooSerializer()
    proto = foo_serializer.dump(instance)
    assert proto.content.value == '2010-05-15'


def test_enum_field():
    class Color(Enum):
        RED = 'red'
        BLUE = 'blue'

    instance = Model(content=Color.RED)

    class FooSerializer(ProtobufSerializer):
        protobuf_class = Foo
        content = fields.WrappedEnumField()

    foo_serializer = FooSerializer()
    proto = foo_serializer.dump(instance)
    assert proto.content.value == 'red'


def test_json_str_field():
    instance = Model(content=dict(a=1, b=2))

    class FooSerializer(ProtobufSerializer):
        protobuf_class = Foo
        content = fields.WrappedJSONStrField()

    foo_serializer = FooSerializer()
    proto = foo_serializer.dump(instance)
    assert json.loads(proto.content.value) == dict(a=1, b=2)


def test_dict_field():
    instance = Model(
        category=dict(name='Foo', type='bar')
    )

    class BarSerializer(ProtobufSerializer):
        protobuf_class = Bar
        category = fields.DictField(fields=('name', 'type'))

    bar_serializer = BarSerializer()
    proto = bar_serializer.dump(instance)
    assert proto.category.name == 'Foo'
    assert proto.category.type == 'bar'
