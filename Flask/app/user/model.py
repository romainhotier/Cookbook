from pymongo import MongoClient
from bson import ObjectId
from flask_bcrypt import generate_password_hash, check_password_hash
from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity


import utils

server = utils.Server
mongo = utils.Mongo


class User(object):
    def __init__(self):
        self.result = {}

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password).decode('utf8')

    @staticmethod
    def check_password(true_password, password_attempt):
        return check_password_hash(true_password, password_attempt)

    def insert(self, data):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        """ hash password """
        data["password"] = self.hash_password(data["password"])
        query = db.insert_one(data)
        result = db.find_one({"_id": ObjectId(query.inserted_id)})
        result.pop("password")
        client.close()
        self.result = mongo.format_json(result)
        return self

    def select_me(self, identifier):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        result = db.find_one({"_id": ObjectId(identifier)}, {"_id": 1, "display_name": 1, "email": 1, "status": 1})
        client.close()
        self.result = mongo.format_json(result)
        return self

    def select_one_by_email(self, email):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        result = db.find_one({"email": email})
        client.close()
        self.result = mongo.format_json(result)
        return self

    @staticmethod
    def check_user_is_unique(email):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        result = db.count_documents({"email": email})
        client.close()
        return result

    @staticmethod
    def get_user_status(identifier):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        result = db.find_one({"_id": ObjectId(identifier)}, {"status": 1})
        client.close()
        try:
            return result["status"]
        except TypeError:
            return []


class Auth(object):

    @staticmethod
    def login_required(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            return f(*args, **kwargs)
        return wrapper

    @staticmethod
    def admin_only(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            if "admin" not in User().get_user_status(get_jwt_identity()):
                return utils.Server.return_response(data=None, api="cookbook", code=403)
            else:
                pass
            return f(*args, **kwargs)
        return wrapper
