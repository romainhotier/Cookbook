import utils
import app.recipe as recipe_model


class Validator(object):

    @staticmethod
    def is_object_id_valid(_id):
        utils.Validator.is_object_id(param="_id", value=_id)
        utils.Validator.is_object_id_in_collection(param="_id", value=_id, collection=utils.Mongo.collection_recipe)
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

    def is_body_valid(self, _id, data):
        self.is_step_valid(data)
        self.is_position_valid(_id, data)

    @staticmethod
    def is_step_valid(data):
        utils.Validator.is_mandatory(param="step", data=data)
        utils.Validator.is_string(param="step", value=data["step"])
        utils.Validator.is_string_non_empty(param="step", value=data["step"])
        return True

    @staticmethod
    def is_position_valid(_id, data):
        if "position" in data.keys():
            utils.Validator.is_int("position", data["position"])
            utils.Validator.is_between_x_y(param="position", value=data["position"], x=0,
                                           y=recipe_model.StepModel.get_steps_length(_id=_id))
            return True
        return True
