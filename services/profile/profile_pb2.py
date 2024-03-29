# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: profile.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rprofile.proto\x12\x07profile\"!\n\x0eGetUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\"\xcd\x01\n\x0fGetUserResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05state\x18\x02 \x01(\t\x12\x11\n\tuser_type\x18\x03 \x01(\x05\x12\n\n\x02id\x18\x04 \x01(\x03\x12\r\n\x05login\x18\x05 \x01(\t\x12\x10\n\x08password\x18\x06 \x01(\t\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x0f\n\x07surname\x18\x08 \x01(\t\x12\x0f\n\x07\x63ompany\x18\t \x01(\t\x12\x16\n\x0e\x63ount_of_posts\x18\n \x01(\x03\x12\x15\n\rprofile_photo\x18\x0b \x01(\x0c\"2\n\x11UpdateNameRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\"1\n\x12UpdateNameResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05state\x18\x02 \x01(\t\"4\n\x12UpdateLoginRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\r\n\x05login\x18\x02 \x01(\t\"2\n\x13UpdateLoginResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05state\x18\x02 \x01(\t\"4\n\x12UpdateAboutRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\r\n\x05\x61\x62out\x18\x02 \x01(\t\"2\n\x13UpdateAboutResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05state\x18\x02 \x01(\t\":\n\x15UpdatePasswordRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x10\n\x08password\x18\x02 \x01(\t\"5\n\x16UpdatePasswordResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05state\x18\x02 \x01(\t\":\n\x12UpdatePhotoRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x13\n\x0bphoto_bytes\x18\x02 \x01(\x0c\"2\n\x13UpdatePhotoResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05state\x18\x02 \x01(\t2O\n\nuserGetter\x12\x41\n\x0cGetUser_ById\x12\x17.profile.GetUserRequest\x1a\x18.profile.GetUserResponse2\x85\x03\n\x0buserUpdater\x12\x45\n\nUpdateName\x12\x1a.profile.UpdateNameRequest\x1a\x1b.profile.UpdateNameResponse\x12H\n\x0bUpdateLogin\x12\x1b.profile.UpdateLoginRequest\x1a\x1c.profile.UpdateLoginResponse\x12H\n\x0bUpdateAbout\x12\x1b.profile.UpdateAboutRequest\x1a\x1c.profile.UpdateAboutResponse\x12Q\n\x0eUpdatePassword\x12\x1e.profile.UpdatePasswordRequest\x1a\x1f.profile.UpdatePasswordResponse\x12H\n\x0bUpdatePhoto\x12\x1b.profile.UpdatePhotoRequest\x1a\x1c.profile.UpdatePhotoResponseb\x06proto3')



_GETUSERREQUEST = DESCRIPTOR.message_types_by_name['GetUserRequest']
_GETUSERRESPONSE = DESCRIPTOR.message_types_by_name['GetUserResponse']
_UPDATENAMEREQUEST = DESCRIPTOR.message_types_by_name['UpdateNameRequest']
_UPDATENAMERESPONSE = DESCRIPTOR.message_types_by_name['UpdateNameResponse']
_UPDATELOGINREQUEST = DESCRIPTOR.message_types_by_name['UpdateLoginRequest']
_UPDATELOGINRESPONSE = DESCRIPTOR.message_types_by_name['UpdateLoginResponse']
_UPDATEABOUTREQUEST = DESCRIPTOR.message_types_by_name['UpdateAboutRequest']
_UPDATEABOUTRESPONSE = DESCRIPTOR.message_types_by_name['UpdateAboutResponse']
_UPDATEPASSWORDREQUEST = DESCRIPTOR.message_types_by_name['UpdatePasswordRequest']
_UPDATEPASSWORDRESPONSE = DESCRIPTOR.message_types_by_name['UpdatePasswordResponse']
_UPDATEPHOTOREQUEST = DESCRIPTOR.message_types_by_name['UpdatePhotoRequest']
_UPDATEPHOTORESPONSE = DESCRIPTOR.message_types_by_name['UpdatePhotoResponse']
GetUserRequest = _reflection.GeneratedProtocolMessageType('GetUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERREQUEST,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:profile.GetUserRequest)
  })
_sym_db.RegisterMessage(GetUserRequest)

GetUserResponse = _reflection.GeneratedProtocolMessageType('GetUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERRESPONSE,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:profile.GetUserResponse)
  })
