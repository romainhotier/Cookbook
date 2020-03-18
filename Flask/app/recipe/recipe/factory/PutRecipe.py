import app.recipe.recipe.model as recipe_model

list_param_recipe_put = recipe_model.Recipe().list_param
list_param_recipe_put.remove("steps")


class Factory(object):

    def clean_body(self, data):
        cleaned = self.remove_foreign_key(data)
        return cleaned

    @staticmethod
    def remove_foreign_key(data):
        clean_data = {}
        for i, j in data.items():
            if i in list_param_recipe_put:
                clean_data[i] = j
        return clean_data
