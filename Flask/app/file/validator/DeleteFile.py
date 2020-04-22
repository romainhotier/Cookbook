import utils


class Validator(object):

    @staticmethod
    def is_object_id_valid(_id):
        utils.Validator.is_object_id(param="_id", value=_id)
        utils.Validator.is_object_id_in_collection(param="_id", value=_id, collection=utils.Mongo.collection_fs_files)
        return True
