import utils


class Validator(object):

    @staticmethod
    def is_object_id_valid(kind, _id):
        utils.Validator.is_object_id(param="_id", value=_id)
        utils.Validator.is_object_id_in_collection(param="_id", value=_id, 
                                                   collection=utils.Mongo.select_collection(kind=kind))
        return True

    @staticmethod
    def is_object_id_valid_special_step(kind, _id_recipe, **optional):
        if kind in ["recipe"]:
            utils.Validator.is_object_id(param="_id_recipe", value=_id_recipe)
            utils.Validator.is_object_id_in_collection(param="_id_recipe", value=_id_recipe,
                                                       collection=utils.Mongo.select_collection(kind=kind))
            return True
        if kind in ["step"]:
            utils.Validator.is_object_id(param="_id_step", value=optional["_id_step"])
            utils.Validator.is_object_id_in_collection_special_step(param="_id_step", _id_recipe=_id_recipe,
                                                                    _id_step=optional["_id_step"])
            return True

    def is_body_valid(self, data):
        self.is_path_valid(data)
        self.is_filename_valid(data)
        self.is_is_main_valid(data)

    @staticmethod
    def is_path_valid(data):
        utils.Validator.is_mandatory(param="path", data=data)
        utils.Validator.is_string(param="path", value=data["path"])
        utils.Validator.is_string_non_empty(param="path", value=data["path"])
        utils.Validator.is_path_exist(param="path", value=data["path"])
        return True

    @staticmethod
    def is_filename_valid(data):
        utils.Validator.is_mandatory(param="filename", data=data)
        utils.Validator.is_string(param="filename", value=data["filename"])
        utils.Validator.is_string_non_empty(param="filename", value=data["filename"])
        return True

    @staticmethod
    def is_is_main_valid(data):
        if "is_main" in data.keys():
            utils.Validator.is_boolean(param="is_main", value=data["is_main"])
            return True
