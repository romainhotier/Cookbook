from flask import Blueprint, request

import utils
import app.recipe.factory as factory
import app.recipe.validator as validator
import app.recipe.model as recipe_model
import app.ingredient.model as ingredient_model
import app.file.model as file_model

apis = Blueprint('recipe', __name__, url_prefix='/recipe')

server = utils.Server()
recipe = recipe_model.Recipe()
step = recipe_model.Step()
ingredient_recipe = ingredient_model.IngredientRecipe()
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
    HTTPS 204

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    validation = validator.DeleteRecipe.Validator()
    """ check param """
    validation.is_object_id_valid(value=_id)
    """ clean files recipe """
    file.clean_file_by_id_parent(_id_parent=_id)
    """ clean files steps and link """
    for _id_step in recipe.get_all_step_id(_id_recipe=_id):
        file.clean_file_by_id_parent(_id_parent=_id_step)
    ingredient_recipe.clean_link_by_id_recipe(_id_recipe=_id)
    """ delete recipe """
    recipe.delete(_id=_id)
    """ return response """
    return server.return_response(data=None, api=apis.name, http_code=204)


@apis.route('/<_id_recipe>/step/<_id_step>', methods=['DELETE'])
def delete_recipe_step(_id_recipe, _id_step):
    """
    @api {delete} /recipe/<_id_recipe>/step/<_id_step>  DeleteRecipeStep
    @apiGroup Recipe
    @apiDescription Delete a recipe's step

    @apiParam (Query param) {String} _id_recipe Recipe's ObjectId
    @apiParam (Query param) {String} _id_step Step's ObjectId
    @apiParam (Query param) {String} [with_files] if "true", add recipe's files

    @apiExample {json} Example usage:
    DELETE http://127.0.0.1:5000/recipe/<_id_recipe>/step/<_id_step>

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.recipe.success.ok',
        'codeStatus': 200,
        'data': {'_id': '5e68acb9e067528c70c75f3c', 'cooking_time': 0, 'level': 0, 'nb_people': 0, 'note': '',
                 'preparation_time': 0, 'resume': '', title': 'qa_rhr', 'slug': '', 'categories': [],
                 'steps': [{'_id': '5e68acb97b0ead079be3cef7', 'description': 'another_previous_step'}]}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an integer', 'param': 'position', 'value': 'invalid'}
    }
    """
    api = factory.DeleteRecipeStep.Factory()
    validation = validator.DeleteRecipeStep.Validator()
    with_files = request.args.get(api.param_with_files)
    """ check param """
    validation.is_with_files_valid(value=with_files)
    validation.is_object_id_valid_recipe(value=_id_recipe)
    validation.is_object_id_valid_steps(_id_recipe=_id_recipe, _id_step=_id_step)
    """ delete step """
    data = step.delete(_id_recipe=_id_recipe, _id_step=_id_step)
    """ clean files """
    file.clean_file_by_id_parent(_id_parent=_id_step)
    """ add enrichment if needed """
    if with_files == "true":
        data.add_enrichment_file_for_one()
    """ return response """
    return server.return_response(data=data.result, api=apis.name, http_code=200)


