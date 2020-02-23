from flask import Blueprint, request

import factory as factory
import ingredient.model as ingredient_model
import ingredient.validator.GetIngredient as validator_GetIngredient
import ingredient.validator.PostIngredient as validator_PostIngredient
import ingredient.validator.PutIngredient as validator_PutIngredient
import ingredient.validator.DeleteIngredient as validator_DeleteIngredient
import ingredient.factory.PostIngredient as factory_PostIngredient
import ingredient.factory.PutIngredient as factory_PutIngredient


ingredient_api = Blueprint('ingredient_api', __name__)

ingredient = ingredient_model.Ingredient()
get_ingredient_validator = validator_GetIngredient.Validator()
post_ingredient_validator = validator_PostIngredient.Validator()
put_ingredient_validator = validator_PutIngredient.Validator()
delete_ingredient_validator = validator_DeleteIngredient.Validator()
post_ingredient_factory = factory_PostIngredient.Factory()
put_ingredient_factory = factory_PutIngredient.Factory()


""" 
ingredient route 

- GET /ingredient
- GET /ingredient/<_id>
- POST /ingredient
- PUT /ingredient
- DELETE /ingredient/<_id>

"""


@ingredient_api.route('/ingredient', methods=['GET'])
def get_all_ingredient():
    """ route get all ingredient """
    result = ingredient.select_all()
    return factory.ServerResponse().format_response(data=result, api="ingredient", is_mongo=True, code=200)


@ingredient_api.route('/ingredient/<_id>', methods=['GET'])
def get_ingredient(_id):
    """ route get one ingredient by his ObjectId """
    get_ingredient_validator.is_object_id(_id)
    result = ingredient.select_one(_id)
    get_ingredient_validator.is_result_empty(result)
    return factory.ServerResponse().format_response(data=result, api="ingredient", is_mongo=True, code=200)


@ingredient_api.route('/ingredient', methods=['POST'])
def post_ingredient():
    """ insert one ingredient """
    """ name is mandatory """
    body = post_ingredient_factory.clean_body(request.json)
    post_ingredient_validator.is_body_valid(body)
    post_ingredient_validator.is_name_already_exist(body)
    inserted = ingredient.insert(body)
    return factory.ServerResponse().format_response(data=inserted, api="ingredient", is_mongo=True, code=201)


@ingredient_api.route('/ingredient/<_id>', methods=['PUT'])
def put_ingredient(_id):
    """ update one ingredient """
    put_ingredient_validator.is_object_id(_id)
    body = put_ingredient_factory.clean_body(request.json)
    put_ingredient_validator.is_body_valid(body)
    put_ingredient_validator.is_name_already_exist(body)
    updated = ingredient.update(_id, body)
    return factory.ServerResponse().format_response(data=updated, api="ingredient", is_mongo=True, code=200)


@ingredient_api.route('/ingredient/<_id>', methods=['DELETE'])
def delete_ingredient(_id):
    """ delete one ingredient """
    delete_ingredient_validator.is_object_id(_id)
    ingredient.delete(_id)
    return factory.ServerResponse().format_response(data=None, api="ingredient", is_mongo=False, code=204)


""" 
ingredient error handler 

http 400
http 404

"""


@ingredient_api.errorhandler(400)
def validator_failed(error):
    """" abort 400 """
    return factory.ServerResponse().format_response(data=error.description, api="ingredient", is_mongo=False, code=400)


@ingredient_api.errorhandler(404)
def not_found(error):
    """" abort 404 """
    return factory.ServerResponse().format_response(data=error.description, api="ingredient", is_mongo=False, code=404)
