from flask import Blueprint, request

import utils
import app.ingredient.factory as factory
import app.ingredient.validator as validator
import app.ingredient.model as ingredient_model
import app.file.model as file_model

apis = Blueprint('ingredient', __name__, url_prefix='/ingredient')

server = utils.Server()
ingredient = ingredient_model.Ingredient()
ingredient_recipe = ingredient_model.IngredientRecipe()
file = file_model.File()


@apis.route('/<_id>', methods=['DELETE'])
def delete_ingredient(_id):
    """
    @api {delete} /ingredient/<_id_ingredient>  DeleteIngredient
    @apiGroup Ingredient
    @apiDescription Delete an ingredient by it's ObjectId

    @apiParam (Query param) {String} _id Ingredient's ObjectId

    @apiExample {json} Example usage:
    DELETE http://127.0.0.1:5000/ingredient/<_id_ingredient>

    @apiSuccessExample {json} Success response:
    HTTPS 204

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    validation = validator.DeleteIngredient.Validator()
    """ check param """
    validation.is_object_id_valid(value=_id)
    """ clean files and link """
    file.clean_file_by_id_parent(_id_parent=_id)
    ingredient_recipe.clean_link_by_id_ingredient(_id_ingredient=_id)
    """ delete ingredient """
    ingredient.delete(_id=_id)
    """ return response """
    return server.return_response(data=None, api=apis.name, http_code=204)


@apis.route('/recipe/<_id>', methods=['DELETE'])
def delete_ingredient_recipe(_id):
    """
    @api {delete} /ingredient/recipe/<_id_ingredient_recipe>  DeleteIngredientRecipe
    @apiGroup Ingredient
    @apiDescription Delete an association ingredient-recipe

    @apiParam (Query param) {String} _id Link's ObjectId

    @apiExample {json} Example usage:
    DELETE http://127.0.0.1:5000/ingredient/recipe/<_id_ingredient_recipe>

    @apiSuccessExample {json} Success response:
    HTTPS 204

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    validation = validator.DeleteIngredientRecipe.Validator()
    """ check param """
    validation.is_object_id_valid(value=_id)
    """ delete link """
    ingredient_recipe.delete(_id=_id)
    """ return response """
    return server.return_response(data=None, api=apis.name, http_code=204)


@apis.route('', methods=['GET'])
def get_all_ingredient():
    """
    @api {get} /ingredient  GetAllIngredient
    @apiGroup Ingredient
    @apiDescription Get file ingredients

    @apiParam (Query param) {String} [with_files] if "true", add ingredient's files

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/ingredient

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.ingredient.success.ok',
        'codeStatus': 200,
        'data': [{'_id': '5e583de9b0fcef0a922a7bc0', 'name': 'aqa_rhr', 'categories': [],
                  'nutriments': {'calories': '0', 'carbohydrates': '0', 'fats': '0', 'proteins': '0',
                                 'info': 'per 100g'}},
                 {'_id': '5e583de9b0fcef0a922a7bc2', 'name': 'bqa_rhr', 'categories': [],
                  'nutriments': {'calories': '0', 'carbohydrates': '0', 'fats': '0', 'proteins': '0',
                                 'info': 'per 100g'}}]
    }
    """
    api = factory.GetAllIngredient.Factory()
    validation = validator.GetAllIngredient.Validator()
    with_files = request.args.get(api.param_with_files)
    """ check param """
    validation.is_with_files_valid(value=with_files)
    """ get all ingredient """
    data = ingredient.select_all()
    """ add enrichment if needed """
    if with_files == "true":
        data.add_enrichment_file_for_all()
    """ return response """
    return server.return_response(data=data.result, api=apis.name, http_code=200)


