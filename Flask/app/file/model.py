from pymongo import MongoClient
import gridfs
from bson import ObjectId
import mimetypes

import utils

mongo = utils.Mongo


class File(object):

    def __init__(self):
        self.result = {}

    def insert(self, kind, _id_parent, metadata):
        client = MongoClient(mongo.ip, mongo.port)
        fs = gridfs.GridFS(client[mongo.name])
        if metadata["is_main"]:
            self.erase_is_main_if_exist(_id_parent=_id_parent)
        with open(metadata["path"], "rb") as f:
            _id = fs.put(f.read(),
                         content_type=mimetypes.guess_type(url=metadata["path"])[0],
                         filename=metadata["filename"],
                         metadata={"kind": kind, "_id": ObjectId(_id_parent), "is_main": metadata["is_main"]})
        client.close()
        return _id

    @staticmethod
    def select_one(_id):
        client = MongoClient(mongo.ip, mongo.port)
        fs = gridfs.GridFS(client[mongo.name])
        f = fs.get(ObjectId(_id))
        client.close()
        return f

    @staticmethod
    def erase_is_main_if_exist(_id_parent):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_fs_files]
        db.update_one({'$and': [{"metadata._id": ObjectId(_id_parent)}, {"metadata.is_main": True}]},
                      {'$set': {"metadata.is_main": False}})
        client.close()
        return

    def get_all_file_by_id_parent(self, _id_parent):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_fs_files]
        cursor = db.find({"metadata._id": ObjectId(_id_parent)})
        client.close()
        self.result = [file for file in cursor]
        return self

    @staticmethod
    def delete(_id):
        client = MongoClient(mongo.ip, mongo.port)
        fs = gridfs.GridFS(client[mongo.name])
        fs.delete(ObjectId(_id))
        client.close()
        return

    @staticmethod
    def clean_file_by_id_parent(_id_parent):
        client = MongoClient(mongo.ip, mongo.port)
        """ file all files """
        db = client[mongo.name][mongo.collection_fs_files]
        files = db.find({"metadata._id": ObjectId(_id_parent)})
        """ delete files """
        fs = gridfs.GridFS(client[mongo.name])
        for file in files:
            fs.delete(ObjectId(file["_id"]))
        client.close()
        return

    def set_is_main_true(self, _id):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_fs_files]
        _id_parent = db.find_one({"_id": ObjectId(_id)})["metadata"]["_id"]
        self.erase_is_main_if_exist(_id_parent=_id_parent)
        db.update_one({"_id": ObjectId(_id)}, {'$set': {"metadata.is_main": True}})
        client.close()
        return _id_parent
