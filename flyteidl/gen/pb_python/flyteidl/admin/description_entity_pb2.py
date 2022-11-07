# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/admin/description_entity.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flyteidl.core import identifier_pb2 as flyteidl_dot_core_dot_identifier__pb2
from flyteidl.admin import common_pb2 as flyteidl_dot_admin_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='flyteidl/admin/description_entity.proto',
  package='flyteidl.admin',
  syntax='proto3',
  serialized_options=_b('Z5github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/admin'),
  serialized_pb=_b('\n\'flyteidl/admin/description_entity.proto\x12\x0e\x66lyteidl.admin\x1a\x1e\x66lyteidl/core/identifier.proto\x1a\x1b\x66lyteidl/admin/common.proto\"\xcb\x01\n\x11\x44\x65scriptionEntity\x12%\n\x02id\x18\x01 \x01(\x0b\x32\x19.flyteidl.core.Identifier\x12\x19\n\x11short_description\x18\x02 \x01(\t\x12\x35\n\x10long_description\x18\x03 \x01(\x0b\x32\x1b.flyteidl.admin.Description\x12/\n\x0bsource_code\x18\x04 \x01(\x0b\x32\x1a.flyteidl.admin.SourceCode\x12\x0c\n\x04tags\x18\x05 \x03(\t\"~\n\x0b\x44\x65scription\x12\x0f\n\x05value\x18\x01 \x01(\tH\x00\x12\r\n\x03uri\x18\x02 \x01(\tH\x00\x12\x31\n\x06\x66ormat\x18\x03 \x01(\x0e\x32!.flyteidl.admin.DescriptionFormat\x12\x11\n\ticon_link\x18\x04 \x01(\tB\t\n\x07\x63ontent\"\x1a\n\nSourceCode\x12\x0c\n\x04link\x18\x01 \x01(\t\"f\n\x15\x44\x65scriptionEntityList\x12>\n\x13\x64\x65scriptionEntities\x18\x01 \x03(\x0b\x32!.flyteidl.admin.DescriptionEntity\x12\r\n\x05token\x18\x02 \x01(\t\"\xdb\x01\n\x1c\x44\x65scriptionEntityListRequest\x12\x32\n\rresource_type\x18\x01 \x01(\x0e\x32\x1b.flyteidl.core.ResourceType\x12\x31\n\x02id\x18\x02 \x01(\x0b\x32%.flyteidl.admin.NamedEntityIdentifier\x12\r\n\x05limit\x18\x03 \x01(\r\x12\r\n\x05token\x18\x04 \x01(\t\x12\x0f\n\x07\x66ilters\x18\x05 \x01(\t\x12%\n\x07sort_by\x18\x06 \x01(\x0b\x32\x14.flyteidl.admin.Sort*\x8d\x01\n\x11\x44\x65scriptionFormat\x12\x1e\n\x1a\x44\x45SCRIPTION_FORMAT_UNKNOWN\x10\x00\x12\x1f\n\x1b\x44\x45SCRIPTION_FORMAT_MARKDOWN\x10\x01\x12\x1b\n\x17\x44\x45SCRIPTION_FORMAT_HTML\x10\x02\x12\x1a\n\x16\x44\x45SCRIPTION_FORMAT_RST\x10\x03\x42\x37Z5github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/adminb\x06proto3')
  ,
  dependencies=[flyteidl_dot_core_dot_identifier__pb2.DESCRIPTOR,flyteidl_dot_admin_dot_common__pb2.DESCRIPTOR,])

_DESCRIPTIONFORMAT = _descriptor.EnumDescriptor(
  name='DescriptionFormat',
  full_name='flyteidl.admin.DescriptionFormat',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DESCRIPTION_FORMAT_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DESCRIPTION_FORMAT_MARKDOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DESCRIPTION_FORMAT_HTML', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DESCRIPTION_FORMAT_RST', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=809,
  serialized_end=950,
)
_sym_db.RegisterEnumDescriptor(_DESCRIPTIONFORMAT)

DescriptionFormat = enum_type_wrapper.EnumTypeWrapper(_DESCRIPTIONFORMAT)
DESCRIPTION_FORMAT_UNKNOWN = 0
DESCRIPTION_FORMAT_MARKDOWN = 1
DESCRIPTION_FORMAT_HTML = 2
DESCRIPTION_FORMAT_RST = 3



_DESCRIPTIONENTITY = _descriptor.Descriptor(
  name='DescriptionEntity',
  full_name='flyteidl.admin.DescriptionEntity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flyteidl.admin.DescriptionEntity.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='short_description', full_name='flyteidl.admin.DescriptionEntity.short_description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='long_description', full_name='flyteidl.admin.DescriptionEntity.long_description', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_code', full_name='flyteidl.admin.DescriptionEntity.source_code', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='flyteidl.admin.DescriptionEntity.tags', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_end=324,
)


_DESCRIPTION = _descriptor.Descriptor(
  name='Description',
  full_name='flyteidl.admin.Description',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='flyteidl.admin.Description.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uri', full_name='flyteidl.admin.Description.uri', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='format', full_name='flyteidl.admin.Description.format', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon_link', full_name='flyteidl.admin.Description.icon_link', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='content', full_name='flyteidl.admin.Description.content',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=326,
  serialized_end=452,
)


