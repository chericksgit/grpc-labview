# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pwm_measurement_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pwm_measurement_service.proto',
  package='measurementservice',
  syntax='proto3',
  serialized_options=b'\n\032labview.measurementserviceB\022MeasurementServiceP\001\242\002\004LVMS',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1dpwm_measurement_service.proto\x12\x12measurementservice\"/\n\x08\x45rrorOut\x12\x0f\n\x07\x65rrCode\x18\x01 \x01(\x05\x12\x12\n\nerrMessage\x18\x02 \x01(\t\")\n\x15PWMOpenSessionRequest\x12\x10\n\x08PWMlines\x18\x01 \x01(\t\"E\n\x16PWMOpenSessionResponse\x12+\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1c.measurementservice.ErrorOut\"X\n\x0fPWMStartRequest\x12\x17\n\x0fPWMInitialState\x18\x01 \x01(\x08\x12\x16\n\x0ePWMInvertLines\x18\x02 \x01(\x08\x12\x14\n\x0cPWMFrequency\x18\x03 \x01(\x05\"\x86\x01\n\x10PWMStartResponse\x12\x17\n\x0fPWMInitialState\x18\x01 \x01(\x08\x12\x16\n\x0ePWMInvertLines\x18\x02 \x01(\x08\x12\x14\n\x0cPWMFrequency\x18\x03 \x01(\x05\x12+\n\x05\x65rror\x18\x04 \x01(\x0b\x32\x1c.measurementservice.ErrorOut\"(\n\x10PWMModifyRequest\x12\x14\n\x0cPWMFrequency\x18\x01 \x01(\x05\"V\n\x11PWMModifyResponse\x12\x14\n\x0cPWMFrequency\x18\x01 \x01(\x05\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.measurementservice.ErrorOut\"\x10\n\x0ePWMStopRequest\">\n\x0fPWMStopResponse\x12+\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1c.measurementservice.ErrorOut\"\x18\n\x16PWMCloseSessionRequest\"F\n\x17PWMCloseSessionResponse\x12+\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1c.measurementservice.ErrorOut\"3\n\rInvokeRequest\x12\x0f\n\x07\x63ommand\x18\x01 \x01(\t\x12\x11\n\tparameter\x18\x02 \x01(\t\" \n\x0eInvokeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x1d\n\x0cQueryRequest\x12\r\n\x05query\x18\x01 \x01(\t\"0\n\rQueryResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\"(\n\x13RegistrationRequest\x12\x11\n\teventName\x18\x01 \x01(\t\"B\n\x0bServerEvent\x12\x11\n\teventData\x18\x01 \x01(\t\x12\x10\n\x08serverId\x18\x02 \x01(\x05\x12\x0e\n\x06status\x18\x03 \x01(\x05\x32\xf5\x05\n\x12MeasurementService\x12Q\n\x06Invoke\x12!.measurementservice.InvokeRequest\x1a\".measurementservice.InvokeResponse\"\x00\x12N\n\x05Query\x12 .measurementservice.QueryRequest\x1a!.measurementservice.QueryResponse\"\x00\x12X\n\x08Register\x12\'.measurementservice.RegistrationRequest\x1a\x1f.measurementservice.ServerEvent\"\x00\x30\x01\x12i\n\x0eOpenPWMSession\x12).measurementservice.PWMOpenSessionRequest\x1a*.measurementservice.PWMOpenSessionResponse\"\x00\x12W\n\x08StartPWM\x12#.measurementservice.PWMStartRequest\x1a$.measurementservice.PWMStartResponse\"\x00\x12Z\n\tModifyPWM\x12$.measurementservice.PWMModifyRequest\x1a%.measurementservice.PWMModifyResponse\"\x00\x12T\n\x07StopPWM\x12\".measurementservice.PWMStopRequest\x1a#.measurementservice.PWMStopResponse\"\x00\x12l\n\x0f\x43losePWMSession\x12*.measurementservice.PWMCloseSessionRequest\x1a+.measurementservice.PWMCloseSessionResponse\"\x00\x42\x39\n\x1alabview.measurementserviceB\x12MeasurementServiceP\x01\xa2\x02\x04LVMSb\x06proto3'
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


