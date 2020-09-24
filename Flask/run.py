from flask import Flask, make_response
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import sys

import utils
import app.file.router
import app.ingredient.router
import app.recipe.router
import app.user.router

backend = Flask(__name__)

backend.config["ENV"] = "production"
backend.config["JWT_SECRET_KEY"] = "super-secret-cookbook"
backend.config["EXPIRATION_TOKEN"] = 5

bcrypt = Bcrypt(backend)
jwt = JWTManager(backend)

backend.register_blueprint(app.file.router.api)
backend.register_blueprint(app.ingredient.router.api)
backend.register_blueprint(app.recipe.router.api)
backend.register_blueprint(app.user.router.api)


@jwt.unauthorized_loader
def missing_handler(e):
    body = utils.Server.return_response(data="missing", api="cookbook", code=401)
    return make_response(body, 401)


@jwt.expired_token_loader
def expired_handler():
    body = utils.Server.return_response(data="expired", api="cookbook", code=401)
    return make_response(body, 401)


@jwt.invalid_token_loader
def invalid_handler(e):
    body = utils.Server.return_response(data="invalid", api="cookbook", code=401)
    return make_response(body, 401)


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
    """ set backend config """
    options = utils.Server.get_backend_options(args=sys.argv)
    backend.config.update(ENV=options["env"], TESTING=options["testing"], DEBUG=options["debug"])
    """ launch server """
    if options["env"] == "development":
        backend.run(host='0.0.0.0', port=utils.Server.port)
    else:
        from waitress import serve
        serve(backend, host="0.0.0.0", port=utils.Server.port)
