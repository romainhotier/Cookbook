from flask import abort
from pymongo import MongoClient
from bson import ObjectId
from os import path

from server import factory as factory, mongo_config as mongo_conf

server = factory.Server()
mongo = mongo_conf.MongoConnection()


class Validator(object):

    @staticmethod
    def is_object_id(_id):
        """ check _id is a correcte ObjectId type """
        if len(_id) != 24:
            detail = {"param": "_id", "msg": server.detail_must_be_an_object_id, "value": _id}
            return abort(400, description=detail)
        else:
            return False

    @staticmethod
    def is_object_id_in_collection(_id, collection):
        """ check objectId is present in a collection """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][collection]
        result = db.count_documents({"_id": ObjectId(_id)})
        client.close()
        if result == 0:
            detail = {"param": "_id", "msg": server.detail_doesnot_exist, "value": _id}
            return abort(400, description=detail)
        else:
            return True

    @staticmethod
    def is_string(param, value):
        """ check param is string """
        if isinstance(value, str):
            return True
        else:
            detail = {"param": param, "msg": server.detail_must_be_a_string, "value": value}
            return abort(400, description=detail)

    @staticmethod
    def is_int(param, value):
        """ check param is int """
        if isinstance(value, int):
            return True
        else:
            try:
                int(value)
                return True
            except (ValueError, TypeError):
                detail = {"param": param, "msg": server.detail_must_be_an_integer, "value": value}
                return abort(400, description=detail)

    @staticmethod
    def is_array(param, value):
        """ check param is array """
        if isinstance(value, list):
            return True
        else:
            detail = {"param": param, "msg": server.detail_must_be_an_array, "value": value}
            return abort(400, description=detail)

    @staticmethod
    def is_object(param, value):
        """ check param is object """
        if isinstance(value, dict):
            return True
        else:
            detail = {"param": param, "msg": server.detail_must_be_an_object, "value": value}
            return abort(400, description=detail)

    @staticmethod
    def is_boolean(param, value):
        """ check param is boolean """
        if isinstance(value, bool):
            return True
        else:
            detail = {"param": param, "msg": server.detail_must_be_a_boolean, "value": value}
            return abort(400, description=detail)

    @staticmethod
    def is_string_non_empty(param, value):
        """ check param is string non empty"""
        if value.strip() == "":
            detail = {"param": param, "msg": server.detail_must_be_not_empty, "value": value}
            return abort(400, description=detail)
        else:
            return True

    @staticmethod
    def is_mandatory(param, data):
        """ check param is string """
        if param in data.keys():
            return True
        else:
            detail = {"param": param, "msg": server.detail_is_required}
            return abort(400, description=detail)

    @staticmethod
    def is_between_x_y(param, value, x, y):
        """ check param is between x and y """
        if x <= value <= y:
            return True
        else:
            detail = {"param": param, "msg": server.detail_must_be_between + " {0} and {1}".format(x, y),
                      "value": value}
            return abort(400, description=detail)

    @staticmethod
    def is_in(param, value, values):
        """ check param is in values """
        if param in values:
            return True
        else:
            detail = {"param": param, "msg": server.detail_must_be_in + values, "value": value}
            return abort(400, description=detail)

    @staticmethod
    def is_path_exist(param, value):
        """ check if path exist """
        if path.exists(value):
            return True
        else:
            detail = {"param": param, "msg": server.detail_doesnot_exist, "value": value}
            return abort(400, description=detail)
