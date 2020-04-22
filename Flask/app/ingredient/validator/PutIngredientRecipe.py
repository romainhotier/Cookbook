import utils


class Validator(object):

    @staticmethod
    def is_object_id_valid(_id):
        utils.Validator.is_object_id(param="_id", value=_id)
        utils.Validator.is_object_id_in_collection(param="_id", value=_id,
                                                   collection=utils.Mongo.collection_ingredient_recipe)
        return True

    def is_body_valid(self, data):
        utils.Validator.has_at_least_one_key(data)
        self.is_quantity_valid(data)
        self.is_unit_valid(data)

    @staticmethod
    def is_quantity_valid(data):
        if "quantity" in data.keys():
            utils.Validator.is_int(param="quantity", value=data["quantity"])
            return True
        return True

    @staticmethod
    def is_unit_valid(data):
        if "unit" in data.keys():
            utils.Validator.is_string(param="unit", value=data["unit"])
            return True
        return True
