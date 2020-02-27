from flask import Blueprint, request

import server.factory as factory
# import app.ingredient.ingredient.model as ingredient_model
# import app.ingredient.ingredient.validator.GetIngredient as validator_GetIngredient
# import app.ingredient.ingredient.validator.PostIngredient as validator_PostIngredient
# import app.ingredient.ingredient.validator.PutIngredient as validator_PutIngredient
# import app.ingredient.ingredient.validator.DeleteIngredient as validator_DeleteIngredient
# import app.ingredient.ingredient.factory.PostIngredient as factory_PostIngredient
# import app.ingredient.ingredient.factory.PutIngredient as factory_PutIngredient


ingredient_api = Blueprint('ingredient_api', __name__)

# ingredient = ingredient_model.Ingredient()
# get_ingredient_validator = validator_GetIngredient.Validator()
# post_ingredient_validator = validator_PostIngredient.Validator()
# put_ingredient_validator = validator_PutIngredient.Validator()
# delete_ingredient_validator = validator_DeleteIngredient.Validator()
# post_ingredient_factory = factory_PostIngredient.Factory()
# put_ingredient_factory = factory_PutIngredient.Factory()


""" 
ingredientFile route 

- Post /ingredient

"""


@ingredient_api.route('/ingredient', methods=['GET'])
def get_all_ingredient():
    """ route get all ingredient """
    result = ingredient.select_all()
    return factory.ServerResponse().format_response(data=result, api="ingredient", is_mongo=True, code=200)


@ingredient_api.route('/ingredient/<_id>', methods=['GET'])
def get_ingredient(_id):
    """ route get one ingredient by his ObjectId """
    get_ingredient_validator.is_object_id_valid(_id)
    result = ingredient.select_one(_id)
    return factory.ServerResponse().format_response(data=result, api="ingredient", is_mongo=True, code=200)