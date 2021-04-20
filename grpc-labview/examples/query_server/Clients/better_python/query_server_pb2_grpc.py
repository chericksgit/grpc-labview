# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import query_server_pb2 as query__server__pb2


class QueryServerStub(object):
  """---------------------------------------------------------------------
  The QueryServer service definition.
  ---------------------------------------------------------------------
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Invoke = channel.unary_unary(
        '/queryserver.QueryServer/Invoke',
        request_serializer=query__server__pb2.InvokeRequest.SerializeToString,
        response_deserializer=query__server__pb2.InvokeResponse.FromString,
        )
    self.Query = channel.unary_unary(
        '/queryserver.QueryServer/Query',
        request_serializer=query__server__pb2.QueryRequest.SerializeToString,
        response_deserializer=query__server__pb2.QueryResponse.FromString,
        )
    self.Register = channel.unary_stream(
        '/queryserver.QueryServer/Register',
        request_serializer=query__server__pb2.RegistrationRequest.SerializeToString,
        response_deserializer=query__server__pb2.ServerEvent.FromString,
        )


class QueryServerServicer(object):
  """---------------------------------------------------------------------
  The QueryServer service definition.
  ---------------------------------------------------------------------
  """

  def Invoke(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Query(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Register(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_QueryServerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Invoke': grpc.unary_unary_rpc_method_handler(
          servicer.Invoke,
          request_deserializer=query__server__pb2.InvokeRequest.FromString,
          response_serializer=query__server__pb2.InvokeResponse.SerializeToString,
      ),
      'Query': grpc.unary_unary_rpc_method_handler(
          servicer.Query,
          request_deserializer=query__server__pb2.QueryRequest.FromString,
          response_serializer=query__server__pb2.QueryResponse.SerializeToString,
      ),
      'Register': grpc.unary_stream_rpc_method_handler(
          servicer.Register,
          request_deserializer=query__server__pb2.RegistrationRequest.FromString,
          response_serializer=query__server__pb2.ServerEvent.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'queryserver.QueryServer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
