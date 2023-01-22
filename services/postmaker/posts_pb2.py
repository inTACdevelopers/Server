# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: posts.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bposts.proto\x12\x05posts\"\x90\x01\n\x0fmakePostRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x13\n\x0bphoto_bytes\x18\x02 \x01(\x0c\x12\x12\n\npost_title\x18\x03 \x01(\t\x12\x18\n\x10post_description\x18\x04 \x01(\t\x12\x16\n\x0eseller_contact\x18\x05 \x01(\t\x12\x0f\n\x07user_id\x18\x06 \x01(\x03\"/\n\x10makePostResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05state\x18\x02 \x01(\t\"W\n\x0eGetPostRequest\x12\x0f\n\x07post_id\x18\x01 \x01(\x03\x12\r\n\x05limit\x18\x02 \x01(\x03\x12\x14\n\x0csession_name\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x04 \x01(\x03\"E\n\x12GetUserPostRequest\x12\x0f\n\x07post_id\x18\x01 \x01(\x03\x12\r\n\x05limit\x18\x02 \x01(\x03\x12\x0f\n\x07user_id\x18\x03 \x01(\x03\"\xd0\x01\n\x0fGetPostResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05state\x18\x02 \x01(\t\x12\x13\n\x0bphoto_bytes\x18\x03 \x01(\x0c\x12\x12\n\npost_title\x18\x04 \x01(\t\x12\x18\n\x10post_description\x18\x05 \x01(\t\x12\x16\n\x0eseller_contact\x18\x06 \x01(\t\x12\x15\n\rcreation_time\x18\x07 \x01(\t\x12\x0f\n\x07post_id\x18\x08 \x01(\x05\x12\x0f\n\x07user_id\x18\t \x01(\x03\x12\x0c\n\x04like\x18\n \x01(\x08\"A\n\x18GetPostPaginatedResponse\x12%\n\x05posts\x18\x01 \x03(\x0b\x32\x16.posts.GetPostResponse\"-\n\x15GetFirstPostIdRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\"\\\n\x16GetFirstPostIdResponse\x12\x15\n\rfirst_post_id\x18\x01 \x01(\x05\x12\r\n\x05state\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\x05\x12\x0e\n\x06weight\x18\x04 \x01(\x01\"5\n\x0fLikePostRequest\x12\x11\n\tfrom_user\x18\x01 \x01(\x03\x12\x0f\n\x07post_id\x18\x02 \x01(\x03\"/\n\x10LikePostResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05state\x18\x02 \x01(\t\"7\n\x11UnLikePostRequest\x12\x11\n\tfrom_user\x18\x01 \x01(\x03\x12\x0f\n\x07post_id\x18\x02 \x01(\x03\"1\n\x12UnLikePostResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05state\x18\x02 \x01(\t2H\n\tpostMaker\x12;\n\x08makePost\x12\x16.posts.makePostRequest\x1a\x17.posts.makePostResponse2\xad\x02\n\npostGetter\x12\x38\n\x07getPost\x12\x15.posts.GetPostRequest\x1a\x16.posts.GetPostResponse\x12J\n\x10GetPostPaginated\x12\x15.posts.GetPostRequest\x1a\x1f.posts.GetPostPaginatedResponse\x12J\n\x0cGetUserPosts\x12\x19.posts.GetUserPostRequest\x1a\x1f.posts.GetPostPaginatedResponse\x12M\n\x0eGetFirstPostId\x12\x1c.posts.GetFirstPostIdRequest\x1a\x1d.posts.GetFirstPostIdResponse2\x86\x01\n\x08LikePost\x12;\n\x08SendLike\x12\x16.posts.LikePostRequest\x1a\x17.posts.LikePostResponse\x12=\n\x06UnLike\x12\x18.posts.UnLikePostRequest\x1a\x19.posts.UnLikePostResponseb\x06proto3')



