from flask import Blueprint, request

from server import factory as factory
import app.recipe.steps.model as steps_model

import app.recipe.steps.validator.PostRecipeStep as validator_PostRecipeStep
import app.recipe.steps.validator.DeleteRecipeStep as validator_DeleteRecipeStep
import app.recipe.steps.factory.PostRecipeStep as factory_PostRecipeStep

recipe_steps_api = Blueprint('recipe_steps_api', __name__)

steps = steps_model.Steps()

post_recipe_step_validator = validator_PostRecipeStep.Validator()
delete_recipe_step_validator = validator_DeleteRecipeStep.Validator()
post_recipe_step_factory = factory_PostRecipeStep.Factory()


""" 
steps route 

- POST /recipe/<_id>/step
- DELETE /recipe/<_id>/step/<_position>

"""


@recipe_steps_api.route('/recipe/<_id>/step', methods=['POST'])
def post_recipe_step(_id):
    """ insert one step to a recipe """
    post_recipe_step_validator.is_object_id_valid(_id)
    body = post_recipe_step_factory.clean_body(request.json)
    post_recipe_step_validator.is_body_valid(_id, body)
    inserted = steps.insert(_id, body)
    return factory.ServerResponse().format_response(data=inserted, api="recipe_steps", is_mongo=True, code=201)


@recipe_steps_api.route('/recipe/<_id>/step/<_position>', methods=['DELETE'])
def delete_recipe_step(_id, _position):
    """ delete one step to a recipe """
    delete_recipe_step_validator.is_object_id_valid(_id)
    delete_recipe_step_validator.is_position_valid(_id, _position)
    deleted = steps.delete(_id, _position)
    return factory.ServerResponse().format_response(data=deleted, api="recipe_steps", is_mongo=True, code=200)


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
