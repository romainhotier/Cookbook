class Factory(object):

    def __init__(self):
        """ Class to work around PostRecipe.
        """
        self.param_title = "title"
        self.param_slug = "slug"
        self.param_level = "level"
        self.param_resume = "resume"
        self.param_cooking_time = "cooking_time"
        self.param_preparation_time = "preparation_time"
        self.param_nb_people = "nb_people"
        self.param_note = "note"
        self.param_categories = "categories"
        self.default_steps = "steps"
        self.body = {}

    def get_body_param(self):
        """ Get PostRecipe's body parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [self.param_title, self.param_slug, self.param_level, self.param_resume, self.param_cooking_time,
                self.param_preparation_time, self.param_nb_people, self.param_note, self.param_categories]

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
        return self.body

    # use in clean_body
    def remove_foreign_key(self):
        """ Remove keys that are not in PostRecipe's parameters.
        """
        for i in list(self.body):
            if i not in self.get_body_param():
                del self.body[i]

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
        return self.body

    # use in fill_body
    def fill_body_missing_key(self):
        """ Fill keys that are not mandatory with default value for PostRecipe.
         - resume/note -> ""
         - level/cooking_time/preparation_time/nb_people -> 0
         - categories -> []
        """
        """ from body """
        for key in self.get_body_param():
            if key not in self.body:
                if key in [self.param_resume, self.param_note]:
                    self.body[key] = ""
                elif key in [self.param_level, self.param_cooking_time, self.param_preparation_time,
                             self.param_nb_people]:
                    self.body[key] = 0
                elif key in [self.param_categories]:
                    self.body[key] = []
        """ from default """
        self.body[self.default_steps] = []
