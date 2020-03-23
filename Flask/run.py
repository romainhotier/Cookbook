from flask import Flask, make_response
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

import server.server as server
import app.user.user.router as user
import app.ingredient.ingredient.router as ingredient
import app.recipe.recipe.router as recipe
import app.recipe.steps.router as recipe_steps
import app.steps.steps.router as steps
import app.file.file.router as file
import app.link.ingredient_recipe.router as link_ingredient_recipe

app = Flask(__name__)
### TBD ### app.config.from_envvar('COOKBOOK_ENV')
app.config["ENV"] = "testing"
app.config["JWT_SECRET_KEY"] = "super-secret-cookbook"
app.config["EXPIRATION_TOKEN"] = 5
###########

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.register_blueprint(user.user_api)
app.register_blueprint(ingredient.ingredient_api)
app.register_blueprint(recipe.recipe_api)
app.register_blueprint(recipe_steps.recipe_steps_api)
app.register_blueprint(steps.steps_api)
app.register_blueprint(file.file_api)
app.register_blueprint(link_ingredient_recipe.ingredient_recipe_api)


@app.errorhandler(404)
def not_found(error):
    """" abort 404 """
    body = server.ServerResponse().return_response(data=error.description, api="cookbook", code=404)
    return make_response(body, 404)


@app.errorhandler(405)
def method_not_allowed(error):
    """" abort 405 """
    body = server.ServerResponse().return_response(data=error.description, api="cookbook", is_mongo=False, code=405)
    return make_response(body, 405)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=(app.config["ENV"] in ["testing", "development"]))

