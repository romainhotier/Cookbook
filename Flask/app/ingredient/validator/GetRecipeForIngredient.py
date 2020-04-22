import utils


class Validator(object):

    @staticmethod
    def is_object_id_valid(_id):
        utils.Validator.is_object_id(param="_id_ingredient", value=_id)
        utils.Validator.is_object_id_in_collection(param="_id_ingredient", value=_id,
                                                   collection=utils.Mongo.collection_ingredient)
        return True

    @staticmethod
    def is_string_boolean(with_title):
        if with_title is None:
            return True, False
        else:
            utils.Validator.is_string(param="with_title", value=with_title)
            utils.Validator.is_in(param="with_title", value=with_title, values=["true", "false"])
            if with_title == "true":
                return True, True
            elif with_title == "false":
                return True, False
