# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import services.sessions.sessions_pb2 as sessions__pb2


class postSessionsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreatePostSession = channel.unary_unary(
                '/sessions.postSessionsService/CreatePostSession',
                request_serializer=sessions__pb2.CreatePostSessionRequest.SerializeToString,
                response_deserializer=sessions__pb2.CreatePostSessionResponse.FromString,
                )
        self.DropPostSession = channel.unary_unary(
                '/sessions.postSessionsService/DropPostSession',
                request_serializer=sessions__pb2.DropSessionRequest.SerializeToString,
                response_deserializer=sessions__pb2.DropSessionResponse.FromString,
                )


class postSessionsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreatePostSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DropPostSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_postSessionsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreatePostSession': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePostSession,
                    request_deserializer=sessions__pb2.CreatePostSessionRequest.FromString,
                    response_serializer=sessions__pb2.CreatePostSessionResponse.SerializeToString,
            ),
            'DropPostSession': grpc.unary_unary_rpc_method_handler(
                    servicer.DropPostSession,
                    request_deserializer=sessions__pb2.DropSessionRequest.FromString,
                    response_serializer=sessions__pb2.DropSessionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sessions.postSessionsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class postSessionsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreatePostSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sessions.postSessionsService/CreatePostSession',
            sessions__pb2.CreatePostSessionRequest.SerializeToString,
            sessions__pb2.CreatePostSessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DropPostSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sessions.postSessionsService/DropPostSession',
            sessions__pb2.DropSessionRequest.SerializeToString,
            sessions__pb2.DropSessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
