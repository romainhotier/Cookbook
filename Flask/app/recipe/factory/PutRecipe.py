from bson import ObjectId


class Factory(object):

    def __init__(self):
        """ Class to work around PutRecipe.
        """
        self.param_id = "_id"
        self.param_categories = "categories"
        self.param_cooking_time = "cooking_time"
        self.param_ingredients = "ingredients"
        self.param_ingredient = "ingredient"
        self.param_ingredient_id = "_id"
        self.param_ingredient_quantity = "quantity"
        self.param_ingredient_unit = "unit"
        self.param_level = "level"
        self.param_nb_people = "nb_people"
        self.param_note = "note"
        self.param_preparation_time = "preparation_time"
        self.param_resume = "resume"
        self.param_slug = "slug"
        self.param_status = "status"
        self.param_steps = "steps"
        self.param_step = "step"
        self.param_step_id = "_id"
        self.param_step_description = "description"
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
        return [self.param_ingredient_id, self.param_ingredient_quantity, self.param_ingredient_unit]

    def get_steps_body_param(self):
        """ Get PutRecipe's step body parameters.

        Returns
        -------
        list
            Ingredients body parameters.
        """
        return [self.param_step_id, self.param_step_description]

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
        self.remove_foreign_key_steps()
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

    # use in clean_body
    def remove_foreign_key_steps(self):
        """ Remove keys that are not in PutRecipe's parameters for step param.
        """
        try:
            steps = self.body[self.param_steps]
            try:
                for index, step in enumerate(steps):
                    if isinstance(step, dict):
                        for i in list(step):
                            if i not in self.get_steps_body_param():
                                del self.body[self.param_steps][index][i]
            except TypeError:
                pass
        except KeyError:
            pass

    def reformat_body(self, data):
        """ Reformat body for PutRecipe.

        Parameters
        ----------
        data : dict
            To be formated.

        Returns
        -------
        dict
            Correct body.
        """
        self.__setattr__("body", data)
        self.reformat_steps()
        return self.body

    # use in fill_body
    def reformat_steps(self):
        """ Fill steps with ObjectId.
        """
        formated_steps = []
        try:
            for step in self.body[self.param_steps]:
                if isinstance(step, str):
                    formated_steps.append({self.param_step_id: ObjectId(),
                                           self.param_step_description: step})
                else:
                    formated_steps.append({self.param_step_id: ObjectId(step[self.param_step_id]),
                                           self.param_step_description: step[self.param_step_description]})
            self.body[self.param_steps] = formated_steps
        except KeyError:
            pass
