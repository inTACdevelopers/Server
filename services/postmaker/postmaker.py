import services.postmaker.posts_pb2 as pb2
import services.postmaker.posts_pb2_grpc as pb2_grpc
from database.posts import *


class PostMakeServise(pb2_grpc.postMakerServicer):
    def makePost(self, request, context):
        print("make post request")
        make_post_response = pb2.makePostResponse()

        code = make_post(request.post_title, request.post_description, request.seller_contact, request.user_id,
                         request.photo_bytes, request.file_name)

        make_post_response.code = code

        if code == 0:
            make_post_response.state = "OK"
        elif code == 1:
            make_post_response.state = "File Exists error (#db)"
        elif code == 2:
            make_post_response.state = "Server Error (#db)"

        return make_post_response


class PostGetter(pb2_grpc.postGetterServicer):
    def getPost(self, request, context):
        print("get post request")
        post = get_post_photo_bytes(request.post_id)

        post_get_response = pb2.GetPostResponse()
        if post is not None:
            post_get_response.post_title = post.title
            post_get_response.post_description = post.descr
            post.seller_contact = post.seller_contact
            post.creation_time = post.creation_date
            post_get_response.bytes = post.photo_bytes

            post_get_response.code = 0
            post_get_response.state = "OK"
        else:
            post_get_response.code = 1
            post_get_response.state = "Error (#server)"
        return post_get_response
