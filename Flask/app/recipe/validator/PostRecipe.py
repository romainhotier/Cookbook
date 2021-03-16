from app import utils
import app.recipe.factory.PostRecipe as Factory

mongo = utils.Mongo()
validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate PostRecipe.
    """

    def is_body_valid(self, data):
        """ Check if body is correct.

        Parameters
        ----------
        data : dict
            PostRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
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
            PostRecipe's body.

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
            PostRecipe's body.

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
            PostRecipe's body.

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
                self.is_ingredient_id_valid(data=ingredient)
                self.is_ingredient_quantity_valid(data=ingredient)
                self.is_ingredient_unit_valid(data=ingredient)
            validator.is_unique_ingredient_associated(param=api.param_ingredient+"."+api.param_ingredient_id, data=data)
            return True
        return True

    # use in is_ingredients_valid
    @staticmethod
    def is_ingredient_id_valid(data):
        """ Check if _id_ingredient is correct.

        Parameters
        ----------
        data : dict
            PostRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        param_name = api.param_ingredient+"."+api.param_ingredient_id
        validator.is_mandatory(name=param_name, param=api.param_ingredient_id, data=data)
        validator.is_object_id(param=param_name, value=data[api.param_ingredient_id])
        validator.is_object_id_in_collection(param=param_name, value=data[api.param_ingredient_id],
                                             collection=mongo.collection_ingredient)
        return True

    # use in is_ingredients_valid
    @staticmethod
    def is_ingredient_quantity_valid(data):
        """ Check if quantity is correct.

        Parameters
        ----------
        data : dict
            PostRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        param_name = api.param_ingredient + "." + api.param_ingredient_quantity
        validator.is_mandatory(name=param_name, param=api.param_ingredient_quantity, data=data)
        validator.is_float(param=param_name, value=data[api.param_ingredient_quantity])
        return True

    # use in is_ingredients_valid
    @staticmethod
    def is_ingredient_unit_valid(data):
        """ Check if unit is correct.

        Parameters
        ----------
        data : dict
            PostRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        param_name = api.param_ingredient + "." + api.param_ingredient_unit
        validator.is_mandatory(name=param_name, param=api.param_ingredient_unit, data=data)
        validator.is_string(param=param_name, value=data[api.param_ingredient_unit])
        return True

    # use in is_body_valid
    @staticmethod
    def is_level_valid(data):
        """ Check if level is correct if specified.

        Parameters
        ----------
        data : dict
            PostRecipe's body.

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
            PostRecipe's body.

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
            PostRecipe's body.

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
            PostRecipe's body.

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
            PostRecipe's body.

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
            PostRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_mandatory(name=api.param_slug, param=api.param_slug, data=data)
        validator.is_string(param=api.param_slug, value=data[api.param_slug])
        validator.is_string_non_empty(param=api.param_slug, value=data[api.param_slug])
        validator.is_unique_recipe(param=api.param_slug, value=data[api.param_slug])
        return True

    # use in is_body_valid
    @staticmethod
    def is_status_valid(data):
        """ Check if status is correct if specified.

        Parameters
        ----------
        data : dict
            PostRecipe's body.

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
            PostRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_steps in data:
            validator.is_array(param=api.param_steps, value=data[api.param_steps])
            if len(data[api.param_steps]) != 0:
                validator.is_array_of_object(param=api.param_steps, value=data[api.param_steps])
                for step in data[api.param_steps]:
                    self.is_description_valid(data=step)
                return True
            return True
        return True

    # use in is_steps_valid
    @staticmethod
    def is_description_valid(data):
        """ Check if description is correct.

        Parameters
        ----------
        data : dict
            PostRecipe's step body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        param_name = api.param_step+"."+api.param_step_description
        validator.is_mandatory(name=param_name, param=api.param_step_description, data=data)
        validator.is_string(param=param_name, value=data[api.param_step_description])
        validator.is_string_non_empty(param=param_name, value=data[api.param_step_description])
        return True

    # use in is_body_valid
    @staticmethod
    def is_title_valid(data):
        """ Check if title is correct.

        Parameters
        ----------
        data : dict
            PostRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_mandatory(name=api.param_title, param=api.param_title, data=data)
        validator.is_string(param=api.param_title, value=data[api.param_title])
        validator.is_string_non_empty(param=api.param_title, value=data[api.param_title])
        validator.is_unique_recipe(param=api.param_title, value=data[api.param_title])
        return True
