""" Flask """

from flask import Flask, render_template, send_from_directory
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from app import utils

import os

""" flask and CORS options"""
backend = Flask(__name__)
CORS(backend)

""" config """
backend.config["ENV"] = "production"
backend.config["JWT_SECRET_KEY"] = "super-secret-cookbook"
backend.config["EXPIRATION_TOKEN"] = 5
backend.config["FLASK_PATH"] = utils.PathExplorer().flask_path
backend.config["FILE_STORAGE_PATH"] = utils.PathExplorer().files_storage_path
backend.config['APPLICATION_ROOT'] = '/flask'
#backend.config["INDEX_PATH"] = "/home/rhr/Workspace/Python/Cookbook/client/build/index.html"
backend.config["INDEX_PATH"] = "./../client/build"

""" JWT for auth """
bcrypt = Bcrypt(backend)
jwt = JWTManager(backend)


@backend.route('/')
def get_index():
    """
    @api {get} /  GetIndex
    @apiGroup Root
    @apiDescription Get Index path

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.ingredient.success.ok',
        'codeStatus': 200,
        'data': 'path/to/index'
    }
    """
    """ return response """
    #return render_template("index.html")
    #return send_from_directory(backend.static_folder, 'index.html')
    #return send_from_directory(directory="/home/rhr/Workspace/Python/Cookbook/client/build/", filename='index.html')
    current_path = os.getcwd()
    p = current_path.replace('Flask', '/client/build')
    print(p)
    return send_from_directory(directory=p, filename='index.html')
    #return utils.ResponseMaker().return_response(data="tata", api="cookbook", http_code=200)


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
    return utils.ResponseMaker().return_response(data=err, api="cookbook", http_code=401)


@jwt.expired_token_loader
def auth_handler_expired(err):
    """ Return a response if auth is expired.

    Parameters
    ----------
    err
        Error from jwt_verify.

    Returns
    -------
    Any
        Server response.
    """
    return utils.ResponseMaker().return_response(data=err, api="cookbook", http_code=401)


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
    return utils.ResponseMaker().return_response(data=err, api="cookbook", http_code=401)


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
    return utils.ResponseMaker().return_response(data=err.description, api="cookbook", http_code=404)


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
    return utils.ResponseMaker().return_response(data=err, api="cookbook", http_code=405)
