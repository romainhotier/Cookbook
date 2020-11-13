from pymongo import MongoClient
from bson import ObjectId
from functools import wraps
from flask import abort
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

import utils

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
        """ return user """
        result = db.find_one({"_id": ObjectId(query.inserted_id)})
        result.pop("password")
        client.close()
        self.result = mongo.to_json(result)
        return self

    def select_me(self, identifier):
        """ Select an User by it's _id.

        Parameters
        ----------
        identifier : ObjectId
            User's ObjectId.

        Returns
        -------
        Any
            User.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        result = db.find_one({"_id": ObjectId(identifier)}, {"_id": 1, "display_name": 1, "email": 1, "status": 1})
        client.close()
        self.result = mongo.to_json(result)
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
        self.result = mongo.to_json(result)
        return self

    @staticmethod
    def check_user_is_unique(email):
        """ Check if an email already exist.

        Parameters
        ----------
        email : str
            User's email.

        Returns
        -------
        bool
            True if email doesn't exist in mongo.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        result = db.count_documents({"email": email})
        client.close()
        if result == 0:
            return True
        else:
            return False

    @staticmethod
    def get_user_status(identifier):
        """ Select status of a User by it's _id.

        Parameters
        ----------
        identifier : str
            User's ObjectId.

        Returns
        -------
        list
            User's status.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        result = db.find_one({"_id": ObjectId(identifier)}, {"status": 1})
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


class Auth(object):

    @staticmethod
    def login_required(f):
        """ Wrapper to check auth.

        Returns
        -------
        Any
           Auth_handler if authentification failed.
        """
        @wraps(f)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            return f(*args, **kwargs)
        return wrapper

    @staticmethod
    def admin_only(f):
        """ Wrapper to check if User is an admin.

        Returns
        -------
        Any
           Server response.
        """
        @wraps(f)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            if "admin" not in User().get_user_status(get_jwt_identity()):
                return abort(status=403)
            else:
                pass
            return f(*args, **kwargs)
        return wrapper
