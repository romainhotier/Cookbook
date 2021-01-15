from app.auth import Auth
from app.user import User


class Factory(object):

    def __init__(self):
        """ Class to work around PostUserLogin.
        """
        self.param_email = "email"
        self.param_password = "password"
        self.body = {}

    """ clean body """
    def clean_body(self, data):
        """ Remove keys that are not in PostUserLogin's parameters.

        Parameters
        ----------
        data : dict
            To be cleaned.

        Returns
        -------
        dict
            Correct body.
        """
        self.__setattr__("body", data)
        self.remove_invalid_key()
        return self.body

    # use in clean_body
    def remove_invalid_key(self):
        """ Remove keys that are not in PostUserLogin's parameters.
        """
        for i in list(self.body):
            if i not in self.get_body_param():
                del self.body[i]

    # use in remove_invalid_key
    def get_body_param(self):
        """ Get PostUserLogin's body parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [self.param_email, self.param_password]

    """ check password """
    def check_password(self, data):
        """ Check access for the user.

        Parameters
        ----------
        data : dict
            PostUserLogin's body.

        Returns
        -------
        bool
            True if the password is correct.
        """
        visitor = User().select_one_by_email(email=data[self.param_email]).result
        return User().check_password(password=visitor["password"], password_attempt=data[self.param_password])

    """ create token """
    @staticmethod
    def create_token(email):
        return Auth().create_token(user_email=email)
