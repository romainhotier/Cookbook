from flask import Blueprint, request

from server import factory as factory
import app.recipe.recipe.model as recipe_model
import app.file.file.model as file_model
import app.recipe.recipe.validator.GetRecipe as validator_GetRecipe
import app.recipe.recipe.validator.GetAllRecipe as validator_GetAllRecipe
import app.recipe.recipe.validator.PostRecipe as validator_PostRecipe
import app.recipe.recipe.validator.PutRecipe as validator_PutRecipe
import app.recipe.recipe.validator.DeleteRecipe as validator_DeleteRecipe
import app.recipe.recipe.factory.PostRecipe as factory_PostRecipe
import app.recipe.recipe.factory.PutRecipe as factory_PutRecipe


recipe_api = Blueprint('recipe_api', __name__)

recipe = recipe_model.Recipe()
file = file_model.File()
get_recipe_validator = validator_GetRecipe.Validator()
get_all_recipe_validator = validator_GetAllRecipe.Validator()
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
    @apiDescription Get file recipes

    @apiParam (Query param) {String} [with_files] if "true", add recipe's files

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/recipe

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.recipe.success.ok',
        'codeStatus': 200,
        'data': [{'_id': '5e71eb8f39358991f2ea19f6', 'categories': [], 'cooking_time': 0, 'level': 0, 'nb_people': 0,
                  'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'steps': [], 'title': 'qa_rhr_1'},
                 {'_id': '5e71eb8f39358991f2ea19f7', 'categories': [], 'cooking_time': 0, 'level': 0, 'nb_people': 0,
                  'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'steps': [], 'title': 'aqa_rhr_2'}]
    }
    """
    """ check param enrichment """
    with_files = get_all_recipe_validator.is_string_boolean(with_files=request.args.get('with_files'))[1]
    """ get all recipe """
    data = recipe.select_all()
    """ add enrichment if needed """
    if with_files:
        data.add_enrichment_file_for_all()
    """ return response """
    return factory.ServerResponse().return_response(data=data.get_result(), api="recipe", code=200)


@recipe_api.route('/recipe/<_id>', methods=['GET'])
def get_recipe(_id):
    """
    @api {get} /recipe/<_id>  GetRecipe
    @apiGroup Recipe
    @apiDescription Get a recipe by it's ObjectId

    @apiParam (Query param) {String} _id Recipe's ObjectId
    @apiParam (Query param) {String} [with_files] if "true", add recipe's files

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/recipe/<_id>

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.recipe.success.ok',
        'codeStatus': 200,
        'data': {'_id': '5e71eb8f39358991f2ea19f6', 'categories': [], 'cooking_time': 0, 'level': 0, 'nb_people': 0,
                 'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'steps': [], 'title': 'aqa_rhr'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    """ check param enrichment """
    with_files = get_recipe_validator.is_string_boolean(with_files=request.args.get('with_files'))[1]
    """ check param _id """
    get_recipe_validator.is_object_id_valid(_id=_id)
    """ get recipe """
    data = recipe.select_one(_id=_id)
    """ add enrichment if needed """
    if with_files:
        data.add_enrichment_file_for_one()
    """ return response """
    return factory.ServerResponse().return_response(data=data.get_result(), api="recipe", code=200)


@recipe_api.route('/recipe', methods=['POST'])
def post_recipe():
    """
    @api {post} /recipe  PostRecipe
    @apiGroup Recipe
    @apiDescription Create a recipe

    @apiParam (Body param) {String} title Recipe's title
    @apiParam (Body param) {String} slug Recipe's slug for url
    @apiParam (Body param) {Integer} [level] Recipe's level (between 0 and 3)
    @apiParam (Body param) {String} [resume] Recipe's resume
    @apiParam (Body param) {Integer} [cooking_time] Recipe's cooking time
    @apiParam (Body param) {Integer} [preparation_time] Recipe's preparation time
    @apiParam (Body param) {String} [nb_people] Recipe's number of people
    @apiParam (Body param) {String} [note] Recipe's note
    @apiParam (Body param) {Array} [steps] Recipe's steps
    @apiParam (Body param) {Array} [categories] Recipe's categories

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
        'data': {'_id': '5e71eb8f39358991f2ea19f6', 'categories': [], 'cooking_time': 0, 'level': 0, 'nb_people': 0,
                 'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'steps': [], 'title': 'aqa_rhr'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be a string', 'param': 'title', 'value': {}}
    }
    """
    """ check body """
    body = post_recipe_factory.clean_body(data=request.json)
    post_recipe_validator.is_body_valid(data=body)
    """ insert recipe """
    data = recipe.insert(data=body)
    """ return result """
    return factory.ServerResponse().return_response(data=data.get_result(), api="recipe", code=201)


@recipe_api.route('/recipe/<_id>', methods=['PUT'])
def put_recipe(_id):
    """
    @api {put} /recipe/<_id>  PutRecipe
    @apiGroup Recipe
    @apiDescription Update a recipe

    @apiParam (Query param) {String} _id Recipe's ObjectId
    @apiParam (Query param) {String} [with_files] if "true", add recipe's files
    @apiParam (Body param) {String} [title] Recipe's title
    @apiParam (Body param) {String} [slug] Recipe's slug for url
    @apiParam (Body param) {String} [level] Recipe's level
    @apiParam (Body param) {String} [resume] Recipe's resume
    @apiParam (Body param) {String} [cooking_time] Recipe's cooking time
    @apiParam (Body param) {String} [preparation_time] Recipe's preparation time
    @apiParam (Body param) {String} [nb_people] Recipe's number of people
    @apiParam (Body param) {String} [note] Recipe's note
    @apiParam (Body param) {Array} [steps] Recipe's steps
    @apiParam (Body param) {Array} [categories] Recipe's categories

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
        'data': {'_id': '5e71eb8f39358991f2ea19f6', 'categories': [], 'cooking_time': 0, 'level': 0, 'nb_people': 0,
                 'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'steps': [], 'title': 'aqa_rhr'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be a string', 'param': 'title', 'value': {}}
    }
    """
    """ check param enrichment """
    with_files = put_recipe_validator.is_string_boolean(with_files=request.args.get('with_files'))[1]
    """ check param _id """
    put_recipe_validator.is_object_id_valid(_id=_id)
    """ check body """
    body = put_recipe_factory.clean_body(data=request.json)
    put_recipe_validator.is_body_valid(data=body)
    """ update recipe """
    data = recipe.update(_id=_id, data=body)
    """ add enrichment if needed """
    if with_files:
        data.add_enrichment_file_for_one()
    """ return response """
    return factory.ServerResponse().return_response(data=data.get_result(), api="recipe", code=200)


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
    """ check param _id """
    delete_recipe_validator.is_object_id_valid(_id=_id)
    """ clean files recipe """
    file.clean_file_by_id_parent(_id_parent=_id)
    """ clean files steps """
    for _id_step in recipe.get_all_step_id(_id=_id):
        file.clean_file_by_id_parent(_id_parent=_id_step)
    """ delete recipe """
    recipe.delete(_id=_id)
    """ return response """
    return factory.ServerResponse().return_response(data=None, api="recipe", code=204)


@recipe_api.errorhandler(400)
def validator_failed(error):
    """" abort 400 """
    return factory.ServerResponse().return_response(data=error.description, api="recipe", code=400)


@recipe_api.errorhandler(404)
def not_found(error):
    """" abort 404 """
    return factory.ServerResponse().return_response(data=error.description, api="recipe", code=404)
