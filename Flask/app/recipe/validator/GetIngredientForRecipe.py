import utils


class Validator(object):

    @staticmethod
    def is_object_id_valid(_id):
        utils.Validator.is_object_id(param="_id_recipe", value=_id)
        utils.Validator.is_object_id_in_collection(param="_id_recipe", value=_id,
                                                   collection=utils.Mongo.collection_recipe)
        return True

    @staticmethod
    def is_string_boolean(with_name):
        if with_name is None:
            return True, False
        else:
            utils.Validator.is_string(param="with_name", value=with_name)
            utils.Validator.is_in(param="with_name", value=with_name, values=["true", "false"])
            if with_name == "true":
                return True, True
            elif with_name == "false":
                return True, False
