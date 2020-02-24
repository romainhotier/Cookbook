import validator as validator
import recipe.steps.model as steps_model

validator = validator.Validator()
steps = steps_model.Steps()


class Validator(object):

    @staticmethod
    def is_object_id(_id):
        validator.is_object_id(_id)
        return True

    @staticmethod
    def is_index_valid(_id, index):
        validator.is_int("index", index)
        validator.is_between_x_y("index", int(index), 0, steps.get_steps_length(_id))
        return True
