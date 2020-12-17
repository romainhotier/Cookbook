from flask import Blueprint, request

import utils
import app.recipe.factory as factory
import app.recipe.validator as validator
import app.recipe.model as recipe_model
import app.file.model as file_model

apis = Blueprint('recipe', __name__, url_prefix='/recipe')

server = utils.Server()
recipe = recipe_model.Recipe()
file = file_model.File()


@apis.route('/<_id>', methods=['DELETE'])
def delete_recipe(_id):
    """
    @api {delete} /recipe/<_id_recipe>  DeleteRecipe
    @apiGroup Recipe
    @apiDescription Delete an recipe by it's ObjectId

    @apiParam (Query param) {String} _id Recipe's ObjectId

    @apiExample {json} Example usage:
    DELETE http://127.0.0.1:5000/recipe/<_id_recipe>

    @apiSuccessExample {json} Success response:
        HTTPS 200
    {
        'codeMsg': 'cookbook.recipe.success.ok',
        'codeStatus': 200,
        'data': 'Deleted Recipe: 5fd770e1a9888551191a8743'
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    validation = validator.DeleteRecipe.Validator()
    api = factory.DeleteRecipe.Factory()
    """ check param """
    validation.is_object_id_valid(value=_id)
    """ clean files recipe """
    file.clean_file_by_id_parent(_id_parent=_id)
    """ clean files steps """
    for _id_step in recipe.get_all_step_id(_id_recipe=_id):
        file.clean_file_by_id_parent(_id_parent=_id_step)
    """ delete recipe """
    recipe.delete(_id=_id)
    """ return response """
    data = api.data_information(_id=_id)
    return server.return_response(data=data, api=apis.name, http_code=200)


@apis.route('', methods=['GET'])
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
        'data': [{'_id': '5e71eb8f39358991f2ea19f6', 'categories': [], 'cooking_time': 0, 'level': 0, 'nb_people': 0,
                  'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'steps': [], 'title': 'qa_rhr_1',
                  'status': 'in_progress'},
                 {'_id': '5e71eb8f39358991f2ea19f7', 'categories': [], 'cooking_time': 0, 'level': 0, 'nb_people': 0,
                  'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'steps': [], 'title': 'aqa_rhr_2',
                  'status': 'in_progress'}]
    }
    """
    """ get all recipe """
    data = recipe.select_all()
    """ return response """
    return server.return_response(data=data.result, api=apis.name, http_code=200)


@apis.route('/<slug>', methods=['GET'])
def get_recipe(slug):
    """
    @api {get} /recipe/<slug>  GetRecipe
    @apiGroup Recipe
    @apiDescription Get a recipe by it's slug

    @apiParam (Query param) {String} slug Recipe's slug

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/recipe/<slug>

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.recipe.success.ok',
        'codeStatus': 200,
        'data': {'_id': '5e71eb8f39358991f2ea19f6', 'categories': [], 'cooking_time': 0, 'level': 0, 'nb_people': 0,
                 'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'steps': [], 'title': 'aqa_rhr',
                 'status': 'in_progress'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be not empty', 'param': 'slug', 'value': ''}
    }
    """
    validation = validator.GetRecipe.Validator()
    """ check param """
    validation.is_slug_valid(value=slug)
    """ get recipe """
    data = recipe.select_one_by_slug(slug=slug)
    """ return response """
    return server.return_response(data=data.result, api=apis.name, http_code=200)


@apis.route('', methods=['POST'])
def post_recipe():
    """
    @api {post} /recipe  PostRecipe
    @apiGroup Recipe
    @apiDescription Create a recipe

    @apiParam (Body param) {Array} [categories]=Empty_Array Recipe's categories
    @apiParam (Body param) {Integer} [cooking_time]=0 Recipe's cooking time
    @apiParam (Body param) {Array} [ingredients]=Empty_Array Recipe's Ingredients
    @apiParam (Body param) {String} ingredients[_id] Ingredient's ObjectId
    @apiParam (Body param) {Integer} ingredients[quantity] Ingredient's quantity
    @apiParam (Body param) {String} [ingredients[unit]=""] Ingredient's unit
    @apiParam (Body param) {Integer} [level]=0 Recipe's level (between 0 and 3)
    @apiParam (Body param) {String} [nb_people]=0 Recipe's number of people
    @apiParam (Body param) {String} [note]="" Recipe's note
    @apiParam (Body param) {Integer} [preparation_time]=0 Recipe's preparation time
    @apiParam (Body param) {String} [resume]="" Recipe's resume
    @apiParam (Body param) {String} slug Recipe's slug for url
    @apiParam (Body param) {String} [status]="in_progress" Recipe's categories ("in_progress" or "finished")
    @apiParam (Body param) {Array} [steps]=Empty_Array Recipe's steps
    @apiParam (Body param) {String} steps[description] Step's description
    @apiParam (Body param) {String} title Recipe's title

    @apiExample {json} Example usage:
    POST http://127.0.0.1:5000/recipe
    {
        'title': <title>,
        'slug': <slug>,
    }

    @apiSuccessExample {json} Success response:
    HTTPS 201
    {
        'codeMsg': 'cookbook.recipe.success.created',
        'codeStatus': 201,
        'data': {'_id': '5e71eb8f39358991f2ea19f6', 'categories': [], 'cooking_time': 0, 'ingredients': [], 'level': 0,
                 'nb_people': 0, 'note': '', 'preparation_time': 0, 'resume': '', 'slug': 'slug_ex',
                 'status': 'in_progress', 'steps': [], 'title': 'title_ex'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be a string', 'param': 'title', 'value': {}}
    }
    """
    api = factory.PostRecipe.Factory()
    validation = validator.PostRecipe.Validator()
    """ check body """
    body = api.clean_body(data=request.json)
    validation.is_body_valid(data=body)
    body_filled = api.fill_body(data=body)
    """ insert recipe """
    data = recipe.insert(data=body_filled)
    """ return result """
    return server.return_response(data=data.result, api=apis.name, http_code=201)


