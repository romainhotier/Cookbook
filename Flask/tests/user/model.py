from functools import wraps
from flask_jwt_extended import create_access_token
from pymongo import MongoClient
from bson import ObjectId
import copy
import re
import datetime


import run as app
import utils
import app.user.model as user

mongo = utils.Mongo()


class UserTest(object):

    def __init__(self):
        """ UserTest model.

        - _id = ObjectId in mongo
        - display_name = User's name
        - email = User's email (Unique)
        - password = Encrypted user's password
        - status = List of user's status
        - token = User's current token
        """
        self._id = ObjectId()
        self.display_name = "qa_rhr_display_name"
        self.email = "qa@rhr.com"
        self.password = "pwd"
        self.status = []
        self.token = ""

    def display(self):
        """ Print UserTest model.

        Returns
        -------
        Any
            Display UserTest
        """
        print(self.__dict__)

    def get_param(self):
        """ Get UserTest parameters.

        Returns
        -------
        list
            UserTest parameters.
        """
        return [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]

    def get_id(self):
        """ Get _id of UserTest.

        Returns
        -------
        str
            UserTest's _id.
        """
        return str(self._id)

    def get(self):
        """ Get UserTest.

        Returns
        -------
        dict
            Copy of UserTest.
        """
        return copy.deepcopy(self.__dict__)

    def get_without_id(self):
        """ Get UserTest without _id attribute.

        Returns
        -------
        dict
            Copy of UserTest without _id.
        """
        data = self.get()
        data.pop("_id")
        return data

    def get_stringify(self):
        """ Get UserTest with ObjectId stringify.

        Returns
        -------
        dict
            Copy of UserTest with ObjectId stringify.
        """
        return mongo.to_json(self.get())

    def custom(self, data):
        """ Update UserTest.

        Parameters
        ----------
        data : dict
            Data to be updated for UserTest.

        Returns
        -------
        Any
            self.
        """
        for i, j in data.items():
            if i in self.get_param():
                if i == '_id':
                    self.__setattr__(i, ObjectId(j))
                else:
                    self.__setattr__(i, j)
        return self

    def select_ok(self):
        """ Check if UserTest is correct.

        Returns
        -------
        Any
            self.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        usr = db.find_one({"_id": ObjectId(self.get_id())})
        client.close()
        assert user is not None
        assert user.User().check_password(password=usr["password"], password_attempt=self.password)
        for value in usr:
            if value not in ["_id", "password"]:
                assert usr[value] == self.__getattribute__(value)

    def select_ok_by_email(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        user = db.find_one({"email": self.email})
        client.close()
        assert user is not None
        assert user.User().check_password(password=user["password"], password_attempt=self.password)
        for value in user:
            if value not in ["_id", "password"]:
                assert user[value] == self.__getattribute__(value)

    def select_nok(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        result = db.count_documents({"_id": ObjectId(self.get_id())})
        client.close()
        assert result == 0

    def select_nok_by_email(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        result = db.count_documents({"email": self.email})
        client.close()
        assert result == 0

    def select_nok_by_display_name(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        result = db.count_documents({"display_name": self.display_name})
        client.close()
        assert result == 0

    def insert(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        data = self.get_without_id()
        data["password"] = user.User().hash_password(password=self.password)
        query = db.insert_one(data)
        client.close()
        self.__setattr__("_id", query.inserted_id)
        return self

    def delete(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        db.delete_one({"_id": ObjectId(self.get_id())})
        client.close()
        return

    @staticmethod
    def clean():
        rgx = re.compile('.*qa_rhr.*', re.IGNORECASE)
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        db.delete_many({"email": {"$regex": rgx}})
        db.delete_many({"display_name": {"$regex": rgx}})
        client.close()
        return

    def login(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            self.insert()
            with app.backend.app_context():
                expires = datetime.timedelta(seconds=app.backend.config["EXPIRATION_TOKEN"])
                access_token = create_access_token(identity=str(self._id), expires_delta=expires)
            f(*args, **kwargs, headers={"Authorization": "Bearer " + access_token}, user=self)
            return self
        return wrapper