@apis.route('/<_id>', methods=['GET'])
def get_ingredient(_id):
    """
    @api {get} /ingredient/<_id_ingredient>  GetIngredient
    @apiGroup Ingredient
    @apiDescription Get an ingredient by it's ObjectId

    @apiParam (Query param) {String} _id Ingredient's ObjectId
    @apiParam (Query param) {String} [with_files] if "true", add ingredient's files

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/ingredient/<_id_ingredient>

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.ingredient.success.ok',
        'codeStatus': 200,
        'data': {'_id': '5e583de9b0fcef0a922a7bc0', 'name': 'aqa_rhr', 'categories': [],
                 'nutriments': {'calories': '0', 'carbohydrates': '0', 'fats': '0', 'proteins': '0',
                                'info': 'per 100g'}}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    api = factory.GetIngredient.Factory()
    validation = validator.GetIngredient.Validator()
    with_files = request.args.get(api.param_with_files)
    """ check param """
    validation.is_with_files_valid(value=with_files)
    validation.is_object_id_valid(value=_id)
    """ get ingredient """
    data = ingredient.select_one(_id=_id)
    """ add enrichment if needed """
    if with_files == "true":
        data.add_enrichment_file_for_one()
    """ return response """
    return server.return_response(data=data.result, api=apis.name, http_code=200)


@apis.route('/<_id>/recipe', methods=['GET'])
def get_recipe_for_ingredient(_id):
    """
    @api {get} /ingredient/<_id_ingredient>/recipe  GetRecipeForIngredient
    @apiGroup Ingredient
    @apiDescription Get all recipes for an ingredient by it's ObjectId

    @apiParam (Query param) {String} _id Ingredient's ObjectId
    @apiParam (Query param) {String} [with_titles] if "true", add recipe's title

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/ingredient/<_id_ingredient>/recipe

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.ingredient.success.ok',
        'codeStatus': 200,
        'data': [{'_id': '5e7347c82222535ac818942b', '_id_ingredient': '5e7347c82222535ac8189425',
                  '_id_recipe': '5e7347c82222535ac8189423', 'quantity': 0, 'unit': 'qa_rhr_unit_qa_rhr'},
                {'_id': '5e7347c82222535ac818942f', '_id_ingredient': '5e7347c82222535ac8189427',
                 '_id_recipe': '5e7347c82222535ac8189423', 'quantity': 0, 'unit': 'qa_rhr_unit_qa_rhr'}]
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    api = factory.GetRecipeForIngredient.Factory()
    validation = validator.GetRecipeForIngredient.Validator()
    with_titles = request.args.get(api.param_with_titles)
    """ check param """
    validation.is_with_titles_valid(value=with_titles)
    validation.is_object_id_valid(value=_id)
    """ get all """
    data = ingredient_recipe.select_all_by_id_ingredient(_id_ingredient=_id)
    """ add enrichment if needed """
    if with_titles == "true":
        data.add_enrichment_title_for_all()
    """ return response """
    return server.return_response(data=data.result, api=apis.name, http_code=200)


