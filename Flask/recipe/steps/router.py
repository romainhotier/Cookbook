from flask import Blueprint, request

import factory as factory
import recipe.recipe.model as recipe_model
import recipe.steps.model as steps_model

#import recipe.recipe.validator.GetRecipe as validator_GetRecipe
import recipe.steps.validator.PostRecipeStep as validator_PostRecipeStep
# import recipe.recipe.validator.PutRecipe as validator_PutRecipe
import recipe.steps.validator.DeleteRecipeStep as validator_DeleteRecipeStep
import recipe.steps.factory.PostRecipeStep as factory_PostRecipeStep
#import recipe.recipe.factory.PutRecipe as factory_PutRecipe

recipe_steps_api = Blueprint('recipe_steps_api', __name__)

#recipe = recipe_model.Recipe()
steps = steps_model.Steps()

#get_recipe_validator = validator_GetRecipe.Validator()
post_recipe_step_validator = validator_PostRecipeStep.Validator()
#put_recipe_validator = validator_PutRecipe.Validator()
delete_recipe_step_validator = validator_DeleteRecipeStep.Validator()
post_recipe_step_factory = factory_PostRecipeStep.Factory()
#put_recipe_factory = factory_PutRecipe.Factory()


""" 
steps route 

- POST /recipe/<_id>/step

"""


@recipe_steps_api.route('/recipe/<_id>/step', methods=['POST'])
def post_recipe_step(_id):
    """ insert one step to a recipe """
    post_recipe_step_validator.is_object_id(_id)
    body = post_recipe_step_factory.clean_body(request.json)
    post_recipe_step_validator.is_body_valid(_id, body)
    inserted = steps.insert(_id, body)
    return factory.ServerResponse().format_response(data=inserted, api="recipe_steps", is_mongo=True, code=201)


@recipe_steps_api.route('/recipe/<_id>/step/<_index>', methods=['DELETE'])
def delete_recipe_step(_id, _index):
    """ delete one step to a recipe """
    delete_recipe_step_validator.is_object_id(_id)
    delete_recipe_step_validator.is_index_valid(_id, _index)
    deleted = steps.delete(_id, _index)
    return factory.ServerResponse().format_response(data=None, api="recipe", is_mongo=True, code=204)



"""
@recipe_api.route('/recipe/<_id>', methods=['PUT'])
def put_recipe(_id):
    "" update one recipe ""
    put_recipe_validator.is_object_id(_id)
    body = put_recipe_factory.clean_body(request.json)
    put_recipe_validator.is_body_valid(body)
    put_recipe_validator.is_title_already_exist(body)
    updated = recipe.update(_id, body)
    return factory.ServerResponse().format_response(data=updated, api="recipe", is_mongo=True, code=200)
"""
"""
@recipe_api.route('/recipe/<_id>', methods=['DELETE'])
def delete_recipe(_id):
    "" delete one recipe ""
    delete_recipe_validator.is_object_id(_id)
    recipe.delete(_id)
    return factory.ServerResponse().format_response(data=None, api="recipe", is_mongo=True, code=204)
"""

""" 
recipe error handler 

http 400
http 404

"""


@recipe_steps_api.errorhandler(400)
def validator_failed(error):
    """" abort 400 """
    return factory.ServerResponse().format_response(data=error.description, api="recipe_steps", is_mongo=False,
                                                    code=400)


@recipe_steps_api.errorhandler(404)
def not_found(error):
    """" abort 404 """
    return factory.ServerResponse().format_response(data=error.description, api="recipe_steps", is_mongo=False,
                                                    code=404)
