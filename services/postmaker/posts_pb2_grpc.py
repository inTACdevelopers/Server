# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import services.postmaker.posts_pb2 as posts__pb2


class postMakerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.makePost = channel.unary_unary(
                '/posts.postMaker/makePost',
                request_serializer=posts__pb2.makePostRequest.SerializeToString,
                response_deserializer=posts__pb2.makePostResponse.FromString,
                )


class postMakerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def makePost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_postMakerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'makePost': grpc.unary_unary_rpc_method_handler(
                    servicer.makePost,
                    request_deserializer=posts__pb2.makePostRequest.FromString,
                    response_serializer=posts__pb2.makePostResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'posts.postMaker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class postMaker(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def makePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/posts.postMaker/makePost',
            posts__pb2.makePostRequest.SerializeToString,
            posts__pb2.makePostResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class postGetterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getPost = channel.unary_unary(
                '/posts.postGetter/getPost',
                request_serializer=posts__pb2.GetPostRequest.SerializeToString,
                response_deserializer=posts__pb2.GetPostResponse.FromString,
                )
        self.GetPostPaginated = channel.unary_unary(
                '/posts.postGetter/GetPostPaginated',
                request_serializer=posts__pb2.GetPostRequest.SerializeToString,
                response_deserializer=posts__pb2.GetPostPaginatedResponse.FromString,
                )
        self.GetUserPosts = channel.unary_unary(
                '/posts.postGetter/GetUserPosts',
                request_serializer=posts__pb2.GetUserPostRequest.SerializeToString,
                response_deserializer=posts__pb2.GetPostPaginatedResponse.FromString,
                )
        self.GetFirstPostId = channel.unary_unary(
                '/posts.postGetter/GetFirstPostId',
                request_serializer=posts__pb2.GetFirstPostIdRequest.SerializeToString,
                response_deserializer=posts__pb2.GetFirstPostIdResponse.FromString,
                )


class postGetterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getPost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPostPaginated(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserPosts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFirstPostId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_postGetterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getPost': grpc.unary_unary_rpc_method_handler(
                    servicer.getPost,
                    request_deserializer=posts__pb2.GetPostRequest.FromString,
                    response_serializer=posts__pb2.GetPostResponse.SerializeToString,
            ),
            'GetPostPaginated': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPostPaginated,
                    request_deserializer=posts__pb2.GetPostRequest.FromString,
                    response_serializer=posts__pb2.GetPostPaginatedResponse.SerializeToString,
            ),
            'GetUserPosts': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserPosts,
                    request_deserializer=posts__pb2.GetUserPostRequest.FromString,
                    response_serializer=posts__pb2.GetPostPaginatedResponse.SerializeToString,
            ),
            'GetFirstPostId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFirstPostId,
                    request_deserializer=posts__pb2.GetFirstPostIdRequest.FromString,
                    response_serializer=posts__pb2.GetFirstPostIdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'posts.postGetter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class postGetter(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getPost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/posts.postGetter/getPost',
            posts__pb2.GetPostRequest.SerializeToString,
            posts__pb2.GetPostResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPostPaginated(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/posts.postGetter/GetPostPaginated',
            posts__pb2.GetPostRequest.SerializeToString,
            posts__pb2.GetPostPaginatedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserPosts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/posts.postGetter/GetUserPosts',
            posts__pb2.GetUserPostRequest.SerializeToString,
            posts__pb2.GetPostPaginatedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFirstPostId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/posts.postGetter/GetFirstPostId',
            posts__pb2.GetFirstPostIdRequest.SerializeToString,
            posts__pb2.GetFirstPostIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class LikePostStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendLike = channel.unary_unary(
                '/posts.LikePost/SendLike',
                request_serializer=posts__pb2.LikePostRequest.SerializeToString,
                response_deserializer=posts__pb2.LikePostResponse.FromString,
                )
        self.UnLike = channel.unary_unary(
                '/posts.LikePost/UnLike',
                request_serializer=posts__pb2.UnLikePostRequest.SerializeToString,
                response_deserializer=posts__pb2.UnLikePostResponse.FromString,
                )


class LikePostServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendLike(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnLike(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LikePostServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendLike': grpc.unary_unary_rpc_method_handler(
                    servicer.SendLike,
                    request_deserializer=posts__pb2.LikePostRequest.FromString,
                    response_serializer=posts__pb2.LikePostResponse.SerializeToString,
            ),
            'UnLike': grpc.unary_unary_rpc_method_handler(
                    servicer.UnLike,
                    request_deserializer=posts__pb2.UnLikePostRequest.FromString,
                    response_serializer=posts__pb2.UnLikePostResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'posts.LikePost', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LikePost(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendLike(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/posts.LikePost/SendLike',
            posts__pb2.LikePostRequest.SerializeToString,
            posts__pb2.LikePostResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnLike(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/posts.LikePost/UnLike',
            posts__pb2.UnLikePostRequest.SerializeToString,
            posts__pb2.UnLikePostResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
