import utils


class Validator(object):

    @staticmethod
    def is_object_id_valid_recipe(_id):
        utils.Validator.is_object_id(param="_id_recipe", value=_id)
        utils.Validator.is_object_id_in_collection(param="_id_recipe", value=_id,
                                                   collection=utils.Mongo.collection_recipe)
        return True

    @staticmethod
    def is_object_id_valid_steps(_id_recipe, _id_step):
        utils.Validator.is_object_id(param="_id_step", value=_id_step)
        utils.Validator.is_object_id_in_collection_special_step(param="_id_step", _id_recipe=_id_recipe,
                                                                _id_step=_id_step)
        return True

    @staticmethod
    def is_string_boolean(with_files):
        if with_files is None:
            return True, False
        else:
            utils.Validator.is_string(param="with_files", value=with_files)
            utils.Validator.is_in(param="with_files", value=with_files, values=["true", "false"])
            if with_files == "true":
                return True, True
            elif with_files == "false":
                return True, False

    def is_body_valid(self, data):
        self.is_step_valid(data)

    @staticmethod
    def is_step_valid(data):
        utils.Validator.is_mandatory(param="step", data=data)
        utils.Validator.is_string(param="step", value=data["step"])
        utils.Validator.is_string_non_empty(param="step", value=data["step"])
        return True
