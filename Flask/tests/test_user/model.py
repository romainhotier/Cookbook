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
user = user.User()


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

    def get_stringify(self):
        """ Get UserTest with ObjectId stringify.

        Returns
        -------
        dict
            Copy of UserTest with ObjectId stringify.
        """
        return mongo.to_json(self.get())

    def insert(self):
        """ Insert UserTest.

        Returns
        -------
        UserTest
            Self
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        data = self.get()
        data.pop("_id")
        data["password"] = user.hash_password(password=self.password)
        query = db.insert_one(data)
        client.close()
        self.__setattr__("_id", query.inserted_id)
        return self

    def custom(self, data):
        """ Update UserTest.

        Parameters
        ----------
        data : dict
            Data to be updated for UserTest.

        Returns
        -------
        UserTest
            Self
        """
        for i, j in data.items():
            if i in self.get_param():
                if i == '_id':
                    self.__setattr__(i, ObjectId(j))
                else:
                    self.__setattr__(i, j)
        return self

    def custom_id_from_body(self, data):
        """ Update UserTest's _id from PostUserLogin's body.

        Parameters
        ----------
        data : dict
            PostUserLogin's body.

        Returns
        -------
        RecipeTest
            Self
        """
        self.__setattr__("_id", ObjectId(data["data"]["_id"]))
        return self

    def check_bdd_data(self):
        """ Check if UserTest is correct.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        result = db.find_one({"_id": ObjectId(self.get_id())})
        client.close()
        assert result is not None
        assert user.check_password(password=result["password"], password_attempt=self.password)
        for value in result:
            if value not in ["_id", "password"]:
                assert result[value] == self.__getattribute__(value)

    def check_bdd_data_by_email(self):
        """ Check if UserTest is correct by email.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        result = db.find_one({"email": self.email})
        client.close()
        assert result is not None
        assert user.check_password(password=result["password"], password_attempt=self.password)
        for value in result:
            if value not in ["_id", "password"]:
                assert result[value] == self.__getattribute__(value)

    def check_doesnt_exist_by_id(self):
        """ Check if UserTest doesn't exist.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        result = db.count_documents({"_id": ObjectId(self.get_id())})
        client.close()
        assert result == 0

    def check_doesnt_exist_by_email(self):
        """ Check if UserTest doesn't exist by email.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        result = db.count_documents({"email": self.email})
        client.close()
        assert result == 0

    def check_doesnt_exist_by_display_name(self):
        """ Check if UserTest doesn't exist by display_name.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        result = db.count_documents({"display_name": self.display_name})
        client.close()
        assert result == 0

    def delete(self):
        """ Delete UserTest.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        db.delete_one({"_id": ObjectId(self.get_id())})
        client.close()
        return

    @staticmethod
    def clean():
        """ Clean UserTest by email and display_name.
        """
        rgx = re.compile('.*qa_rhr.*', re.IGNORECASE)
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        db.delete_many({"email": {"$regex": rgx}})
        db.delete_many({"display_name": {"$regex": rgx}})
        client.close()
        return

    def login(self, f):
        """ Wrapper to login.
        """
        @wraps(f)
        def wrapper(*args, **kwargs):
            self.insert()
            with app.backend.app_context():
                expires = datetime.timedelta(seconds=app.backend.config["EXPIRATION_TOKEN"])
                access_token = create_access_token(identity=str(self._id), expires_delta=expires)
            f(*args, **kwargs, headers={"Authorization": "Bearer " + access_token}, user=self)
            return self
        return wrapper