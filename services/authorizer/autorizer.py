import services.authorizer.authorization_pb2 as pb2
import services.authorizer.authorization_pb2_grpc as pb2_grpc
from database.users import *


class SingUpService(pb2_grpc.authorizerServicer):
    def SingUp(self, request, context):
        print("sing up request")
        sing_up_reply = pb2.SingUpResponse()

        user = get_user_by_login_password(request.login, request.password)
        user.user_type = 0

        if user.company != "None":
            user.user_type = 1

        if user is not None:
            sing_up_reply.code = 0
            sing_up_reply.state = "OK"
        else:
            sing_up_reply.code = 1
            sing_up_reply.state = "No such user"

        sing_up_reply.user_type = user.user_type
        return sing_up_reply