@apis.route('', methods=['GET'])
def get_all_recipe():
    """
    @api {get} /recipe  GetAllRecipe
    @apiGroup Recipe
    @apiDescription Get all recipes

    @apiParam (Query param) {String} [with_files] if "true", add recipe's files

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
    api = factory.GetAllRecipe.Factory()
    validation = validator.GetAllRecipe.Validator()
    with_files = request.args.get(api.param_with_files)
    """ check param """
    validation.is_with_files_valid(value=with_files)
    """ get all recipe """
    data = recipe.select_all()
    """ add enrichment if needed """
    if with_files == "true":
        data.add_enrichment_file_for_all()
    """ return response """
    return server.return_response(data=data.result, api=apis.name, http_code=200)


@apis.route('/<_id_recipe>/ingredient', methods=['GET'])
def get_ingredient_for_recipe(_id_recipe):
    """
    @api {get} /recipe/<_id_recipe>/ingredient  GetIngredientForRecipe
    @apiGroup Recipe
    @apiDescription Get all ingredients for a recipe by it's ObjectId

    @apiParam (Query param) {String} _id Recipe's ObjectId
    @apiParam (Query param) {String} [with_names] if "true", add ingredient's name

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/recipe/<_id_recipe>/ingredient

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.recipe.success.ok',
        'codeStatus': 200,
        'data': [{'_id': '5e7347c82222535ac818942b', '_id_ingredient': '5e7347c82222535ac8189425',
                  '_id_recipe': '5e7347c82222535ac8189423', 'quantity': 0, 'unit': 'qa_rhr_unit_qa_rhr'},
                {'_id': '5e7347c82222535ac818942f', '_id_ingredient': '5e7347c82222535ac8189427',
                 '_id_recipe': '5e7347c82222535ac8189423', 'quantity': 0, 'unit': 'qa_rhr_unit_qa_rhr'}]
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    api = factory.GetIngredientForRecipe.Factory()
    validation = validator.GetIngredientForRecipe.Validator()
    with_names = request.args.get(api.param_with_names)
    """ check param """
    validation.is_with_names_valid(value=with_names)
    validation.is_object_id_valid(value=_id_recipe)
    """ get all """
    data = ingredient_recipe.select_all_by_id_recipe(_id_recipe=_id_recipe)
    """ add enrichment if needed """
    if with_names == "true":
        data.add_enrichment_name_for_all()
    """ return response """
    return server.return_response(data=data.result, api=apis.name, http_code=200)


@apis.route('/<slug>', methods=['GET'])
def get_recipe(slug):
    """
    @api {get} /recipe/<slug>  GetRecipe
    @apiGroup Recipe
    @apiDescription Get a recipe by it's slug

    @apiParam (Query param) {String} slug Recipe's slug
    @apiParam (Query param) {String} [with_files] if "true", add recipe's files

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
    api = factory.GetRecipe.Factory()
    validation = validator.GetRecipe.Validator()
    with_files = request.args.get(api.param_with_files)
    """ check param """
    validation.is_with_files_valid(value=with_files)
    validation.is_slug_valid(value=slug)
    """ get recipe """
    data = recipe.select_one_by_slug(slug=slug)
    """ add enrichment if needed """
    if with_files == "true":
        data.add_enrichment_file_for_one()
    """ return response """
    return server.return_response(data=data.result, api=apis.name, http_code=200)


@apis.route('', methods=['POST'])
def post_recipe():
    """
    @api {post} /recipe  PostRecipe
    @apiGroup Recipe
    @apiDescription Create a recipe

    @apiParam (Body param) {String} title Recipe's title
    @apiParam (Body param) {String} slug Recipe's slug for url
    @apiParam (Body param) {Integer} [level]=0 Recipe's level (between 0 and 3)
    @apiParam (Body param) {String} [resume]="" Recipe's resume
    @apiParam (Body param) {Integer} [cooking_time]=0 Recipe's cooking time
    @apiParam (Body param) {Integer} [preparation_time]=0 Recipe's preparation time
    @apiParam (Body param) {String} [nb_people]=0 Recipe's number of people
    @apiParam (Body param) {String} [note]="" Recipe's note
    @apiParam (Body param) {Array} [categories]=Empty_Array Recipe's categories
    @apiParam (Body param) {String} [status]="in_progress" Recipe's categories ("in_progress" or "finished")

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


