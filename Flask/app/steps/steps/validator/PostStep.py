from server import mongo_config as mongo_conf, validator as validator
import app.recipe.steps.model as steps_model

validator = validator.Validator()
mongo = mongo_conf.MongoConnection()
steps = steps_model.Steps()


class Validator(object):

    def is_body_valid(self, data):
        self.is_step_valid(data)

    @staticmethod
    def is_step_valid(data):
        validator.is_mandatory(param="step", data=data)
        validator.is_string(param="step", value=data["step"])
        validator.is_string_non_empty(param="step", value=data["step"])
        return True
