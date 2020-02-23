from flask import abort

import factory as factory

server = factory.Server()


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
    def is_result_mongo_empty(result_mongo):
        """ check cursor mongo is not empty """
        if result_mongo.count() == 0:
            detail = ""
            return abort(404, description=detail)
        else:
            return False

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
