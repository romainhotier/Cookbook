import utils

server = utils.Server()


class GetMe(object):
    """ Class to test GetMe.
    """

    def __init__(self):
        self.url = 'user/me'
        self.rep_code_msg_ok = server.rep_code_msg_ok.replace("xxx", "user")
        self.rep_code_msg_error_401 = server.rep_code_msg_error_401.replace("xxx", "cookbook")

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
    def data_expected(user):
        """ Format data's response.

        Parameters
        ----------
        user : Any
            UserTest.

        Returns
        -------
        str
            Data's response.
        """
        return {'_id': user.get_id(),
                'display_name': user.display_name,
                'email': user.email,
                'status': user.status}
