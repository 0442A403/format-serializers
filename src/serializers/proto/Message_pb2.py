# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rMessage.proto\"%\n\x06\x43ourse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x05\"F\n\x0eUniversityData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04year\x18\x02 \x01(\x05\x12\x18\n\x07\x63ourses\x18\x03 \x03(\x0b\x32\x07.Course\"\x9a\x01\n\x07Message\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x13\n\x0bmiddle_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x11\n\x04year\x18\x04 \x01(\x05H\x00\x88\x01\x01\x12(\n\nuniversity\x18\x05 \x01(\x0b\x32\x0f.UniversityDataH\x01\x88\x01\x01\x42\x07\n\x05_yearB\r\n\x0b_universityb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Message_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_COURSE']._serialized_start=17
  _globals['_COURSE']._serialized_end=54
  _globals['_UNIVERSITYDATA']._serialized_start=56
  _globals['_UNIVERSITYDATA']._serialized_end=126
  _globals['_MESSAGE']._serialized_start=129
  _globals['_MESSAGE']._serialized_end=283
# @@protoc_insertion_point(module_scope)