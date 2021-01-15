import datetime

from flask import abort
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity, create_access_token
from functools import wraps

from app import backend
from app.user import User


class Auth(object):
    """ For token and right gestion """

    """ create token """
    @staticmethod
    def create_token(**kwargs):
        """ Create token for authentification.

        Parameters
        ----------
        kwargs : str
            can be email or _id.

        Returns
        -------
        str
           Access token.
        """
        user_id = ""
        if "email" in kwargs:
            user_id = User().get_user_id_by_email(email=kwargs["email"])
        elif "_id" in kwargs:
            user_id = kwargs["_id"]
        with backend.app_context():
            expires = datetime.timedelta(seconds=backend.config["EXPIRATION_TOKEN"])
            access_token = create_access_token(identity=user_id, expires_delta=expires)
            return access_token

    """ wrapper """
    @staticmethod
    def login_required(f):
        """ Wrapper to check auth.

        Returns
        -------
        Any
           Auth_handler if authentification failed.
        """
        @wraps(f)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            return f(*args, **kwargs)
        return wrapper

    @staticmethod
    def admin_only(f):
        """ Wrapper to check if User is an admin.

        Returns
        -------
        Any
           Server response.
        """
        @wraps(f)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            if "admin" not in User().get_user_status(get_jwt_identity()):
                return abort(status=403)
            else:
                pass
            return f(*args, **kwargs)
        return wrapper
