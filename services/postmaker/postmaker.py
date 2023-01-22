import services.postmaker.posts_pb2 as pb2
import services.postmaker.posts_pb2_grpc as pb2_grpc
from database.posts import *
from database.users import get_user_id


class PostMakeServise(pb2_grpc.postMakerServicer):
    def makePost(self, request, context):
        print("make post request")
        make_post_response = pb2.makePostResponse()

        code = make_post(request.post_title, request.post_description, request.seller_contact, request.user_id,
                         request.photo_bytes)

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
        print(f"get post pagination request id(p)=={request.post_id}")

        get_posts_paginated_response = pb2.GetPostPaginatedResponse()
        posts_array = get_posts_paginated(request.post_id, request.limit, request.session_name)
        posts = []

        if posts_array is not None and type(posts_array) is not int:
            if len(posts_array) == 0:
                post = pb2.GetPostResponse()

                post.state = "Empty scroll!"
                post.code = 3
                posts.append(post)
                get_posts_paginated_response.posts.extend(posts)

            for item in posts_array:
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
            post.state = "Server Error (#db)"
            post.code = 3
            posts.append(post)

        get_posts_paginated_response.posts.extend(posts)


        get_posts_paginated_response.posts.extend(posts)

        return get_posts_paginated_response

    def GetFirstPostId(self, request, context):

        get_first_id_response = pb2.GetFirstPostIdResponse()
        print("get first post id request")

        data = get_first_post(request.session_name)

        if data != None:
            get_first_id_response.weight = data[8] + 1

            get_first_id_response.state = "OK"
            get_first_id_response.code = 0
        else:

            get_first_id_response.state = "Server Error (#db)"
            get_first_id_response.code = 1

        return get_first_id_response

    def GetUserPosts(self, request, context):
        print(f'Get user post user: {request.user_id} id: {request.post_id}')
        get_user_post_response = pb2.GetPostPaginatedResponse()

        hash = hashlib.sha256()
        hash.update(request.user_id.to_bytes(8, 'big'))
        token = hash.hexdigest()

        posts_array = get_users_posts_paginated(request.post_id, request.limit, token)
        posts = []

        if posts_array is not None:
            if len(posts_array) == 0:
                post = pb2.GetPostResponse()

                post.state = "Empty scroll!"
                post.code = 3
                posts.append(post)
                get_user_post_response.posts.extend(posts)

            for item in posts_array:
                post = pb2.GetPostResponse()

                post.post_id = item.id
                post.post_title = item.title
                post.photo_bytes = item.photo_bytes
                post.post_description = item.descr
                post.seller_contact = item.seller_contact
                post.creation_time = item.creation_date
                post.user_id = item.from_user
                # post.weight = item.weight
                post.state = "OK"
                post.code = 0

                posts.append(post)

        else:
            post = pb2.GetPostResponse()
            post.state = "Server Error (#db)"
            post.code = 3
            posts.append(post)

        get_user_post_response.posts.extend(posts)

        return get_user_post_response


class PostLiker(pb2_grpc.LikePostServicer):

    def SendLike(self, request, context):
        print(f"Send Like request post:{request.post_id} from:{request.from_user}")

        response = pb2.LikePostResponse()
        response.code = likePost(request.post_id)

        calculate_weight(request.post_id)

        if response.code == 0:
            response.state = "OK"
        else:
            response.state = "Server error"

        return response

    def UnLike(self, request, context):
        print(f"UnLike request post:{request.post_id} from:{request.from_user}")

        response = pb2.UnLikePostResponse()
        response.code = un_likePost(request.post_id)

        calculate_weight(request.post_id)

        if response.code == 0:
            response.state = "OK"
        else:
            response.state = "Server error"

        return response
