from flask import Flask, make_response
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

import utils
import app.file.router
import app.ingredient.router
import app.recipe.router
import app.user.router

backend = Flask(__name__)

""" backend.config.from_envvar('COOKBOOK_ENV') """
backend.config["ENV"] = "testing"
backend.config["JWT_SECRET_KEY"] = "super-secret-cookbook"
backend.config["EXPIRATION_TOKEN"] = 5

bcrypt = Bcrypt(backend)
jwt = JWTManager(backend)

backend.register_blueprint(app.file.router.api)
backend.register_blueprint(app.ingredient.router.api)
backend.register_blueprint(app.recipe.router.api)
backend.register_blueprint(app.user.router.api)


@backend.errorhandler(404)
def not_found(error):
    """" abort 404 """
    body = utils.Server.return_response(data=error.description, api="cookbook", code=404)
    return make_response(body, 404)


@backend.errorhandler(405)
def method_not_allowed(error):
    """" abort 405 """
    body = utils.Server.return_response(data=error.description, api="cookbook", is_mongo=False, code=405)
    return make_response(body, 405)


if __name__ == "__main__":
    """ check mongo up """
    utils.Mongo.check_mongodb_up()
    """ launch server """
    backend.run(host='0.0.0.0', port=5000, debug=(backend.config["ENV"] in ["testing", "development"]))
