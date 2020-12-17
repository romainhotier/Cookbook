from flask import Blueprint, request

import utils

import app.file.model as file_model
import app.file.factory as factory
import app.file.validator as validator
import app.ingredient.model as ingredient_model
import app.recipe.model as recipe_model

apis = Blueprint('file', __name__, url_prefix='/file')

server = utils.Server()
file = file_model.File()
ingredient = ingredient_model.Ingredient()
recipe = recipe_model.Recipe()


@apis.route('/<_id>', methods=['DELETE'])
def delete_file(_id):
    """
    @api {delete} /file/<_id_file>  DeleteFile
    @apiGroup File
    @apiDescription Delete a file by it's ObjectId

    @apiParam (Query param) {String} _id File's ObjectId

    @apiExample {json} Example usage:
    DELETE http://127.0.0.1:5000/file/<_id_file>

    @apiSuccessExample {json} Success response:
    HTTPS 204

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.file.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    validation = validator.DeleteFile.Validator()
    """ check param """
    validation.is_object_id_valid(value=_id)
    """ delete file """
    file.delete(_id=_id)
    """ return response """
    return server.return_response(data=None, api=apis.name, http_code=204)


@apis.route('/<_id>', methods=['GET'])
def get_file(_id):
    """
    @api {get} /file/<_id_file>  DownloadFile
    @apiGroup File
    @apiDescription Get a file by it's ObjectId

    @apiParam (Query param) {String} _id File's ObjectId

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/file/<_id_file>

    @apiSuccessExample {json} Success response:
    HTTPS 200
    �PNG
    np������Q*D�l1<��j3

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.file.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    validation = validator.GetFile.Validator()
    """ check param """
    validation.is_object_id_valid(value=_id)
    """ get file """
    data = file.select_one(_id=_id)
    """ return response """
    return server.return_response(data=data, api=apis.name, http_code=200, file=True)


