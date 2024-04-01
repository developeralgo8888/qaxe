# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: coms.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='coms.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ncoms.proto\"0\n\x08QRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\n\n\x02op\x18\x02 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"4\n\tQResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05\x65rror\x18\x02 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"9\n\x08QControl\x12\x11\n\tstate_1v2\x18\x01 \x01(\x05\x12\x0c\n\x04pwm1\x18\x02 \x01(\x05\x12\x0c\n\x04pwm2\x18\x03 \x01(\x05\"9\n\x06QState\x12\x11\n\tpgood_1v2\x18\x01 \x01(\x05\x12\r\n\x05temp1\x18\x02 \x01(\x05\x12\r\n\x05temp2\x18\x03 \x01(\x05\x62\x06proto3'
)




_QREQUEST = _descriptor.Descriptor(
  name='QRequest',
  full_name='QRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='QRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='op', full_name='QRequest.op', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='QRequest.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=14,
  serialized_end=62,
)


_QRESPONSE = _descriptor.Descriptor(
  name='QResponse',
  full_name='QResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='QResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='QResponse.error', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='QResponse.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=64,
  serialized_end=116,
)


_QCONTROL = _descriptor.Descriptor(
  name='QControl',
  full_name='QControl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state_1v2', full_name='QControl.state_1v2', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pwm1', full_name='QControl.pwm1', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pwm2', full_name='QControl.pwm2', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=118,
  serialized_end=175,
)


_QSTATE = _descriptor.Descriptor(
  name='QState',
  full_name='QState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pgood_1v2', full_name='QState.pgood_1v2', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='temp1', full_name='QState.temp1', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='temp2', full_name='QState.temp2', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=177,
  serialized_end=234,
)

DESCRIPTOR.message_types_by_name['QRequest'] = _QREQUEST
DESCRIPTOR.message_types_by_name['QResponse'] = _QRESPONSE
DESCRIPTOR.message_types_by_name['QControl'] = _QCONTROL
DESCRIPTOR.message_types_by_name['QState'] = _QSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QRequest = _reflection.GeneratedProtocolMessageType('QRequest', (_message.Message,), {
  'DESCRIPTOR' : _QREQUEST,
  '__module__' : 'coms_pb2'
  # @@protoc_insertion_point(class_scope:QRequest)
  })
_sym_db.RegisterMessage(QRequest)

QResponse = _reflection.GeneratedProtocolMessageType('QResponse', (_message.Message,), {
  'DESCRIPTOR' : _QRESPONSE,
  '__module__' : 'coms_pb2'
  # @@protoc_insertion_point(class_scope:QResponse)
  })
_sym_db.RegisterMessage(QResponse)

QControl = _reflection.GeneratedProtocolMessageType('QControl', (_message.Message,), {
  'DESCRIPTOR' : _QCONTROL,
  '__module__' : 'coms_pb2'
  # @@protoc_insertion_point(class_scope:QControl)
  })
_sym_db.RegisterMessage(QControl)

QState = _reflection.GeneratedProtocolMessageType('QState', (_message.Message,), {
  'DESCRIPTOR' : _QSTATE,
  '__module__' : 'coms_pb2'
  # @@protoc_insertion_point(class_scope:QState)
  })
_sym_db.RegisterMessage(QState)


# @@protoc_insertion_point(module_scope)
