from pymongo import MongoClient
from bson import ObjectId
from flask_bcrypt import generate_password_hash, check_password_hash

from app import utils

mongo = utils.Mongo()


class User(object):

    def __init__(self):
        """ User model.

        - _id = ObjectId in mongo
        - display_name = User's name
        - email = User's email (Unique)
        - password = Encrypted user's password
        - status = List of user's status
        - token = User's current token
        """
        self.result = {}

    @staticmethod
    def hash_password(password):
        """ Encrypt a password.

        Parameters
        ----------
        password : str
            Password to be encrypted.

        Returns
        -------
        str
            Encrypted password.
        """
        return generate_password_hash(password).decode('utf8')

    @staticmethod
    def check_password(password, password_attempt):
        """ Verify password.

        Parameters
        ----------
        password : str
            Correct User's password.
        password_attempt: str
            Attempt password.

        Returns
        -------
        bool
            True if same
        """
        return check_password_hash(password, password_attempt)

    def insert(self, data):
        """ Insert a User.

        Parameters
        ----------
        data : dict
            User's data.

        Returns
        -------
        Any
            Inserted User.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        """ hash password """
        data["password"] = self.hash_password(data["password"])
        query = db.insert_one(data)
        """ return user without password """
        result = db.find_one({"_id": ObjectId(query.inserted_id)})
        result.pop("password")
        client.close()
        self.result = mongo.convert_to_json(result)
        return self

    def select_me(self, _id):
        """ Select an User by it's _id.

        Parameters
        ----------
        _id : ObjectId
            User's ObjectId.

        Returns
        -------
        Any
            User.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        result = db.find_one({"_id": ObjectId(_id)}, {"_id": 1, "display_name": 1, "email": 1, "status": 1})
        client.close()
        self.result = mongo.convert_to_json(result)
        return self

    def select_one_by_email(self, email):
        """ Select an User by it's email.

        Parameters
        ----------
        email : str
            User's email.

        Returns
        -------
        Any
            User.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        result = db.find_one({"email": email})
        client.close()
        self.result = mongo.convert_to_json(result)
        return self

    @staticmethod
    def get_user_status(_id):
        """ Select status of a User by it's _id.

        Parameters
        ----------
        _id : str
            User's ObjectId.

        Returns
        -------
        list
            User's status.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        result = db.find_one({"_id": ObjectId(_id)}, {"status": 1})
        client.close()
        try:
            return result["status"]
        except TypeError:
            return []

    @staticmethod
    def get_user_id_by_email(email):
        """ Get ObjectId by email.

        Parameters
        ----------
        email : str
            User's email.

        Returns
        -------
        str
            User's ObjectId stringify.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        result = db.find_one({"email": email}, {"_id": 1})
        client.close()
        return str(result["_id"])