_PWMOPENSESSIONREQUEST = _descriptor.Descriptor(
  name='PWMOpenSessionRequest',
  full_name='measurementservice.PWMOpenSessionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='PWMlines', full_name='measurementservice.PWMOpenSessionRequest.PWMlines', index=0,
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
  serialized_start=102,
  serialized_end=143,
)


_PWMOPENSESSIONRESPONSE = _descriptor.Descriptor(
  name='PWMOpenSessionResponse',
  full_name='measurementservice.PWMOpenSessionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='measurementservice.PWMOpenSessionResponse.error', index=0,
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
  serialized_start=145,
  serialized_end=214,
)


_PWMSTARTREQUEST = _descriptor.Descriptor(
  name='PWMStartRequest',
  full_name='measurementservice.PWMStartRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='PWMInitialState', full_name='measurementservice.PWMStartRequest.PWMInitialState', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='PWMInvertLines', full_name='measurementservice.PWMStartRequest.PWMInvertLines', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='PWMFrequency', full_name='measurementservice.PWMStartRequest.PWMFrequency', index=2,
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
  serialized_start=216,
  serialized_end=304,
)


_PWMSTARTRESPONSE = _descriptor.Descriptor(
  name='PWMStartResponse',
  full_name='measurementservice.PWMStartResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='PWMInitialState', full_name='measurementservice.PWMStartResponse.PWMInitialState', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='PWMInvertLines', full_name='measurementservice.PWMStartResponse.PWMInvertLines', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='PWMFrequency', full_name='measurementservice.PWMStartResponse.PWMFrequency', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='measurementservice.PWMStartResponse.error', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=307,
  serialized_end=441,
)


_PWMMODIFYREQUEST = _descriptor.Descriptor(
  name='PWMModifyRequest',
  full_name='measurementservice.PWMModifyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='PWMFrequency', full_name='measurementservice.PWMModifyRequest.PWMFrequency', index=0,
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
  serialized_start=443,
  serialized_end=483,
)


_PWMMODIFYRESPONSE = _descriptor.Descriptor(
  name='PWMModifyResponse',
  full_name='measurementservice.PWMModifyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='PWMFrequency', full_name='measurementservice.PWMModifyResponse.PWMFrequency', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='measurementservice.PWMModifyResponse.error', index=1,
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
  serialized_start=485,
  serialized_end=571,
)


_PWMSTOPREQUEST = _descriptor.Descriptor(
  name='PWMStopRequest',
  full_name='measurementservice.PWMStopRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=573,
  serialized_end=589,
)


_PWMSTOPRESPONSE = _descriptor.Descriptor(
  name='PWMStopResponse',
  full_name='measurementservice.PWMStopResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='measurementservice.PWMStopResponse.error', index=0,
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
  serialized_start=591,
  serialized_end=653,
)


_PWMCLOSESESSIONREQUEST = _descriptor.Descriptor(
  name='PWMCloseSessionRequest',
  full_name='measurementservice.PWMCloseSessionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=655,
  serialized_end=679,
)


_PWMCLOSESESSIONRESPONSE = _descriptor.Descriptor(
  name='PWMCloseSessionResponse',
  full_name='measurementservice.PWMCloseSessionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='measurementservice.PWMCloseSessionResponse.error', index=0,
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
  serialized_start=681,
  serialized_end=751,
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
  serialized_start=753,
  serialized_end=804,
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
  serialized_start=806,
  serialized_end=838,
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
  serialized_start=840,
  serialized_end=869,
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
  serialized_start=871,
  serialized_end=919,
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
  serialized_start=921,
  serialized_end=961,
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
  serialized_start=963,
  serialized_end=1029,
)

