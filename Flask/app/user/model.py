from pymongo import MongoClient
from bson import ObjectId
from flask_bcrypt import generate_password_hash, check_password_hash
import utils

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
