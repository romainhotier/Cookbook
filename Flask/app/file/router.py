from flask import Blueprint, make_response, request

import server.factory as factory
import app.file.model as ingredient_file_model
import app.file.validator.GetFile as validator_GetFile
import app.file.factory.PostIngredientFile as factory_PostIngredientFile
import app.file.validator.PostIngredientFile as validator_PostIngredientFile

file_api = Blueprint('file_api', __name__)

file = ingredient_file_model.File()
get_file_validator = validator_GetFile.Validator()
post_ingredient_file_factory = factory_PostIngredientFile.Factory()
post_ingredient_file_validator = validator_PostIngredientFile.Validator()


@file_api.route('/file/<_id>', methods=['GET'])
def get_file(_id):
    """
    @api {get} /file/<_id>  DownloadFile
    @apiGroup File
    @apiDescription Get an file by it's ObjectId

    @apiParam (Query param) {String} _id File's ObjectId

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/file/<_id>

    @apiSuccessExample {json} Success response:
    HTTPS 200 OK
    �PNG
    np������Q*D�l1<��j3

    @apiErrorExample {json} Error response:
    HTTPS 400 OK
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


@file_api.route('/file/ingredient/<_id>', methods=['POST'])
def post_ingredient_file(_id):
    body = post_ingredient_file_factory.clean_body(request.json)
    post_ingredient_file_validator.is_body_valid(body)
    inserted_id = file.insert(kind="ingredient", _id_parent=_id, metadata=body)
    data = post_ingredient_file_factory.enrich_ingredient(_id_ingredient=_id, _id_file=inserted_id, metadata=body)
    detail = post_ingredient_file_factory.detail_information(_id_file=inserted_id)
    return factory.ServerResponse().format_response(data=data, api="file", is_mongo=True, code=201, detail=detail)


@file_api.errorhandler(400)
def validator_failed(error):
    """" abort 400 """
    return factory.ServerResponse().format_response(data=error.description, api="file", is_mongo=False, code=400)


@file_api.errorhandler(404)
def not_found(error):
    """" abort 404 """
    return factory.ServerResponse().format_response(data=error.description, api="file", is_mongo=False, code=404)
