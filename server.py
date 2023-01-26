import grpc

from concurrent import futures

from services.authorizer import authorization_pb2_grpc
from services.postmaker import posts_pb2_grpc
from services.registrar import registration_pb2_grpc
from services.YmlParser import yml_pb2_grpc
from services.sessions import sessions_pb2_grpc
from services.profile import profile_pb2_grpc
from services.authorizer.autorizer import SingUpService
from services.registrar.registrar import SingInService
from services.postmaker.postmaker import PostMakeServise, PostGetter, PostLiker
from services.YmlParser.ymlUploader import YmlUploaderServise
from services.sessions.sessions import SessionService
from services.profile.profile_servise import UserGetterServise
from services.profile.profile_servise import userUpdater
from config import *


# python -m grpc_tools.protoc -I./protos --python_out=services/authorizer --grpc_python_out=services/authorizer protos/authorization.proto
# python -m grpc_tools.protoc -I./protos --python_out=services/registrar --grpc_python_out=services/registrar protos/registration.proto
# python -m grpc_tools.protoc -I./protos --python_out=services/postmaker --grpc_python_out=services/postmaker protos/posts.proto
# python -m grpc_tools.protoc -I./protos --python_out=services/YmlParser --grpc_python_out=services/YmlParser protos/yml.proto
# python -m grpc_tools.protoc -I./protos --python_out=services/sessions --grpc_python_out=services/sessions protos/sessions.proto
# python -m grpc_tools.protoc -I./protos --python_out=services/profile --grpc_python_out=services/profile protos/profile.proto

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1000))

    registration_pb2_grpc.add_registrarServicer_to_server(SingInService(), server)
    authorization_pb2_grpc.add_authorizerServicer_to_server(SingUpService(), server)
    posts_pb2_grpc.add_postMakerServicer_to_server(PostMakeServise(), server)
    posts_pb2_grpc.add_postGetterServicer_to_server(PostGetter(), server)
    yml_pb2_grpc.add_YmlPostMakerServicer_to_server(YmlUploaderServise(), server)
    posts_pb2_grpc.add_LikePostServicer_to_server(PostLiker(), server)
    sessions_pb2_grpc.add_postSessionsServiceServicer_to_server(SessionService(), server)
    profile_pb2_grpc.add_userGetterServicer_to_server(UserGetterServise(), server)
    profile_pb2_grpc.add_userUpdaterServicer_to_server(userUpdater(), server)

    connection = f'{SERVER_IP}:{SERVER_PORT}'

    if DEBAG:
        connection = f"{DEBAG_SERVER_IP}:{DEBAG_SERVER_PORT}"
    server.add_insecure_port(connection)
    server.start()

    print(f"Server started at {connection}")
    server.wait_for_termination()