_SOURCECODE = _descriptor.Descriptor(
  name='SourceCode',
  full_name='flyteidl.admin.SourceCode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='link', full_name='flyteidl.admin.SourceCode.link', index=0,
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
  serialized_start=454,
  serialized_end=480,
)


_DESCRIPTIONENTITYLIST = _descriptor.Descriptor(
  name='DescriptionEntityList',
  full_name='flyteidl.admin.DescriptionEntityList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='descriptionEntities', full_name='flyteidl.admin.DescriptionEntityList.descriptionEntities', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='flyteidl.admin.DescriptionEntityList.token', index=1,
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
  serialized_start=482,
  serialized_end=584,
)


_DESCRIPTIONENTITYLISTREQUEST = _descriptor.Descriptor(
  name='DescriptionEntityListRequest',
  full_name='flyteidl.admin.DescriptionEntityListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_type', full_name='flyteidl.admin.DescriptionEntityListRequest.resource_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='flyteidl.admin.DescriptionEntityListRequest.id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='flyteidl.admin.DescriptionEntityListRequest.limit', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='flyteidl.admin.DescriptionEntityListRequest.token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filters', full_name='flyteidl.admin.DescriptionEntityListRequest.filters', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sort_by', full_name='flyteidl.admin.DescriptionEntityListRequest.sort_by', index=5,
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
  serialized_start=587,
  serialized_end=806,
)

_DESCRIPTIONENTITY.fields_by_name['id'].message_type = flyteidl_dot_core_dot_identifier__pb2._IDENTIFIER
_DESCRIPTIONENTITY.fields_by_name['long_description'].message_type = _DESCRIPTION
_DESCRIPTIONENTITY.fields_by_name['source_code'].message_type = _SOURCECODE
_DESCRIPTION.fields_by_name['format'].enum_type = _DESCRIPTIONFORMAT
_DESCRIPTION.oneofs_by_name['content'].fields.append(
  _DESCRIPTION.fields_by_name['value'])
_DESCRIPTION.fields_by_name['value'].containing_oneof = _DESCRIPTION.oneofs_by_name['content']
_DESCRIPTION.oneofs_by_name['content'].fields.append(
  _DESCRIPTION.fields_by_name['uri'])
_DESCRIPTION.fields_by_name['uri'].containing_oneof = _DESCRIPTION.oneofs_by_name['content']
_DESCRIPTIONENTITYLIST.fields_by_name['descriptionEntities'].message_type = _DESCRIPTIONENTITY
_DESCRIPTIONENTITYLISTREQUEST.fields_by_name['resource_type'].enum_type = flyteidl_dot_core_dot_identifier__pb2._RESOURCETYPE
_DESCRIPTIONENTITYLISTREQUEST.fields_by_name['id'].message_type = flyteidl_dot_admin_dot_common__pb2._NAMEDENTITYIDENTIFIER
_DESCRIPTIONENTITYLISTREQUEST.fields_by_name['sort_by'].message_type = flyteidl_dot_admin_dot_common__pb2._SORT
DESCRIPTOR.message_types_by_name['DescriptionEntity'] = _DESCRIPTIONENTITY
DESCRIPTOR.message_types_by_name['Description'] = _DESCRIPTION
DESCRIPTOR.message_types_by_name['SourceCode'] = _SOURCECODE
DESCRIPTOR.message_types_by_name['DescriptionEntityList'] = _DESCRIPTIONENTITYLIST
DESCRIPTOR.message_types_by_name['DescriptionEntityListRequest'] = _DESCRIPTIONENTITYLISTREQUEST
DESCRIPTOR.enum_types_by_name['DescriptionFormat'] = _DESCRIPTIONFORMAT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DescriptionEntity = _reflection.GeneratedProtocolMessageType('DescriptionEntity', (_message.Message,), dict(
  DESCRIPTOR = _DESCRIPTIONENTITY,
  __module__ = 'flyteidl.admin.description_entity_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.DescriptionEntity)
  ))
_sym_db.RegisterMessage(DescriptionEntity)

Description = _reflection.GeneratedProtocolMessageType('Description', (_message.Message,), dict(
  DESCRIPTOR = _DESCRIPTION,
  __module__ = 'flyteidl.admin.description_entity_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.Description)
  ))
_sym_db.RegisterMessage(Description)

SourceCode = _reflection.GeneratedProtocolMessageType('SourceCode', (_message.Message,), dict(
  DESCRIPTOR = _SOURCECODE,
  __module__ = 'flyteidl.admin.description_entity_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.SourceCode)
  ))
_sym_db.RegisterMessage(SourceCode)

DescriptionEntityList = _reflection.GeneratedProtocolMessageType('DescriptionEntityList', (_message.Message,), dict(
  DESCRIPTOR = _DESCRIPTIONENTITYLIST,
  __module__ = 'flyteidl.admin.description_entity_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.DescriptionEntityList)
  ))
_sym_db.RegisterMessage(DescriptionEntityList)

DescriptionEntityListRequest = _reflection.GeneratedProtocolMessageType('DescriptionEntityListRequest', (_message.Message,), dict(
  DESCRIPTOR = _DESCRIPTIONENTITYLISTREQUEST,
  __module__ = 'flyteidl.admin.description_entity_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.DescriptionEntityListRequest)
  ))
_sym_db.RegisterMessage(DescriptionEntityListRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
