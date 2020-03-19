from server import factory as factory, validator as validator, mongo_config as mongo_conf

server = factory.Server()
mongo = mongo_conf.MongoConnection()
validator = validator.Validator()


class Validator(object):

    @staticmethod
    def is_object_id_valid(_id):
        validator.is_object_id(param="_id_ingredient", value=_id)
        validator.is_object_id_in_collection(param="_id_ingredient", value=_id, collection=mongo.collection_ingredient)
        return True

    @staticmethod
    def is_string_boolean(with_title):
        if with_title is None:
            return True, False
        else:
            validator.is_string(param="with_title", value=with_title)
            validator.is_in(param="with_title", value=with_title, values=["true", "false"])
            if with_title == "true":
                return True, True
            elif with_title == "false":
                return True, False
