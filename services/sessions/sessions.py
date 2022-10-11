import services.sessions.sessions_pb2 as pb2
import services.sessions.sessions_pb2_grpc as pb2_grpc
from database.users import *


class SessionService(pb2_grpc.postSessionsServiceServicer):
    def CreatePostSession(self, request, context):
        print("Create Session Request")

        session_name = str(abs(str(request.user_id).__hash__()))
        code = create_user_post_session(session_name)

        session_response = pb2.CreatePostSessionResponse()

        session_response.code = code
        session_response.session_name = session_name

        if code == 0:
            session_response.state = "OK"
        else:
            session_response.state = "Server error (#db)"

        return session_response

    def DropPostSession(self, request, context):
        print("Drop Session Request")

        code = drop_user_post_session(request.session_name)

        session_response = pb2.DropSessionResponse()

        session_response.code = code

        if code == 0:
            session_response.state = "OK"
        else:
            session_response.state = "Server error (#db)"

        return session_response
