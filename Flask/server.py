from flask import Flask, make_response

import factory as factory
import ingredient.router as ingredient
import recipe.recipe.router as recipe
import recipe.steps.router as recipe_steps


app = Flask(__name__)

app.register_blueprint(ingredient.ingredient_api)
app.register_blueprint(recipe.recipe_api)
app.register_blueprint(recipe_steps.recipe_steps_api)


@app.errorhandler(404)
def not_found(error):
    """" abort 404 """
    body = factory.ServerResponse().format_response(data=error.description, api="cookbook", is_mongo=False, code=404)
    return make_response(body, 404)


@app.errorhandler(405)
def method_not_allowed(error):
    """" abort 405 """
    body = factory.ServerResponse().format_response(data=error.description, api="cookbook", is_mongo=False, code=405)
    return make_response(body, 405)


if __name__ == "__main__":
    app.run(debug=False)
