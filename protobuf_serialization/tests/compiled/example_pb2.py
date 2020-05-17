# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='example.proto',
  package='example',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rexample.proto\x12\x07\x65xample\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\x1b\n\nFooRequest\x12\r\n\x05value\x18\x01 \x01(\t\"\xda\x01\n\x03\x46oo\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12-\n\x07\x63ontent\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\tis_active\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12+\n\x05\x63ount\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x90\x01\n\x04\x43oin\x12%\n\x04tags\x18\x01 \x03(\x0b\x32\x17.example.Coin.TagsEntry\x12\r\n\x05names\x18\x02 \x03(\t\x12%\n\ncategories\x18\x03 \x03(\x0b\x32\x11.example.Category\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"b\n\x06Parent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\x05label\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x1d\n\x05\x63hild\x18\x03 \x01(\x0b\x32\x0e.example.Child\"g\n\x05\x43hild\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\x05label\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12#\n\x08\x63\x61tegory\x18\x03 \x01(\x0b\x32\x11.example.Category\"*\n\x03\x42\x61r\x12#\n\x08\x63\x61tegory\x18\x01 \x01(\x0b\x32\x11.example.Category\"&\n\x08\x43\x61tegory\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t2\xec\x01\n\x06\x46ooApi\x12+\n\x06GetFoo\x12\x13.example.FooRequest\x1a\x0c.example.Foo\x12:\n\x13GetFooRequestStream\x12\x13.example.FooRequest\x1a\x0c.example.Foo(\x01\x12;\n\x14GetFooResponseStream\x12\x13.example.FooRequest\x1a\x0c.example.Foo0\x01\x12<\n\x13GetFooBidirectional\x12\x13.example.FooRequest\x1a\x0c.example.Foo(\x01\x30\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_FOOREQUEST = _descriptor.Descriptor(
  name='FooRequest',
  full_name='example.FooRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='example.FooRequest.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=118,
)


_FOO = _descriptor.Descriptor(
  name='Foo',
  full_name='example.Foo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='example.Foo.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='example.Foo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='example.Foo.content', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_active', full_name='example.Foo.is_active', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='example.Foo.count', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='example.Foo.created_at', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=339,
)


_COIN_TAGSENTRY = _descriptor.Descriptor(
  name='TagsEntry',
  full_name='example.Coin.TagsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='example.Coin.TagsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='example.Coin.TagsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=443,
  serialized_end=486,
)

_COIN = _descriptor.Descriptor(
  name='Coin',
  full_name='example.Coin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tags', full_name='example.Coin.tags', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='names', full_name='example.Coin.names', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='categories', full_name='example.Coin.categories', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COIN_TAGSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=342,
  serialized_end=486,
)


_PARENT = _descriptor.Descriptor(
  name='Parent',
  full_name='example.Parent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='example.Parent.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='example.Parent.label', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='child', full_name='example.Parent.child', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=488,
  serialized_end=586,
)


_CHILD = _descriptor.Descriptor(
  name='Child',
  full_name='example.Child',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='example.Child.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='example.Child.label', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='example.Child.category', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=588,
  serialized_end=691,
)


_BAR = _descriptor.Descriptor(
  name='Bar',
  full_name='example.Bar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='category', full_name='example.Bar.category', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=693,
  serialized_end=735,
)


_CATEGORY = _descriptor.Descriptor(
  name='Category',
  full_name='example.Category',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='example.Category.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='example.Category.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=737,
  serialized_end=775,
)

_FOO.fields_by_name['content'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_FOO.fields_by_name['is_active'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_FOO.fields_by_name['count'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT64VALUE
_FOO.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_COIN_TAGSENTRY.containing_type = _COIN
_COIN.fields_by_name['tags'].message_type = _COIN_TAGSENTRY
_COIN.fields_by_name['categories'].message_type = _CATEGORY
_PARENT.fields_by_name['label'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_PARENT.fields_by_name['child'].message_type = _CHILD
_CHILD.fields_by_name['label'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CHILD.fields_by_name['category'].message_type = _CATEGORY
_BAR.fields_by_name['category'].message_type = _CATEGORY
DESCRIPTOR.message_types_by_name['FooRequest'] = _FOOREQUEST
DESCRIPTOR.message_types_by_name['Foo'] = _FOO
DESCRIPTOR.message_types_by_name['Coin'] = _COIN
DESCRIPTOR.message_types_by_name['Parent'] = _PARENT
DESCRIPTOR.message_types_by_name['Child'] = _CHILD
DESCRIPTOR.message_types_by_name['Bar'] = _BAR
DESCRIPTOR.message_types_by_name['Category'] = _CATEGORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FooRequest = _reflection.GeneratedProtocolMessageType('FooRequest', (_message.Message,), {
  'DESCRIPTOR' : _FOOREQUEST,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.FooRequest)
  })
_sym_db.RegisterMessage(FooRequest)

Foo = _reflection.GeneratedProtocolMessageType('Foo', (_message.Message,), {
  'DESCRIPTOR' : _FOO,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.Foo)
  })
_sym_db.RegisterMessage(Foo)

Coin = _reflection.GeneratedProtocolMessageType('Coin', (_message.Message,), {

  'TagsEntry' : _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), {
    'DESCRIPTOR' : _COIN_TAGSENTRY,
    '__module__' : 'example_pb2'
    # @@protoc_insertion_point(class_scope:example.Coin.TagsEntry)
    })
  ,
  'DESCRIPTOR' : _COIN,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.Coin)
  })
_sym_db.RegisterMessage(Coin)
_sym_db.RegisterMessage(Coin.TagsEntry)

Parent = _reflection.GeneratedProtocolMessageType('Parent', (_message.Message,), {
  'DESCRIPTOR' : _PARENT,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.Parent)
  })
_sym_db.RegisterMessage(Parent)

Child = _reflection.GeneratedProtocolMessageType('Child', (_message.Message,), {
  'DESCRIPTOR' : _CHILD,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.Child)
  })
_sym_db.RegisterMessage(Child)

Bar = _reflection.GeneratedProtocolMessageType('Bar', (_message.Message,), {
  'DESCRIPTOR' : _BAR,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.Bar)
  })
_sym_db.RegisterMessage(Bar)

Category = _reflection.GeneratedProtocolMessageType('Category', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORY,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.Category)
  })
_sym_db.RegisterMessage(Category)


_COIN_TAGSENTRY._options = None

_FOOAPI = _descriptor.ServiceDescriptor(
  name='FooApi',
  full_name='example.FooApi',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=778,
  serialized_end=1014,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFoo',
    full_name='example.FooApi.GetFoo',
    index=0,
    containing_service=None,
    input_type=_FOOREQUEST,
    output_type=_FOO,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetFooRequestStream',
    full_name='example.FooApi.GetFooRequestStream',
    index=1,
    containing_service=None,
    input_type=_FOOREQUEST,
    output_type=_FOO,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetFooResponseStream',
    full_name='example.FooApi.GetFooResponseStream',
    index=2,
    containing_service=None,
    input_type=_FOOREQUEST,
    output_type=_FOO,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetFooBidirectional',
    full_name='example.FooApi.GetFooBidirectional',
    index=3,
    containing_service=None,
    input_type=_FOOREQUEST,
    output_type=_FOO,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FOOAPI)

DESCRIPTOR.services_by_name['FooApi'] = _FOOAPI

# @@protoc_insertion_point(module_scope)
