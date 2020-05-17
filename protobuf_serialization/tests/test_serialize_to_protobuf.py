from typing import Optional
from dataclasses import dataclass
import functools

import pytest
from protobuf_serialization.tests.utils import utcnow

from protobuf_serialization.tests.compiled.example_pb2 import Foo, Parent, Coin
from protobuf_serialization.serialization.auto import serialize_to_protobuf as _serialize_to_protobuf
from protobuf_serialization.serialization import auto
from protobuf_serialization.deserialization import proto_timestamp_to_datetime, protobuf_to_dict
from protobuf_serialization.utils import create_message_proto_map


@pytest.fixture(autouse=True)
def reset_serializer_registry():
    auto.serializer_registry = {}
    yield


message_proto_map = create_message_proto_map(
    package_paths=['protobuf_serialization.tests.compiled']
)

serialize_to_protobuf = functools.partial(
    _serialize_to_protobuf, message_proto_map=message_proto_map
)


def test_serialize_to_protobuf(mocker):
    build_serializer_cls_spy = mocker.spy(auto, '_build_serializer_cls_for_proto_cls')
    assert len(auto.serializer_registry) == 0
    created_at = utcnow()
    source = dict(
        id=1,
        name='val',
        content='stuff',
        is_active=True,
        count=12,
        created_at=created_at
    )

    data = serialize_to_protobuf(source, Foo)

    assert len(auto.serializer_registry) == 1
    assert 'example.Foo' in auto.serializer_registry

    assert isinstance(data, Foo)
    assert data.id == 1
    assert data.name == 'val'
    assert data.content.value == 'stuff'
    assert data.is_active.value is True
    assert data.count.value == 12
    assert proto_timestamp_to_datetime(data.created_at) == created_at

    # Cool little serialization -> deserialization check
    assert protobuf_to_dict(data) == source

    data2 = serialize_to_protobuf(source, Foo)

    assert data2 == data

    assert len(auto.serializer_registry) == 1

    assert build_serializer_cls_spy.call_count == 1


def test_serialize_to_protobuf_nodict():

    @dataclass
    class FooData:
        id: Optional[int] = None
        name: Optional[str] = None
        content: Optional[str] = None

    foo = FooData(id=1, name='val', content='stuff')

    data = serialize_to_protobuf(foo, Foo, for_dict=False)
    assert data.id == 1
    assert data.name == 'val'
    assert data.content.value == 'stuff'


def test_serialize_to_protobuf_nested():
    parent = dict(
        name='parent',
        child=dict(
            name='child',
            label='trust',
            category=dict(
                name='foo',
                type='bar',
            )
        )
    )

    data = serialize_to_protobuf(parent, Parent)
    assert data.name == 'parent'
    assert data.child.name == 'child'
    assert data.child.label.value == 'trust'
    assert data.child.category.name == 'foo'
    assert data.child.category.type == 'bar'


def test_serialize_to_protobuf_nested_repeated():
    coin = dict(
        categories=[
            dict(name='foo', type='FOO'),
            dict(name='bar', type='BAR'),
        ]
    )
    proto = serialize_to_protobuf(coin, Coin)
    assert len(proto.categories) == 2
    assert proto.categories[0].name == 'foo'
    assert proto.categories[0].type == 'FOO'
    assert proto.categories[1].name == 'bar'
    assert proto.categories[1].type == 'BAR'
