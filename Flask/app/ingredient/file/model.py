from pymongo import MongoClient
import gridfs
from bson import ObjectId
import mimetypes
import re
import copy
import json

from server import mongo_config as mongo_conf

mongo = mongo_conf.MongoConnection()
json_format = mongo_conf.JSONEncoder()


class IngredientFile(object):

    def __init__(self):
        self.list_param = ["name"]

    @staticmethod
    def put_file(path, filename, is_profil):
        client = MongoClient(mongo.ip, mongo.port)
        fs = gridfs.GridFS(client[mongo.name])
        with open(path, "rb") as f:
            fs.put(f.read(), content_type=mimetypes.guess_type(url=path)[0], filename=filename, metadata={"type": "ingredient", "is profil": is_profil})
        client.close()
        return

    @staticmethod
    def select_one(_id):
        client = MongoClient(mongo.ip, mongo.port)
        fs = gridfs.GridFS(client[mongo.name])
        f = fs.get(ObjectId(_id))
        client.close()
        return f


#a= IngredientFile()
#a.put_file(path="C:/Users/Arkane/Desktop/Cookbook/Flask/app/ingredient/file/test/PostIngredientFile/example.txt", filename="text", is_profil=False)
#a.put_file(path="C:/Users/Arkane/Desktop/Cookbook/Flask/app/ingredient/file/test/PostIngredientFile/file_png.png", filename="photo", is_profil=False)
#a.select_debug()