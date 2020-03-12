from server import mongo_config as mongo_conf, validator as validator
import app.recipe.steps.model as steps_model

validator = validator.Validator()
mongo = mongo_conf.MongoConnection()
steps = steps_model.Steps()


class Validator(object):

    @staticmethod
    def is_object_id_valid(_id):
        validator.is_object_id(param="_id", value=_id)
        validator.is_object_id_in_collection(param="_id", value=_id, collection=mongo.collection_recipe)
        return True

    def is_body_valid(self, _id, data):
        self.is_step_valid(data)
        self.is_position_valid(_id, data)

    @staticmethod
    def is_step_valid(data):
        validator.is_mandatory(param="step", data=data)
        validator.is_string(param="step", value=data["step"])
        validator.is_string_non_empty(param="step", value=data["step"])
        return True

    @staticmethod
    def is_position_valid(_id, data):
        if "position" in data.keys():
            validator.is_int("position", data["position"])
            validator.is_between_x_y("position", data["position"], 0, steps.get_steps_length(_id=_id))
            return True
        return True