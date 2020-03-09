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
    get_file_validator.is_object_id_valid(_id)
    result = file.select_one(_id)
    response = make_response(result.read(), 200)
    response.mimetype = result.content_type
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
    delete_file_validator.is_object_id_valid(_id)
    file.delete(_id)
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
    post_file_validator.is_object_id_valid(_id, kind="ingredient")
    body = post_file_factory.clean_body(request.json)
    post_file_validator.is_body_valid(body)
    inserted_id = file.insert(kind="ingredient", _id_parent=_id, metadata=body)
    data = ingredient.select_one_with_enrichment(_id=_id)
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

    @apiSuccessExample {json} Success response:
    HTTPS 201
    {
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.file.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    post_file_validator.is_object_id_valid(_id, kind="recipe")
    body = post_file_factory.clean_body(request.json)
    post_file_validator.is_body_valid(body)
    inserted_id = file.insert(kind="recipe", _id_parent=_id, metadata=body)
    data = recipe.select_one_with_enrichment(_id=_id)
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
