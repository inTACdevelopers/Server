import services.authorizer.authorization_pb2 as pb2
import services.authorizer.authorization_pb2_grpc as pb2_grpc


class SingUpService(pb2_grpc.authorizerServicer):
    def SingUp(self, request, context):

        # Some Code with DataBase connection
        sing_up_reply = pb2.SingUpResponse()

        sing_up_reply.code = 0
        sing_up_reply.state = "OK"

        print(request.login)
        print(request.password)

        return sing_up_reply
