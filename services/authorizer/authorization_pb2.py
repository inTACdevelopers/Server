# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: authorization.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x61uthorization.proto\x12\rauthorization\"0\n\rSingUpRequest\x12\r\n\x05login\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"-\n\x0eSingUpResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05state\x18\x02 \x01(\t2S\n\nauthorizer\x12\x45\n\x06SingUp\x12\x1c.authorization.SingUpRequest\x1a\x1d.authorization.SingUpResponseb\x06proto3')



_SINGUPREQUEST = DESCRIPTOR.message_types_by_name['SingUpRequest']
_SINGUPRESPONSE = DESCRIPTOR.message_types_by_name['SingUpResponse']
SingUpRequest = _reflection.GeneratedProtocolMessageType('SingUpRequest', (_message.Message,), {
  'DESCRIPTOR' : _SINGUPREQUEST,
  '__module__' : 'authorization_pb2'
  # @@protoc_insertion_point(class_scope:authorization.SingUpRequest)
  })
_sym_db.RegisterMessage(SingUpRequest)

SingUpResponse = _reflection.GeneratedProtocolMessageType('SingUpResponse', (_message.Message,), {
  'DESCRIPTOR' : _SINGUPRESPONSE,
  '__module__' : 'authorization_pb2'
  # @@protoc_insertion_point(class_scope:authorization.SingUpResponse)
  })
_sym_db.RegisterMessage(SingUpResponse)

_AUTHORIZER = DESCRIPTOR.services_by_name['authorizer']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SINGUPREQUEST._serialized_start=38
  _SINGUPREQUEST._serialized_end=86
  _SINGUPRESPONSE._serialized_start=88
  _SINGUPRESPONSE._serialized_end=133
  _AUTHORIZER._serialized_start=135
  _AUTHORIZER._serialized_end=218
# @@protoc_insertion_point(module_scope)