from flask import Blueprint, request

import server.factory as factory
import app.ingredient.ingredient.model as ingredient_model
import app.ingredient.ingredient.validator.GetIngredient as validator_GetIngredient
import app.ingredient.ingredient.validator.PostIngredient as validator_PostIngredient
import app.ingredient.ingredient.validator.PutIngredient as validator_PutIngredient
import app.ingredient.ingredient.validator.DeleteIngredient as validator_DeleteIngredient
import app.ingredient.ingredient.factory.PostIngredient as factory_PostIngredient
import app.ingredient.ingredient.factory.PutIngredient as factory_PutIngredient


ingredient_api = Blueprint('ingredient_api', __name__)

ingredient = ingredient_model.Ingredient()
get_ingredient_validator = validator_GetIngredient.Validator()
post_ingredient_validator = validator_PostIngredient.Validator()
put_ingredient_validator = validator_PutIngredient.Validator()
delete_ingredient_validator = validator_DeleteIngredient.Validator()
post_ingredient_factory = factory_PostIngredient.Factory()
put_ingredient_factory = factory_PutIngredient.Factory()


@ingredient_api.route('/ingredient', methods=['GET'])
def get_all_ingredient():
    """
    @api {get} /ingredient  GetAllIngredient
    @apiGroup Ingredient
    @apiDescription Get file ingredients

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
    data = ingredient.select_all().get_result()
    return factory.ServerResponse().return_response(data=data, api="ingredient", code=200)


@ingredient_api.route('/ingredient/<_id>', methods=['GET'])
def get_ingredient(_id):
    """
    @api {get} /ingredient/<_id>  GetIngredient
    @apiGroup Ingredient
    @apiDescription Get an ingredient by it's ObjectId

    @apiParam (Query param) {String} _id Ingredient's ObjectId

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
    get_ingredient_validator.is_object_id_valid(_id)
    data = ingredient.select_one(_id).get_result()
    return factory.ServerResponse().return_response(data=data, api="ingredient", code=200)


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
    body = post_ingredient_factory.clean_body(request.json)
    post_ingredient_validator.is_body_valid(body)
    post_ingredient_validator.is_name_already_exist(body)
    data = ingredient.insert(body).get_result()
    return factory.ServerResponse().return_response(data=data, api="ingredient", code=201)


@ingredient_api.route('/ingredient/<_id>', methods=['PUT'])
def put_ingredient(_id):
    """
    @api {put} /ingredient/<_id>  UpdateIngredient
    @apiGroup Ingredient
    @apiDescription Update an ingredient by it's ObjectId

    @apiParam (Query param) {String} _id Ingredient's ObjectId
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
    put_ingredient_validator.is_object_id_valid(_id)
    body = put_ingredient_factory.clean_body(request.json)
    put_ingredient_validator.is_body_valid(body)
    put_ingredient_validator.is_name_already_exist(body)
    data = ingredient.update(_id, body).get_result()
    return factory.ServerResponse().return_response(data=data, api="ingredient", code=200)


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
    delete_ingredient_validator.is_object_id_valid(_id)
    ingredient.delete(_id)
    return factory.ServerResponse().return_response(data=None, api="ingredient", code=204)


@ingredient_api.errorhandler(400)
def validator_failed(error):
    """" abort 400 """
    return factory.ServerResponse().return_response(data=error.description, api="ingredient", code=400)


@ingredient_api.errorhandler(404)
def not_found(error):
    """" abort 404 """
    return factory.ServerResponse().return_response(data=error.description, api="ingredient", code=404)
