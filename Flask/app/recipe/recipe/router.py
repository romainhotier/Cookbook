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


@recipe_api.route('/recipe', methods=['GET'])
def get_all_recipe():
    """
    @api {get} /recipe  GetAllRecipe
    @apiGroup Recipe
    @apiDescription Get all recipes

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/recipe

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.recipe.success.ok',
        'codeStatus': 200,
        'data': [{'_id': '5e58484037c99f3231407fbe', 'cooking_time': '', 'ingredients': {}, 'level': '',
                  'nb_people': '', 'note': '', 'preparation_time': '', 'resume': '', 'steps': [], 'title': 'aqa_rhr'},
                 {'_id': '5e58484037c99f3231407fc0', 'cooking_time': '', 'ingredients': {}, 'level': '',
                  'nb_people': '', 'note': '', 'preparation_time': '', 'resume': '', 'steps': [], 'title': 'bqa_rhr'}]
    }
    """
    result = recipe.select_all()
    return factory.ServerResponse().format_response(data=result, api="recipe", code=200)


@recipe_api.route('/recipe/<_id>', methods=['GET'])
def get_recipe(_id):
    """
    @api {get} /recipe/<_id>  GetRecipe
    @apiGroup Recipe
    @apiDescription Get a recipe by it's ObjectId

    @apiParam (Query param) {String} _id Recipe's ObjectId

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/recipe/<_id>

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.recipe.success.ok',
        'codeStatus': 200,
        'data': {'_id': '5e58484037c99f3231407fbe', 'cooking_time': '', 'ingredients': {}, 'level': '',
                  'nb_people': '', 'note': '', 'preparation_time': '', 'resume': '', 'steps': [], 'title': 'aqa_rhr'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    get_recipe_validator.is_object_id_valid(_id)
    result = recipe.select_one(_id)
    return factory.ServerResponse().format_response(data=result, api="recipe", code=200)


@recipe_api.route('/recipe', methods=['POST'])
def post_recipe():
    """
    @api {post} /recipe  PostRecipe
    @apiGroup Recipe
    @apiDescription Create a recipe

    @apiParam (Body param) {String} title Recipe's title
    @apiParam (Body param) {String} [level] Recipe's level
    @apiParam (Body param) {String} [resume] Recipe's resume
    @apiParam (Body param) {String} [cooking_time] Recipe's cooking time
    @apiParam (Body param) {String} [preparation_time] Recipe's preparation time
    @apiParam (Body param) {String} [nb_people] Recipe's number of people
    @apiParam (Body param) {String} [note] Recipe's note
    @apiParam (Body param) {Object} [ingredients] Recipe's ingredients
    @apiParam (Body param) {Array} [steps] Recipe's steps

    @apiExample {json} Example usage:
    POST http://127.0.0.1:5000/recipe
    {
        'title': <title>
    }

    @apiSuccessExample {json} Success response:
    HTTPS 201
    {
        'codeMsg': 'cookbook.recipe.success.created',
        'codeStatus': 201,
        'data': {'_id': '5e584a621e2e0101d1d937e3', 'cooking_time': '', 'ingredients': {}, 'level': '', 'nb_people': '',
                 'note': '', 'preparation_time': '', 'resume': '', 'steps': [], 'title': 'qa_rhr_title'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be a string', 'param': 'title', 'value': {}}
    }
    """
    body = post_recipe_factory.clean_body(request.json)
    post_recipe_validator.is_body_valid(body)
    post_recipe_validator.is_title_already_exist(body)
    inserted = recipe.insert(body)
    return factory.ServerResponse().format_response(data=inserted, api="recipe", code=201)


@recipe_api.route('/recipe/<_id>', methods=['PUT'])
def put_recipe(_id):
    """
    @api {put} /recipe/<_id>  PutRecipe
    @apiGroup Recipe
    @apiDescription Update a recipe

    @apiParam (Query param) {String} _id Recipe's ObjectId
    @apiParam (Body param) {String} title Recipe's title
    @apiParam (Body param) {String} [level] Recipe's level
    @apiParam (Body param) {String} [resume] Recipe's resume
    @apiParam (Body param) {String} [cooking_time] Recipe's cooking time
    @apiParam (Body param) {String} [preparation_time] Recipe's preparation time
    @apiParam (Body param) {String} [nb_people] Recipe's number of people
    @apiParam (Body param) {String} [note] Recipe's note
    @apiParam (Body param) {Object} [ingredients] Recipe's ingredients
    @apiParam (Body param) {Array} [steps] Recipe's steps

    @apiExample {json} Example usage:
    PUT http://127.0.0.1:5000/recipe/<_id>
    {
        'title': <title>
    }

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.recipe.success.created',
        'codeStatus': 201,
        'data': {'_id': '5e584a621e2e0101d1d937e3', 'cooking_time': '', 'ingredients': {}, 'level': '', 'nb_people': '',
                 'note': '', 'preparation_time': '', 'resume': '', 'steps': [], 'title': 'qa_rhr_title_update'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be a string', 'param': 'title', 'value': {}}
    }
    """
    put_recipe_validator.is_object_id_valid(_id)
    body = put_recipe_factory.clean_body(request.json)
    put_recipe_validator.is_body_valid(body)
    put_recipe_validator.is_title_already_exist(body)
    updated = recipe.update(_id, body)
    return factory.ServerResponse().format_response(data=updated, api="recipe", code=200)


@recipe_api.route('/recipe/<_id>', methods=['DELETE'])
def delete_recipe(_id):
    """
    @api {delete} /recipe/<_id>  DeleteRecipe
    @apiGroup Recipe
    @apiDescription Delete an recipe by it's ObjectId

    @apiParam (Query param) {String} _id Recipe's ObjectId

    @apiExample {json} Example usage:
    DELETE http://127.0.0.1:5000/recipe/<_id>

    @apiSuccessExample {json} Success response:
    HTTPS 204

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    delete_recipe_validator.is_object_id_valid(_id)
    recipe.delete(_id)
    return factory.ServerResponse().format_response(data=None, api="recipe", code=204)


@recipe_api.errorhandler(400)
def validator_failed(error):
    """" abort 400 """
    return factory.ServerResponse().format_response(data=error.description, api="recipe", code=400)


@recipe_api.errorhandler(404)
def not_found(error):
    """" abort 404 """
    return factory.ServerResponse().format_response(data=error.description, api="recipe", code=404)
