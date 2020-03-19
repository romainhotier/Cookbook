from server import factory as factory, validator as validator, mongo_config as mongo_conf

server = factory.Server()
mongo = mongo_conf.MongoConnection()
validator = validator.Validator()


class Validator(object):

    @staticmethod
    def is_object_id_valid(_id):
        validator.is_object_id(param="_id_recipe", value=_id)
        validator.is_object_id_in_collection(param="_id_recipe", value=_id, collection=mongo.collection_recipe)
        return True

    @staticmethod
    def is_string_boolean(with_name):
        if with_name is None:
            return True, False
        else:
            validator.is_string(param="with_name", value=with_name)
            validator.is_in(param="with_name", value=with_name, values=["true", "false"])
            if with_name == "true":
                return True, True
            elif with_name == "false":
                return True, False
