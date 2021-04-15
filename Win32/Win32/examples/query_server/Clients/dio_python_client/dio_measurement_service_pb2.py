# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dio_measurement_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dio_measurement_service.proto',
  package='measurementservice',
  syntax='proto3',
  serialized_options=b'\n\032labview.measurementserviceB\022MeasurementServiceP\001\242\002\004LVMS',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1d\x64io_measurement_service.proto\x12\x12measurementservice\"/\n\x08\x45rrorOut\x12\x0f\n\x07\x65rrCode\x18\x01 \x01(\x05\x12\x12\n\nerrMessage\x18\x02 \x01(\t\">\n\x14\x44IOpenSessionRequest\x12\x15\n\rDISessionName\x18\x01 \x01(\t\x12\x0f\n\x07\x44Ilines\x18\x02 \x01(\t\"[\n\x15\x44IOpenSessionResponse\x12\x15\n\rDISessionName\x18\x01 \x01(\t\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.measurementservice.ErrorOut\">\n\x14\x44OOpenSessionRequest\x12\x15\n\rDOSessionName\x18\x01 \x01(\t\x12\x0f\n\x07\x44Olines\x18\x02 \x01(\t\"[\n\x15\x44OOpenSessionResponse\x12\x15\n\rDOSessionName\x18\x01 \x01(\t\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.measurementservice.ErrorOut\"\'\n\rReadDIRequest\x12\x16\n\x0e\x44IOSessionName\x18\x01 \x01(\t\"e\n\x0eReadDIResponse\x12\x16\n\x0e\x44IOSessionName\x18\x01 \x01(\t\x12\x0e\n\x06\x44IData\x18\x02 \x03(\x08\x12+\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x1c.measurementservice.ErrorOut\"8\n\x0eWriteDORequest\x12\x16\n\x0e\x44IOSessionName\x18\x01 \x01(\t\x12\x0e\n\x06\x44OData\x18\x02 \x03(\x08\"V\n\x0fWriteDOResponse\x12\x16\n\x0e\x44IOSessionName\x18\x01 \x01(\t\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.measurementservice.ErrorOut\".\n\x15\x44ICloseSessionRequest\x12\x15\n\rDISessionName\x18\x01 \x01(\t\"E\n\x16\x44ICloseSessionResponse\x12+\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1c.measurementservice.ErrorOut\".\n\x15\x44OCloseSessionRequest\x12\x15\n\rDOSessionName\x18\x01 \x01(\t\"E\n\x16\x44OCloseSessionResponse\x12+\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1c.measurementservice.ErrorOut\"3\n\rInvokeRequest\x12\x0f\n\x07\x63ommand\x18\x01 \x01(\t\x12\x11\n\tparameter\x18\x02 \x01(\t\" \n\x0eInvokeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x1d\n\x0cQueryRequest\x12\r\n\x05query\x18\x01 \x01(\t\"0\n\rQueryResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\"(\n\x13RegistrationRequest\x12\x11\n\teventName\x18\x01 \x01(\t\"B\n\x0bServerEvent\x12\x11\n\teventData\x18\x01 \x01(\t\x12\x10\n\x08serverId\x18\x02 \x01(\x05\x12\x0e\n\x06status\x18\x03 \x01(\x05\x32\xe0\x06\n\x12MeasurementService\x12Q\n\x06Invoke\x12!.measurementservice.InvokeRequest\x1a\".measurementservice.InvokeResponse\"\x00\x12N\n\x05Query\x12 .measurementservice.QueryRequest\x1a!.measurementservice.QueryResponse\"\x00\x12X\n\x08Register\x12\'.measurementservice.RegistrationRequest\x1a\x1f.measurementservice.ServerEvent\"\x00\x30\x01\x12\x66\n\rOpenDISession\x12(.measurementservice.DIOpenSessionRequest\x1a).measurementservice.DIOpenSessionResponse\"\x00\x12\x66\n\rOpenDOSession\x12(.measurementservice.DOOpenSessionRequest\x1a).measurementservice.DOOpenSessionResponse\"\x00\x12Q\n\x06ReadDI\x12!.measurementservice.ReadDIRequest\x1a\".measurementservice.ReadDIResponse\"\x00\x12T\n\x07WriteDO\x12\".measurementservice.WriteDORequest\x1a#.measurementservice.WriteDOResponse\"\x00\x12i\n\x0e\x43loseDISession\x12).measurementservice.DICloseSessionRequest\x1a*.measurementservice.DICloseSessionResponse\"\x00\x12i\n\x0e\x43loseDOSession\x12).measurementservice.DOCloseSessionRequest\x1a*.measurementservice.DOCloseSessionResponse\"\x00\x42\x39\n\x1alabview.measurementserviceB\x12MeasurementServiceP\x01\xa2\x02\x04LVMSb\x06proto3'
)




