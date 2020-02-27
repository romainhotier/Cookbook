import app.ingredient.ingredient.model as ingredient_model

list_param_ingredient = ingredient_model.Ingredient().list_param


class Factory(object):

    def clean_body(self, data):
        cleaned = self.remove_foreign_key(data)
        return cleaned

    @staticmethod
    def remove_foreign_key(data):
        clean_data = {}
        for i, j in data.items():
            if i in list_param_ingredient:
                clean_data[i] = j
        return clean_data
