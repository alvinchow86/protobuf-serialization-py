from datetime import datetime

from dateutil.tz import UTC
from google.protobuf.wrappers_pb2 import StringValue
import pytest

from protobuf_serialization.tests.compiled.example_pb2 import Foo, Parent, Child, Coin, Category
from protobuf_serialization.utils import write_datetime_to_message
from protobuf_serialization.deserialization import protobuf_to_dict


@pytest.fixture
def foo():
    foo = Foo(
        id=123,
        name='val',
    )
    foo.content.value = 'crypto'
    foo.is_active.value = True
    foo.count.value = 501
    dt = datetime(2019, 1, 1, 12, 0, tzinfo=UTC)
    write_datetime_to_message(foo.created_at, dt)
    return foo


def test_protobuf_to_dict_basic():
    foo = Foo(
        id=123,
        name='val',
    )
    foo.content.value = 'crypto'
    foo.is_active.value = True
    foo.count.value = 501

    dt = datetime(2019, 1, 1, 12, 0, tzinfo=UTC)
    write_datetime_to_message(foo.created_at, dt)

    data = protobuf_to_dict(foo)

    assert data == dict(
        id=123,
        name='val',
        content='crypto',
        is_active=True,
        count=501,
        created_at=dt,
    )


def test_fields(foo):
    data = protobuf_to_dict(foo, fields=('id', 'content'))
    assert set(data.keys()) == {'id', 'content'}


def test_unset_wrapped_fields():
    # Test that None is returned for Wrapped fields that are unset
    foo = Foo(
        id=123,
        name='val',
    )
    data = protobuf_to_dict(foo)
    assert data == dict(
        id=123,
        name='val',
        content=None,
        is_active=None,
        count=None,
        created_at=None,
    )


def test_omit_keys_if_null():
    # Test omit_keys_if_null option
    foo = Foo(
        id=123,
        name='val',
    )
    data = protobuf_to_dict(foo, omit_keys_if_null=True)
    assert data == dict(
        id=123,
        name='val'
    )

    foo.content.value = 'stuff'
    data = protobuf_to_dict(foo, omit_keys_if_null=True)
    assert data == dict(
        id=123,
        name='val',
        content='stuff'
    )


def test_nested_deserialization():
    child = Child(name='child', label=StringValue(value='small'))
    parent = Parent(name='parent', label=StringValue(value='big'), child=child)

    data = protobuf_to_dict(parent)
    assert data == dict(
        name='parent',
        label='big',
        child=dict(
            name='child',
            label='small',
            category=None,
        )
    )


def test_advanced_fields():
    coin = Coin()
    data = protobuf_to_dict(coin)

    assert data == dict(
        tags={},
        names=[],
        categories=[],
    )

    coin.tags['USD'] = 'TUSD'
    coin.tags['HKD'] = 'THKD'
    coin.names.append('alpha')
    coin.names.append('beta')
    cat1 = Category(name='foo', type='cool')
    cat2 = Category(name='bar', type='lame')
    coin.categories.extend([cat1, cat2])

    data = protobuf_to_dict(coin)

    assert data == dict(
        tags=dict(USD='TUSD', HKD='THKD'),
        names=['alpha', 'beta'],
        categories=[
            dict(name='foo', type='cool'),
            dict(name='bar', type='lame'),
        ]
    )
