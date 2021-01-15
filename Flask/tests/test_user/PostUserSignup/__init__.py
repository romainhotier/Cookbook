from tests import rep


class PostUserSignup(object):
    """ Class to test PostUserSignup.
    """

    def __init__(self):
        self.url = 'user/signup'
        self.param_display_name = "display_name"
        self.param_email = "email"
        self.param_password = "password"
        self.rep_code_msg_created = rep.code_msg_created.replace("xxx", "user")
        self.rep_code_msg_error_400 = rep.code_msg_error_400.replace("xxx", "user")
        self.rep_code_msg_error_404_url = rep.code_msg_error_404.replace("xxx", "cookbook")

    @staticmethod
    def create_schema(user):
        """ Format schema's response.

        Parameters
        ----------
        user : UserTest
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


api = PostUserSignup()
