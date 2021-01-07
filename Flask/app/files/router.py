from flask import Blueprint, request, send_from_directory

import utils

import app.files.factory as factory
import app.files.validator as validator
import app.ingredient.model as ingredient_model
import app.recipe.model as recipe_model

apis = Blueprint('files', __name__, url_prefix='/files')

server = utils.Server()
ingredient = ingredient_model.Ingredient()
recipe = recipe_model.Recipe()


@apis.route('/<path:path>', methods=['GET'])
def get_files(path):
    """
    @api {get} /files/<path> GetFiles
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
    return send_from_directory(directory=utils.Server().path_file_storage, filename=path)


@apis.route('/recipe/<_id>', methods=['POST'])
def post_recipe_files(_id):
    """
    @api {post} /files/recipe/<_id_recipe>  PostRecipeFiles
    @apiGroup Files
    @apiDescription Add files to a recipe

    @apiParam (Query param) {String} _id Recipe's ObjectId
    @apiParam (Multipart/form-data) files Recipe's Files

    @apiExample {json} Example usage:
    POST http://127.0.0.1:5000/files/recipe/<_id_recipe>
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
    api = factory.PostFiles.Factory()
    validation = validator.PostFiles.Validator()
    """ check param """
    validation.is_object_id_valid(kind="recipe", value=_id)
    """ save files """
    urls = api.save_files(kind="recipe", _id=_id, files=request.files.getlist('files'))
    """ update ingredient """
    recipe.add_files(_id=_id, data=urls)
    """ return response """
    return server.return_response(data=urls, api=apis.name, http_code=201)


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
