import server.mongo_config as mongo_conf
import app.ingredient.ingredient.model as ingredient_model
import app.file.file.model as file_model

mongo = mongo_conf.MongoConnection()
json_format = mongo_conf.JSONEncoder()
ingredient = ingredient_model.Ingredient()
file = file_model.File()

list_param_file = file_model.File().list_param


class Factory(object):

    def clean_body(self, data):
        cleaned = self.remove_foreign_key(data)
        filled = self.fill_body_with_missing_key(cleaned)
        return filled

    @staticmethod
    def remove_foreign_key(data):
        clean_data = {}
        for i, j in data.items():
            if i in list_param_file:
                clean_data[i] = j
        return clean_data

    @staticmethod
    def fill_body_with_missing_key(data):
        for key in list_param_file:
            if key not in data.keys():
                if key in ["is_main"]:
                    data[key] = False
        return data

    @staticmethod
    def detail_information(_id_file):
        return "added file ObjectId: {0}".format(str(_id_file))
