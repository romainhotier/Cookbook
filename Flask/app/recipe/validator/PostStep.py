import utils


class Validator(object):

    def is_body_valid(self, data):
        self.is_step_valid(data)

    @staticmethod
    def is_step_valid(data):
        utils.Validator.is_mandatory(param="step", data=data)
        utils.Validator.is_string(param="step", value=data["step"])
        utils.Validator.is_string_non_empty(param="step", value=data["step"])
        return True
