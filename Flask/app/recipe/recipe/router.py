from flask import Blueprint, request

from server import factory as factory
import app.recipe.recipe.model as recipe_model
import app.recipe.recipe.validator.GetRecipe as validator_GetRecipe
import app.recipe.recipe.validator.PostRecipe as validator_PostRecipe
import app.recipe.recipe.validator.PutRecipe as validator_PutRecipe
import app.recipe.recipe.validator.DeleteRecipe as validator_DeleteRecipe
import app.recipe.recipe.factory.PostRecipe as factory_PostRecipe
import app.recipe.recipe.factory.PutRecipe as factory_PutRecipe


recipe_api = Blueprint('recipe_api', __name__)

recipe = recipe_model.Recipe()
get_recipe_validator = validator_GetRecipe.Validator()
post_recipe_validator = validator_PostRecipe.Validator()
put_recipe_validator = validator_PutRecipe.Validator()
delete_recipe_validator = validator_DeleteRecipe.Validator()
post_recipe_factory = factory_PostRecipe.Factory()
put_recipe_factory = factory_PutRecipe.Factory()


""" 
recipe route 

- GET /recipe
- GET /recipe/<_id>
- POST /recipe
- PUT /recipe
- DELETE /recipe/<_id>

"""


@recipe_api.route('/recipe', methods=['GET'])
def get_all_recipe():
    """
    @api {get} /recipe  Get all recipe
    @apiName GetAllRecipe
    @apiGroup Recipe
    """
    result = recipe.select_all()
    return factory.ServerResponse().format_response(data=result, api="recipe", is_mongo=True, code=200)


@recipe_api.route('/recipe/<_id>', methods=['GET'])
def get_recipe(_id):
    """ route get one recipe by his ObjectId """
    get_recipe_validator.is_object_id_valid(_id)
    result = recipe.select_one(_id)
    return factory.ServerResponse().format_response(data=result, api="recipe", is_mongo=True, code=200)


@recipe_api.route('/recipe', methods=['POST'])
def post_recipe():
    """ insert one recipe """
    body = post_recipe_factory.clean_body(request.json)
    post_recipe_validator.is_body_valid(body)
    post_recipe_validator.is_title_already_exist(body)
    inserted = recipe.insert(body)
    return factory.ServerResponse().format_response(data=inserted, api="recipe", is_mongo=True, code=201)


@recipe_api.route('/recipe/<_id>', methods=['PUT'])
def put_recipe(_id):
    """ update one recipe """
    put_recipe_validator.is_object_id_valid(_id)
    body = put_recipe_factory.clean_body(request.json)
    put_recipe_validator.is_body_valid(body)
    put_recipe_validator.is_title_already_exist(body)
    updated = recipe.update(_id, body)
    return factory.ServerResponse().format_response(data=updated, api="recipe", is_mongo=True, code=200)


@recipe_api.route('/recipe/<_id>', methods=['DELETE'])
def delete_recipe(_id):
    """ delete one recipe """
    delete_recipe_validator.is_object_id_valid(_id)
    recipe.delete(_id)
    return factory.ServerResponse().format_response(data=None, api="recipe", is_mongo=True, code=204)


""" 
recipe error handler 

http 400
http 404

"""


@recipe_api.errorhandler(400)
def validator_failed(error):
    """" abort 400 """
    return factory.ServerResponse().format_response(data=error.description, api="recipe", is_mongo=False, code=400)


@recipe_api.errorhandler(404)
def not_found(error):
    """" abort 404 """
    return factory.ServerResponse().format_response(data=error.description, api="recipe", is_mongo=False, code=404)