_MAKEPOSTREQUEST = DESCRIPTOR.message_types_by_name['makePostRequest']
_MAKEPOSTRESPONSE = DESCRIPTOR.message_types_by_name['makePostResponse']
_GETPOSTREQUEST = DESCRIPTOR.message_types_by_name['GetPostRequest']
_GETUSERPOSTREQUEST = DESCRIPTOR.message_types_by_name['GetUserPostRequest']
_GETPOSTRESPONSE = DESCRIPTOR.message_types_by_name['GetPostResponse']
_GETPOSTPAGINATEDRESPONSE = DESCRIPTOR.message_types_by_name['GetPostPaginatedResponse']
_GETFIRSTPOSTIDREQUEST = DESCRIPTOR.message_types_by_name['GetFirstPostIdRequest']
_GETFIRSTPOSTIDRESPONSE = DESCRIPTOR.message_types_by_name['GetFirstPostIdResponse']
_LIKEPOSTREQUEST = DESCRIPTOR.message_types_by_name['LikePostRequest']
_LIKEPOSTRESPONSE = DESCRIPTOR.message_types_by_name['LikePostResponse']
_UNLIKEPOSTREQUEST = DESCRIPTOR.message_types_by_name['UnLikePostRequest']
_UNLIKEPOSTRESPONSE = DESCRIPTOR.message_types_by_name['UnLikePostResponse']
makePostRequest = _reflection.GeneratedProtocolMessageType('makePostRequest', (_message.Message,), {
  'DESCRIPTOR' : _MAKEPOSTREQUEST,
  '__module__' : 'posts_pb2'
  # @@protoc_insertion_point(class_scope:posts.makePostRequest)
  })
_sym_db.RegisterMessage(makePostRequest)

makePostResponse = _reflection.GeneratedProtocolMessageType('makePostResponse', (_message.Message,), {
  'DESCRIPTOR' : _MAKEPOSTRESPONSE,
  '__module__' : 'posts_pb2'
  # @@protoc_insertion_point(class_scope:posts.makePostResponse)
  })
_sym_db.RegisterMessage(makePostResponse)

GetPostRequest = _reflection.GeneratedProtocolMessageType('GetPostRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPOSTREQUEST,
  '__module__' : 'posts_pb2'
  # @@protoc_insertion_point(class_scope:posts.GetPostRequest)
  })
_sym_db.RegisterMessage(GetPostRequest)

GetUserPostRequest = _reflection.GeneratedProtocolMessageType('GetUserPostRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERPOSTREQUEST,
  '__module__' : 'posts_pb2'
  # @@protoc_insertion_point(class_scope:posts.GetUserPostRequest)
  })
_sym_db.RegisterMessage(GetUserPostRequest)

GetPostResponse = _reflection.GeneratedProtocolMessageType('GetPostResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPOSTRESPONSE,
  '__module__' : 'posts_pb2'
  # @@protoc_insertion_point(class_scope:posts.GetPostResponse)
  })
_sym_db.RegisterMessage(GetPostResponse)

GetPostPaginatedResponse = _reflection.GeneratedProtocolMessageType('GetPostPaginatedResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPOSTPAGINATEDRESPONSE,
  '__module__' : 'posts_pb2'
  # @@protoc_insertion_point(class_scope:posts.GetPostPaginatedResponse)
  })
_sym_db.RegisterMessage(GetPostPaginatedResponse)

GetFirstPostIdRequest = _reflection.GeneratedProtocolMessageType('GetFirstPostIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFIRSTPOSTIDREQUEST,
  '__module__' : 'posts_pb2'
  # @@protoc_insertion_point(class_scope:posts.GetFirstPostIdRequest)
  })
_sym_db.RegisterMessage(GetFirstPostIdRequest)

GetFirstPostIdResponse = _reflection.GeneratedProtocolMessageType('GetFirstPostIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETFIRSTPOSTIDRESPONSE,
  '__module__' : 'posts_pb2'
  # @@protoc_insertion_point(class_scope:posts.GetFirstPostIdResponse)
  })
