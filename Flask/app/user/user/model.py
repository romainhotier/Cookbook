from pymongo import MongoClient
from bson import ObjectId
import json
import copy
import re
from flask_bcrypt import generate_password_hash, check_password_hash
from server import mongo_config as mongo_conf

mongo = mongo_conf.MongoConnection()
json_format = mongo_conf.JSONEncoder()


class User(object):
    def __init__(self):
        self.list_param = ["display_name", "email", "password"]
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
        self.result = result
        return self

    @staticmethod
    def select_one_by_email(email):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        result = db.find_one({"email": email})
        client.close()
        return result

    def get_result(self):
        return json.loads(json_format.encode(self.result))


class UserTest(object):
    def __init__(self):
        self.data = {"_id": "",
                     "display_name": "",
                     "email": "a@a.com",
                     "password": "adm"
                     }

    def display(self):
        print(self.data)

    def get_data(self):
        return self.data

    def get_data_stringify_object_id(self):
        return json.loads(json_format.encode(self.data))

    def get_data_without_id(self):
        data_without_id = copy.deepcopy(self.get_data())
        data_without_id.pop("_id")
        return data_without_id

    def get_id(self):
        return str(self.data["_id"])

    def set_id(self, _id):
        self.data["_id"] = _id

    def delete_id(self):
        self.data.pop("_id")

    def get_data_value(self, value):
        return self.data[value]

    def custom(self, data):
        for i, j in data.items():
            if i in ["_id", "display_name", "email", "password"]:
                self.data[i] = j
        return self

    def custom_test(self, data):
        for i, j in data.items():
            if i in ["_id", "display_name", "email", "password"]:
                self.data[i] = j
        self.data["email"] = "qa_rhr" + self.data["email"]
        return self

    def select_ok(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        result = db.find({"_id": ObjectId(self.get_id())})
        client.close()
        assert result.count() == 1
        assert isinstance(result[0]["_id"], ObjectId)
        assert User().check_password(true_password=result[0]["password"], password_attempt=self.data["password"])
        for value in result[0]:
            if value not in ["_id", "password"]:
                assert result[0][value] == self.data[value]

    def select_ok_by_email(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        result = db.find({"email": self.data['email']})
        client.close()
        assert result.count() == 1
        assert isinstance(result[0]["_id"], ObjectId)
        for value in result[0]:
            if value not in ["_id"]:
                assert result[0][value] == self.data[value]

    def select_nok(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        result = db.count_documents({"_id": ObjectId(self.get_id())})
        client.close()
        assert result == 0

    def select_nok_by_email(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        result = db.count_documents({"email": self.data['email']})
        client.close()
        assert result == 0

    def select_nok_by_display_name(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        result = db.count_documents({"display_name": self.data['display_name']})
        client.close()
        assert result == 0

    def insert(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_user]
        self.delete_id()
        data = copy.deepcopy(self.get_data())
        data["password"] = User().hash_password(password=self.data["password"])
        query = db.insert_one(data)
        client.close()
        self.set_id(query.inserted_id)
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
        db.delete_many({"email": rgx})
        db.delete_many({"display_name": rgx})
        client.close()
        return
