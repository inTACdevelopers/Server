import grpc

from concurrent import futures

from services.authorizer import authorization_pb2_grpc
from services.authorizer.autorizer import SingUpService
from services.registrar import registration_pb2_grpc
from services.registrar.registrar import SingInService

from config import *


# python -m grpc_tools.protoc -I./protos --python_out=services/authorizer --grpc_python_out=services/authorizer protos/authorization.proto
# python -m grpc_tools.protoc -I./protos --python_out=services/registrar --grpc_python_out=services/registrar protos/registration.proto

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=100))

    registration_pb2_grpc.add_registrarServicer_to_server(SingInService(), server)
    authorization_pb2_grpc.add_authorizerServicer_to_server(SingUpService(), server)

    connection = f'{SERVER_IP}:{SERVER_PORT}'
    if DEBAG:
        connection = f"{DEBAG_SERVER_IP}:{DEBAG_SERVER_PORT}"
    server.add_insecure_port(connection)
    server.start()

    print(f"Server started at {connection}")
    server.wait_for_termination()
