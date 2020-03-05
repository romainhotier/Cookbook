from pymongo import MongoClient
import gridfs
from bson import ObjectId
import mimetypes
import re


from server import mongo_config as mongo_conf

mongo = mongo_conf.MongoConnection()


class File(object):

    def __init__(self):
        self.list_param = ["path", "filename", "is_main"]

    @staticmethod
    def insert(kind, _id_parent, metadata):
        client = MongoClient(mongo.ip, mongo.port)
        fs = gridfs.GridFS(client[mongo.name])
        with open(metadata["path"], "rb") as f:
            _id = fs.put(f.read(),
                         content_type=mimetypes.guess_type(url=metadata["path"])[0],
                         filename=metadata["filename"],
                         metadata={"kind": kind, "_id": _id_parent, "is_main": metadata["is_main"]})
        client.close()
        return _id

    @staticmethod
    def select_one(_id):
        client = MongoClient(mongo.ip, mongo.port)
        fs = gridfs.GridFS(client[mongo.name])
        f = fs.get(ObjectId(_id))
        client.close()
        return f


class FileTest(object):

    def __init__(self):
        self._id = ""
        self.data = b'test file qa rhr',
        self.content_type = 'text/plain'
        self.filename = "qa_rhr_filename"
        self.metadata = {"kind": "kind_file",
                         "is_main": False}

    def display(self):
        print(self.data)

    def get_id(self):
        return str(self._id)

    def get_data(self):
        return self.data[0].decode("utf-8")

    def insert(self):
        client = MongoClient(mongo.ip, mongo.port)
        fs = gridfs.GridFS(client[mongo.name])
        _id = fs.put(self.data[0], content_type=self.content_type, filename=self.filename, metadata=self.metadata)
        self._id = _id
        client.close()
        return self

    @staticmethod
    def clean():
        rgx = re.compile('.*qa_rhr.*', re.IGNORECASE)
        client = MongoClient(mongo.ip, mongo.port)
        """ select all testfile """
        db = client[mongo.name][mongo.collection_fs_files]
        files_to_clean = db.find({"filename": rgx})
        """ delete gridfs """
        fs = gridfs.GridFS(client[mongo.name])
        for test_file in files_to_clean:
            fs.delete(file_id=test_file["_id"])
        client.close()
        return
