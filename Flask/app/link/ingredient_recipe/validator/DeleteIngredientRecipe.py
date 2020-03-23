from server import server as server, validator as validator, mongo_config as mongo_conf

server = server.Server()
mongo = mongo_conf.MongoConnection()
validator = validator.Validator()


class Validator(object):

    @staticmethod
    def is_object_id_valid(_id):
        validator.is_object_id(param="_id", value=_id)
        validator.is_object_id_in_collection(param="_id", value=_id, collection=mongo.collection_link_ingr_recip)
        return True
