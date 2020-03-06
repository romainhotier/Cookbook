from flask import Blueprint, make_response

import server.factory as factory
import app.file.all.model as ingredient_file_model
import app.file.all.validator.GetFile as validator_GetFile


file_api = Blueprint('file_api', __name__)

file = ingredient_file_model.File()
get_file_validator = validator_GetFile.Validator()


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


@file_api.errorhandler(400)
def validator_failed(error):
    """" abort 400 """
    return factory.ServerResponse().format_response(data=error.description, api="file", code=400)


@file_api.errorhandler(404)
def not_found(error):
    """" abort 404 """
    return factory.ServerResponse().format_response(data=error.description, api="file", code=404)
