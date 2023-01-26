import services.profile.profile_pb2_grpc as pb2_grpc
import services.profile.profile_pb2 as pb2

from database.users import *
from database.posts import *


class UserGetterServise(pb2_grpc.userGetterServicer):
    def GetUser_ById(self, request, context):
        print(f"Get User for Profile Request id = {request.user_id}")
        get_user_response = pb2.GetUserResponse()

        user = get_user_id(request.user_id)

        hash = hashlib.sha256()
        hash.update(user.id.to_bytes(8, 'big'))
        sha_id = hash.hexdigest()

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
        get_user_response.company = user.company
        get_user_response.count_of_posts = get_count_of_user_posts(sha_id)
        get_user_response.profile_photo = get_user_photo(request.user_id)
        
        return get_user_response


class userUpdater(pb2_grpc.userUpdaterServicer):
    def UpdateAbout(self, request, context):
        print(f"UpdateAbout Request <user:{request.user_id}>")
        update_user_response = pb2.UpdateAboutResponse()

        update_user_response.code = update_user_about(request.user_id, request.about)

        if update_user_response.code == 0:
            update_user_response.state = "OK"
            return update_user_response

        update_user_response.state = "Server Error (#db)"
        return update_user_response

    def UpdateLogin(self, request, context):
        print(f"Update login request <user:{request.user_id}>")

        update_user_response = pb2.UpdateLoginResponse()

        update_user_response.code = update_user_login(request.user_id, request.login)

        if update_user_response.code == 0:
            update_user_response.state = "OK"
            return update_user_response

        update_user_response.state = "Server Error (#db)"
        return update_user_response

    def UpdateName(self, request, context):
        print(f"Update name request <user:{request.user_id}>")

        update_user_response = pb2.UpdateNameResponse()

        update_user_response.code = update_user_name(request.user_id, request.name)

        if update_user_response.code == 0:
            update_user_response.state = "OK"
            return update_user_response

        update_user_response.state = "Server Error (#db)"
        return update_user_response

    def UpdatePassword(self, request, context):
        print(f"Update password request <user:{request.user_id}>")

        update_user_response = pb2.UpdatePasswordResponse()

        update_user_response.code = update_user_password(request.user_id, request.password)

        if update_user_response.code == 0:
            update_user_response.state = "OK"
            return update_user_response

        update_user_response.state = "Server Error (#db)"
        return update_user_response

    def UpdatePhoto(self, request, context):
        print(f"Update Profile photo request <user:{request.user_id}>")

        update_user_response = pb2.UpdatePhotoResponse()

        update_user_response.code = update_user_photo(request.user_id, request.photo_bytes)

        if update_user_response.code == 0:
            update_user_response.state = "OK"
            return update_user_response

        update_user_response.state = "Server Error (#db)"
        return update_user_response
