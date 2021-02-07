""" Flask and blueprint registry"""

from app.flask import backend
import app.files.router as files_routes
import app.ingredient.router as ingredient_routes
import app.recipe.router as recipe_routes
import app.user.router as user_routes

backend.register_blueprint(files_routes.apis, url_prefix='/flask/files')
backend.register_blueprint(ingredient_routes.apis, url_prefix='/flask/ingredient')
backend.register_blueprint(recipe_routes.apis, url_prefix='/flask/recipe')
backend.register_blueprint(user_routes.apis, url_prefix='/flask/user')
