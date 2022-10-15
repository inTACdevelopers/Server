from io import BytesIO

import services.YmlParser.yml_pb2 as pb2
import  services.YmlParser.yml_pb2_grpc as pb2_grpc
from services.YmlParser.parser import *
from database.posts import *


class YmlUploaderServise(pb2_grpc.YmlPostMakerServicer):
    def UploadPosts(self, request, context):
        print("Yml Upload posts request")

        response = pb2.UploadResponse()

        try:
            xml_file_name = getyml(request.url)
            for item in parse_offersinfo_yml(xml_file_name):
                for id in item.keys():
                    curr_good = item[id]

                    if 'name' in curr_good.keys():
                        title = curr_good['name']
                    else:
                        title = curr_good['typePrefix'] + " " + curr_good['vendor'] + " " + curr_good['model']

                    description = curr_good['description']

                    contact = curr_good['url']
                    image = curr_good['picture']

                    response = requests.get(image, stream=True)
                    photo = BytesIO(response.content).read()

                    make_post(title, description, contact, request.from_user, photo)
            response.code = 0
            response.state = "OK"
        except Exception as ex:
            print(f"Error YmlUploaderServise -- UploadPosts")
            print(ex)
            response.code = 1
            response.state = "Server error Try again"
        finally:
            if os.path.exists(xml_file_name):
                os.remove(xml_file_name)
            return response

