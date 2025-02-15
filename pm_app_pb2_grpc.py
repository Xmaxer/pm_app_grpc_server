# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import pm_app_pb2 as pm__app__pb2


class PMAppStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetData = channel.unary_stream(
        '/pm_app.PMApp/GetData',
        request_serializer=pm__app__pb2.AssetDetails.SerializeToString,
        response_deserializer=pm__app__pb2.DataPoint.FromString,
        )
    self.SendData = channel.stream_unary(
        '/pm_app.PMApp/SendData',
        request_serializer=pm__app__pb2.DataPoint.SerializeToString,
        response_deserializer=pm__app__pb2.Empty.FromString,
        )
    self.SaveData = channel.unary_unary(
        '/pm_app.PMApp/SaveData',
        request_serializer=pm__app__pb2.ResultDataPoint.SerializeToString,
        response_deserializer=pm__app__pb2.Empty.FromString,
        )


class PMAppServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetData(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendData(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SaveData(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PMAppServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetData': grpc.unary_stream_rpc_method_handler(
          servicer.GetData,
          request_deserializer=pm__app__pb2.AssetDetails.FromString,
          response_serializer=pm__app__pb2.DataPoint.SerializeToString,
      ),
      'SendData': grpc.stream_unary_rpc_method_handler(
          servicer.SendData,
          request_deserializer=pm__app__pb2.DataPoint.FromString,
          response_serializer=pm__app__pb2.Empty.SerializeToString,
      ),
      'SaveData': grpc.unary_unary_rpc_method_handler(
          servicer.SaveData,
          request_deserializer=pm__app__pb2.ResultDataPoint.FromString,
          response_serializer=pm__app__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'pm_app.PMApp', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
