from flask import Blueprint, request, send_from_directory

from app import utils, backend
from app.recipe import Recipe
from app.files import File
import app.files.factory as factory
import app.files.validator as validator

apis = Blueprint('files', __name__, url_prefix='/files')


@apis.route('/<path:path>', methods=['DELETE'])
def delete_file(path):
    """
    @api {delete} /files/<path> DeleteFile
    @apiGroup Files
    @apiDescription Delete a file

    @apiParam (Query param) {String} path File's path

    @apiExample {json} Example usage:
    DELETE http://127.0.0.1:5000/files/<path>

    @apiSuccessExample {json} Success response:
    HTTPS 204
    TBD

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.cookbook.error.bad_request',
        'codeStatus': 404,
        'detail': 'The requested URL was not found on the server'
    }
    """
    api = factory.DeleteFile.Factory()
    validation = validator.DeleteFile.Validator()
    """ check param """
    validation.is_path_valid(value=path)
    """ delete file """
    deleted_path = File().delete(short_path=path)
    """ clean in recipe """
    Recipe().delete_file(path=path)
    """ return response """
    return utils.ResponseMaker().return_response(data=deleted_path, api=apis.name, http_code=200)


@apis.route('/<path:path>', methods=['GET'])
def get_file(path):
    """
    @api {get} /files/<path> GetFile
    @apiGroup Files
    @apiDescription Get a file

    @apiParam (Query param) {String} path File's path

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/files/recipe/<path>

    @apiSuccessExample {json} Success response:
    Files Streamed

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.cookbook.error.bad_request',
        'codeStatus': 404,
        'detail': 'The requested URL was not found on the server'
    }
    """
    """ return response """
    return send_from_directory(directory=backend.config["FILE_STORAGE_PATH"], filename=path)


@apis.route('/recipe/<_id>', methods=['POST'])
def post_files_recipe(_id):
    """
    @api {post} /files/<_id>  PostFiles
    @apiGroup Files
    @apiDescription Add files to an element

    @apiParam (Query param) {String} _id Recipe's ObjectId
    @apiParam (Multipart/form-data) files Files

    @apiExample {json} Example usage:
    POST http://127.0.0.1:5000/files/recipe/<_id>
    files = [
             ('files', ('qa_rhr_filename.txt', open(path1, 'rb'), mimetypes)),
             ('files', ('qa_rhr_filename2.png', open(path2, 'rb'), mimetypes)),
             ('files', ('qa_rhr_filename3.jpeg', open(path3, 'rb'), mimetypes))]

    @apiSuccessExample {json} Success response:
    HTTPS 201
    {
        'codeMsg': 'cookbook.files.success.created',
        'codeStatus': 201,
        'data': ['recipe/5ff5869625fcd58c3ecc5f17/qa_rhr_filename.txt',
                 'recipe/5ff5869625fcd58c3ecc5f17/qa_rhr_filename2.png',
                 'recipe/5ff5869625fcd58c3ecc5f17/qa_rhr_filename3.jpeg']}

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.files.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    validation = validator.PostFilesRecipe.Validator()
    """ check param """
    validation.is_object_id_valid(value=_id)
    """ save files """
    urls = File().save_files(short_path="recipe/{}".format(_id), files=request.files.getlist('files'))
    """ update ingredient """
    Recipe().add_files(_id=_id, data=urls)
    """ return response """
    return utils.ResponseMaker().return_response(data=urls, api=apis.name, http_code=201)


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
    return utils.ResponseMaker().return_response(data=err.description, api=apis.name, http_code=400)


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
    return utils.ResponseMaker().return_response(data=err, api=apis.name, http_code=404)