@apis.route('/step/<_id>', methods=['POST'])
def post_recipe_step(_id):
    """
    @api {post} /recipe/step/<_id_recipe> PostRecipeStep
    @apiGroup Recipe
    @apiDescription Create a recipe's step. Can specify where to add the step

    @apiParam (Query param) {String} _id Recipe's ObjectId
    @apiParam (Query param) {String} [with_files] if "true", add recipe's files
    @apiParam (Body param) {String} description Step's description to add
    @apiParam (Body param) {Integer} [position] Position in recipe's steps array.
                                                If not specified, add at the end of the array

    @apiExample {json} Example usage:
    POST http://127.0.0.1:5000/recipe/step/<_id_recipe>
    {
        'description': <description>,
        'position': <position>
    }

    @apiSuccessExample {json} Success response:
    HTTPS 201
    {
        'codeMsg': 'cookbook.recipe.success.created',
        'codeStatus': 201,
        'data': {'_id': '5e68acb9e067528c70c75f3c', 'cooking_time': 0, 'level': 0, 'nb_people': 0, 'note': '',
                 'preparation_time': 0, 'resume': '', title': 'qa_rhr', 'slug': '', 'categories': [],
                 'steps': [{'_id': '5e68acb97b0ead079be3cef7', 'description': 'new_step'}]}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an integer', 'param': 'position', 'value': 'invalid'}
    }
    """
    api = factory.PostRecipeStep.Factory()
    validation = validator.PostRecipeStep.Validator()
    with_files = request.args.get(api.param_with_files)
    """ check param """
    validation.is_with_files_valid(value=with_files)
    validation.is_object_id_valid(value=_id)
    """ check body """
    body = api.clean_body(data=request.json)
    validation.is_body_valid(_id_recipe=_id, data=body)
    """ insert step """
    data = step.insert(_id=_id, data=body)
    """ add enrichment if needed """
    if with_files == "true":
        data.add_enrichment_file_for_one()
    """ return response """
    return server.return_response(data=data.result, api=apis.name, http_code=201)


