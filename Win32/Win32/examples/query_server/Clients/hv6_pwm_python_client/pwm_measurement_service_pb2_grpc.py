# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pwm_measurement_service_pb2 as pwm__measurement__service__pb2


class MeasurementServiceStub(object):
    """---------------------------------------------------------------------
    The MeasurementService service definition.
    ---------------------------------------------------------------------
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Invoke = channel.unary_unary(
                '/measurementservice.MeasurementService/Invoke',
                request_serializer=pwm__measurement__service__pb2.InvokeRequest.SerializeToString,
                response_deserializer=pwm__measurement__service__pb2.InvokeResponse.FromString,
                )
        self.Query = channel.unary_unary(
                '/measurementservice.MeasurementService/Query',
                request_serializer=pwm__measurement__service__pb2.QueryRequest.SerializeToString,
                response_deserializer=pwm__measurement__service__pb2.QueryResponse.FromString,
                )
        self.Register = channel.unary_stream(
                '/measurementservice.MeasurementService/Register',
                request_serializer=pwm__measurement__service__pb2.RegistrationRequest.SerializeToString,
                response_deserializer=pwm__measurement__service__pb2.ServerEvent.FromString,
                )
        self.OpenPWMSession = channel.unary_unary(
                '/measurementservice.MeasurementService/OpenPWMSession',
                request_serializer=pwm__measurement__service__pb2.PWMOpenSessionRequest.SerializeToString,
                response_deserializer=pwm__measurement__service__pb2.PWMOpenSessionResponse.FromString,
                )
        self.StartPWM = channel.unary_unary(
                '/measurementservice.MeasurementService/StartPWM',
                request_serializer=pwm__measurement__service__pb2.PWMStartRequest.SerializeToString,
                response_deserializer=pwm__measurement__service__pb2.PWMStartResponse.FromString,
                )
        self.ModifyPWM = channel.unary_unary(
                '/measurementservice.MeasurementService/ModifyPWM',
                request_serializer=pwm__measurement__service__pb2.PWMModifyRequest.SerializeToString,
                response_deserializer=pwm__measurement__service__pb2.PWMModifyResponse.FromString,
                )
        self.StopPWM = channel.unary_unary(
                '/measurementservice.MeasurementService/StopPWM',
                request_serializer=pwm__measurement__service__pb2.PWMStopRequest.SerializeToString,
                response_deserializer=pwm__measurement__service__pb2.PWMStopResponse.FromString,
                )
        self.ClosePWMSession = channel.unary_unary(
                '/measurementservice.MeasurementService/ClosePWMSession',
                request_serializer=pwm__measurement__service__pb2.PWMCloseSessionRequest.SerializeToString,
                response_deserializer=pwm__measurement__service__pb2.PWMCloseSessionResponse.FromString,
                )


class MeasurementServiceServicer(object):
    """---------------------------------------------------------------------
    The MeasurementService service definition.
    ---------------------------------------------------------------------
    """

    def Invoke(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Query(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OpenPWMSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartPWM(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ModifyPWM(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopPWM(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClosePWMSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MeasurementServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Invoke': grpc.unary_unary_rpc_method_handler(
                    servicer.Invoke,
                    request_deserializer=pwm__measurement__service__pb2.InvokeRequest.FromString,
                    response_serializer=pwm__measurement__service__pb2.InvokeResponse.SerializeToString,
            ),
            'Query': grpc.unary_unary_rpc_method_handler(
                    servicer.Query,
                    request_deserializer=pwm__measurement__service__pb2.QueryRequest.FromString,
                    response_serializer=pwm__measurement__service__pb2.QueryResponse.SerializeToString,
            ),
            'Register': grpc.unary_stream_rpc_method_handler(
                    servicer.Register,
                    request_deserializer=pwm__measurement__service__pb2.RegistrationRequest.FromString,
                    response_serializer=pwm__measurement__service__pb2.ServerEvent.SerializeToString,
            ),
            'OpenPWMSession': grpc.unary_unary_rpc_method_handler(
                    servicer.OpenPWMSession,
                    request_deserializer=pwm__measurement__service__pb2.PWMOpenSessionRequest.FromString,
                    response_serializer=pwm__measurement__service__pb2.PWMOpenSessionResponse.SerializeToString,
            ),
            'StartPWM': grpc.unary_unary_rpc_method_handler(
                    servicer.StartPWM,
                    request_deserializer=pwm__measurement__service__pb2.PWMStartRequest.FromString,
                    response_serializer=pwm__measurement__service__pb2.PWMStartResponse.SerializeToString,
            ),
            'ModifyPWM': grpc.unary_unary_rpc_method_handler(
                    servicer.ModifyPWM,
                    request_deserializer=pwm__measurement__service__pb2.PWMModifyRequest.FromString,
                    response_serializer=pwm__measurement__service__pb2.PWMModifyResponse.SerializeToString,
            ),
            'StopPWM': grpc.unary_unary_rpc_method_handler(
                    servicer.StopPWM,
                    request_deserializer=pwm__measurement__service__pb2.PWMStopRequest.FromString,
                    response_serializer=pwm__measurement__service__pb2.PWMStopResponse.SerializeToString,
            ),
            'ClosePWMSession': grpc.unary_unary_rpc_method_handler(
                    servicer.ClosePWMSession,
                    request_deserializer=pwm__measurement__service__pb2.PWMCloseSessionRequest.FromString,
                    response_serializer=pwm__measurement__service__pb2.PWMCloseSessionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'measurementservice.MeasurementService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MeasurementService(object):
    """---------------------------------------------------------------------
    The MeasurementService service definition.
    ---------------------------------------------------------------------
    """

    @staticmethod
    def Invoke(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/measurementservice.MeasurementService/Invoke',
            pwm__measurement__service__pb2.InvokeRequest.SerializeToString,
            pwm__measurement__service__pb2.InvokeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Query(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/measurementservice.MeasurementService/Query',
            pwm__measurement__service__pb2.QueryRequest.SerializeToString,
            pwm__measurement__service__pb2.QueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/measurementservice.MeasurementService/Register',
            pwm__measurement__service__pb2.RegistrationRequest.SerializeToString,
            pwm__measurement__service__pb2.ServerEvent.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OpenPWMSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/measurementservice.MeasurementService/OpenPWMSession',
            pwm__measurement__service__pb2.PWMOpenSessionRequest.SerializeToString,
            pwm__measurement__service__pb2.PWMOpenSessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartPWM(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/measurementservice.MeasurementService/StartPWM',
            pwm__measurement__service__pb2.PWMStartRequest.SerializeToString,
            pwm__measurement__service__pb2.PWMStartResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ModifyPWM(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/measurementservice.MeasurementService/ModifyPWM',
            pwm__measurement__service__pb2.PWMModifyRequest.SerializeToString,
            pwm__measurement__service__pb2.PWMModifyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopPWM(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/measurementservice.MeasurementService/StopPWM',
            pwm__measurement__service__pb2.PWMStopRequest.SerializeToString,
            pwm__measurement__service__pb2.PWMStopResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClosePWMSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/measurementservice.MeasurementService/ClosePWMSession',
            pwm__measurement__service__pb2.PWMCloseSessionRequest.SerializeToString,
            pwm__measurement__service__pb2.PWMCloseSessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)