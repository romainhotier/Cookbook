from tests import rep


class PostUserLogin(object):
    """ Class to test PostUserLogin.
    """

    def __init__(self):
        self.url = 'user/login'
        self.param_email = "email"
        self.param_password = "password"
        self.rep_code_msg_ok = rep.code_msg_ok.replace("xxx", "user")
        self.rep_code_msg_error_400 = rep.code_msg_error_400.replace("xxx", "user")
        self.rep_code_msg_error_404_url = rep.code_msg_error_404.replace("xxx", "cookbook")
        self.data_regex = "[A-Za-z0-9\-\._~\+\/]+=*"


api = PostUserLogin()
