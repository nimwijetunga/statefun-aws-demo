# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/inventory.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf/inventory.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18protobuf/inventory.proto\"\x1f\n\x0bRequestItem\x12\x10\n\x08quantity\x18\x01 \x01(\x05\",\n\x0cItemReserved\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x05\"/\n\x0fItemUnavailable\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x05\"\x1c\n\x08Reserved\x12\x10\n\x08quantity\x18\x01 \x01(\x05\"\x1b\n\x07InStock\x12\x10\n\x08quantity\x18\x01 \x01(\x05\x62\x06proto3')
)




_REQUESTITEM = _descriptor.Descriptor(
  name='RequestItem',
  full_name='RequestItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quantity', full_name='RequestItem.quantity', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=28,
  serialized_end=59,
)


_ITEMRESERVED = _descriptor.Descriptor(
  name='ItemReserved',
  full_name='ItemReserved',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ItemReserved.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='ItemReserved.quantity', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=61,
  serialized_end=105,
)


_ITEMUNAVAILABLE = _descriptor.Descriptor(
  name='ItemUnavailable',
  full_name='ItemUnavailable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ItemUnavailable.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='ItemUnavailable.quantity', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=107,
  serialized_end=154,
)


_RESERVED = _descriptor.Descriptor(
  name='Reserved',
  full_name='Reserved',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quantity', full_name='Reserved.quantity', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=156,
  serialized_end=184,
)


_INSTOCK = _descriptor.Descriptor(
  name='InStock',
  full_name='InStock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quantity', full_name='InStock.quantity', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=186,
  serialized_end=213,
)

DESCRIPTOR.message_types_by_name['RequestItem'] = _REQUESTITEM
DESCRIPTOR.message_types_by_name['ItemReserved'] = _ITEMRESERVED
DESCRIPTOR.message_types_by_name['ItemUnavailable'] = _ITEMUNAVAILABLE
DESCRIPTOR.message_types_by_name['Reserved'] = _RESERVED
DESCRIPTOR.message_types_by_name['InStock'] = _INSTOCK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestItem = _reflection.GeneratedProtocolMessageType('RequestItem', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTITEM,
  __module__ = 'protobuf.inventory_pb2'
  # @@protoc_insertion_point(class_scope:RequestItem)
  ))
_sym_db.RegisterMessage(RequestItem)

ItemReserved = _reflection.GeneratedProtocolMessageType('ItemReserved', (_message.Message,), dict(
  DESCRIPTOR = _ITEMRESERVED,
  __module__ = 'protobuf.inventory_pb2'
  # @@protoc_insertion_point(class_scope:ItemReserved)
  ))
_sym_db.RegisterMessage(ItemReserved)

ItemUnavailable = _reflection.GeneratedProtocolMessageType('ItemUnavailable', (_message.Message,), dict(
  DESCRIPTOR = _ITEMUNAVAILABLE,
  __module__ = 'protobuf.inventory_pb2'
  # @@protoc_insertion_point(class_scope:ItemUnavailable)
  ))
_sym_db.RegisterMessage(ItemUnavailable)

Reserved = _reflection.GeneratedProtocolMessageType('Reserved', (_message.Message,), dict(
  DESCRIPTOR = _RESERVED,
  __module__ = 'protobuf.inventory_pb2'
  # @@protoc_insertion_point(class_scope:Reserved)
  ))
_sym_db.RegisterMessage(Reserved)

InStock = _reflection.GeneratedProtocolMessageType('InStock', (_message.Message,), dict(
  DESCRIPTOR = _INSTOCK,
  __module__ = 'protobuf.inventory_pb2'
  # @@protoc_insertion_point(class_scope:InStock)
  ))
_sym_db.RegisterMessage(InStock)


# @@protoc_insertion_point(module_scope)
