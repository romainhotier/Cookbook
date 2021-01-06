from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import sys

import utils
import app.file_mongo.router as file_mongo_routes
import app.files.router as files_routes
import app.ingredient.router as ingredient_routes
import app.recipe.router as recipe_routes
import app.user.router as user_routes

backend = Flask(__name__)
CORS(backend)

backend.config["ENV"] = "production"
backend.config["JWT_SECRET_KEY"] = "super-secret-cookbook"
backend.config["EXPIRATION_TOKEN"] = 5

bcrypt = Bcrypt(backend)
jwt = JWTManager(backend)

backend.register_blueprint(file_mongo_routes.apis)
backend.register_blueprint(files_routes.apis)
backend.register_blueprint(ingredient_routes.apis)
backend.register_blueprint(recipe_routes.apis)
backend.register_blueprint(user_routes.apis)


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
    return utils.Server().return_response(data=err, api="cookbook", http_code=401)


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
    return utils.Server().return_response(data=err, api="cookbook", http_code=401)


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
    return utils.Server().return_response(data=err, api="cookbook", http_code=401)


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
    return utils.Server().return_response(data=err.description, api="cookbook", http_code=404)


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
    return utils.Server().return_response(data=err, api="cookbook", http_code=405)


if __name__ == "__main__":
    """ check mongo up """
    utils.Mongo().check_mongodb_up()
    """ set backend config """
    options = utils.Server().get_backend_options(args=sys.argv)
    backend.config.update(ENV=options["env"], TESTING=options["testing"], DEBUG=options["debug"])
    """ launch server """
    if options["env"] == "development":
        backend.run(host='0.0.0.0', port=utils.Server().port)
    else:
        from waitress import serve
        serve(backend, host="0.0.0.0", port=utils.Server().port)
