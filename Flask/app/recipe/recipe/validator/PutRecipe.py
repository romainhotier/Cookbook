from flask import abort

from server import factory as factory, mongo_config as mongo_conf, validator as validator
import app.recipe.recipe.model as recipe


server = factory.Server()
validator = validator.Validator()
mongo = mongo_conf.MongoConnection()
recipe = recipe.Recipe()


class Validator(object):

    @staticmethod
    def is_object_id_valid(_id):
        validator.is_object_id(param="_id", value=_id)
        validator.is_object_id_in_collection(param="_id", value=_id, collection=mongo.collection_recipe)
        return True

    def is_body_valid(self, data):
        self.is_title_valid(data)
        self.is_level_valid(data)
        self.is_resume_valid(data)
        self.is_cooking_time_valid(data)
        self.is_preparation_time_valid(data)
        self.is_nb_people_valid(data)
        self.is_note_valid(data)
        self.is_steps_valid(data)

    @staticmethod
    def is_title_valid(data):
        validator.is_mandatory(param="title", data=data)
        validator.is_string(param="title", value=data["title"])
        validator.is_string_non_empty(param="title", value=data["title"])
        return True

    @staticmethod
    def is_level_valid(data):
        if "level" in data.keys():
            validator.is_string(param="level", value=data["level"])
            return True
        return True

    @staticmethod
    def is_resume_valid(data):
        if "resume" in data.keys():
            validator.is_string(param="resume", value=data["resume"])
            return True
        return True

    @staticmethod
    def is_cooking_time_valid(data):
        if "cooking_time" in data.keys():
            validator.is_string(param="cooking_time", value=data["cooking_time"])
            return True
        return True

    @staticmethod
    def is_preparation_time_valid(data):
        if "preparation_time" in data.keys():
            validator.is_string(param="preparation_time", value=data["preparation_time"])
            return True
        return True

    @staticmethod
    def is_nb_people_valid(data):
        if "nb_people" in data.keys():
            validator.is_string(param="nb_people", value=data["nb_people"])
            return True
        return True

    @staticmethod
    def is_note_valid(data):
        if "note" in data.keys():
            validator.is_string(param="note", value=data["note"])
            return True
        return True

    @staticmethod
    def is_steps_valid(data):
        if "steps" in data.keys():
            validator.is_array(param="steps", value=data["steps"])
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
