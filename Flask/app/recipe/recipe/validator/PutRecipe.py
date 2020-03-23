from flask import abort

from server import server as server, mongo_config as mongo_conf, validator as validator
import app.recipe.recipe.model as recipe


server = server.Server()
validator = validator.Validator()
mongo = mongo_conf.MongoConnection()
recipe = recipe.Recipe()


class Validator(object):

    @staticmethod
    def is_object_id_valid(_id):
        validator.is_object_id(param="_id", value=_id)
        validator.is_object_id_in_collection(param="_id", value=_id, collection=mongo.collection_recipe)
        return True

    @staticmethod
    def is_string_boolean(with_files):
        if with_files is None:
            return True, False
        else:
            validator.is_string(param="with_files", value=with_files)
            validator.is_in(param="with_files", value=with_files, values=["true", "false"])
            if with_files == "true":
                return True, True
            elif with_files == "false":
                return True, False

    def is_body_valid(self, data):
        validator.has_at_least_one_key(data)
        self.is_title_valid(data)
        self.is_slug_valid(data)
        self.is_level_valid(data)
        self.is_resume_valid(data)
        self.is_cooking_time_valid(data)
        self.is_preparation_time_valid(data)
        self.is_nb_people_valid(data)
        self.is_note_valid(data)
        self.is_categories_valid(data)

    def is_title_valid(self, data):
        if "title" in data.keys():
            validator.is_string(param="title", value=data["title"])
            validator.is_string_non_empty(param="title", value=data["title"])
            self.is_title_already_exist(value=data["title"])
            return True
        return True

    @staticmethod
    def is_slug_valid(data):
        if "slug" in data.keys():
            validator.is_string(param="slug", value=data["slug"])
            validator.is_string_non_empty(param="slug", value=data["slug"])
            return True
        return True

    @staticmethod
    def is_level_valid(data):
        if "level" in data.keys():
            validator.is_int(param="level", value=data["level"])
            validator.is_between_x_y(param="level", value=data["level"], x=0, y=3)
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
            validator.is_int(param="cooking_time", value=data["cooking_time"])
            return True
        return True

    @staticmethod
    def is_preparation_time_valid(data):
        if "preparation_time" in data.keys():
            validator.is_int(param="preparation_time", value=data["preparation_time"])
            return True
        return True

    @staticmethod
    def is_nb_people_valid(data):
        if "nb_people" in data.keys():
            validator.is_int(param="nb_people", value=data["nb_people"])
            return True
        return True

    @staticmethod
    def is_note_valid(data):
        if "note" in data.keys():
            validator.is_string(param="note", value=data["note"])
            return True
        return True

    @staticmethod
    def is_categories_valid(data):
        if "categories" in data.keys():
            validator.is_array(param="categories", value=data["categories"])
            return True
        return True

    @staticmethod
    def is_title_already_exist(value):
        """ check title already exist """
        result_mongo = recipe.select_one_by_title(title=value)
        if result_mongo.count() == 0:
            return False
        else:
            detail = {"param": "title", "msg": server.detail_already_exist, "value": value}
            return abort(400, description=detail)
