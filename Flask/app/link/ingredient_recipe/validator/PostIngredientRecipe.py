from flask import abort

from server import server as server, validator as validator, mongo_config as mongo_conf
import app.link.ingredient_recipe.model as link

server = server.Server()
mongo = mongo_conf.MongoConnection()
validator = validator.Validator()
link = link.LinkIngredientRecipe()


class Validator(object):

    def is_body_valid(self, data):
        self.is_id_ingredient_valid(data)
        self.is_id_recipe_valid(data)
        self.is_quantity_valid(data)
        self.is_unit_valid(data)
        self.is_link_already_exist(_id_ingredient=data["_id_ingredient"], _id_recipe=data["_id_recipe"])

    @staticmethod
    def is_id_ingredient_valid(data):
        validator.is_mandatory(param="_id_ingredient", data=data)
        validator.is_object_id(param="_id_ingredient", value=data["_id_ingredient"])
        validator.is_object_id_in_collection(param="_id_ingredient", value=data["_id_ingredient"],
                                             collection=mongo.collection_ingredient)
        return True

    @staticmethod
    def is_id_recipe_valid(data):
        validator.is_mandatory(param="_id_recipe", data=data)
        validator.is_object_id(param="_id_recipe", value=data["_id_recipe"])
        validator.is_object_id_in_collection(param="_id_recipe", value=data["_id_recipe"],
                                             collection=mongo.collection_recipe)
        return True

    @staticmethod
    def is_quantity_valid(data):
        validator.is_mandatory(param="quantity", data=data)
        validator.is_int(param="quantity", value=data["quantity"])
        return True

    @staticmethod
    def is_unit_valid(data):
        validator.is_mandatory(param="unit", data=data)
        validator.is_string(param="unit", value=data["unit"])
        return True

    @staticmethod
    def is_link_already_exist(_id_ingredient, _id_recipe):
        """ check title already exist """
        result_mongo = link.check_link_is_unique(_id_ingredient=_id_ingredient, _id_recipe=_id_recipe)
        if result_mongo is None:
            return False
        else:
            detail = "link between {} and {} ".format(_id_ingredient, _id_recipe) + server.detail_already_exist.lower()
            return abort(400, description=detail)
