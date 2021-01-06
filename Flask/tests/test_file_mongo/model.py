from pymongo import MongoClient
import gridfs
from bson import ObjectId
import copy
import re

import utils

mongo = utils.Mongo()


class FileMongoTest(object):

    def __init__(self):
        """ FileMongoTest model.

        - _id = ObjectId in mongo
        - content_type = File's content_type
        - data = File's raw data
        - filename = File's name
        - metadata = File's information
        """
        self._id = ""
        self.filename = "qa_rhr_filename"
        self.content_type = 'text/plain'
        self.data = b'test file qa rhr',
        self.metadata = {"kind": "kind_file",
                         "_id_parent": ObjectId(),
                         "is_main": False}

    def display(self):
        """ Print FileMongoTest model.

        Returns
        -------
        Any
            Display FileMongoTest.
        """
        print(self.__dict__)

    def get_param(self):
        """ Get FileMongoTest parameters.

        Returns
        -------
        list
            FileMongoTest parameters.
        """
        return [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]

    def get_id(self):
        """ Get FileMongoTest's _id.

        Returns
        -------
        str
            FileMongoTest's _id.
        """
        return str(self._id)

    def get_is_main(self):
        """ Get FileMongoTest's metadata.is_main.

        Returns
        -------
        str
            FileMongoTest's is_main.
        """
        return self.metadata["is_main"]

    def get_data(self):
        """ Get FileMongoTest's data.

        Returns
        -------
        str
            FileMongoTest's data.
        """
        return copy.deepcopy(self.data[0].decode("utf-8"))

    def get_enrichment(self):
        """ Get FileMongoTest's enrichment data.

        Returns
        -------
        str
            FileMongoTest's enrichment data.
        """
        return {"_id": str(self._id), "is_main": self.get_is_main()}

    def insert(self):
        """ Insert FileMongoTest.

        Returns
        -------
        FileMongoTest
            Self
        """
        client = MongoClient(mongo.ip, mongo.port)
        fs = gridfs.GridFS(client[mongo.name])
        _id = fs.put(self.data[0], content_type=self.content_type, filename=self.filename, metadata=self.metadata)
        self._id = _id
        client.close()
        return self

    def custom(self, data):
        """ Update FileMongoTest.

        Parameters
        ----------
        data : dict
            Data to be updated for FileMongoTest.

        Returns
        -------
        FileMongoTest
            Self
        """
        for i, j in data.items():
            if i in self.get_param():
                if i == '_id':
                    self.__setattr__(i, ObjectId(j))
                else:
                    self.__setattr__(i, j)
        return self

    def custom_is_main(self, is_main):
        """ Update FileMongoTest's is_main.

        Parameters
        ----------
        is_main : bool
            Is_main's value.

        Returns
        -------
        FileMongoTest
            Self
        """
        self.metadata["is_main"] = is_main
        return self

    def custom_id_from_body(self, data):
        """ Update FileMongoTest's filename from PostIngredientFile's body.

        Parameters
        ----------
        data : dict
            PostIngredientFile's body.

        Returns
        -------
        FileMongoTest
            Self
        """
        self.__setattr__("filename", data["filename"])
        return self

    def check_exist_by_id(self):
        """ Check if FileMongoTest exist by ObjectId.
        """
        client = MongoClient(mongo.ip, mongo.port)
        fs = gridfs.GridFS(client[mongo.name])
        client.close()
        assert fs.exists(_id=ObjectId(self._id))

    def check_bdd_data(self):
        """ Check if FileMongoTest.
        """
        client = MongoClient(mongo.ip, mongo.port)
        """ check file file exist """
        self.check_exist_by_id()
        """ check metadata and more """
        db = client[mongo.name][mongo.collection_fs_files]
        file = db.find_one({"_id": ObjectId(self.get_id())})
        client.close()
        assert file["filename"] == self.filename
        assert file["metadata"] == self.metadata

    def check_doesnt_exist_by_id(self):
        """ Check if FileMongoTest doesn't exist.
        """
        client = MongoClient(mongo.ip, mongo.port)
        fs = gridfs.GridFS(client[mongo.name])
        client.close()
        assert not fs.exists({"_id": ObjectId(self.get_id())})

    def check_doesnt_exist_by_filename(self):
        """ Check if FileMongoTest doesn't exist by filename.
        """
        client = MongoClient(mongo.ip, mongo.port)
        fs = gridfs.GridFS(client[mongo.name])
        client.close()
        assert not fs.exists({"filename": self.filename})

    @staticmethod
    def clean():
        """ Clean FileMongoTest by filename.
        """
        rgx = re.compile('.*qa_rhr.*', re.IGNORECASE)
        client = MongoClient(mongo.ip, mongo.port)
        """ select file testfile """
        db = client[mongo.name][mongo.collection_fs_files]
        files_to_clean = db.find({"filename": {"$regex": rgx}})
        """ delete gridfs """
        fs = gridfs.GridFS(client[mongo.name])
        for test_file in files_to_clean:
            fs.delete(file_id=test_file["_id"])
        client.close()
        return
