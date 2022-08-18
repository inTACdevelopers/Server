import services.registrar.registration_pb2 as pb2
import services.registrar.registration_pb2_grpc as pb2_grpc


class SingInService(pb2_grpc.registrarServicer):
    def SingIn(self, request, context):
        # Some code with DataBase connection
        sing_in_response = pb2.SingInResponse()

        sing_in_response.code = 0
        sing_in_response.state = "OK"

        return sing_in_response
