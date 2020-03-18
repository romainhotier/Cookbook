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

    @staticmethod
    def get_all_file_by_id_parent(_id_parent):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_fs_files]
        result = db.find({"metadata._id": ObjectId(_id_parent)})
        client.close()
        return result

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


class FileTest(object):

    def __init__(self):
        self._id = ""
        self.filename = "qa_rhr_filename"
        self.content_type = 'text/plain'
        self.data = b'test file qa rhr',
        self.metadata = {"kind": "kind_file",
                         "_id": ObjectId(),
                         "is_main": False}

    def display(self):
        print(self._id)
        print(self.filename)
        print(self.data[0].decode("utf-8"))
        print(self.metadata)

    def get_id(self):
        return str(self._id)

    def set_id(self, identifier):
        self._id = identifier
        return self

    def get_data(self):
        return self.data[0].decode("utf-8")

    def get_data_for_enrichment(self):
        return {"_id": self._id, "is_main": self.metadata["is_main"]}

    def custom_filename(self, filename):
        self.filename = filename
        return self

    def custom_metadata(self, data):
        for i, j in data.items():
            if i in ["kind", "is_main"]:
                self.metadata[i] = j
            elif i in ["_id"]:
                self.metadata[i] = ObjectId(j)
        return self

    def insert(self):
        client = MongoClient(mongo.ip, mongo.port)
        fs = gridfs.GridFS(client[mongo.name])
        _id = fs.put(self.data[0], content_type=self.content_type, filename=self.filename, metadata=self.metadata)
        self._id = _id
        client.close()
        return self

    def select_if_present_by_id(self):
        client = MongoClient(mongo.ip, mongo.port)
        fs = gridfs.GridFS(client[mongo.name])
        assert fs.exists(_id=ObjectId(self._id))

    def select_ok(self):
        client = MongoClient(mongo.ip, mongo.port)
        """ check file file exist """
        self.select_if_present_by_id()
        """ check metadata and more """
        db = client[mongo.name][mongo.collection_fs_files]
        result = db.find_one({"_id": ObjectId(self.get_id())})
        client.close()
        assert result["filename"] == self.filename
        assert result["metadata"] == self.metadata

    def select_nok(self):
        client = MongoClient(mongo.ip, mongo.port)
        fs = gridfs.GridFS(client[mongo.name])
        assert not fs.exists({"_id": ObjectId(self.get_id())})

    def select_nok_by_filename(self):
        client = MongoClient(mongo.ip, mongo.port)
        fs = gridfs.GridFS(client[mongo.name])
        assert not fs.exists({"filename": self.filename})

    @staticmethod
    def clean():
        rgx = re.compile('.*qa_rhr.*', re.IGNORECASE)
        client = MongoClient(mongo.ip, mongo.port)
        """ select file testfile """
        db = client[mongo.name][mongo.collection_fs_files]
        files_to_clean = db.find({"filename": rgx})
        """ delete gridfs """
        fs = gridfs.GridFS(client[mongo.name])
        for test_file in files_to_clean:
            fs.delete(file_id=test_file["_id"])
        client.close()
        return