_sym_db.RegisterMessage(GetFirstPostIdResponse)

LikePostRequest = _reflection.GeneratedProtocolMessageType('LikePostRequest', (_message.Message,), {
  'DESCRIPTOR' : _LIKEPOSTREQUEST,
  '__module__' : 'posts_pb2'
  # @@protoc_insertion_point(class_scope:posts.LikePostRequest)
  })
_sym_db.RegisterMessage(LikePostRequest)

LikePostResponse = _reflection.GeneratedProtocolMessageType('LikePostResponse', (_message.Message,), {
  'DESCRIPTOR' : _LIKEPOSTRESPONSE,
  '__module__' : 'posts_pb2'
  # @@protoc_insertion_point(class_scope:posts.LikePostResponse)
  })
_sym_db.RegisterMessage(LikePostResponse)

UnLikePostRequest = _reflection.GeneratedProtocolMessageType('UnLikePostRequest', (_message.Message,), {
  'DESCRIPTOR' : _UNLIKEPOSTREQUEST,
  '__module__' : 'posts_pb2'
  # @@protoc_insertion_point(class_scope:posts.UnLikePostRequest)
  })
_sym_db.RegisterMessage(UnLikePostRequest)

UnLikePostResponse = _reflection.GeneratedProtocolMessageType('UnLikePostResponse', (_message.Message,), {
  'DESCRIPTOR' : _UNLIKEPOSTRESPONSE,
  '__module__' : 'posts_pb2'
  # @@protoc_insertion_point(class_scope:posts.UnLikePostResponse)
  })
_sym_db.RegisterMessage(UnLikePostResponse)

_POSTMAKER = DESCRIPTOR.services_by_name['postMaker']
_POSTGETTER = DESCRIPTOR.services_by_name['postGetter']
_LIKEPOST = DESCRIPTOR.services_by_name['LikePost']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MAKEPOSTREQUEST._serialized_start=23
  _MAKEPOSTREQUEST._serialized_end=167
  _MAKEPOSTRESPONSE._serialized_start=169
  _MAKEPOSTRESPONSE._serialized_end=216
  _GETPOSTREQUEST._serialized_start=218
  _GETPOSTREQUEST._serialized_end=305
  _GETUSERPOSTREQUEST._serialized_start=307
  _GETUSERPOSTREQUEST._serialized_end=376
  _GETPOSTRESPONSE._serialized_start=379
  _GETPOSTRESPONSE._serialized_end=587
  _GETPOSTPAGINATEDRESPONSE._serialized_start=589
  _GETPOSTPAGINATEDRESPONSE._serialized_end=654
  _GETFIRSTPOSTIDREQUEST._serialized_start=656
  _GETFIRSTPOSTIDREQUEST._serialized_end=701
  _GETFIRSTPOSTIDRESPONSE._serialized_start=703
  _GETFIRSTPOSTIDRESPONSE._serialized_end=795
  _LIKEPOSTREQUEST._serialized_start=797
  _LIKEPOSTREQUEST._serialized_end=850
  _LIKEPOSTRESPONSE._serialized_start=852
  _LIKEPOSTRESPONSE._serialized_end=899
  _UNLIKEPOSTREQUEST._serialized_start=901
  _UNLIKEPOSTREQUEST._serialized_end=956
  _UNLIKEPOSTRESPONSE._serialized_start=958
  _UNLIKEPOSTRESPONSE._serialized_end=1007
  _POSTMAKER._serialized_start=1009
  _POSTMAKER._serialized_end=1081
  _POSTGETTER._serialized_start=1084
  _POSTGETTER._serialized_end=1385
  _LIKEPOST._serialized_start=1388
  _LIKEPOST._serialized_end=1522
# @@protoc_insertion_point(module_scope)
