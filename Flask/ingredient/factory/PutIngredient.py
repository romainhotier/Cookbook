import ingredient.model as ingredient_model

list_param_ingredient = ingredient_model.Ingredient().list_param


class Factory(object):

    @staticmethod
    def clean_body(data):
        clean_body = {}
        for i, j in data.items():
            if i in list_param_ingredient:
                clean_body[i] = j
        return clean_body