_PWMOPENSESSIONRESPONSE.fields_by_name['error'].message_type = _ERROROUT
_PWMSTARTRESPONSE.fields_by_name['error'].message_type = _ERROROUT
_PWMMODIFYRESPONSE.fields_by_name['error'].message_type = _ERROROUT
_PWMSTOPRESPONSE.fields_by_name['error'].message_type = _ERROROUT
_PWMCLOSESESSIONRESPONSE.fields_by_name['error'].message_type = _ERROROUT
DESCRIPTOR.message_types_by_name['ErrorOut'] = _ERROROUT
DESCRIPTOR.message_types_by_name['PWMOpenSessionRequest'] = _PWMOPENSESSIONREQUEST
DESCRIPTOR.message_types_by_name['PWMOpenSessionResponse'] = _PWMOPENSESSIONRESPONSE
DESCRIPTOR.message_types_by_name['PWMStartRequest'] = _PWMSTARTREQUEST
DESCRIPTOR.message_types_by_name['PWMStartResponse'] = _PWMSTARTRESPONSE
DESCRIPTOR.message_types_by_name['PWMModifyRequest'] = _PWMMODIFYREQUEST
DESCRIPTOR.message_types_by_name['PWMModifyResponse'] = _PWMMODIFYRESPONSE
DESCRIPTOR.message_types_by_name['PWMStopRequest'] = _PWMSTOPREQUEST
DESCRIPTOR.message_types_by_name['PWMStopResponse'] = _PWMSTOPRESPONSE
DESCRIPTOR.message_types_by_name['PWMCloseSessionRequest'] = _PWMCLOSESESSIONREQUEST
DESCRIPTOR.message_types_by_name['PWMCloseSessionResponse'] = _PWMCLOSESESSIONRESPONSE
DESCRIPTOR.message_types_by_name['InvokeRequest'] = _INVOKEREQUEST
DESCRIPTOR.message_types_by_name['InvokeResponse'] = _INVOKERESPONSE
DESCRIPTOR.message_types_by_name['QueryRequest'] = _QUERYREQUEST
DESCRIPTOR.message_types_by_name['QueryResponse'] = _QUERYRESPONSE
DESCRIPTOR.message_types_by_name['RegistrationRequest'] = _REGISTRATIONREQUEST
DESCRIPTOR.message_types_by_name['ServerEvent'] = _SERVEREVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ErrorOut = _reflection.GeneratedProtocolMessageType('ErrorOut', (_message.Message,), {
  'DESCRIPTOR' : _ERROROUT,
  '__module__' : 'pwm_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.ErrorOut)
  })
_sym_db.RegisterMessage(ErrorOut)

PWMOpenSessionRequest = _reflection.GeneratedProtocolMessageType('PWMOpenSessionRequest', (_message.Message,), {
  'DESCRIPTOR' : _PWMOPENSESSIONREQUEST,
  '__module__' : 'pwm_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.PWMOpenSessionRequest)
  })
_sym_db.RegisterMessage(PWMOpenSessionRequest)

PWMOpenSessionResponse = _reflection.GeneratedProtocolMessageType('PWMOpenSessionResponse', (_message.Message,), {
  'DESCRIPTOR' : _PWMOPENSESSIONRESPONSE,
  '__module__' : 'pwm_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.PWMOpenSessionResponse)
  })
_sym_db.RegisterMessage(PWMOpenSessionResponse)

PWMStartRequest = _reflection.GeneratedProtocolMessageType('PWMStartRequest', (_message.Message,), {
  'DESCRIPTOR' : _PWMSTARTREQUEST,
  '__module__' : 'pwm_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.PWMStartRequest)
  })
_sym_db.RegisterMessage(PWMStartRequest)

PWMStartResponse = _reflection.GeneratedProtocolMessageType('PWMStartResponse', (_message.Message,), {
  'DESCRIPTOR' : _PWMSTARTRESPONSE,
  '__module__' : 'pwm_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.PWMStartResponse)
  })
_sym_db.RegisterMessage(PWMStartResponse)

PWMModifyRequest = _reflection.GeneratedProtocolMessageType('PWMModifyRequest', (_message.Message,), {
  'DESCRIPTOR' : _PWMMODIFYREQUEST,
  '__module__' : 'pwm_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.PWMModifyRequest)
  })
_sym_db.RegisterMessage(PWMModifyRequest)

PWMModifyResponse = _reflection.GeneratedProtocolMessageType('PWMModifyResponse', (_message.Message,), {
  'DESCRIPTOR' : _PWMMODIFYRESPONSE,
  '__module__' : 'pwm_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.PWMModifyResponse)
  })
_sym_db.RegisterMessage(PWMModifyResponse)

PWMStopRequest = _reflection.GeneratedProtocolMessageType('PWMStopRequest', (_message.Message,), {
  'DESCRIPTOR' : _PWMSTOPREQUEST,
  '__module__' : 'pwm_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.PWMStopRequest)
  })