@apis.route('', methods=['POST'])
def post_ingredient():
    """
    @api {post} /ingredient  PostIngredient
    @apiGroup Ingredient
    @apiDescription Create an ingredient

    @apiParam (Body param) {String} name Ingredient's name
    @apiParam (Body param) {String} slug Ingredient's slug
    @apiParam (Body param) {String[]} [categories=[]] Ingredient's categories
    @apiParam (Body param) {Object} [nutriments] Ingredient's nutriments
    @apiParam (Body param) {Number} nutriments[calories=0] Ingredient's nutriments
    @apiParam (Body param) {Number} nutriments[carbohydrates=0] Ingredient's nutriments
    @apiParam (Body param) {Number} nutriments[fats=0] Ingredient's nutriments
    @apiParam (Body param) {Number} nutriments[proteins=0] Ingredient's nutriments
    @apiParam (Body param) {String} [nutriments[info="per 100g"]] Ingredient's nutriments


    @apiExample {json} Example usage:
    POST http://127.0.0.1:5000/ingredient
    {
        'name': <name>
        'slug': <slug>
        'categories': [<category1>, <category2>],
        'nutriments': {'calories': 10, 'carbohydrates': 20, 'fats': 30, 'proteins': 40, 'info': 'peer 100g'}
    }

    @apiSuccessExample {json} Success response:
    HTTPS 201
    {
        'codeMsg': 'cookbook.ingredient.success.created',
        'codeStatus': 201,
        'data': {'_id': '5e5840e63ed55d9119064649', 'name': 'qa_rhr_name', 'slug': 'qa_rhr_slug',
                 'categories': ['qa_rhr_category'],
                 'nutriments': {'calories': '10', 'carbohydrates': '20', 'fats': '30', 'proteins': '40',
                                'info': 'per 100g'}}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Is required', 'param': 'name'}}
    }
    """
    api = factory.PostIngredient.Factory()
    validation = validator.PostIngredient.Validator()
    """ check body """
    req_body = api.clean_body(data=request.json)
    validation.is_body_valid(data=req_body)
    body = api.fill_body(req_body)
    """ add ingredient in bdd """
    data = ingredient.insert(data=body)
    """ return response """
    return server.return_response(data=data.result, api=apis.name, http_code=201)


@apis.route('/recipe', methods=['POST'])
def post_ingredient_recipe():
    """
    @api {post} /ingredient/recipe  PostIngredientRecipe
    @apiGroup Ingredient
    @apiDescription Associate an ingredient to a recipe

    @apiParam (Body param) {String} _id_ingredient Ingredient's ObjectId to link
    @apiParam (Body param) {String} _id_recipe Recipe's ObjectId to link
    @apiParam (Body param) {Integer} quantity Ingredient's quantity for the recipe
    @apiParam (Body param) {String} unit Ingredient's unit for the recipe

    @apiExample {json} Example usage:
    POST http://127.0.0.1:5000/ingredient/recipe
    {
        '_id_ingredient': <_id_ingredient>,
        '_id_recipe': <_id_recipe>,
        'quantity': <quantity>,
        'unit': <unit>,
    }

    @apiSuccessExample {json} Success response:
    HTTPS 201
    {
        'codeMsg': 'cookbook.ingredient.success.created',
        'codeStatus': 201,
        'data': {'_id': '5e722e87f94648b72c7d8f03', '_id_ingredient': '5e722e875754d5e780a8f1e5',
                 '_id_recipe': '5e722e875754d5e780a8f1e3', 'quantity': 5, 'unit': 'qa_rhr_unit'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id_ingredient', 'value': 'invalid'}
    }
    """
    api = factory.PostIngredientRecipe.Factory()
    validation = validator.PostIngredientRecipe.Validator()
    """ check body """
    body = api.format_body(data=request.json)
    validation.is_body_valid(data=body)
    """ add link """
    data = ingredient_recipe.insert(data=body)
    """ return response """
    return server.return_response(data=data.result, api=apis.name, http_code=201)


