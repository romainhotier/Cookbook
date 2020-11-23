from pymongo import MongoClient
import gridfs
from bson import ObjectId
import copy
import re

import utils

mongo = utils.Mongo()


class FileTest(object):

    def __init__(self):
        """ FileTest model.

        - _id = ObjectId in mongo
        - filename = File's name
        - content_type = File's content_type
        - data = File's raw data
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
        """ Print FileTest model.

        Returns
        -------
        Any
            Display FileTest.
        """
        print(self.__dict__)

    def get_param(self):
        """ Get FileTest parameters.

        Returns
        -------
        list
            FileTest parameters.
        """
        return [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]

    def get_id(self):
        """ Get FileTest's _id.

        Returns
        -------
        str
            FileTest's _id.
        """
        return str(self._id)

    def get_is_main(self):
        """ Get FileTest's metadata.is_main.

        Returns
        -------
        str
            FileTest's is_main.
        """
        return self.metadata["is_main"]

    def get_data(self):
        """ Get FileTest's data.

        Returns
        -------
        str
            FileTest's data.
        """
        return copy.deepcopy(self.data[0].decode("utf-8"))

    def get_for_enrichment(self):
        """ Get FileTest's _id and is_main for enrichment.

        Returns
        -------
        dict
            FileTest's info for enrichment.
            - _id
            - is_main
        """
        return copy.deepcopy({"_id": self._id, "is_main": self.metadata["is_main"]})

    def custom(self, data):
        """ Update FileTest.

        Parameters
        ----------
        data : dict
            Data to be updated for FileTest.

        Returns
        -------
        Any
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
        """ Update FileTest's is_main.

        Parameters
        ----------
        is_main : bool
            Is_main's value.

        Returns
        -------
        Any
            Self
        """
        self.metadata["is_main"] = is_main
        return self

    def insert(self):
        """ Insert FileTest.

        Returns
        -------
        Any
            Self
        """
        client = MongoClient(mongo.ip, mongo.port)
        fs = gridfs.GridFS(client[mongo.name])
        _id = fs.put(self.data[0], content_type=self.content_type, filename=self.filename, metadata=self.metadata)
        self._id = _id
        client.close()
        return self

    def select_if_present_by_id(self):
        """ Check if FileTest exist by ObjectId.
        """
        client = MongoClient(mongo.ip, mongo.port)
        fs = gridfs.GridFS(client[mongo.name])
        client.close()
        assert fs.exists(_id=ObjectId(self._id))

    def select_ok(self):
        """ Check if FileTest.
        """
        client = MongoClient(mongo.ip, mongo.port)
        """ check file file exist """
        self.select_if_present_by_id()
        """ check metadata and more """
        db = client[mongo.name][mongo.collection_fs_files]
        file = db.find_one({"_id": ObjectId(self.get_id())})
        client.close()
        assert file["filename"] == self.filename
        assert file["metadata"] == self.metadata

    def select_nok(self):
        """ Check if FileTest doesn't exist.
        """
        client = MongoClient(mongo.ip, mongo.port)
        fs = gridfs.GridFS(client[mongo.name])
        client.close()
        assert not fs.exists({"_id": ObjectId(self.get_id())})

    def select_nok_by_filename(self):
        """ Check if FileTest doesn't exist by filename.
        """
        client = MongoClient(mongo.ip, mongo.port)
        fs = gridfs.GridFS(client[mongo.name])
        client.close()
        assert not fs.exists({"filename": self.filename})

    @staticmethod
    def clean():
        """ Clean FileTest by filename.
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
