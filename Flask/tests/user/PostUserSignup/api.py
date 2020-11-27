import jsonschema

import utils


server = utils.Server()


class PostUserSignup(object):
    """ Class to test PostUserSignup.
    """

    def __init__(self):
        self.url = 'user/signup'
        self.param_display_name = "display_name"
        self.param_email = "email"
        self.param_password = "password"
        self.rep_code_msg_created = server.rep_code_msg_created.replace("xxx", "user")
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "user")
        self.rep_code_msg_error_404_url = server.rep_code_msg_error_404.replace("xxx", "cookbook")

    @staticmethod
    def create_detail(param, msg, **kwargs):
        """ Format Server's detail response.

        Parameters
        ----------
        param : str
            Tested parameter.
        msg : str
            Server's message.
        kwargs : str
            Value if one existed.

        Returns
        -------
        dict
            Server's detail response.
        """
        detail = {"param": param, "msg": msg}
        if "value" in kwargs:
            detail["value"] = kwargs["value"]
        return detail

    @staticmethod
    def check_not_present(value, rep):
        """ Check if data/detail is not present in Server's response.

        Parameters
        ----------
        value : str
            Tested value.
        rep : dict
            Server's response.

        Returns
        -------
        bool
        """
        if value in rep.keys():
            return False
        else:
            return True

    @staticmethod
    def create_schema(user):
        """ Format schema's response.

        Parameters
        ----------
        user : Any
            UserTest.

        Returns
        -------
        dict
            Schema.
        """
        return {"type": "object",
                "properties": {
                    "_id": {"type": "string"},
                    "display_name": {"enum": [user.display_name]},
                    "email": {"enum": [user.email]}},
                "required": ["_id", "display_name", "email"],
                "additionalProperties": False}

    def json_check(self, data, data_expected):
        """ Format schema's response.

        Parameters
        ----------
        data : dict
            Server's response.
        data_expected : Any
            Schema from UserTest.

        Returns
        -------
        dict
            Result and err if exist.
        """
        try:
            jsonschema.validate(instance=data, schema=self.create_schema(user=data_expected))
            return {"result": True, "error": None}
        except jsonschema.exceptions.ValidationError as err:
            return {"result": False, "error": err}
