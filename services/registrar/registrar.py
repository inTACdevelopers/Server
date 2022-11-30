import services.registrar.registration_pb2 as pb2
import services.registrar.registration_pb2_grpc as pb2_grpc
from database.users import *
import hashlib


class SingInService(pb2_grpc.registrarServicer):
    def SingIn(self, request, context):
        print("sing in request")

        sing_in_response = pb2.SingInResponse()

        hash = hashlib.sha256()
        hash.update((request.login + request.password).encode())
        token = hash.hexdigest()

        sing_in_response.code = new_user(request.login, request.password, request.surname, request.name,
                                         request.birth_date, token, request.company)

        if sing_in_response.code == 0:
            sing_in_response.state = "OK"

            user = get_user(request.login)
            if user is not None:
                print(f"USER ID {user.id}")
                hash = hashlib.sha256()
                hash.update(user.id.to_bytes(8,'big'))
                sha_id = hash.hexdigest()
                create_users_posts_table(sha_id)


        elif sing_in_response.code == 1:
            sing_in_response.state = "User already exist"
        elif sing_in_response.code == 2:
            sing_in_response.state = "Company already exist"
        elif sing_in_response.code == 3:
            sing_in_response.state = "Server Error (#db)"
        return sing_in_response
