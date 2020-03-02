from flask import Blueprint, request, make_response

import server.factory as factory
import app.ingredient.file.model as ingredient_file_model
# import app.ingredient.ingredient.validator.GetIngredient as validator_GetIngredient
# import app.ingredient.ingredient.validator.PostIngredient as validator_PostIngredient
# import app.ingredient.ingredient.validator.PutIngredient as validator_PutIngredient
# import app.ingredient.ingredient.validator.DeleteIngredient as validator_DeleteIngredient
# import app.ingredient.ingredient.factory.PostIngredient as factory_PostIngredient
# import app.ingredient.ingredient.factory.PutIngredient as factory_PutIngredient


ingredient_file_api = Blueprint('ingredient_file_api', __name__)

ingredient_file = ingredient_file_model.IngredientFile()
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

@ingredient_file_api.route('/ingredient/file/<_id>', methods=['GET'])
def get_ingredient_file(_id):
    aa = ingredient_file.select_one(_id)
    #result = ingredient.select_all()
    #return factory.ServerResponse().format_response(data=result, api="ingredient", is_mongo=True, code=200)
    response = make_response(aa.read())
    #response.mimetype = "text/plain"
    response.mimetype = "image/png"
    return response

"""
@ingredient_api.route('/ingredient/<_id>', methods=['GET'])
def get_ingredient(_id):
    file_upload = Upload.objects.get(integer_key=request_id)
    response = make_response(file_upload.filename.read())
    response.mimetype = file_upload.content_type
    return response
    get_ingredient_validator.is_object_id_valid(_id)
    result = ingredient.select_one(_id)
    return factory.ServerResponse().format_response(data=result, api="ingredient", is_mongo=True, code=200)
"""