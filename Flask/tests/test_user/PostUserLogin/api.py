import utils

server = utils.Server()


class PostUserLogin(object):
    """ Class to test PostUserLogin.
    """

    def __init__(self):
        self.url = 'user/login'
        self.param_email = "email"
        self.param_password = "password"
        self.rep_code_msg_ok = server.rep_code_msg_ok.replace("xxx", "user")
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "user")
        self.rep_code_msg_error_404_url = server.rep_code_msg_error_404.replace("xxx", "cookbook")
        self.data_regex = "[A-Za-z0-9\-\._~\+\/]+=*"

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