_sym_db.RegisterMessage(GetUserResponse)

UpdateNameRequest = _reflection.GeneratedProtocolMessageType('UpdateNameRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATENAMEREQUEST,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:profile.UpdateNameRequest)
  })
_sym_db.RegisterMessage(UpdateNameRequest)

UpdateNameResponse = _reflection.GeneratedProtocolMessageType('UpdateNameResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATENAMERESPONSE,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:profile.UpdateNameResponse)
  })
_sym_db.RegisterMessage(UpdateNameResponse)

UpdateLoginRequest = _reflection.GeneratedProtocolMessageType('UpdateLoginRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATELOGINREQUEST,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:profile.UpdateLoginRequest)
  })
_sym_db.RegisterMessage(UpdateLoginRequest)

UpdateLoginResponse = _reflection.GeneratedProtocolMessageType('UpdateLoginResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATELOGINRESPONSE,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:profile.UpdateLoginResponse)
  })
_sym_db.RegisterMessage(UpdateLoginResponse)

UpdateAboutRequest = _reflection.GeneratedProtocolMessageType('UpdateAboutRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEABOUTREQUEST,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:profile.UpdateAboutRequest)
  })
_sym_db.RegisterMessage(UpdateAboutRequest)

UpdateAboutResponse = _reflection.GeneratedProtocolMessageType('UpdateAboutResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEABOUTRESPONSE,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:profile.UpdateAboutResponse)
  })
_sym_db.RegisterMessage(UpdateAboutResponse)

UpdatePasswordRequest = _reflection.GeneratedProtocolMessageType('UpdatePasswordRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPASSWORDREQUEST,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:profile.UpdatePasswordRequest)
  })
_sym_db.RegisterMessage(UpdatePasswordRequest)

UpdatePasswordResponse = _reflection.GeneratedProtocolMessageType('UpdatePasswordResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPASSWORDRESPONSE,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:profile.UpdatePasswordResponse)
  })
_sym_db.RegisterMessage(UpdatePasswordResponse)

UpdatePhotoRequest = _reflection.GeneratedProtocolMessageType('UpdatePhotoRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPHOTOREQUEST,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:profile.UpdatePhotoRequest)
  })
_sym_db.RegisterMessage(UpdatePhotoRequest)

UpdatePhotoResponse = _reflection.GeneratedProtocolMessageType('UpdatePhotoResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPHOTORESPONSE,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:profile.UpdatePhotoResponse)
  })
_sym_db.RegisterMessage(UpdatePhotoResponse)

_USERGETTER = DESCRIPTOR.services_by_name['userGetter']
_USERUPDATER = DESCRIPTOR.services_by_name['userUpdater']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETUSERREQUEST._serialized_start=26
  _GETUSERREQUEST._serialized_end=59
  _GETUSERRESPONSE._serialized_start=62
  _GETUSERRESPONSE._serialized_end=267
  _UPDATENAMEREQUEST._serialized_start=269
  _UPDATENAMEREQUEST._serialized_end=319
  _UPDATENAMERESPONSE._serialized_start=321
  _UPDATENAMERESPONSE._serialized_end=370
  _UPDATELOGINREQUEST._serialized_start=372
  _UPDATELOGINREQUEST._serialized_end=424
  _UPDATELOGINRESPONSE._serialized_start=426
  _UPDATELOGINRESPONSE._serialized_end=476
  _UPDATEABOUTREQUEST._serialized_start=478
  _UPDATEABOUTREQUEST._serialized_end=530
  _UPDATEABOUTRESPONSE._serialized_start=532
  _UPDATEABOUTRESPONSE._serialized_end=582
  _UPDATEPASSWORDREQUEST._serialized_start=584
  _UPDATEPASSWORDREQUEST._serialized_end=642
  _UPDATEPASSWORDRESPONSE._serialized_start=644
  _UPDATEPASSWORDRESPONSE._serialized_end=697
  _UPDATEPHOTOREQUEST._serialized_start=699
  _UPDATEPHOTOREQUEST._serialized_end=757
  _UPDATEPHOTORESPONSE._serialized_start=759
  _UPDATEPHOTORESPONSE._serialized_end=809
  _USERGETTER._serialized_start=811
  _USERGETTER._serialized_end=890
  _USERUPDATER._serialized_start=893
  _USERUPDATER._serialized_end=1282
# @@protoc_insertion_point(module_scope)
