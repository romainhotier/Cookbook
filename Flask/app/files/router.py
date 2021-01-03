from flask import Blueprint, request

import utils

import app.files.factory as factory
import app.files.validator as validator
import app.ingredient.model as ingredient_model
import app.recipe.model as recipe_model

apis = Blueprint('files', __name__, url_prefix='/files')

server = utils.Server()
ingredient = ingredient_model.Ingredient()
recipe = recipe_model.Recipe()


@apis.route('/recipe/<_id>', methods=['POST'])
def post_recipe_file(_id):
    """
    @api {post} /file/recipe/<_id_recipe>  PostRecipeFile
    @apiGroup File
    @apiDescription Add a file to a recipe

    @apiParam (Query param) {String} _id Recipe's ObjectId

    @apiExample {json} Example usage:
    POST http://127.0.0.1:5000/file/recipe/<_id_recipe>
    files = [
             ('files', ('qa_rhr_filename.png', open(path1, 'rb'), mimetypes)),
             ('files', ('qa_rhr_filename2.jpeg', open(path2, 'rb'), mimetypes))]

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
    api = factory.PostFiles.Factory()
    validation = validator.PostFiles.Validator()
    """ check param """
    validation.is_object_id_valid(kind="recipe", value=_id)
    """ save files """
    urls = api.save_files(kind="ingredient", _id=_id, files=request.files.getlist('files'))
    """ update ingredient """
    recipe.add_fs(_id=_id, data=urls)
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
