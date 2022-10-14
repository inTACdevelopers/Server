# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import services.authorizer.authorization_pb2 as authorization__pb2


class authorizerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SingUp = channel.unary_unary(
                '/authorization.authorizer/SingUp',
                request_serializer=authorization__pb2.SingUpRequest.SerializeToString,
                response_deserializer=authorization__pb2.SingUpResponse.FromString,
                )
        self.SingUpByToken = channel.unary_unary(
                '/authorization.authorizer/SingUpByToken',
                request_serializer=authorization__pb2.SingUpByTokenRequest.SerializeToString,
                response_deserializer=authorization__pb2.SingUpResponse.FromString,
                )


class authorizerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SingUp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SingUpByToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_authorizerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SingUp': grpc.unary_unary_rpc_method_handler(
                    servicer.SingUp,
                    request_deserializer=authorization__pb2.SingUpRequest.FromString,
                    response_serializer=authorization__pb2.SingUpResponse.SerializeToString,
            ),
            'SingUpByToken': grpc.unary_unary_rpc_method_handler(
                    servicer.SingUpByToken,
                    request_deserializer=authorization__pb2.SingUpByTokenRequest.FromString,
                    response_serializer=authorization__pb2.SingUpResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'authorization.authorizer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class authorizer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SingUp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authorization.authorizer/SingUp',
            authorization__pb2.SingUpRequest.SerializeToString,
            authorization__pb2.SingUpResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SingUpByToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authorization.authorizer/SingUpByToken',
            authorization__pb2.SingUpByTokenRequest.SerializeToString,
            authorization__pb2.SingUpResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
