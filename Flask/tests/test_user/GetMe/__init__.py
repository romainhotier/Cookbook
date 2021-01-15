from tests import rep


class GetMe(object):
    """ Class to test GetMe.
    """

    def __init__(self):
        self.url = 'user/me'
        self.rep_code_msg_ok = rep.code_msg_ok.replace("xxx", "user")
        self.rep_code_msg_error_401 = rep.code_msg_error_401.replace("xxx", "cookbook")

    @staticmethod
    def data_expected(user):
        """ Format data's response.

        Parameters
        ----------
        user : UserTest
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


api = GetMe()