_ERROROUT = _descriptor.Descriptor(
  name='ErrorOut',
  full_name='measurementservice.ErrorOut',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='errCode', full_name='measurementservice.ErrorOut.errCode', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='errMessage', full_name='measurementservice.ErrorOut.errMessage', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=53,
  serialized_end=100,
)


_DIOPENSESSIONREQUEST = _descriptor.Descriptor(
  name='DIOpenSessionRequest',
  full_name='measurementservice.DIOpenSessionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='DISessionName', full_name='measurementservice.DIOpenSessionRequest.DISessionName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='DIlines', full_name='measurementservice.DIOpenSessionRequest.DIlines', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=102,
  serialized_end=164,
)


_DIOPENSESSIONRESPONSE = _descriptor.Descriptor(
  name='DIOpenSessionResponse',
  full_name='measurementservice.DIOpenSessionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='DISessionName', full_name='measurementservice.DIOpenSessionResponse.DISessionName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='measurementservice.DIOpenSessionResponse.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=166,
  serialized_end=257,
)


_DOOPENSESSIONREQUEST = _descriptor.Descriptor(
  name='DOOpenSessionRequest',
  full_name='measurementservice.DOOpenSessionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='DOSessionName', full_name='measurementservice.DOOpenSessionRequest.DOSessionName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='DOlines', full_name='measurementservice.DOOpenSessionRequest.DOlines', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=259,
  serialized_end=321,
)


_DOOPENSESSIONRESPONSE = _descriptor.Descriptor(
  name='DOOpenSessionResponse',
  full_name='measurementservice.DOOpenSessionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='DOSessionName', full_name='measurementservice.DOOpenSessionResponse.DOSessionName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='measurementservice.DOOpenSessionResponse.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=323,
  serialized_end=414,
)


_READDIREQUEST = _descriptor.Descriptor(
  name='ReadDIRequest',
  full_name='measurementservice.ReadDIRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='DIOSessionName', full_name='measurementservice.ReadDIRequest.DIOSessionName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=416,
  serialized_end=455,
)


_READDIRESPONSE = _descriptor.Descriptor(
  name='ReadDIResponse',
  full_name='measurementservice.ReadDIResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='DIOSessionName', full_name='measurementservice.ReadDIResponse.DIOSessionName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='DIData', full_name='measurementservice.ReadDIResponse.DIData', index=1,
      number=2, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='measurementservice.ReadDIResponse.error', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=457,
  serialized_end=558,
)


_WRITEDOREQUEST = _descriptor.Descriptor(
  name='WriteDORequest',
  full_name='measurementservice.WriteDORequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='DIOSessionName', full_name='measurementservice.WriteDORequest.DIOSessionName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='DOData', full_name='measurementservice.WriteDORequest.DOData', index=1,
      number=2, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=560,
  serialized_end=616,
)


_WRITEDORESPONSE = _descriptor.Descriptor(
  name='WriteDOResponse',
  full_name='measurementservice.WriteDOResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='DIOSessionName', full_name='measurementservice.WriteDOResponse.DIOSessionName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='measurementservice.WriteDOResponse.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=618,
  serialized_end=704,
)


_DICLOSESESSIONREQUEST = _descriptor.Descriptor(
  name='DICloseSessionRequest',
  full_name='measurementservice.DICloseSessionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='DISessionName', full_name='measurementservice.DICloseSessionRequest.DISessionName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=706,
  serialized_end=752,
)


_DICLOSESESSIONRESPONSE = _descriptor.Descriptor(
  name='DICloseSessionResponse',
  full_name='measurementservice.DICloseSessionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='measurementservice.DICloseSessionResponse.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=754,
  serialized_end=823,
)


