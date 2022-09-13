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
        post = get_post(request.post_id)

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

    def GetPostPaginated(self, request, context):
        print(f"get post pagination request post_id == {request.post_id}")

        arr = get_posts_paginated(request.post_id, 4)

        get_posts_paginated_response = pb2.GetPostPaginatedResponse()
        posts = []
        if arr is not None or request.post_id >= get_first_post()[0]:

            if type(arr) is int and arr == 1:
                post = pb2.GetPostResponse()
                it = get_post(get_first_post()[0])

                post.post_id = it.id
                post.post_title = it.title
                post.photo_bytes = it.photo_bytes
                post.post_description = it.descr
                post.seller_contact = it.seller_contact
                post.creation_time = it.creation_date
                post.user_id = it.from_user
                post.state = "Empty"
                post.code = 3
                posts.append(post)
                get_posts_paginated_response.posts.extend(posts)
                return get_posts_paginated_response
            elif type(arr) is not int:

                for item in arr:
                    post = pb2.GetPostResponse()

                    post.post_id = item.id
                    post.post_title = item.title
                    post.photo_bytes = item.photo_bytes
                    post.post_description = item.descr
                    post.seller_contact = item.seller_contact
                    post.creation_time = item.creation_date
                    post.user_id = item.from_user
                    post.state = "OK"
                    post.code = 0

                    posts.append(post)
        else:
            post = pb2.GetPostResponse()
            if type(arr) is int and arr == 2:
                post.state = "Server Error (#db)"
                post.code = 1
            elif request.post_id > get_first_post()[0]:
                post.state = "Incorrect Post Id (#server)"
                post.code = 2

            posts.append(post)

        get_posts_paginated_response.posts.extend(posts)

        return get_posts_paginated_response

    def GetFirstPostId(self, request, context):

        get_first_id_response = pb2.GetFirstPostIdResponse()
        print("get first post id request")

        data = get_first_post()

        if data != None:
            get_first_id_response.first_post_id = data[0]
            get_first_id_response.state = "OK"
            get_first_id_response.code = 0
        else:

            get_first_id_response.state = "Server Error (#db)"
            get_first_id_response.code = 1


        return get_first_id_response