_sym_db.RegisterMessage(PWMStopRequest)

PWMStopResponse = _reflection.GeneratedProtocolMessageType('PWMStopResponse', (_message.Message,), {
  'DESCRIPTOR' : _PWMSTOPRESPONSE,
  '__module__' : 'pwm_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.PWMStopResponse)
  })
_sym_db.RegisterMessage(PWMStopResponse)

PWMCloseSessionRequest = _reflection.GeneratedProtocolMessageType('PWMCloseSessionRequest', (_message.Message,), {
  'DESCRIPTOR' : _PWMCLOSESESSIONREQUEST,
  '__module__' : 'pwm_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.PWMCloseSessionRequest)
  })
_sym_db.RegisterMessage(PWMCloseSessionRequest)

PWMCloseSessionResponse = _reflection.GeneratedProtocolMessageType('PWMCloseSessionResponse', (_message.Message,), {
  'DESCRIPTOR' : _PWMCLOSESESSIONRESPONSE,
  '__module__' : 'pwm_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.PWMCloseSessionResponse)
  })
_sym_db.RegisterMessage(PWMCloseSessionResponse)

InvokeRequest = _reflection.GeneratedProtocolMessageType('InvokeRequest', (_message.Message,), {
  'DESCRIPTOR' : _INVOKEREQUEST,
  '__module__' : 'pwm_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.InvokeRequest)
  })
_sym_db.RegisterMessage(InvokeRequest)

InvokeResponse = _reflection.GeneratedProtocolMessageType('InvokeResponse', (_message.Message,), {
  'DESCRIPTOR' : _INVOKERESPONSE,
  '__module__' : 'pwm_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.InvokeResponse)
  })
_sym_db.RegisterMessage(InvokeResponse)

QueryRequest = _reflection.GeneratedProtocolMessageType('QueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYREQUEST,
  '__module__' : 'pwm_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.QueryRequest)
  })
_sym_db.RegisterMessage(QueryRequest)

QueryResponse = _reflection.GeneratedProtocolMessageType('QueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESPONSE,
  '__module__' : 'pwm_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.QueryResponse)
  })
_sym_db.RegisterMessage(QueryResponse)

RegistrationRequest = _reflection.GeneratedProtocolMessageType('RegistrationRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRATIONREQUEST,
  '__module__' : 'pwm_measurement_service_pb2'
  # @@protoc_insertion_point(class_scope:measurementservice.RegistrationRequest)
  })
_sym_db.RegisterMessage(RegistrationRequest)

ServerEvent = _reflection.GeneratedProtocolMessageType('ServerEvent', (_message.Message,), {
  'DESCRIPTOR' : _SERVEREVENT,
  '__module__' : 'pwm_measurement_service_pb2'
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
  serialized_start=1032,
  serialized_end=1789,
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
    name='OpenPWMSession',
    full_name='measurementservice.MeasurementService.OpenPWMSession',
    index=3,
    containing_service=None,
    input_type=_PWMOPENSESSIONREQUEST,
    output_type=_PWMOPENSESSIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StartPWM',
    full_name='measurementservice.MeasurementService.StartPWM',
    index=4,
    containing_service=None,
    input_type=_PWMSTARTREQUEST,
    output_type=_PWMSTARTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ModifyPWM',
    full_name='measurementservice.MeasurementService.ModifyPWM',
    index=5,
    containing_service=None,
    input_type=_PWMMODIFYREQUEST,
    output_type=_PWMMODIFYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StopPWM',
    full_name='measurementservice.MeasurementService.StopPWM',
    index=6,
    containing_service=None,
    input_type=_PWMSTOPREQUEST,
    output_type=_PWMSTOPRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ClosePWMSession',
    full_name='measurementservice.MeasurementService.ClosePWMSession',
    index=7,
    containing_service=None,
    input_type=_PWMCLOSESESSIONREQUEST,
    output_type=_PWMCLOSESESSIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MEASUREMENTSERVICE)

DESCRIPTOR.services_by_name['MeasurementService'] = _MEASUREMENTSERVICE

# @@protoc_insertion_point(module_scope)
