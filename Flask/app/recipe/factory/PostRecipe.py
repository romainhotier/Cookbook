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

    def get_body_param(self):
        """ Get PostRecipe's body parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [self.param_title, self.param_slug, self.param_level, self.param_resume, self.param_cooking_time,
                self.param_preparation_time, self.param_nb_people, self.param_note, self.param_categories]

    def format_body(self, data):
        """ Format body for PostRecipe.

        Parameters
        ----------
        data : dict
            To be cleaned.

        Returns
        -------
        dict
            Correct body.
        """
        cleaned = self.remove_foreign_key(data)
        filled = self.fill_body_with_missing_key(cleaned)
        return filled

    # use in format_body
    def remove_foreign_key(self, data):
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
        for i in list(data):
            if i not in self.get_body_param():
                del data[i]
        return data

    # use in format_body
    def fill_body_with_missing_key(self, data):
        """ Fill keys that are not mandatory with default value for PostRecipe.
         - resume/note -> ""
         - level/cooking_time/preparation_time/nb_people -> 0
         - categories -> []

        Parameters
        ----------
        data : dict
            Dict to be filled with default value.

        Returns
        -------
        dict
            Filled dict.
        """
        """ from body """
        for key in self.get_body_param():
            if key not in data:
                if key in [self.param_resume, self.param_note]:
                    data[key] = ""
                elif key in [self.param_level, self.param_cooking_time, self.param_preparation_time,
                             self.param_nb_people]:
                    data[key] = 0
                elif key in [self.param_categories]:
                    data[key] = []
        """ from default """
        data[self.default_steps] = []
        return data
