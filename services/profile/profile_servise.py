import services.profile.profile_pb2_grpc as pb2_grpc
import services.profile.profile_pb2 as pb2

from database.users import *
from database.posts import *


class UserGetterServise(pb2_grpc.userGetterServicer):
    def GetUser(self, request, context):
        print(f"Get User for Profile Request id = {request.user_id}")
        get_user_response = pb2.GetUserResponse()

        user = get_user_id(request.user_id)

        if user is None:
            get_user_response.code = 1
            get_user_response.state = "Server error (#db)"
            return get_user_response

        get_user_response.code = 0
        get_user_response.state = "OK"

        get_user_response.user_type = user.user_type
        get_user_response.login = user.login
        get_user_response.name = user.name
        get_user_response.surname = user.surname
        get_user_response.company= user.company
        return get_user_response
