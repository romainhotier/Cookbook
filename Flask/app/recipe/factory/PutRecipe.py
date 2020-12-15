class Factory(object):

    def __init__(self):
        """ Class to work around PutRecipe.
        """
        self.param_id = "_id"
        self.param_categories = "categories"
        self.param_cooking_time = "cooking_time"
        self.param_ingredients = "ingredients"
        self.param_ingredients_id = "_id"
        self.param_ingredients_quantity = "quantity"
        self.param_ingredients_unit = "unit"
        self.param_level = "level"
        self.param_nb_people = "nb_people"
        self.param_note = "note"
        self.param_preparation_time = "preparation_time"
        self.param_resume = "resume"
        self.param_slug = "slug"
        self.param_status = "status"
        self.param_steps = "steps"
        self.param_steps_description = "description"
        self.param_title = "title"
        self.body = {}

    def get_body_param(self):
        """ Get PutRecipe's body parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [self.param_categories, self.param_cooking_time, self.param_ingredients, self.param_level,
                self.param_nb_people, self.param_note, self.param_preparation_time, self.param_resume, self.param_slug,
                self.param_status, self.param_status, self.param_steps, self.param_title]

    def get_ingredients_body_param(self):
        """ Get PutRecipe's ingredients body parameters.

        Returns
        -------
        list
            Ingredients body parameters.
        """
        return [self.param_ingredients_id, self.param_ingredients_quantity, self.param_ingredients_unit]

    def clean_body(self, data):
        """ Remove keys that are not in PutRecipe's parameters.

        Parameters
        ----------
        data : dict
            To be cleaned.

        Returns
        -------
        dict
            Correct body.
        """
        self.__setattr__("body", data)
        self.remove_foreign_key()
        self.remove_foreign_key_ingredients()
        return self.body

    # use in clean_body
    def remove_foreign_key(self):
        """ Remove keys that are not in PutRecipe's parameters.
        """
        for i in list(self.body):
            if i not in self.get_body_param():
                del self.body[i]

    # use in clean_body
    def remove_foreign_key_ingredients(self):
        """ Remove keys that are not in PutRecipe's parameters for ingredients param.
        """
        try:
            ingredients = self.body[self.param_ingredients]
            try:
                for index, ingredient in enumerate(ingredients):
                    for i in list(ingredient):
                        if i not in self.get_ingredients_body_param():
                            del self.body[self.param_ingredients][index][i]
            except TypeError:
                pass
        except KeyError:
            pass
