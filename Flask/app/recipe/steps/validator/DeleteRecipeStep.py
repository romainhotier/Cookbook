from server import mongo_config as mongo_conf, validator as validator
import app.recipe.steps.model as steps_model


validator = validator.Validator()
mongo = mongo_conf.MongoConnection()
steps = steps_model.Steps()


class Validator(object):

    @staticmethod
    def is_object_id_valid(_id):
        validator.is_object_id(_id)
        validator.is_object_id_in_collection(_id, mongo.collection_recipe)
        return True

    @staticmethod
    def is_position_valid(_id, position):
        validator.is_int("position", position)
        validator.is_between_x_y("position", int(position), 0, steps.get_steps_length(_id, mode="delete"))
        return True
