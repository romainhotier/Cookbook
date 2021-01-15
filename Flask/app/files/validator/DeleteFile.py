from app import utils
import app.files.factory.DeleteFile as Factory

validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate DeleteFiles.
    """

    @staticmethod
    def is_path_valid(value):
        """ Check if path is correct.

        Parameters
        ----------
        value : str
            ObjectId of the parent.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_string(param=api.param_path, value=value)
        validator.is_string_non_empty(param=api.param_path, value=value)
        validator.is_string_path(param=api.param_path, value=value)
