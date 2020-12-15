from flask import Blueprint, request

import utils
import app.ingredient.factory as factory
import app.ingredient.validator as validator
import app.ingredient.model as ingredient_model
import app.recipe.model as recipe_model
import app.file.model as file_model

apis = Blueprint('ingredient', __name__, url_prefix='/ingredient')

server = utils.Server()
ingredient = ingredient_model.Ingredient()
recipe = recipe_model.Recipe()
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
    HTTPS 200
    {
        'codeMsg': 'cookbook.ingredient.success.ok',
        'codeStatus': 200,
        'data': 'Deleted Ingredient: 5fd770e1a9888551191a8743'
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    validation = validator.DeleteIngredient.Validator()
    api = factory.DeleteIngredient.Factory()
    """ check param """
    validation.is_object_id_valid(value=_id)
    """ clean files and link """
    file.clean_file_by_id_parent(_id_parent=_id)
    recipe.clean_ingredients_by_id(_id_ingredient=_id)
    """ delete ingredient """
    ingredient.delete(_id=_id)
    """ return response """
    data = api.data_information(_id=_id)
    return server.return_response(data=data, api=apis.name, http_code=200)


@apis.route('', methods=['GET'])
def get_all_ingredient():
    """
    @api {get} /ingredient  GetAllIngredient
    @apiGroup Ingredient
    @apiDescription Get file ingredients

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/ingredient

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.ingredient.success.ok',
        'codeStatus': 200,
        'data': [{'_id': '5e583de9b0fcef0a922a7bc0', 'categories': [], 'name': 'aqa_rhr',
                  'nutriments': {'calories': '0', 'carbohydrates': '0', 'fats': '0', 'proteins': '0',
                                 'info': 'per 100g'},
                  'slug': 'slug_ex1'},
                 {'_id': '5e583de9b0fcef0a922a7bc2', 'categories': [], 'name': 'bqa_rhr',
                  'nutriments': {'calories': '0', 'carbohydrates': '0', 'fats': '0', 'proteins': '0',
                                 'info': 'per 100g'},
                  'slug': 'slug_ex2'}]
    }
    """
    """ get all ingredient """
    data = ingredient.select_all()
    """ return response """
    return server.return_response(data=data.result, api=apis.name, http_code=200)


@apis.route('/<_id>', methods=['GET'])
def get_ingredient(_id):
    """
    @api {get} /ingredient/<_id_ingredient>  GetIngredient
    @apiGroup Ingredient
    @apiDescription Get an ingredient by it's ObjectId

    @apiParam (Query param) {String} _id Ingredient's ObjectId

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/ingredient/<_id_ingredient>

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.ingredient.success.ok',
        'codeStatus': 200,
        'data': {'_id': '5e583de9b0fcef0a922a7bc0', 'categories': [], 'name': 'aqa_rhr',
                 'nutriments': {'calories': '0', 'carbohydrates': '0', 'fats': '0', 'proteins': '0',
                                 'info': 'per 100g'},
                 'slug': 'slug_ex'}}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    validation = validator.GetIngredient.Validator()
    """ check param """
    validation.is_object_id_valid(value=_id)
    """ get ingredient """
    data = ingredient.select_one(_id=_id)
    """ return response """
    return server.return_response(data=data.result, api=apis.name, http_code=200)


@apis.route('', methods=['POST'])
def post_ingredient():
    """
    @api {post} /ingredient  PostIngredient
    @apiGroup Ingredient
    @apiDescription Create an ingredient

    @apiParam (Body param) {Array} [categories=Empty_Array] Ingredient's categories
    @apiParam (Body param) {String} name Ingredient's name
    @apiParam (Body param) {Object} [nutriments] Ingredient's nutriments
    @apiParam (Body param) {Number} nutriments[calories]=0 Ingredient's calories
    @apiParam (Body param) {Number} nutriments[carbohydrates]=0 Ingredient's carbohydrates
    @apiParam (Body param) {Number} nutriments[fats]=0 Ingredient's fats
    @apiParam (Body param) {String} [nutriments[info]="per 100g"] Ingredient's info
    @apiParam (Body param) {Number} nutriments[proteins=0] Ingredient's proteins
    @apiParam (Body param) {String} slug Ingredient's slug

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
    body = api.clean_body(data=request.json)
    validation.is_body_valid(data=body)
    body_filled = api.fill_body(data=body)
    """ add ingredient in bdd """
    data = ingredient.insert(data=body_filled)
    """ return response """
    return server.return_response(data=data.result, api=apis.name, http_code=201)


@apis.route('/<_id>', methods=['PUT'])
def put_ingredient(_id):
    """
    @api {put} /ingredient/<_id_ingredient>  PutIngredient
    @apiGroup Ingredient
    @apiDescription Update an ingredient by it's ObjectId

    @apiParam (Query param) {String} _id Ingredient's ObjectId
    @apiParam (Body param) {Array} [categories] Ingredient's categories
    @apiParam (Body param) {String} [name] Ingredient's name
    @apiParam (Body param) {Object} [nutriments] Ingredient's nutriments
    @apiParam (Body param) {Number} [nutriments[calories]] Ingredient's calories
    @apiParam (Body param) {Number} [nutriments[carbohydrates]] Ingredient's carbohydrates
    @apiParam (Body param) {Number} [nutriments[fats]] Ingredient's fats
    @apiParam (Body param) {String} [nutriments[info]] Ingredient's info
    @apiParam (Body param) {Number} [nutriments[proteins]] Ingredient's proteins
    @apiParam (Body param) {String} [slug] Ingredient's slug

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
        'data': {'_id': '5e583de9b0fcef0a922a7bc0', 'categories': [], 'name': 'aqa_rhr_update',
                 'nutriments': {'calories': '0', 'carbohydrates': '0', 'fats': '0', 'proteins': '0',
                                 'info': 'per 100g'},
                 'slug': 'slug_ex'}
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
    """ check params """
    validation.is_object_id_valid(value=_id)
    """ check body """
    body = api.clean_body(data=request.json)
    validation.is_body_valid(data=body)
    """ update ingredient """
    data = ingredient.update(_id=_id, data=body)
    """ return response """
    return server.return_response(data=data.result, api=apis.name, http_code=200)


@apis.route('/search', methods=['GET'])
def search_ingredient():
    """
    @api {get} /ingredient/search SearchIngredient
    @apiGroup Ingredient
    @apiDescription Search an ingredient by key/value

    @apiParam (Query param) {String} [categories] ingredient's categories
    @apiParam (Query param) {String} [name] ingredient's name
    @apiParam (Query param) {String} [slug] ingredient's slug


    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/ingredient/search?name=<ingredient_name>

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.ingredient.success.ok',
        'codeStatus': 200,
        'data': [{'_id': '5e583de9b0fcef0a922a7bc0', 'categories': [], 'name': 'aqa_rhr',
                 'nutriments': {'calories': '0', 'carbohydrates': '0', 'fats': '0', 'proteins': '0',
                                 'info': 'per 100g'},
                 'slug': 'slug_ex'}]
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
    """ check search """
    search = api.format_body(data=request.args)
    validation.is_search_valid(data=search)
    """ get all recipe """
    data = ingredient.search(data=search)
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