_DOCLOSESESSIONREQUEST = _descriptor.Descriptor(
  name='DOCloseSessionRequest',
  full_name='measurementservice.DOCloseSessionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='DOSessionName', full_name='measurementservice.DOCloseSessionRequest.DOSessionName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=825,
  serialized_end=871,
)


_DOCLOSESESSIONRESPONSE = _descriptor.Descriptor(
  name='DOCloseSessionResponse',
  full_name='measurementservice.DOCloseSessionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='measurementservice.DOCloseSessionResponse.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=873,
  serialized_end=942,
)


_INVOKEREQUEST = _descriptor.Descriptor(
  name='InvokeRequest',
  full_name='measurementservice.InvokeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='measurementservice.InvokeRequest.command', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parameter', full_name='measurementservice.InvokeRequest.parameter', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=944,
  serialized_end=995,
)


_INVOKERESPONSE = _descriptor.Descriptor(
  name='InvokeResponse',
  full_name='measurementservice.InvokeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='measurementservice.InvokeResponse.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=997,
  serialized_end=1029,
)


_QUERYREQUEST = _descriptor.Descriptor(
  name='QueryRequest',
  full_name='measurementservice.QueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='measurementservice.QueryRequest.query', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1031,
  serialized_end=1060,
)


_QUERYRESPONSE = _descriptor.Descriptor(
  name='QueryResponse',
  full_name='measurementservice.QueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='measurementservice.QueryResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='measurementservice.QueryResponse.status', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=1062,
  serialized_end=1110,
)


_REGISTRATIONREQUEST = _descriptor.Descriptor(
  name='RegistrationRequest',
  full_name='measurementservice.RegistrationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='eventName', full_name='measurementservice.RegistrationRequest.eventName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1112,
  serialized_end=1152,
)


_SERVEREVENT = _descriptor.Descriptor(
  name='ServerEvent',
  full_name='measurementservice.ServerEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='eventData', full_name='measurementservice.ServerEvent.eventData', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serverId', full_name='measurementservice.ServerEvent.serverId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='measurementservice.ServerEvent.status', index=2,
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
  serialized_start=1154,
  serialized_end=1220,
)

_DIOPENSESSIONRESPONSE.fields_by_name['error'].message_type = _ERROROUT
_DOOPENSESSIONRESPONSE.fields_by_name['error'].message_type = _ERROROUT
_READDIRESPONSE.fields_by_name['error'].message_type = _ERROROUT
_WRITEDORESPONSE.fields_by_name['error'].message_type = _ERROROUT
_DICLOSESESSIONRESPONSE.fields_by_name['error'].message_type = _ERROROUT
_DOCLOSESESSIONRESPONSE.fields_by_name['error'].message_type = _ERROROUT
DESCRIPTOR.message_types_by_name['ErrorOut'] = _ERROROUT
DESCRIPTOR.message_types_by_name['DIOpenSessionRequest'] = _DIOPENSESSIONREQUEST
DESCRIPTOR.message_types_by_name['DIOpenSessionResponse'] = _DIOPENSESSIONRESPONSE
DESCRIPTOR.message_types_by_name['DOOpenSessionRequest'] = _DOOPENSESSIONREQUEST
DESCRIPTOR.message_types_by_name['DOOpenSessionResponse'] = _DOOPENSESSIONRESPONSE
DESCRIPTOR.message_types_by_name['ReadDIRequest'] = _READDIREQUEST
DESCRIPTOR.message_types_by_name['ReadDIResponse'] = _READDIRESPONSE
DESCRIPTOR.message_types_by_name['WriteDORequest'] = _WRITEDOREQUEST
DESCRIPTOR.message_types_by_name['WriteDOResponse'] = _WRITEDORESPONSE
DESCRIPTOR.message_types_by_name['DICloseSessionRequest'] = _DICLOSESESSIONREQUEST
DESCRIPTOR.message_types_by_name['DICloseSessionResponse'] = _DICLOSESESSIONRESPONSE
DESCRIPTOR.message_types_by_name['DOCloseSessionRequest'] = _DOCLOSESESSIONREQUEST
DESCRIPTOR.message_types_by_name['DOCloseSessionResponse'] = _DOCLOSESESSIONRESPONSE
DESCRIPTOR.message_types_by_name['InvokeRequest'] = _INVOKEREQUEST
DESCRIPTOR.message_types_by_name['InvokeResponse'] = _INVOKERESPONSE
DESCRIPTOR.message_types_by_name['QueryRequest'] = _QUERYREQUEST
DESCRIPTOR.message_types_by_name['QueryResponse'] = _QUERYRESPONSE
DESCRIPTOR.message_types_by_name['RegistrationRequest'] = _REGISTRATIONREQUEST
DESCRIPTOR.message_types_by_name['ServerEvent'] = _SERVEREVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ErrorOut = _reflection.GeneratedProtocolMessageType('ErrorOut', (_message.Message,), {
  'DESCRIPTOR' : _ERROROUT,
  '__module__' : 'dio_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.ErrorOut)
  })
