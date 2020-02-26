from pymongo import MongoClient
from bson import ObjectId

import mongo_config as mongo_conf

mongo = mongo_conf.MongoConnection()
json_format = mongo_conf.JSONEncoder()


class Steps(object):

    def __init__(self):
        self.list_param = ["step", "position"]

    @staticmethod
    def get_steps_length(_id):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        if result is None:
            return 0
        else:
            steps_length = len(result["steps"])
            return steps_length

    @staticmethod
    def insert(_id, data):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        new_step = data["step"]
        if "position" in data.keys():
            position = data["position"]
            db.update_one({"_id": ObjectId(_id)}, {'$push': {"steps": {"$each": [new_step], "$position": position}}})
        else:
            db.update_one({"_id": ObjectId(_id)}, {'$push': {"steps": {"$each": [new_step]}}})
        """ return result """
        result = db.find({"_id": ObjectId(_id)})
        client.close()
        return result

    @staticmethod
    def delete(_id, position):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.update_one({"_id": ObjectId(_id)}, {'$unset': {"steps.{}".format(position): 1}})
        db.update_one({"_id": ObjectId(_id)}, {'$pull': {"steps": None}})
        """ return result """
        result = db.find({"_id": ObjectId(_id)})
        client.close()
        return result


"""
    @staticmethod
    def update(_id, data):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.update_one({"_id": ObjectId(_id)}, {'$set': data})
        result = db.find({"_id": ObjectId(_id)})
        client.close()
        return result

    @staticmethod
    def delete(_id):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.delete_one({"_id": ObjectId(_id)})
        client.close()
        return
"""

"""
class RecipeTest(object):

    def __init__(self):
        self.data = {"_id": "",
                     "title": "",
                     "level": "",
                     "resume": "",
                     "cooking_time": "",
                     "preparation_time": "",
                     "nb_people": "",
                     "note": "",
                     "ingredients": {},
                     "steps": []
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
            if i in Recipe().list_param or i == "_id":
                self.data[i] = j
        return self

    def custom_test(self, data):
        for i, j in data.items():
            if i in Recipe().list_param or i == "_id":
                self.data[i] = j
        self.data["title"] = self.data["title"] + "qa_rhr"
        return self

    def select_ok(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.find({"_id": ObjectId(self.get_id())})
        client.close()
        assert result.count() == 1
        assert isinstance(result[0]["_id"], ObjectId)
        for value in result[0]:
            if value not in ["_id"]:
                assert result[0][value] == self.data[value]

    def select_ok_by_title(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.find({"title": self.data['title']})
        client.close()
        assert result.count() == 1
        assert isinstance(result[0]["_id"], ObjectId)
        for value in result[0]:
            if value not in ["_id"]:
                assert result[0][value] == self.data[value]

    def select_nok(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.count_documents({"_id": ObjectId(self.get_id())})
        client.close()
        assert result == 0

    def select_nok_by_title(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.count_documents({"title": self.data['title']})
        client.close()
        assert result == 0

    def insert(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        self.delete_id()
        query = db.insert_one(self.get_data())
        client.close()
        self.set_id(query.inserted_id)
        return self

    def delete(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.delete_one({"_id": ObjectId(self.get_id())})
        client.close()
        return

    @staticmethod
    def clean():
        rgx = re.compile('.*qa_rhr.*', re.IGNORECASE)
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.delete_many({"title": rgx})
        client.close()
        return
"""
