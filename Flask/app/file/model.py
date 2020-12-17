from pymongo import MongoClient
import gridfs
from bson import ObjectId
import mimetypes

import utils

mongo = utils.Mongo()


class File(object):

    def __init__(self):
        """ User model.

        - _id = ObjectId in mongo
        - filename = File's name
        - metadata.kind = Parent's Type
        - metadata._id_parent = Parent's ObjectId
        - metadata.is_main = Is primary or not
        """
        self.result = {}

    def insert(self, kind, _id_parent, metadata):
        """ Insert a File.

        Parameters
        ----------
        kind : str
            Parent's type.
        _id_parent : str
            Parent's ObjectId.
        metadata : dict
            File's metadata.

        Returns
        -------
        str
            Inserted ObjectId.
        """
        client = MongoClient(mongo.ip, mongo.port)
        fs = gridfs.GridFS(client[mongo.name])
        """ check is_main """
        if metadata["is_main"]:
            self.erase_is_main_if_exist(_id_parent=_id_parent)
        """ insert """
        with open(metadata["path"], "rb") as f:
            _id = fs.put(f.read(),
                         content_type=mimetypes.guess_type(url=metadata["path"])[0],
                         filename=metadata["filename"],
                         metadata={"kind": kind,
                                   "_id_parent": ObjectId(_id_parent),
                                   "is_main": metadata["is_main"]})
        client.close()
        return str(_id)

    @staticmethod
    def select_one(_id):
        """ Get a File by it's ObjectId.

        Parameters
        ----------
        _id : str
            File's ObjectId.

        Returns
        -------
        Any
            Raw File.
        """
        client = MongoClient(mongo.ip, mongo.port)
        fs = gridfs.GridFS(client[mongo.name])
        f = fs.get(ObjectId(_id))
        client.close()
        return f

    def get_all_file_by_id_parent(self, _id_parent):
        """ Get all Files for a parent.

        Parameters
        ----------
        _id_parent : str
            Parent's ObjectId.

        Returns
        -------
        Any
            List of parent's Files.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_fs_files]
        cursor = db.find({"metadata._id_parent": ObjectId(_id_parent)})
        client.close()
        self.result = [file for file in cursor]
        return self

    @staticmethod
    def delete(_id):
        """ Delete a File.

        Parameters
        ----------
        _id : str
            File's ObjectId.
        """
        client = MongoClient(mongo.ip, mongo.port)
        fs = gridfs.GridFS(client[mongo.name])
        fs.delete(ObjectId(_id))
        client.close()
        return

    @staticmethod
    def clean_file_by_id_parent(_id_parent):
        """ Delete all Files associated to a parent.

        Parameters
        ----------
        _id_parent : str
            Parent's ObjectId.
        """
        client = MongoClient(mongo.ip, mongo.port)
        """ file all files """
        db = client[mongo.name][mongo.collection_fs_files]
        files = db.find({"metadata._id_parent": ObjectId(_id_parent)})
        """ delete files """
        fs = gridfs.GridFS(client[mongo.name])
        for file in files:
            fs.delete(ObjectId(file["_id"]))
        client.close()
        return

    def set_is_main_true(self, _id):
        """ Set is_main to True.

        Parameters
        ----------
        _id : str
            File's ObjectId.

        Returns
        -------
        str
            Parent's ObjectId.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_fs_files]
        _id_parent = db.find_one({"_id": ObjectId(_id)})["metadata"]["_id_parent"]
        self.erase_is_main_if_exist(_id_parent=_id_parent)
        db.update_one({"_id": ObjectId(_id)}, {'$set': {"metadata.is_main": True}})
        client.close()
        return str(_id_parent)

    @staticmethod
    def erase_is_main_if_exist(_id_parent):
        """ Set is_main to False if there was a primary File.

        Parameters
        ----------
        _id_parent : str
            Parent's ObjectId.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_fs_files]
        db.update_one({'$and': [{"metadata._id_parent": ObjectId(_id_parent)}, {"metadata.is_main": True}]},
                      {'$set': {"metadata.is_main": False}})
        client.close()
        return