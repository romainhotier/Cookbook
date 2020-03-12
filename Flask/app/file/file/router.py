from flask import Blueprint, make_response, request

import server.factory as factory
import app.ingredient.ingredient.model as ingredient_model
import app.recipe.recipe.model as recipe_model
import app.file.file.model as file_model
import app.file.file.validator.GetFile as validator_GetFile
import app.file.file.validator.DeleteFile as validator_DeleteFile
import app.file.file.factory.PostFile as factory_PostFile
import app.file.file.validator.PostFile as validator_PostFile


file_api = Blueprint('file_api', __name__)

file = file_model.File()
ingredient = ingredient_model.Ingredient()
recipe = recipe_model.Recipe()
get_file_validator = validator_GetFile.Validator()
delete_file_validator = validator_DeleteFile.Validator()
post_file_factory = factory_PostFile.Factory()
post_file_validator = validator_PostFile.Validator()


@file_api.route('/file/<_id>', methods=['GET'])
def get_file(_id):
    """
    @api {get} /file/<_id>  DownloadFile
    @apiGroup File
    @apiDescription Get a file by it's ObjectId

    @apiParam (Query param) {String} _id File's ObjectId

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/file/<_id>

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
    get_file_validator.is_object_id_valid(_id=_id)
    data = file.select_one(_id=_id)
    response = make_response(data.read(), 200)
    response.mimetype = data.content_type
    return response


@file_api.route('/file/<_id>', methods=['DELETE'])
def delete_file(_id):
    """
    @api {delete} /file/<_id>  DeleteFile
    @apiGroup File
    @apiDescription Delete a file by it's ObjectId

    @apiParam (Query param) {String} _id Ingredient's ObjectId

    @apiExample {json} Example usage:
    DELETE http://127.0.0.1:5000/file/<_id>

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
    delete_file_validator.is_object_id_valid(_id=_id)
    file.delete(_id=_id)
    return factory.ServerResponse().return_response(data=None, api="file", code=204)


@file_api.route('/file/ingredient/<_id>', methods=['POST'])
def post_ingredient_file(_id):
    """
    @api {post} /file/ingredient/<_id>  PostIngredientFile
    @apiGroup File
    @apiDescription Add a file to an ingredient

    @apiParam (Query param) {String} _id Ingredient's ObjectId
    @apiParam (Body Param) {String} path File's path
    @apiParam (Body Param) {String} filename File's filename
    @apiParam (Body Param) {Boolean} [is_main] If True, file will be the main file. False by default

    @apiExample {json} Example usage:
    POST http://127.0.0.1:5000/file/ingredient/<_id>
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
    post_file_validator.is_object_id_valid(kind="ingredient", _id=_id)
    body = post_file_factory.clean_body(data=request.json)
    post_file_validator.is_body_valid(data=body)
    inserted_id = file.insert(kind="ingredient", _id_parent=_id, metadata=body)
    data = ingredient.select_one(_id=_id).add_enrichment_file().get_result()
    detail = post_file_factory.detail_information(_id_file=inserted_id)
    return factory.ServerResponse().return_response(data=data, api="file", code=201, detail=detail)


@file_api.route('/file/recipe/<_id>', methods=['POST'])
def post_recipe_file(_id):
    """
    @api {post} /file/recipe/<_id>  PostRecipeFile
    @apiGroup File
    @apiDescription Add a file to a recipe

    @apiParam (Query param) {String} _id Recipe's ObjectId
    @apiParam (Body Param) {String} path File's path
    @apiParam (Body Param) {String} filename File's filename
    @apiParam (Body Param) {Boolean} [is_main] If True, file will be the main file. False by default

    @apiExample {json} Example usage:
    POST http://127.0.0.1:5000/file/recipe/<_id>
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
        'data': {'_id': '5e67a99745378d7c10124235', 'cooking_time': '',
                 'files': [{'_id': '5e67a997ed11fd9361b2e374', 'is_main': False}], 'level': '', 'nb_people': '',
                 'note': '', 'preparation_time': '', 'resume': '', 'steps': [], 'title': 'qa_rhr'},
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
    post_file_validator.is_object_id_valid(kind="recipe", _id=_id)
    body = post_file_factory.clean_body(data=request.json)
    post_file_validator.is_body_valid(data=body)
    inserted_id = file.insert(kind="recipe", _id_parent=_id, metadata=body)
    data = recipe.select_one(_id=_id).add_enrichment_file().get_result()
    detail = post_file_factory.detail_information(_id_file=inserted_id)
    return factory.ServerResponse().return_response(data=data, api="file", code=201, detail=detail)


@file_api.route('/file/recipe/<_id_recipe>/step/<_id_step>', methods=['POST'])
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
        'data': {'_id': '5e6a4223e664b60da7cd8626', 'cooking_time': '', 'files': [], 'level': '', 'nb_people': '',
                 'note': '', 'preparation_time': '', 'resume': '',
                 'steps': [{'_id': '111111111111111111111111', 'files': [{'_id': '5e6a42237e59e8439a883d99',
                 'is_main': False}], 'step': 'a'}, {'_id': '222222222222222222222222', 'files': [], 'step': 'b'}],
                 'title': 'qa_rhr'},
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
    post_file_validator.is_object_id_valid_special_step(kind="recipe", _id_recipe=_id_recipe)
    post_file_validator.is_object_id_valid_special_step(kind="step", _id_recipe=_id_recipe, _id_step=_id_step)
    body = post_file_factory.clean_body(data=request.json)
    post_file_validator.is_body_valid(data=body)
    inserted_id = file.insert(kind="step", _id_parent=_id_step, metadata=body)
    data = recipe.select_one(_id=_id_recipe).add_enrichment_file().get_result()
    detail = post_file_factory.detail_information(_id_file=inserted_id)
    return factory.ServerResponse().return_response(data=data, api="file", code=201, detail=detail)


@file_api.errorhandler(400)
def validator_failed(error):
    """" abort 400 """
    return factory.ServerResponse().return_response(data=error.description, api="file", code=400)


@file_api.errorhandler(404)
def not_found(error):
    """" abort 404 """
    return factory.ServerResponse().return_response(data=error.description, api="file", code=404)
