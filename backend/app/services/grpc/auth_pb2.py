# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nauth.proto\x12\x04\x61uth\"\x16\n\x05Token\x12\r\n\x05token\x18\x01 \x01(\t\"\x18\n\x05Reply\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x32\x33\n\x07\x43hecker\x12(\n\nCheckToken\x12\x0b.auth.Token\x1a\x0b.auth.Reply\"\x00\x62\x06proto3')



_TOKEN = DESCRIPTOR.message_types_by_name['Token']
_REPLY = DESCRIPTOR.message_types_by_name['Reply']
Token = _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), {
  'DESCRIPTOR' : _TOKEN,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.Token)
  })
_sym_db.RegisterMessage(Token)

Reply = _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), {
  'DESCRIPTOR' : _REPLY,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.Reply)
  })
_sym_db.RegisterMessage(Reply)

_CHECKER = DESCRIPTOR.services_by_name['Checker']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TOKEN._serialized_start=20
  _TOKEN._serialized_end=42
  _REPLY._serialized_start=44
  _REPLY._serialized_end=68
  _CHECKER._serialized_start=70
  _CHECKER._serialized_end=121
# @@protoc_insertion_point(module_scope)