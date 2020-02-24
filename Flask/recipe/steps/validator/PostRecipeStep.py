import validator as validator
import recipe.steps.model as steps_model

validator = validator.Validator()
steps = steps_model.Steps()


class Validator(object):

    @staticmethod
    def is_object_id(_id):
        validator.is_object_id(_id)
        return True

    def is_body_valid(self, _id, data):
        self.is_step_valid(data)
        self.is_position_valid(_id, data)

    @staticmethod
    def is_step_valid(data):
        validator.is_mandatory("step", data)
        validator.is_string("step", data["step"])
        validator.is_string_non_empty("step", data["step"])
        return True

    @staticmethod
    def is_position_valid(_id, data):
        if "position" in data.keys():
            validator.is_int("position", data["position"])
            validator.is_between_x_y("position", data["position"], 0, steps.get_steps_length(_id))
            return True
        return True
