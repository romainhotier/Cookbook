from flask import Blueprint, make_response, request

import utils
import app.file as file_model
import app.file.factory as factory
import app.file.validator as validator
import app.ingredient as ingredient_model
import app.recipe as recipe_model

api = Blueprint('file', __name__, url_prefix='/file')

file = file_model.FileModel
ingredient = ingredient_model.IngredientModel
recipe = recipe_model.RecipeModel


@api.route('/<_id>', methods=['DELETE'])
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
    """ check param _id """
    validator.ValidatorDeleteFile.is_object_id_valid(_id=_id)
    """ delete file """
    file.delete(_id=_id)
    """ return response """
    return utils.Server.return_response(data=None, api=api.name, code=204)


@api.route('/<_id>', methods=['GET'])
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
    """ check param _id """
    validator.ValidatorGetFile.is_object_id_valid(_id=_id)
    """ get file """
    data = file.select_one(_id=_id)
    """ return response """
    response = make_response(data.read(), 200)
    response.mimetype = data.content_type
    return response


@api.route('/ingredient/<_id>', methods=['POST'])
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
        'data': {'_id': '5e622b52c49ed1e0df987e55',
                'name': 'qa_rhr',
                'files': [{'_id': '5e622b537aa097121df95d93', 'is_main': False}]},
        'detail': 'added file ObjectId: 5e622b537aa097121df95d93'
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.file.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    """ check param _id """
    validator.ValidatorPostFile.is_object_id_valid(kind="ingredient", _id=_id)
    """ check body """
    body = factory.FactoryPostFile.clean_body(data=request.json)
    validator.ValidatorPostFile.is_body_valid(data=body)
    """ insert file """
    inserted_id = file.insert(kind="ingredient", _id_parent=_id, metadata=body)
    """ return response """
    data = ingredient.select_one(_id=_id).add_enrichment_file_for_one()
    detail = factory.FactoryPostFile.detail_information(_id_file=inserted_id)
    return utils.Server.return_response(data=data.json, api=api.name, code=201, detail=detail)


@api.route('/recipe/<_id>', methods=['POST'])
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
        'data': {'_id': '5e67a99745378d7c10124235', 'cooking_time': 0,
                 'files': [{'_id': '5e67a997ed11fd9361b2e374', 'is_main': False}], 'level': 0, 'nb_people': 0,
                 'note': '', 'preparation_time': 0, 'resume': '', 'steps': [], 'title': 'qa_rhr', 'slug': 'x',
                 'categories': []},
        'detail': 'added file ObjectId: 5e67a997ed11fd9361b2e374'
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.file.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    """ check param _id """
    validator.ValidatorPostFile.is_object_id_valid(kind="recipe", _id=_id)
    """ check body """
    body = factory.FactoryPostFile.clean_body(data=request.json)
    validator.ValidatorPostFile.is_body_valid(data=body)
    """ insert file """
    inserted_id = file.insert(kind="recipe", _id_parent=_id, metadata=body)
    """ return response """
    data = recipe.select_one(_id=_id).add_enrichment_file_for_one()
    detail = factory.FactoryPostFile.detail_information(_id_file=inserted_id)
    return utils.Server.return_response(data=data.json, api=api.name, code=201, detail=detail)


@api.route('/recipe/<_id_recipe>/step/<_id_step>', methods=['POST'])
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
        'data': {'_id': '5e6a4223e664b60da7cd8626', 'cooking_time': 0, 'files': [], 'level': 0, 'nb_people': 0,
                 'note': '', 'preparation_time': 0, 'resume': '',
                 'steps': [{'_id': '111111111111111111111111', 'files': [{'_id': '5e6a42237e59e8439a883d99',
                 'is_main': False}], 'step': 'a'}, {'_id': '222222222222222222222222', 'files': [], 'step': 'b'}],
                 'title': 'qa_rhr', 'slug': 'x', 'categories': []},
        'detail': 'added file ObjectId: 5e6a42237e59e8439a883d99'
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.file.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    """ check param _id """
    validator.ValidatorPostFile.is_object_id_valid_special_step(kind="recipe", _id_recipe=_id_recipe)
    validator.ValidatorPostFile.is_object_id_valid_special_step(kind="step", _id_recipe=_id_recipe, _id_step=_id_step)
    """ check body """
    body = factory.FactoryPostFile.clean_body(data=request.json)
    validator.ValidatorPostFile.is_body_valid(data=body)
    """ insert file """
    inserted_id = file.insert(kind="step", _id_parent=_id_step, metadata=body)
    """ return response """
    data = recipe.select_one(_id=_id_recipe).add_enrichment_file_for_one()
    detail = factory.FactoryPostFile.detail_information(_id_file=inserted_id)
    return utils.Server.return_response(data=data.json, api=api.name, code=201, detail=detail)


@api.route('/is_main/<_id>', methods=['PUT'])
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
    """ check param _id """
    validator.ValidatorPutFile.is_object_id_valid(_id=_id)
    """ update file """
    _id_parent = file.set_is_main_true(_id=_id)
    """ return response """
    data = factory.FactoryPutFile.data_information(_id_file=_id, _id_parent=_id_parent)
    return utils.Server.return_response(data=data, api=api.name, code=200)


@api.errorhandler(400)
def validator_failed(error):
    """" abort 400 """
    return utils.Server.return_response(data=error.description, api=api.name, code=400)


@api.errorhandler(404)
def not_found(error):
    """" abort 404 """
    return utils.Server.return_response(data=error.description, api=api.name, code=404)
