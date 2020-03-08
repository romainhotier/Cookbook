from flask import Blueprint, make_response, request

import server.factory as factory
import app.ingredient.ingredient.model as ingredient_model
import app.file.all.model as file_model
import app.file.ingredient.factory.PostIngredientFile as factory_PostIngredientFile
import app.file.ingredient.validator.PostIngredientFile as validator_PostIngredientFile

file_ingredient_api = Blueprint('file_ingredient_api', __name__)

ingredient = ingredient_model.Ingredient()
file = file_model.File()
post_ingredient_file_factory = factory_PostIngredientFile.Factory()
post_ingredient_file_validator = validator_PostIngredientFile.Validator()


@file_ingredient_api.route('/file/ingredient/<_id>', methods=['POST'])
def post_ingredient_file(_id):
    """
    @api {post} /file/ingredient/<_id>  PostIngredientFile
    @apiGroup Ingredient File
    @apiDescription Add a file to a ingredient

    @apiParam (Query param) {String} _id Ingredient's ObjectId
    @apiParam (Body Param) {String} path File's path
    @apiParam (Body Param) {String} filename File's filename
    @apiParam (Body Param) {Boolean} [is_main] If True, file will be the main file. False by default

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/file/ingredient/<_id>

    @apiSuccessExample {json} Success response:
    HTTPS 201
    {
        'codeMsg': 'cookbook.file_ingredient.success.created',
        'codeStatus': 201,
        'data': {'_id': '5e622b52c49ed1e0df987e55',
                'name': 'qa_rhr',
                'files': [{'_id': '5e622b537aa097121df95d93', 'is_main': False}]},
        'detail': 'added file ObjectId: 5e622b537aa097121df95d93'
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.file_ingredient.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    post_ingredient_file_validator.is_object_id_valid(_id)
    body = post_ingredient_file_factory.clean_body(request.json)
    post_ingredient_file_validator.is_body_valid(body)
    inserted_id = file.insert(kind="ingredient", _id_parent=_id, metadata=body)
    data = ingredient.select_one_with_enrichment(_id=_id)
    detail = post_ingredient_file_factory.detail_information(_id_file=inserted_id)
    return factory.ServerResponse().format_response(data=data, api="file_ingredient", code=201, detail=detail)


@file_ingredient_api.errorhandler(400)
def validator_failed(error):
    """" abort 400 """
    return factory.ServerResponse().format_response(data=error.description, api="file_ingredient", code=400)


@file_ingredient_api.errorhandler(404)
def not_found(error):
    """" abort 404 """
    return factory.ServerResponse().format_response(data=error.description, api="file_ingredient", code=404)
