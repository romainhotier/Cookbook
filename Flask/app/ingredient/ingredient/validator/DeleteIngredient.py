from server import mongo_config as mongo_conf, validator as validator

validator = validator.Validator()
mongo = mongo_conf.MongoConnection()


class Validator(object):

    @staticmethod
    def is_object_id_valid(_id):
        validator.is_object_id(param="_id", value=_id)
        validator.is_object_id_in_collection(param="_id", value=_id, collection=mongo.collection_ingredient)
        return True
