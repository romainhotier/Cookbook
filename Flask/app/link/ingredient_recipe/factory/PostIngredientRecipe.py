import app.link.ingredient_recipe.model as ingredient_recipe_model

list_param_ingredient_recipe = ingredient_recipe_model.LinkIngredientRecipe().list_param


class Factory(object):

    def clean_body(self, data):
        cleaned = self.remove_foreign_key(data)
        return cleaned

    @staticmethod
    def remove_foreign_key(data):
        clean_data = {}
        for i, j in data.items():
            if i in list_param_ingredient_recipe:
                clean_data[i] = j
        return clean_data
