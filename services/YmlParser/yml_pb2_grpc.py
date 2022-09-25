# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import services.YmlParser.yml_pb2 as yml__pb2


class YmlPostMakerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UploadPosts = channel.unary_unary(
                '/yml.YmlPostMaker/UploadPosts',
                request_serializer=yml__pb2.UploadRequest.SerializeToString,
                response_deserializer=yml__pb2.UploadResponse.FromString,
                )


class YmlPostMakerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UploadPosts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_YmlPostMakerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UploadPosts': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadPosts,
                    request_deserializer=yml__pb2.UploadRequest.FromString,
                    response_serializer=yml__pb2.UploadResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yml.YmlPostMaker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class YmlPostMaker(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UploadPosts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yml.YmlPostMaker/UploadPosts',
            yml__pb2.UploadRequest.SerializeToString,
            yml__pb2.UploadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
