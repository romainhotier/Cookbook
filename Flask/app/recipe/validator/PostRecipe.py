from flask import abort

import utils
import app.recipe as recipe_model


class Validator(object):

    def is_body_valid(self, data):
        self.is_title_valid(data)
        self.is_slug_valid(data)
        self.is_level_valid(data)
        self.is_resume_valid(data)
        self.is_cooking_time_valid(data)
        self.is_preparation_time_valid(data)
        self.is_nb_people_valid(data)
        self.is_note_valid(data)
        self.is_categories_valid(data)
        self.is_steps_valid(data)

    def is_title_valid(self, data):
        utils.Validator.is_mandatory(param="title", data=data)
        utils.Validator.is_string(param="title", value=data["title"])
        utils.Validator.is_string_non_empty(param="title", value=data["title"])
        self.is_title_already_exist(value=data["title"])
        return True

    @staticmethod
    def is_slug_valid(data):
        utils.Validator.is_mandatory(param="slug", data=data)
        utils.Validator.is_string(param="slug", value=data["slug"])
        utils.Validator.is_string_non_empty(param="slug", value=data["slug"])
        return True

    @staticmethod
    def is_level_valid(data):
        if "level" in data.keys():
            utils.Validator.is_int(param="level", value=data["level"])
            utils.Validator.is_between_x_y(param="level", value=data["level"], x=0, y=3)
            return True
        return True

    @staticmethod
    def is_resume_valid(data):
        if "resume" in data.keys():
            utils.Validator.is_string(param="resume", value=data["resume"])
            return True
        return True

    @staticmethod
    def is_cooking_time_valid(data):
        if "cooking_time" in data.keys():
            utils.Validator.is_int(param="cooking_time", value=data["cooking_time"])
            return True
        return True

    @staticmethod
    def is_preparation_time_valid(data):
        if "preparation_time" in data.keys():
            utils.Validator.is_int(param="preparation_time", value=data["preparation_time"])
            return True
        return True

    @staticmethod
    def is_nb_people_valid(data):
        if "nb_people" in data.keys():
            utils.Validator.is_int(param="nb_people", value=data["nb_people"])
            return True
        return True

    @staticmethod
    def is_note_valid(data):
        if "note" in data.keys():
            utils.Validator.is_string(param="note", value=data["note"])
            return True
        return True

    @staticmethod
    def is_categories_valid(data):
        if "categories" in data.keys():
            utils.Validator.is_array(param="categories", value=data["categories"])
            return True
        return True

    @staticmethod
    def is_steps_valid(data):
        if "steps" in data.keys():
            utils.Validator.is_array(param="steps", value=data["steps"])
            return True
        return True

    @staticmethod
    def is_title_already_exist(value):
        """ check title already exist """
        result = recipe_model.RecipeModel.check_recipe_is_unique(title=value)
        if result== 0:
            return False
        else:
            detail = {"param": "title", "msg": utils.Server.detail_already_exist, "value": value}
            return abort(400, description=detail)
