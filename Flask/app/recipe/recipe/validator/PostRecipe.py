from flask import abort

from server import factory as factory, validator as validator
import app.recipe.recipe.model as recipe


server = factory.Server()
validator = validator.Validator()
recipe = recipe.Recipe()


class Validator(object):

    def is_body_valid(self, data):
        self.is_title_valid(data)
        self.is_level_valid(data)
        self.is_resume_valid(data)
        self.is_cooking_time_valid(data)
        self.is_preparation_time_valid(data)
        self.is_nb_people_valid(data)
        self.is_note_valid(data)
        self.is_ingredients_valid(data)
        self.is_steps_valid(data)

    @staticmethod
    def is_title_valid(data):
        validator.is_mandatory("title", data)
        validator.is_string("title", data["title"])
        validator.is_string_non_empty("title", data["title"])
        return True

    @staticmethod
    def is_level_valid(data):
        if "level" in data.keys():
            validator.is_string("level", data["level"])
            return True
        return True

    @staticmethod
    def is_resume_valid(data):
        if "resume" in data.keys():
            validator.is_string("resume", data["resume"])
            return True
        return True

    @staticmethod
    def is_cooking_time_valid(data):
        if "cooking_time" in data.keys():
            validator.is_string("cooking_time", data["cooking_time"])
            return True
        return True

    @staticmethod
    def is_preparation_time_valid(data):
        if "preparation_time" in data.keys():
            validator.is_string("preparation_time", data["preparation_time"])
            return True
        return True

    @staticmethod
    def is_nb_people_valid(data):
        if "nb_people" in data.keys():
            validator.is_string("nb_people", data["nb_people"])
            return True
        return True

    @staticmethod
    def is_note_valid(data):
        if "note" in data.keys():
            validator.is_string("note", data["note"])
            return True
        return True

    @staticmethod
    def is_steps_valid(data):
        if "steps" in data.keys():
            validator.is_array("steps", data["steps"])
            return True
        return True

    @staticmethod
    def is_ingredients_valid(data):
        if "ingredients" in data.keys():
            validator.is_object("ingredients", data["ingredients"])
            return True
        return True

    @staticmethod
    def is_title_already_exist(data):
        """ check title already exist """
        title = data["title"]
        result_mongo = recipe.select_one_by_title(title=title)
        if result_mongo.count() == 0:
            return False
        else:
            detail = {"param": "title", "msg": server.detail_already_exist, "value": title}
            return abort(400, description=detail)
