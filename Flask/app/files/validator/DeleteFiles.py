from flask import abort
import utils
import app.files.factory.DeleteFiles as Factory
import app.files.model as files_model

server = utils.Server()
mongo = utils.Mongo()
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
        splits = value.split("/")
        if len(splits) == 3:
            if not files_model.Files().check_exist(path=value):
                detail = server.format_detail(param=api.param_path, msg=server.detail_doesnot_exist, value=value)
                return abort(status=400, description=detail)
        else:
            pass  # TBD for steps
        return True
