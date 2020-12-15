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

    def is_body_valid(self, data):
        validator.has_at_least_one_key(param="body", data=data)
        self.is_categories_valid(data=data)
        self.is_cooking_time_valid(data=data)
        self.is_ingredients_valid(data=data)
        self.is_level_valid(data=data)
        self.is_nb_people_valid(data=data)
        self.is_note_valid(data=data)
        self.is_preparation_time_valid(data=data)
        self.is_resume_valid(data=data)
        self.is_slug_valid(data=data)
        self.is_status_valid(data=data)
        self.is_steps_valid(data=data)
        self.is_title_valid(data=data)

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
    def is_ingredients_valid(self, data):
        """ Check if ingredients is correct.

        Parameters
        ----------
        data : dict
            PutRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_ingredients in data:
            validator.is_array(param=api.param_ingredients, value=data[api.param_ingredients])
            validator.is_array_non_empty(param=api.param_ingredients, value=data[api.param_ingredients])
            validator.is_array_of_object(param=api.param_ingredients, value=data[api.param_ingredients])
            for ingredient in data[api.param_ingredients]:
                self.is_id_ingredient_valid(data=ingredient)
                self.is_quantity_valid(data=ingredient)
                self.is_unit_valid(data=ingredient)
            validator.is_unique_link_multi(param=api.param_ingredients_id, data=data)
            return True
        return True

    # use in is_ingredients_valid
    @staticmethod
    def is_id_ingredient_valid(data):
        """ Check if _id_ingredient is correct.

        Parameters
        ----------
        data : dict
            PutRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_mandatory(param=api.param_ingredients_id, data=data)
        validator.is_object_id(param=api.param_ingredients_id, value=data[api.param_ingredients_id])
        validator.is_object_id_in_collection(param=api.param_ingredients_id, value=data[api.param_ingredients_id],
                                             collection=mongo.collection_ingredient)
        return True

    # use in is_ingredients_valid
    @staticmethod
    def is_quantity_valid(data):
        """ Check if quantity is correct.

        Parameters
        ----------
        data : dict
            PutRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_mandatory(param=api.param_ingredients_quantity, data=data)
        validator.is_int(param=api.param_ingredients_quantity, value=data[api.param_ingredients_quantity])
        return True

    # use in is_ingredients_valid
    @staticmethod
    def is_unit_valid(data):
        """ Check if unit is correct.

        Parameters
        ----------
        data : dict
            PutRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_mandatory(param=api.param_ingredients_unit, data=data)
        validator.is_string(param=api.param_ingredients_unit, value=data[api.param_ingredients_unit])
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
    def is_status_valid(data):
        """ Check if status is correct if specified.

        Parameters
        ----------
        data : dict
            PutRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_status in data:
            validator.is_in(param=api.param_status, value=data[api.param_status], values=["in_progress", "finished"])
            return True
        return True

    # use in is_body_valid
    def is_steps_valid(self, data):
        """ Check if steps is correct.

        Parameters
        ----------
        data : dict
            PutRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_steps in data:
            validator.is_array(param=api.param_steps, value=data[api.param_steps])
            validator.is_array_non_empty(param=api.param_steps, value=data[api.param_steps])
            for step in data[api.param_steps]:
                if isinstance(data, str):
                    self.is_description_valid_string(data=step)
                elif isinstance(data, dict):
                    self.is_description_valid_object(data=step)
                else:
                    pass
            return True
        return True

    # use in is_steps_valid
    @staticmethod
    def is_description_valid_string(data):
        """ Check if description is correct.

        Parameters
        ----------
        data : str
            PutRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_string_non_empty(param=api.param_steps_description, value=data)
        return True

    # use in is_steps_valid
    @staticmethod
    def is_description_valid_object(data):
        """ Check if description is correct.

        Parameters
        ----------
        data : str
            PutRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        return True

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
