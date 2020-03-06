from server import mongo_config as mongo_conf, validator as validator

validator = validator.Validator()
mongo = mongo_conf.MongoConnection()


class Validator(object):

    @staticmethod
    def is_object_id_valid(_id):
        validator.is_object_id(_id)
        validator.is_object_id_in_collection(_id, mongo.collection_ingredient)
        return True

    def is_body_valid(self, data):
        self.is_path_valid(data)
        self.is_filename_valid(data)
        self.is_is_main_valid(data)

    @staticmethod
    def is_path_valid(data):
        validator.is_mandatory(param="path", data=data)
        validator.is_string(param="path", value=data["path"])
        validator.is_string_non_empty(param="path", value=data["path"])
        validator.is_path_exist(param="path", value=data["path"])
        return True

    @staticmethod
    def is_filename_valid(data):
        validator.is_mandatory(param="filename", data=data)
        validator.is_string(param="filename", value=data["filename"])
        validator.is_string_non_empty(param="filename", value=data["filename"])
        return True

    @staticmethod
    def is_is_main_valid(data):
        if "is_main" in data.keys():
            validator.is_boolean(param="is_main", value=data["is_main"])
            return True