@apis.route('/<_id>', methods=['PUT'])
def put_recipe(_id):
    """
    @api {put} /recipe/<_id_recipe>  PutRecipe
    @apiGroup Recipe
    @apiDescription Update a recipe

    @apiParam (Query param) {String} _id Recipe's ObjectId
    @apiParam (Body param) {Array} [categories]=Empty_Array Recipe's categories
    @apiParam (Body param) {Integer} [cooking_time]=0 Recipe's cooking time
    @apiParam (Body param) {Array} [ingredients]=Empty_Array Recipe's Ingredients
    @apiParam (Body param) {String} ingredients[_id] Ingredient's ObjectId
    @apiParam (Body param) {Integer} ingredients[quantity] Ingredient's quantity
    @apiParam (Body param) {String} [ingredients[unit]=""] Ingredient's unit
    @apiParam (Body param) {Integer} [level]=0 Recipe's level (between 0 and 3)
    @apiParam (Body param) {String} [nb_people]=0 Recipe's number of people
    @apiParam (Body param) {String} [note]="" Recipe's note
    @apiParam (Body param) {Integer} [preparation_time]=0 Recipe's preparation time
    @apiParam (Body param) {String} [resume]="" Recipe's resume
    @apiParam (Body param) {String} slug Recipe's slug for url
    @apiParam (Body param) {String} [status]="in_progress" Recipe's categories ("in_progress" or "finished")
    @apiParam (Body param) {Array} [steps]=Empty_Array Recipe's steps
    @apiParam (Body param) {String} steps[description] Step's description
    @apiParam (Body param) {String} title Recipe's title

    @apiExample {json} Example usage:
    PUT http://127.0.0.1:5000/recipe/<_id_recipe>
    {
        'title': <title>
    }

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.recipe.success.created',
        'codeStatus': 201,
        'data': {'_id': '5e71eb8f39358991f2ea19f6', 'categories': [], 'cooking_time': 0, 'level': 0, 'nb_people': 0,
                 'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'steps': [], 'title': 'aqa_rhr',
                 'status': 'in_progress'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be a string', 'param': 'title', 'value': {}}
    }
    """
    api = factory.PutRecipe.Factory()
    validation = validator.PutRecipe.Validator()
    """ check param """
    validation.is_object_id_valid(value=_id)
    """ check body """
    body = api.clean_body(data=request.json)
    validation.is_body_valid(data=body, _id=_id)
    body_formated = api.reformat_body(data=body)
    """ update recipe """
    data = recipe.update(_id=_id, data=body_formated)
    """ clean steps file """
    """TBD"""
    """ return response """
    return server.return_response(data=data.result, api=apis.name, http_code=200)


@apis.route('/search', methods=['GET'])
def search_recipe():
    """
    @api {get} /recipe/search  SearchRecipe
    @apiGroup Recipe
    @apiDescription Search an recipe by unique or multiple key/value ($and in query)
    @apiParam (Query param) {String} [categories] search by categories
    @apiParam (Query param) {String} [cooking_time] search by cooking_time
    @apiParam (Query param) {String} [level] search by level
    @apiParam (Query param) {String} [nb_people] search by nb_people
    @apiParam (Query param) {String} [preparation_time] search by preparation_time
    @apiParam (Query param) {String} [slug] search by slug
    @apiParam (Query param) {String} [status] search by status
    @apiParam (Query param) {String} [title] search by title

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/recipe/search?title=<recipe_title>

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.recipe.success.ok',
        'codeStatus': 200,
        'data': [{'_id': '5e71eb8f39358991f2ea19f6', 'categories': [], 'cooking_time': 0, 'ingredients': [], 'level': 0,
                 'nb_people': 0, 'note': '', 'preparation_time': 0, 'resume': '', 'slug': 'slug_ex',
                 'status': 'in_progress', 'steps': [], 'title': 'title_ex'},
                 {'_id': '5e71eb8f39358991f2ea19f7', 'categories': [], 'cooking_time': 0, 'ingredients': [], 'level': 0,
                 'nb_people': 0, 'note': '', 'preparation_time': 0, 'resume': '', 'slug': 'slug_ex',
                 'status': 'in_progress', 'steps': [], 'title': 'title_ex2'}]
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be not empty', 'param': 'title', 'value': ''}
    }
    """
    api = factory.SearchRecipe.Factory()
    validation = validator.SearchRecipe.Validator()
    """ check search """
    search = api.format_body(data=request.args)
    validation.is_search_valid(data=search)
    """ get all recipe """
    data = recipe.search(data=search)
    """ return response """
    return server.return_response(data=data.result, api=apis.name, http_code=200)


@apis.errorhandler(400)
def api_handler_validator_failed(err):
    """ Return a response for bad request.

    Parameters
    ----------
    err
        Error from Flask.

    Returns
    -------
    Any
        Server response.
    """
    return server.return_response(data=err.description, api=apis.name, http_code=400)


@apis.errorhandler(404)
def api_handler_url_not_found(err):
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
    return server.return_response(data=err, api=apis.name, http_code=404)
