import utils
import app.recipe.factory.PutRecipe as Factory

mongo = utils.Mongo()
validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate PutRecipe.
    """

    @staticmethod
    def is_object_id_valid(value):
        """ Check if _id is correct.

        Parameters
        ----------
        value : str
            Recipe's ObjectId.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_object_id(param=api.param_id, value=value)
        validator.is_object_id_in_collection(param=api.param_id, value=value, collection=mongo.collection_recipe)
        return True

    @staticmethod
    def is_with_files_valid(value):
        """ Check if with_files is correct if specified.

        Parameters
        ----------
        value : str
            With_files's value.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_string_boolean_or_none(param=api.param_with_files, value=value)
        return True

    def is_body_valid(self, data):
        validator.has_at_least_one_key(data=data)
        self.is_title_valid(data=data)
        self.is_slug_valid(data=data)
        self.is_level_valid(data=data)
        self.is_resume_valid(data=data)
        self.is_cooking_time_valid(data=data)
        self.is_preparation_time_valid(data=data)
        self.is_nb_people_valid(data=data)
        self.is_note_valid(data=data)
        self.is_categories_valid(data=data)

# use in is_body_valid
    @staticmethod
    def is_title_valid(data):
        """ Check if title is correct.

        Parameters
        ----------
        data : dict
            PutRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_title in data:
            validator.is_string(param=api.param_title, value=data[api.param_title])
            validator.is_string_non_empty(param=api.param_title, value=data[api.param_title])
            validator.is_unique_recipe(param=api.param_title, value=data[api.param_title])
            return True
        return True

    # use in is_body_valid
    @staticmethod
    def is_slug_valid(data):
        """ Check if slug is correct.

        Parameters
        ----------
        data : dict
            PutRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_slug in data:
            validator.is_string(param=api.param_slug, value=data[api.param_slug])
            validator.is_string_non_empty(param=api.param_slug, value=data[api.param_slug])
            validator.is_unique_recipe(param=api.param_slug, value=data[api.param_slug])
            return True
        return True

    # use in is_body_valid
    @staticmethod
    def is_level_valid(data):
        """ Check if level is correct if specified.

        Parameters
        ----------
        data : dict
            PutRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_level in data:
            validator.is_int(param=api.param_level, value=data[api.param_level])
            validator.is_between_x_y(param=api.param_level, value=data[api.param_level], x=0, y=3)
            return True
        return True

    # use in is_body_valid
    @staticmethod
    def is_resume_valid(data):
        """ Check if resume is correct if specified.

        Parameters
        ----------
        data : dict
            PutRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_resume in data:
            validator.is_string(param=api.param_resume, value=data[api.param_resume])
            return True
        return True

    # use in is_body_valid
    @staticmethod
    def is_cooking_time_valid(data):
        """ Check if cooking_time is correct if specified.

        Parameters
        ----------
        data : dict
            PutRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_cooking_time in data:
            validator.is_int(param=api.param_cooking_time, value=data[api.param_cooking_time])
            return True
        return True

    # use in is_body_valid
    @staticmethod
    def is_preparation_time_valid(data):
        """ Check if preparation_time is correct if specified.

        Parameters
        ----------
        data : dict
            PutRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_preparation_time in data:
            validator.is_int(param=api.param_preparation_time, value=data[api.param_preparation_time])
            return True
        return True

    # use in is_body_valid
    @staticmethod
    def is_nb_people_valid(data):
        """ Check if nb_people is correct if specified.

        Parameters
        ----------
        data : dict
            PutRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_nb_people in data:
            validator.is_int(param=api.param_nb_people, value=data[api.param_nb_people])
            return True
        return True

    # use in is_body_valid
    @staticmethod
    def is_note_valid(data):
        """ Check if note is correct if specified.

        Parameters
        ----------
        data : dict
            PutRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_note in data:
            validator.is_string(param=api.param_note, value=data[api.param_note])
            return True
        return True

    # use in is_body_valid
    @staticmethod
    def is_categories_valid(data):
        """ Check if categories is correct if specified.

        Parameters
        ----------
        data : dict
            PutRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_categories in data:
            validator.is_array(param=api.param_categories, value=data[api.param_categories])
            return True
        return True
