import grpc

from concurrent import futures

from services.authorizer import authorization_pb2_grpc
from services.authorizer.autorizer import SingUpService
from services.registrar import registration_pb2_grpc
from services.registrar.registrar import SingInService


# python -m grpc_tools.protoc -I./protos --python_out=services/authorizer --grpc_python_out=services/authorizer protos/authorization.proto

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=100))

    registration_pb2_grpc.add_registrarServicer_to_server(SingInService(), server)
    authorization_pb2_grpc.add_authorizerServicer_to_server(SingUpService(), server)

    server.add_insecure_port("localhost:8080")
    server.start()

    print("Server started at localhost:8080")
    server.wait_for_termination()
