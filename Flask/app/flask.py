""" Flask """

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from app import utils


""" flask and CORS options"""
backend = Flask(__name__)
CORS(backend)

""" config """
backend.config["ENV"] = "production"
backend.config["JWT_SECRET_KEY"] = "super-secret-cookbook"
backend.config["EXPIRATION_TOKEN"] = 5
backend.config["SYSTEM"] = utils.PathExplorer().system
backend.config["FLASK_PATH"] = utils.PathExplorer().flask_path
backend.config["FILE_STORAGE_PATH"] = utils.PathExplorer().files_storage_path

""" JWT for auth """
bcrypt = Bcrypt(backend)
jwt = JWTManager(backend)


@jwt.unauthorized_loader
def auth_handler_missing(err):
    """ Return a response if auth is missing.

    Parameters
    ----------
    err
        Error from jwt_verify.

    Returns
    -------
    Any
        Server response.
    """
    return utils.Response().sent(api="cookbook", http_code=401, detail=err)


@jwt.expired_token_loader
def auth_handler_expired(err, data):
    """ Return a response if auth is expired.

    Parameters
    ----------
    err
        Error from jwt_verify.
    data:
        Other data.

    Returns
    -------
    Any
        Server response.
    """
    return utils.Response().sent(api="cookbook", http_code=401, detail=err, other=data)


@jwt.invalid_token_loader
def auth_handler_invalid(err):
    """ Return a response if auth is invalid.

    Parameters
    ----------
    err
        Error from jwt_verify.

    Returns
    -------
    Any
        Server response.
    """
    return utils.Response().sent(api="cookbook", http_code=401, detail=err)


@backend.errorhandler(404)
def back_handler_url_not_found(err):
    """ Return a response for url not found.

    Parameters
    ----------
    err
        Error from Flask.

    Returns
    -------
    Any
        Server response.
    """
    return utils.Response().sent(api="cookbook", http_code=404, detail=err)


@backend.errorhandler(405)
def back_handler_not_allowed(err):
    """ Return a response for request not allowed.

    Parameters
    ----------
    err
        Error from Flask.

    Returns
    -------
    Any
        Server response.
    """
    return utils.Response().sent(api="cookbook", http_code=405, detail=err)