@apis.route('/<_id>', methods=['PUT'])
def put_recipe(_id):
    """
    @api {put} /recipe/<_id_recipe>  PutRecipe
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
    @apiParam (Body param) {Array} [categories] Recipe's categories
    @apiParam (Body param) {String} [status]="in_progress" Recipe's categories ("in_progress" or "finished")

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
    with_files = request.args.get(api.param_with_files)
    """ check param """
    validation.is_with_files_valid(value=with_files)
    validation.is_object_id_valid(value=_id)
    """ check body """
    body = api.clean_body(data=request.json)
    validation.is_body_valid(data=body)
    """ update recipe """
    data = recipe.update(_id=_id, data=body)
    """ add enrichment if needed """
    if with_files == "true":
        data.add_enrichment_file_for_one()
    """ return response """
    return server.return_response(data=data.result, api=apis.name, http_code=200)


@apis.route('/<_id_recipe>/step/<_id_step>', methods=['PUT'])
def put_recipe_step(_id_recipe, _id_step):
    """
    @api {put} /recipe/<_id_recipe>/step/<_id_step>  PutRecipeStep
    @apiGroup Recipe
    @apiDescription Update a recipe's step

    @apiParam (Query param) {String} _id_recipe Recipe's ObjectId
    @apiParam (Query param) {String} _id_step Step's ObjectId
    @apiParam (Query param) {String} [with_files] if "true", add recipe's files
    @apiParam (Body param) {String} description Step's description to add

    @apiExample {json} Example usage:
    PUT http://127.0.0.1:5000/recipe/<_id_recipe>/step/<_id_step>
    {
        'description': <description>
    }

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.recipe.success.ok',
        'codeStatus': 200,
        'data': {'_id': '5e68acb9e067528c70c75f3c', 'cooking_time': 0, 'level': 0, 'nb_people': 0, 'note': '',
                 'preparation_time': 0, 'resume': '', title': 'qa_rhr', 'slug': '', 'categories': [],
                 'steps': [{'_id': '5e68acb97b0ead079be3cef7', 'description': 'updated_step'}]}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an integer', 'param': 'position', 'value': 'invalid'}
    }
    """
    api = factory.PutRecipeStep.Factory()
    validation = validator.PutRecipeStep.Validator()
    with_files = request.args.get(api.param_with_files)
    """ check param """
    validation.is_with_files_valid(value=with_files)
    validation.is_object_id_valid_recipe(value=_id_recipe)
    validation.is_object_id_valid_steps(_id_recipe=_id_recipe, _id_step=_id_step)
    """ check body """
    body = api.clean_body(data=request.json)
    validation.is_body_valid(data=body)
    """ update step """
    data = step.update(_id_recipe=_id_recipe, _id_step=_id_step, data=body)
    """ add enrichment if needed """
    if with_files == "true":
        data.add_enrichment_file_for_one()
    """ return response """
    return server.return_response(data=data.result, api=apis.name, http_code=200)


@apis.route('/steps/<_id>', methods=['PUT'])
def put_recipe_steps(_id):
    """
    @api {put} /recipe/steps/<_id_recipe> PutRecipeSteps
    @apiGroup Recipe
    @apiDescription Create recipe's steps.

    @apiParam (Query param) {String} _id Recipe's ObjectId
    @apiParam (Query param) {String} [with_files] if "true", add recipe's files
    @apiParam (Body param) {String} description Step's description to add

    @apiExample {json} Example usage:
    PUT http://127.0.0.1:5000/recipe/steps/<_id_recipe>
    {
        'steps': [{'description': <description1>},
                  {'description': <description2>}]
    }

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.recipe.success.created',
        'codeStatus': 200,
        'data': {'_id': '5e68acb9e067528c70c75f3c', 'cooking_time': 0, 'level': 0, 'nb_people': 0, 'note': '',
                 'preparation_time': 0, 'resume': '', title': 'qa_rhr', 'slug': '', 'categories': [],
                 'steps': [{'_id': '5e68acb97b0ead079be3cef7', 'description': 'new_step'},
                           {'_id': '5e68acb97b0ead079be3cef8', 'description': 'new_step2'}]}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an integer', 'param': 'position', 'value': 'invalid'}
    }
    """
    api = factory.PutRecipeSteps.Factory()
    validation = validator.PutRecipeSteps.Validator()
    with_files = request.args.get(api.param_with_files)
    """ check param """
    validation.is_with_files_valid(value=with_files)
    validation.is_object_id_valid(value=_id)
    """ check body """
    body = api.clean_body(data=request.json)
    validation.is_body_valid(data=body)
    """ update steps """
    data = step.update_multi(_id=_id, data=body)
    """ add enrichment if needed """
    if with_files == "true":
        data.add_enrichment_file_for_one()
    """ return response """
    return server.return_response(data=data.result, api=apis.name, http_code=200)


@apis.route('/search', methods=['GET'])
def search_recipe():
    """
    @api {get} /recipe/search  SearchRecipe
    @apiGroup Recipe
    @apiDescription Search an recipe by unique or multiple key/value ($and in query)

    @apiParam (Query param) {String} [title] search by title
    @apiParam (Query param) {String} [slug] search by slug
    @apiParam (Query param) {String} [level] search by level
    @apiParam (Query param) {String} [cooking_time] search by cooking_time
    @apiParam (Query param) {String} [preparation_time] search by preparation_time
    @apiParam (Query param) {String} [nb_people] search by nb_people
    @apiParam (Query param) {String} [categories] search by categories
    @apiParam (Query param) {String} [with_files] if "true", add recipe's files
    @apiParam (Query param) {String} [status] search by status

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/recipe/search?title=<recipe_title>

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
    with_files = request.args.get(api.param_with_files)
    """ check param """
    validation.is_with_files_valid(value=with_files)
    """ check search """
    search = api.format_body(data=request.args)
    validation.is_search_valid(data=search)
    """ get all recipe """
    data = recipe.search(data=search)
    """ add enrichment if needed """
    if with_files == "true":
        data.add_enrichment_file_for_all()
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