_sym_db.RegisterMessage(ErrorOut)

DIOpenSessionRequest = _reflection.GeneratedProtocolMessageType('DIOpenSessionRequest', (_message.Message,), {
  'DESCRIPTOR' : _DIOPENSESSIONREQUEST,
  '__module__' : 'dio_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.DIOpenSessionRequest)
  })
_sym_db.RegisterMessage(DIOpenSessionRequest)

DIOpenSessionResponse = _reflection.GeneratedProtocolMessageType('DIOpenSessionResponse', (_message.Message,), {
  'DESCRIPTOR' : _DIOPENSESSIONRESPONSE,
  '__module__' : 'dio_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.DIOpenSessionResponse)
  })
_sym_db.RegisterMessage(DIOpenSessionResponse)

DOOpenSessionRequest = _reflection.GeneratedProtocolMessageType('DOOpenSessionRequest', (_message.Message,), {
  'DESCRIPTOR' : _DOOPENSESSIONREQUEST,
  '__module__' : 'dio_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.DOOpenSessionRequest)
  })
_sym_db.RegisterMessage(DOOpenSessionRequest)

DOOpenSessionResponse = _reflection.GeneratedProtocolMessageType('DOOpenSessionResponse', (_message.Message,), {
  'DESCRIPTOR' : _DOOPENSESSIONRESPONSE,
  '__module__' : 'dio_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.DOOpenSessionResponse)
  })
_sym_db.RegisterMessage(DOOpenSessionResponse)

ReadDIRequest = _reflection.GeneratedProtocolMessageType('ReadDIRequest', (_message.Message,), {
  'DESCRIPTOR' : _READDIREQUEST,
  '__module__' : 'dio_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.ReadDIRequest)
  })
_sym_db.RegisterMessage(ReadDIRequest)

ReadDIResponse = _reflection.GeneratedProtocolMessageType('ReadDIResponse', (_message.Message,), {
  'DESCRIPTOR' : _READDIRESPONSE,
  '__module__' : 'dio_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.ReadDIResponse)
  })
_sym_db.RegisterMessage(ReadDIResponse)

WriteDORequest = _reflection.GeneratedProtocolMessageType('WriteDORequest', (_message.Message,), {
  'DESCRIPTOR' : _WRITEDOREQUEST,
  '__module__' : 'dio_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.WriteDORequest)
  })
_sym_db.RegisterMessage(WriteDORequest)

WriteDOResponse = _reflection.GeneratedProtocolMessageType('WriteDOResponse', (_message.Message,), {
  'DESCRIPTOR' : _WRITEDORESPONSE,
  '__module__' : 'dio_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.WriteDOResponse)
  })
_sym_db.RegisterMessage(WriteDOResponse)

DICloseSessionRequest = _reflection.GeneratedProtocolMessageType('DICloseSessionRequest', (_message.Message,), {
  'DESCRIPTOR' : _DICLOSESESSIONREQUEST,
  '__module__' : 'dio_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.DICloseSessionRequest)
  })
_sym_db.RegisterMessage(DICloseSessionRequest)

DICloseSessionResponse = _reflection.GeneratedProtocolMessageType('DICloseSessionResponse', (_message.Message,), {
  'DESCRIPTOR' : _DICLOSESESSIONRESPONSE,
  '__module__' : 'dio_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.DICloseSessionResponse)
  })
_sym_db.RegisterMessage(DICloseSessionResponse)

DOCloseSessionRequest = _reflection.GeneratedProtocolMessageType('DOCloseSessionRequest', (_message.Message,), {
  'DESCRIPTOR' : _DOCLOSESESSIONREQUEST,
  '__module__' : 'dio_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.DOCloseSessionRequest)
  })
