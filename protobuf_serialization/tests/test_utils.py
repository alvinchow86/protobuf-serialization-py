from protobuf_serialization.utils import create_message_proto_map
from protobuf_serialization.tests.compiled import example_pb2


def test_message_proto_map():
    message_proto_map = create_message_proto_map(package_paths=['protobuf_serialization.tests.compiled'])
    assert message_proto_map['example.Foo'] == example_pb2.Foo
    assert message_proto_map['example.Coin'] == example_pb2.Coin
