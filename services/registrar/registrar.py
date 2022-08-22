import services.registrar.registration_pb2 as pb2
import services.registrar.registration_pb2_grpc as pb2_grpc
from database.users import User


class SingInService(pb2_grpc.registrarServicer):
    def SingIn(self, request, context):
        print("sing in request")
        user = User(request.login, request.password)

        sing_in_response = pb2.SingInResponse()

        sing_in_response.state = user.new_user()

        if sing_in_response.state == "OK":
            sing_in_response.code = 0
        else:
            sing_in_response.code = 1

        return sing_in_response
