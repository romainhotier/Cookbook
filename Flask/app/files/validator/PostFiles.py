import utils
import app.files.factory.PostFiles as Factory

mongo = utils.Mongo()
validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate PostFiles.
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
