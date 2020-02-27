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


@recipe_steps_api.route('/recipe/<_id>/step', methods=['POST'])
def post_recipe_step(_id):
    """
    @api {post} /recipe/<_id>/step' PostRecipeStep
    @apiGroup RecipeSteps
    @apiDescription Create a recipe's step. Can specify where to add the step

    @apiParam (Query param) {String} _id Recipe's ObjectId
    @apiParam (Body param) {String} step Step's value to add
    @apiParam (Body param) {Integer} [position] Position in recipe's steps array.
                                                If not specified, add at the end of the array

    @apiExample {json} Example usage:
    POST http://127.0.0.1:5000/recipe/<_id>/step
    {
        'step': <step>,
        'position': <position>
    }

    @apiSuccessExample {json} Success response:
    HTTPS 201 OK
    {
        'codeMsg': 'cookbook.recipe_steps.success.created',
        'codeStatus': 201,
        'data': {'_id': '5e584e658269f301022369ff', 'cooking_time': '', 'ingredients': {}, 'level': '', 'nb_people': '',
                 'note': '', 'preparation_time': '', 'resume': '', 'steps': ['a', 'new_step', 'b'], 'title': 'qa_rhr'}}

    @apiErrorExample {json} Error response:
    HTTPS 400 OK
    {
        'codeMsg': 'cookbook.recipe_steps.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an integer', 'param': 'position', 'value': 'invalid'}
    }
    """
    post_recipe_step_validator.is_object_id_valid(_id)
    body = post_recipe_step_factory.clean_body(request.json)
    post_recipe_step_validator.is_body_valid(_id, body)
    inserted = steps.insert(_id, body)
    return factory.ServerResponse().format_response(data=inserted, api="recipe_steps", is_mongo=True, code=201)


@recipe_steps_api.route('/recipe/<_id>/step/<position>', methods=['DELETE'])
def delete_recipe_step(_id, position):
    """
    @api {delete} /recipe/<_id>/step/<_position>  DeleteRecipeStep
    @apiGroup RecipeSteps
    @apiDescription Delete a recipe's step by it's position in the array

    @apiParam (Query param) {String} _id Recipe's ObjectId
    @apiParam (Query param) {String} position Position in recipe's steps array

    @apiExample {json} Example usage:
    DELETE http://127.0.0.1:5000/recipe/<_id>/step/<position>

    @apiSuccessExample {json} Success response:
    HTTPS 200 OK
    {
        'codeMsg': 'cookbook.recipe_steps.success.ok',
        'codeStatus': 200,
        'data': {'_id': '5e584ffd0e7d15c4c1022389', 'cooking_time': '', 'ingredients': {}, 'level': '', 'nb_people': '',
                 'note': '', 'preparation_time': '', 'resume': '', 'steps': ['a'], 'title': 'qa_rhr'}}

    @apiErrorExample {json} Error response:
    HTTPS 400 OK
    {
        'codeMsg': 'cookbook.recipe_steps.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an integer', 'param': 'position', 'value': 'invalid'}
    }
    """
    delete_recipe_step_validator.is_object_id_valid(_id)
    delete_recipe_step_validator.is_position_valid(_id, position)
    deleted = steps.delete(_id, position)
    return factory.ServerResponse().format_response(data=deleted, api="recipe_steps", is_mongo=True, code=200)


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