@apis.route('/<_id>', methods=['PUT'])
def put_ingredient(_id):
    """
    @api {put} /ingredient/<_id_ingredient>  UpdateIngredient
    @apiGroup Ingredient
    @apiDescription Update an ingredient by it's ObjectId

    @apiParam (Query param) {String} _id Ingredient's ObjectId
    @apiParam (Query param) {String} [with_files] if "true", add ingredient's files
    @apiParam (Body Param) {String} [name] Ingredient's name
    @apiParam (Body Param) {String} [slug] Ingredient's slug
    @apiParam (Body param) {String[]} [categories=[]] Ingredient's categories
    @apiParam (Body param) {Object} [nutriments] Ingredient's nutriments
    @apiParam (Body param) {Number} nutriments[calories=0] Ingredient's nutriments
    @apiParam (Body param) {Number} nutriments[carbohydrates=0] Ingredient's nutriments
    @apiParam (Body param) {Number} nutriments[fats=0] Ingredient's nutriments
    @apiParam (Body param) {Number} nutriments[proteins=0] Ingredient's nutriments
    @apiParam (Body param) {String} [nutriments[info="per 100g"]] Ingredient's nutriments

    @apiExample {json} Example usage:
    PUT http://127.0.0.1:5000/ingredient/<_id_ingredient>
    {
        'name': <name>
    }

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.ingredient.success.ok',
        'codeStatus': 20O,
        'data': {'_id': '5e5840e63ed55d9119064649', 'name': 'qa_rhr_name_update'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Is required', 'param': 'name'}}
    }
    """
    api = factory.PutIngredient.Factory()
    validation = validator.PutIngredient.Validator()
    with_files = request.args.get(api.param_with_files)
    """ check params """
    validation.is_object_id_valid(value=_id)
    validation.is_with_files_valid(value=with_files)
    """ check body """
    body = api.clean_body(data=request.json)
    validation.is_body_valid(data=body)
    """ update ingredient """
    data = ingredient.update(_id=_id, data=body)
    """ add enrichment if needed """
    if with_files == "true":
        data.add_enrichment_file_for_one()
    """ return response """
    return server.return_response(data=data.result, api=apis.name, http_code=200)


@apis.route('/recipe/<_id>', methods=['PUT'])
def put_ingredient_recipe(_id):
    """
    @api {put} /ingredient/recipe/<_id_ingredient_recipe>  PutIngredientRecipe
    @apiGroup Ingredient
    @apiDescription Update quantity and unit of an association ingredient-recipe

    @apiParam (Query param) {String} _id Link's ObjectId
    @apiParam (Body param) {Integer} [quantity] Ingredient's quantity for the recipe
    @apiParam (Body param) {String} [unit] Ingredient's unit for the recipe

    @apiExample {json} Example usage:
    PUT http://127.0.0.1:5000/ingredient/recipe/<_id_ingredient_recipe>
    {
        'quantity': <quantity>,
        'unit': <unit>,
    }

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.ingredient.success.created',
        'codeStatus': 201,
        'data': {'_id': '5e722e87f94648b72c7d8f03', '_id_ingredient': '5e722e875754d5e780a8f1e5',
                 '_id_recipe': '5e722e875754d5e780a8f1e3', 'quantity': 10, 'unit': 'qa_rhr_unit_update'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    api = factory.PutIngredientRecipe.Factory()
    validation = validator.PutIngredientRecipe.Validator()
    """ check param """
    validation.is_object_id_valid(value=_id)
    """ check body """
    body = api.format_body(data=request.json)
    validation.is_body_valid(data=body)
    """ update link """
    data = ingredient_recipe.update(_id=_id, data=body)
    """ return response """
    return server.return_response(data=data.result, api=apis.name, http_code=200)


@apis.route('/search', methods=['GET'])
def search_ingredient():
    """
    @api {get} /ingredient/search SearchIngredient
    @apiGroup Ingredient
    @apiDescription Search an ingredient by key/value

    @apiParam (Query param) {String} [name] ingredient's name
    @apiParam (Query param) {String} [slug] ingredient's slug
    @apiParam (Query param) {String} [categories] ingredient's categories
    @apiParam (Query param) {String} [with_files] if "true", add ingredient's files

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/ingredient/search?name=<ingredient_name>

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.ingredient.success.ok',
        'codeStatus': 200,
        'data': [{'_id': '5e583de9b0fcef0a922a7bc0', 'name': 'aqa_rhr'}]
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be a string', 'param': 'name', 'value': ''}
    }
    """
    api = factory.SearchIngredient.Factory()
    validation = validator.SearchIngredient.Validator()
    with_files = request.args.get(api.param_with_files)
    """ check param """
    validation.is_with_files_valid(value=request.args.get(api.param_with_files))
    """ check search """
    search = api.format_body(data=request.args)
    validation.is_search_valid(data=search)
    """ get all recipe """
    data = ingredient.search(data=search)
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
