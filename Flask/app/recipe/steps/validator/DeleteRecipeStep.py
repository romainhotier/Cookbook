from server import mongo_config as mongo_conf, validator as validator
import app.recipe.steps.model as steps_model


validator = validator.Validator()
mongo = mongo_conf.MongoConnection()
steps = steps_model.Steps()


class Validator(object):

    @staticmethod
    def is_object_id_valid_recipe(_id):
        validator.is_object_id(param="_id_recipe", value=_id)
        validator.is_object_id_in_collection(param="_id_recipe", value=_id, collection=mongo.collection_recipe)
        return True

    @staticmethod
    def is_object_id_valid_steps(_id_recipe, _id_step):
        validator.is_object_id(param="_id_step", value=_id_step)
        validator.is_object_id_in_collection_special_step(param="_id_step", _id_recipe=_id_recipe, _id_step=_id_step)
        return True

    @staticmethod
    def is_string_boolean(with_files):
        if with_files is None:
            return True, False
        else:
            validator.is_string(param="with_files", value=with_files)
            validator.is_in(param="with_files", value=with_files, values=["true", "false"])
            if with_files == "true":
                return True, True
            elif with_files == "false":
                return True, False
