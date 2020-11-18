class Factory(object):

    def __init__(self):
        """ Class to work around PutRecipe.
        """
        self.param_id = "_id"
        self.param_with_files = "with_files"
        self.param_title = "title"
        self.param_slug = "slug"
        self.param_level = "level"
        self.param_resume = "resume"
        self.param_cooking_time = "cooking_time"
        self.param_preparation_time = "preparation_time"
        self.param_nb_people = "nb_people"
        self.param_note = "note"
        self.param_categories = "categories"
        self.body = {}

    def get_body_param(self):
        """ Get PutRecipe's body parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [self.param_title, self.param_slug, self.param_level, self.param_resume, self.param_cooking_time,
                self.param_preparation_time, self.param_nb_people, self.param_note, self.param_categories]

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
        return self.body

    # use in clean_body
    def remove_foreign_key(self):
        """ Remove keys that are not in PutRecipe's parameters.
        """
        for i in list(self.body):
            if i not in self.get_body_param():
                del self.body[i]
