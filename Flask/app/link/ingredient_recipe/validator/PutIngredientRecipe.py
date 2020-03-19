from server import factory as factory, validator as validator, mongo_config as mongo_conf

server = factory.Server()
mongo = mongo_conf.MongoConnection()
validator = validator.Validator()


class Validator(object):

    @staticmethod
    def is_object_id_valid(_id):
        validator.is_object_id(param="_id", value=_id)
        validator.is_object_id_in_collection(param="_id", value=_id, collection=mongo.collection_link_ingr_recip)
        return True

    def is_body_valid(self, data):
        validator.has_at_least_one_key(data)
        self.is_quantity_valid(data)
        self.is_unit_valid(data)

    @staticmethod
    def is_quantity_valid(data):
        if "quantity" in data.keys():
            validator.is_int(param="quantity", value=data["quantity"])
            return True
        return True

    @staticmethod
    def is_unit_valid(data):
        if "unit" in data.keys():
            validator.is_string(param="unit", value=data["unit"])
            return True
        return True
