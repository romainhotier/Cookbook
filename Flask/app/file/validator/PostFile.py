import utils
import app.file.factory.PostFile as Factory

mongo = utils.Mongo()
validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate PostFile.
    """

    @staticmethod
    def is_object_id_valid(kind, value):
        """ Check if _id is correct.

        Parameters
        ----------
        kind : str
            Type of the parent.
        value : str
            ObjectId of the parent.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_object_id(param=api.param_id, value=value)
        validator.is_object_id_in_collection(param=api.param_id, value=value,
                                             collection=mongo.select_collection(kind=kind))
        return True

    @staticmethod
    def is_object_id_valid_special_step(kind, _id_recipe, **kwargs):
        """ Check if _id is correct for both recipe and step.

        Parameters
        ----------
        kind : str
            Type of the parent.
        _id_recipe : str
            Recipe's ObjectId.
        kwargs : Any
            _id_step : Step's ObjectId.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if kind in ["recipe"]:
            validator.is_object_id(param=api.param_id_recipe, value=_id_recipe)
            validator.is_object_id_in_collection(param=api.param_id_recipe, value=_id_recipe,
                                                 collection=mongo.select_collection(kind=kind))
            return True
        if kind in ["step"]:
            validator.is_object_id(param=api.param_id_step, value=kwargs[api.param_id_step])
            validator.is_object_id_in_recipe_steps(param=api.param_id_step, _id_recipe=_id_recipe,
                                                   _id_step=kwargs[api.param_id_step])
            return True
        return True

    def is_body_valid(self, data):
        """ Check if body is correct.

        Parameters
        ----------
        data : dict
            PostFile's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        self.is_path_valid(data=data)
        self.is_filename_valid(data=data)
        self.is_is_main_valid(data=data)

    # use in is_body_valid
    @staticmethod
    def is_path_valid(data):
        """ Check if path is correct.

        Parameters
        ----------
        data : dict
            PostFile's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_mandatory(name=api.param_path, param=api.param_path, data=data)
        validator.is_string(param=api.param_path, value=data[api.param_path])
        validator.is_string_non_empty(param=api.param_path, value=data[api.param_path])
        validator.is_path_exist(param=api.param_path, value=data[api.param_path])
        return True

    # use in is_body_valid
    @staticmethod
    def is_filename_valid(data):
        """ Check if filename is correct.

        Parameters
        ----------
        data : dict
            PostFile's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_mandatory(name=api.param_filename, param=api.param_filename, data=data)
        validator.is_string(param=api.param_filename, value=data[api.param_filename])
        validator.is_string_non_empty(param=api.param_filename, value=data[api.param_filename])
        return True

    # use in is_body_valid
    @staticmethod
    def is_is_main_valid(data):
        """ Check if is_main is correct if specified.

        Parameters
        ----------
        data : dict
            PostFile's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_is_main in data:
            validator.is_boolean(param=api.param_is_main, value=data[api.param_is_main])
            return True
        return True
