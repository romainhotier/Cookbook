from bson import ObjectId


class Factory(object):

    def __init__(self):
        """ Class to work around PostRecipe.
        """
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
        """ Get PostRecipe's body parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [self.param_categories, self.param_cooking_time, self.param_ingredients, self.param_level,
                self.param_nb_people, self.param_note, self.param_preparation_time, self.param_resume, self.param_slug,
                self.param_status, self.param_status, self.param_steps, self.param_title]

    def get_ingredients_body_param(self):
        """ Get PostRecipe's ingredients body parameters.

        Returns
        -------
        list
            Ingredients body parameters.
        """
        return [self.param_ingredients_id, self.param_ingredients_quantity, self.param_ingredients_unit]

    def clean_body(self, data):
        """ Remove keys that are not in PostRecipe's parameters.

        Parameters
        ----------
        data : dict
            To be cleaned.

        Returns
        -------
        dict
            Cleaned dict.
        """
        """ body keys """
        self.__setattr__("body", data)
        self.remove_foreign_key()
        self.remove_foreign_key_ingredients()
        return self.body

    # use in clean_body
    def remove_foreign_key(self):
        """ Remove keys that are not in PostRecipe's parameters.
        """
        for i in list(self.body):
            if i not in self.get_body_param():
                del self.body[i]

    # use in clean_body
    def remove_foreign_key_ingredients(self):
        """ Remove keys that are not in PostRecipe's parameters for ingredients param.
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

    def fill_body(self, data):
        """ Fill body for PostRecipe.

        Parameters
        ----------
        data : dict
            To be filled.

        Returns
        -------
        dict
            Correct body.
        """
        self.__setattr__("body", data)
        self.fill_body_missing_key()
        self.reformat_steps()
        return self.body

    # use in fill_body
    def fill_body_missing_key(self):
        """ Fill keys that are not mandatory with default value for PostRecipe.
         - resume/note -> ""
         - level/cooking_time/preparation_time/nb_people -> 0
         - categories/ingredients/steps -> []
         - status -> "in_progress"
        """
        for key in self.get_body_param():
            if key not in self.body:
                if key in [self.param_resume, self.param_note]:
                    self.body[key] = ""
                elif key in [self.param_level, self.param_cooking_time, self.param_preparation_time,
                             self.param_nb_people]:
                    self.body[key] = 0
                elif key in [self.param_categories, self.param_ingredients, self.param_steps]:
                    self.body[key] = []
                elif key in [self.param_status]:
                    self.body[key] = "in_progress"

    # use in fill_body
    def reformat_steps(self):
        """ Fill steps with ObjectId.
        """
        formated_steps = []
        for step in self.body[self.param_steps]:
            formated_steps.append({"_id": ObjectId(), self.param_steps_description: step})
        self.body[self.param_steps] = formated_steps