@apis.route('/ingredient/<_id>', methods=['POST'])
def post_ingredient_file(_id):
    """
    @api {post} /file/ingredient/<_id_ingredient>  PostIngredientFile
    @apiGroup File
    @apiDescription Add a file to an ingredient

    @apiParam (Query param) {String} _id Ingredient's ObjectId
    @apiParam (Body Param) {String} path File's path
    @apiParam (Body Param) {String} filename File's filename
    @apiParam (Body Param) {Boolean} [is_main] If True, file will be the main file. False by default

    @apiExample {json} Example usage:
    POST http://127.0.0.1:5000/file/ingredient/<_id_ingredient>
    {
        'path': <path>,
        'filename': <filename>,
        'is_main': <is_main>
    }

    @apiSuccessExample {json} Success response:
    HTTPS 201
    {
        'codeMsg': 'cookbook.file.success.created',
        'codeStatus': 201,
        'data': 'added file ObjectId: 5e622b537aa097121df95d93'
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.file.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    api = factory.PostFile.Factory()
    validation = validator.PostFile.Validator()
    """ check param """
    validation.is_object_id_valid(kind="ingredient", value=_id)
    """ check body """
    body = api.clean_body(data=request.json)
    validation.is_body_valid(data=body)
    body_filled = api.fill_body(data=body)
    """ insert file """
    inserted_id = file.insert(kind="ingredient", _id_parent=_id, metadata=body_filled)
    """ return response """
    data = api.detail_information(_id_file=inserted_id)
    return server.return_response(data=data, api=apis.name, http_code=201)


@apis.route('/recipe/<_id>', methods=['POST'])
def post_recipe_file(_id):
    """
    @api {post} /file/recipe/<_id_recipe>  PostRecipeFile
    @apiGroup File
    @apiDescription Add a file to a recipe

    @apiParam (Query param) {String} _id Recipe's ObjectId
    @apiParam (Body Param) {String} path File's path
    @apiParam (Body Param) {String} filename File's filename
    @apiParam (Body Param) {Boolean} [is_main] If True, file will be the main file. False by default

    @apiExample {json} Example usage:
    POST http://127.0.0.1:5000/file/recipe/<_id_recipe>
    {
        'path': <path>,
        'filename': <filename>,
        'is_main': <is_main>
    }

    @apiSuccessExample {json} Success response:
    HTTPS 201
    {
        'codeMsg': 'cookbook.file.success.created',
        'codeStatus': 201,
        'data': 'added file ObjectId: 5e67a997ed11fd9361b2e374'
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.file.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    api = factory.PostFile.Factory()
    validation = validator.PostFile.Validator()
    """ check param """
    validation.is_object_id_valid(kind="recipe", value=_id)
    """ check body """
    body = api.clean_body(data=request.json)
    validation.is_body_valid(data=body)
    body_filled = api.fill_body(data=body)
    """ insert file """
    inserted_id = file.insert(kind="recipe", _id_parent=_id, metadata=body_filled)
    """ return response """
    data = api.detail_information(_id_file=inserted_id)
    return server.return_response(data=data, api=apis.name, http_code=201)


@apis.route('/recipe/<_id_recipe>/step/<_id_step>', methods=['POST'])
def post_step_file(_id_recipe, _id_step):
    """
    @api {post} /file/recipe/<_id_recipe>/step/<_id_step> PostStepFile
    @apiGroup File
    @apiDescription Add a file to a step

    @apiParam (Query param) {String} _id_recipe Recipe's ObjectId
    @apiParam (Query param) {String} _id_step Steps's ObjectId
    @apiParam (Body Param) {String} path File's path
    @apiParam (Body Param) {String} filename File's filename
    @apiParam (Body Param) {Boolean} [is_main] If True, file will be the main file. False by default

    @apiExample {json} Example usage:
    POST http://127.0.0.1:5000/file/recipe/<_id_recipe>/step/<_id_step>
    {
        'path': <path>,
        'filename': <filename>,
        'is_main': <is_main>
    }

    @apiSuccessExample {json} Success response:
    HTTPS 201
    {
        'codeMsg': 'cookbook.file.success.created',
        'codeStatus': 201,
        'data': 'added file ObjectId: 5e6a42237e59e8439a883d99'
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.file.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    api = factory.PostFile.Factory()
    validation = validator.PostFile.Validator()
    """ check param """
    validation.is_object_id_valid_special_step(kind="recipe", _id_recipe=_id_recipe)
    validation.is_object_id_valid_special_step(kind="step", _id_recipe=_id_recipe, _id_step=_id_step)
    """ check body """
    body = api.clean_body(data=request.json)
    validation.is_body_valid(data=body)
    body_filled = api.fill_body(data=body)
    """ insert file """
    inserted_id = file.insert(kind="step", _id_parent=_id_step, metadata=body_filled)
    """ return response """
    data = api.detail_information(_id_file=inserted_id)
    return server.return_response(data=data, api=apis.name, http_code=201)


@apis.route('/is_main/<_id>', methods=['PUT'])
def put_file_is_main(_id):
    """
    @api {put} /file/<_id_file>  PutFileIsMain
    @apiGroup File
    @apiDescription Update a file and set is_main to True by it's ObjectId

    @apiParam (Query param) {String} _id File's ObjectId

    @apiExample {json} Example usage:
    PUT http://127.0.0.1:5000/file/is_main/<_id_file>

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.file.success.ok',
        'codeStatus': 200,
        'data': '5e71f5c94acb9085a19f10b4 is now set as main file for 111111111111111111111111'}

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.file.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    api = factory.PutFile.Factory()
    validation = validator.PutFile.Validator()
    """ check param """
    validation.is_object_id_valid(value=_id)
    """ update file """
    _id_parent = file.set_is_main_true(_id=_id)
    """ return response """
    data = api.data_information(_id_file=_id, _id_parent=_id_parent)
    return server.return_response(data=data, api=apis.name, http_code=200)


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
