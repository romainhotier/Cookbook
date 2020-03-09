import app.recipe.recipe.model as recipe_model

list_param_recipe = recipe_model.Recipe().list_param


class Factory(object):

    def clean_body(self, data):
        cleaned = self.remove_foreign_key(data)
        filled = self.fill_body_with_missing_key(cleaned)
        return filled

    @staticmethod
    def remove_foreign_key(data):
        clean_data = {}
        for i, j in data.items():
            if i in list_param_recipe:
                clean_data[i] = j
        return clean_data

    @staticmethod
    def fill_body_with_missing_key(data):
        for key in list_param_recipe:
            if key not in data.keys():
                if key in ["level", "resume", "cooking_time", "preparation_time", "nb_people", "note"]:
                    data[key] = ""
                elif key in ["steps"]:
                    data[key] = []
        return data
