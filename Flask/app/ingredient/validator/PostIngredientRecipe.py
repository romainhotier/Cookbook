from flask import abort

import utils
import app.ingredient as ingredient_model


class Validator(object):

    def is_body_valid(self, data):
        self.is_id_ingredient_valid(data)
        self.is_id_recipe_valid(data)
        self.is_quantity_valid(data)
        self.is_unit_valid(data)
        self.is_link_already_exist(_id_ingredient=data["_id_ingredient"], _id_recipe=data["_id_recipe"])

    @staticmethod
    def is_id_ingredient_valid(data):
        utils.Validator.is_mandatory(param="_id_ingredient", data=data)
        utils.Validator.is_object_id(param="_id_ingredient", value=data["_id_ingredient"])
        utils.Validator.is_object_id_in_collection(param="_id_ingredient", value=data["_id_ingredient"],
                                                   collection=utils.Mongo.collection_ingredient)
        return True

    @staticmethod
    def is_id_recipe_valid(data):
        utils.Validator.is_mandatory(param="_id_recipe", data=data)
        utils.Validator.is_object_id(param="_id_recipe", value=data["_id_recipe"])
        utils.Validator.is_object_id_in_collection(param="_id_recipe", value=data["_id_recipe"],
                                                   collection=utils.Mongo.collection_recipe)
        return True

    @staticmethod
    def is_quantity_valid(data):
        utils.Validator.is_mandatory(param="quantity", data=data)
        utils.Validator.is_int(param="quantity", value=data["quantity"])
        return True

    @staticmethod
    def is_unit_valid(data):
        utils.Validator.is_mandatory(param="unit", data=data)
        utils.Validator.is_string(param="unit", value=data["unit"])
        return True

    @staticmethod
    def is_link_already_exist(_id_ingredient, _id_recipe):
        """ check title already exist """
        result = ingredient_model.IngredientRecipeModel.\
            check_link_is_unique(_id_ingredient=_id_ingredient, _id_recipe=_id_recipe)
        if result == 0:
            return False
        else:
            detail = "link between {} and {} ".format(_id_ingredient, _id_recipe) + \
                     utils.Server.detail_already_exist.lower()
            return abort(400, description=detail)
