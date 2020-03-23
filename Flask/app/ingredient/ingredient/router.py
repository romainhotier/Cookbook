from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

import server.server as server
import server.auth as auth
import app.ingredient.ingredient.model as ingredient_model
import app.file.file.model as file_model
import app.link.ingredient_recipe.model as link_model
import app.ingredient.ingredient.validator.GetAllIngredient as validator_GetAllIngredient
import app.ingredient.ingredient.validator.GetIngredient as validator_GetIngredient
import app.ingredient.ingredient.validator.PostIngredient as validator_PostIngredient
import app.ingredient.ingredient.validator.PutIngredient as validator_PutIngredient
import app.ingredient.ingredient.validator.DeleteIngredient as validator_DeleteIngredient
import app.ingredient.ingredient.factory.PostIngredient as server_PostIngredient
import app.ingredient.ingredient.factory.PutIngredient as server_PutIngredient


ingredient_api = Blueprint('ingredient_api', __name__)
auth = auth.Auth()


ingredient = ingredient_model.Ingredient()
file = file_model.File()
link = link_model.LinkIngredientRecipe()
get_all_ingredient_validator = validator_GetAllIngredient.Validator()
get_ingredient_validator = validator_GetIngredient.Validator()
post_ingredient_validator = validator_PostIngredient.Validator()
put_ingredient_validator = validator_PutIngredient.Validator()
delete_ingredient_validator = validator_DeleteIngredient.Validator()
post_ingredient_factory = server_PostIngredient.Factory()
put_ingredient_factory = server_PutIngredient.Factory()


#@ingredient_api.before_request
#@auth.login_required
#def protect():
#    pass


@ingredient_api.route('/ingredient', methods=['GET'])
def get_all_ingredient():
    """
    @api {get} /ingredient  GetAllIngredient
    @apiGroup Ingredient
    @apiDescription Get file ingredients

    @apiParam (Query param) {String} [with_files] if "true", add ingredient's files

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/ingredient

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.ingredient.success.ok',
        'codeStatus': 200,
        'data': [{'_id': '5e583de9b0fcef0a922a7bc0', 'name': 'aqa_rhr'},
                 {'_id': '5e583de9b0fcef0a922a7bc2', 'name': 'bqa_rhr'}]
    }
    """
    """ check param enrichment """
    with_files = get_all_ingredient_validator.is_string_boolean(with_files=request.args.get('with_files'))[1]
    """ get all ingredient """
    data = ingredient.select_all()
    """ add enrichment if needed """
    if with_files:
        data.add_enrichment_file_for_all()
    #print(get_jwt_identity())
    #headers={"Authorization": "Bearer " + token}
    """ return response """
    return server.ServerResponse().return_response(data=data.get_result(), api="ingredient", code=200)


@ingredient_api.route('/ingredient/<_id>', methods=['GET'])
def get_ingredient(_id):
    """
    @api {get} /ingredient/<_id>  GetIngredient
    @apiGroup Ingredient
    @apiDescription Get an ingredient by it's ObjectId

    @apiParam (Query param) {String} _id Ingredient's ObjectId
    @apiParam (Query param) {String} [with_files] if "true", add ingredient's files

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/ingredient/<_id>

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.ingredient.success.ok',
        'codeStatus': 200,
        'data': {'_id': '5e583de9b0fcef0a922a7bc0', 'name': 'aqa_rhr'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    """ check param enrichment """
    with_files = get_ingredient_validator.is_string_boolean(with_files=request.args.get('with_files'))[1]
    """ check param _id """
    get_ingredient_validator.is_object_id_valid(_id=_id)
    """ get ingredient """
    data = ingredient.select_one(_id=_id)
    """ add enrichment if needed """
    if with_files:
        data.add_enrichment_file_for_one()
    """ return response """
    return server.ServerResponse().return_response(data=data.get_result(), api="ingredient", code=200)


@ingredient_api.route('/ingredient', methods=['POST'])
def post_ingredient():
    """
    @api {post} /ingredient  PostIngredient
    @apiGroup Ingredient
    @apiDescription Create an ingredient

    @apiParam (Body param) {String} name Ingredient's name

    @apiExample {json} Example usage:
    POST http://127.0.0.1:5000/ingredient
    {
        'name': <name>
    }

    @apiSuccessExample {json} Success response:
    HTTPS 201
    {
        'codeMsg': 'cookbook.ingredient.success.created',
        'codeStatus': 201,
        'data': {'_id': '5e5840e63ed55d9119064649', 'name': 'qa_rhr_name'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Is required', 'param': 'name'}}
    }
    """
    """ check body """
    body = post_ingredient_factory.clean_body(data=request.json)
    post_ingredient_validator.is_body_valid(data=body)
    """ add ingredient """
    data = ingredient.insert(data=body)
    """ return response """
    return server.ServerResponse().return_response(data=data.get_result(), api="ingredient", code=201)


@ingredient_api.route('/ingredient/<_id>', methods=['PUT'])
def put_ingredient(_id):
    """
    @api {put} /ingredient/<_id>  UpdateIngredient
    @apiGroup Ingredient
    @apiDescription Update an ingredient by it's ObjectId

    @apiParam (Query param) {String} _id Ingredient's ObjectId
    @apiParam (Query param) {String} [with_files] if "true", add ingredient's files
    @apiParam (Body Param) {String} name Ingredient's name

    @apiExample {json} Example usage:
    PUT http://127.0.0.1:5000/ingredient/<_id>
    {
        'name': <name>
    }

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.ingredient.success.ok',
        'codeStatus': 20O,
        'data': {'_id': '5e5840e63ed55d9119064649', 'name': 'qa_rhr_name_update'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Is required', 'param': 'name'}}
    }
    """
    """ check param enrichment """
    with_files = put_ingredient_validator.is_string_boolean(with_files=request.args.get('with_files'))[1]
    """ check param _id """
    put_ingredient_validator.is_object_id_valid(_id=_id)
    """ check body """
    body = put_ingredient_factory.clean_body(data=request.json)
    put_ingredient_validator.is_body_valid(data=body)
    """ update ingredient """
    data = ingredient.update(_id=_id, data=body)
    """ add enrichment if needed """
    if with_files:
        data.add_enrichment_file_for_one()
    """ return response """
    return server.ServerResponse().return_response(data=data.get_result(), api="ingredient", code=200)


@ingredient_api.route('/ingredient/<_id>', methods=['DELETE'])
def delete_ingredient(_id):
    """
    @api {delete} /ingredient/<_id>  DeleteIngredient
    @apiGroup Ingredient
    @apiDescription Delete an ingredient by it's ObjectId

    @apiParam (Query param) {String} _id Ingredient's ObjectId

    @apiExample {json} Example usage:
    DELETE http://127.0.0.1:5000/ingredient/<_id>

    @apiSuccessExample {json} Success response:
    HTTPS 204

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    """ check param _id """
    delete_ingredient_validator.is_object_id_valid(_id=_id)
    """ clean files and link """
    file.clean_file_by_id_parent(_id_parent=_id)
    link.clean_link_by_id_ingredient(_id_ingredient=_id)
    """ delete ingredient """
    ingredient.delete(_id=_id)
    return server.ServerResponse().return_response(data=None, api="ingredient", code=204)


@ingredient_api.errorhandler(400)
def validator_failed(error):
    """" abort 400 """
    return server.ServerResponse().return_response(data=error.description, api="ingredient", code=400)


@ingredient_api.errorhandler(404)
def not_found(error):
    """" abort 404 """
    return server.ServerResponse().return_response(data=error.description, api="ingredient", code=404)
