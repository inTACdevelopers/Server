import services.authorizer.authorization_pb2 as pb2
import services.authorizer.authorization_pb2_grpc as pb2_grpc
from database.users import *


class SingUpService(pb2_grpc.authorizerServicer):
    def SingUp(self, request, context):
        print("sing up request")
        sing_up_reply = pb2.SingUpResponse()

        user = get_user_by_login_password(request.login, request.password)

        if user is not None:

            sing_up_reply.code = 0
            sing_up_reply.state = "OK"
            sing_up_reply.id = user.id
            sing_up_reply.login = user.login
            sing_up_reply.password = user.password
            sing_up_reply.name = user.name
            sing_up_reply.surname = user.surname
            sing_up_reply.company = user.company
            user.user_type = 0
            if user.company != "None":
                user.user_type = 1

            sing_up_reply.user_type = user.user_type

        else:
            sing_up_reply.code = 1
            sing_up_reply.state = "No such user"

        return sing_up_reply