_sym_db.RegisterMessage(DOCloseSessionRequest)

DOCloseSessionResponse = _reflection.GeneratedProtocolMessageType('DOCloseSessionResponse', (_message.Message,), {
  'DESCRIPTOR' : _DOCLOSESESSIONRESPONSE,
  '__module__' : 'dio_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.DOCloseSessionResponse)
  })
_sym_db.RegisterMessage(DOCloseSessionResponse)

InvokeRequest = _reflection.GeneratedProtocolMessageType('InvokeRequest', (_message.Message,), {
  'DESCRIPTOR' : _INVOKEREQUEST,
  '__module__' : 'dio_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.InvokeRequest)
  })
_sym_db.RegisterMessage(InvokeRequest)

InvokeResponse = _reflection.GeneratedProtocolMessageType('InvokeResponse', (_message.Message,), {
  'DESCRIPTOR' : _INVOKERESPONSE,
  '__module__' : 'dio_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.InvokeResponse)
  })
_sym_db.RegisterMessage(InvokeResponse)

QueryRequest = _reflection.GeneratedProtocolMessageType('QueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYREQUEST,
  '__module__' : 'dio_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.QueryRequest)
  })
_sym_db.RegisterMessage(QueryRequest)

QueryResponse = _reflection.GeneratedProtocolMessageType('QueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESPONSE,
  '__module__' : 'dio_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.QueryResponse)
  })
_sym_db.RegisterMessage(QueryResponse)

RegistrationRequest = _reflection.GeneratedProtocolMessageType('RegistrationRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRATIONREQUEST,
  '__module__' : 'dio_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.RegistrationRequest)
  })
_sym_db.RegisterMessage(RegistrationRequest)

ServerEvent = _reflection.GeneratedProtocolMessageType('ServerEvent', (_message.Message,), {
  'DESCRIPTOR' : _SERVEREVENT,
  '__module__' : 'dio_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.ServerEvent)
  })
_sym_db.RegisterMessage(ServerEvent)


DESCRIPTOR._options = None

_MEASUREMENTSERVICE = _descriptor.ServiceDescriptor(
  name='MeasurementService',
  full_name='measurementservice.MeasurementService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1223,
  serialized_end=2087,
  methods=[
  _descriptor.MethodDescriptor(
    name='Invoke',
    full_name='measurementservice.MeasurementService.Invoke',
    index=0,
    containing_service=None,
    input_type=_INVOKEREQUEST,
    output_type=_INVOKERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Query',
    full_name='measurementservice.MeasurementService.Query',
    index=1,
    containing_service=None,
    input_type=_QUERYREQUEST,
    output_type=_QUERYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Register',
    full_name='measurementservice.MeasurementService.Register',
    index=2,
    containing_service=None,
    input_type=_REGISTRATIONREQUEST,
    output_type=_SERVEREVENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='OpenDISession',
    full_name='measurementservice.MeasurementService.OpenDISession',
    index=3,
    containing_service=None,
    input_type=_DIOPENSESSIONREQUEST,
    output_type=_DIOPENSESSIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='OpenDOSession',
    full_name='measurementservice.MeasurementService.OpenDOSession',
    index=4,
    containing_service=None,
    input_type=_DOOPENSESSIONREQUEST,
    output_type=_DOOPENSESSIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReadDI',
    full_name='measurementservice.MeasurementService.ReadDI',
    index=5,
    containing_service=None,
    input_type=_READDIREQUEST,
    output_type=_READDIRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='WriteDO',
    full_name='measurementservice.MeasurementService.WriteDO',
    index=6,
    containing_service=None,
    input_type=_WRITEDOREQUEST,
    output_type=_WRITEDORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CloseDISession',
    full_name='measurementservice.MeasurementService.CloseDISession',
    index=7,
    containing_service=None,
    input_type=_DICLOSESESSIONREQUEST,
    output_type=_DICLOSESESSIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CloseDOSession',
    full_name='measurementservice.MeasurementService.CloseDOSession',
    index=8,
    containing_service=None,
    input_type=_DOCLOSESESSIONREQUEST,
    output_type=_DOCLOSESESSIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MEASUREMENTSERVICE)

DESCRIPTOR.services_by_name['MeasurementService'] = _MEASUREMENTSERVICE

# @@protoc_insertion_point(module_scope)
