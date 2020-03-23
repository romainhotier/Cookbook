from flask import Blueprint, request

import server.server as server
import app.recipe.steps.model as steps_model
import app.file.file.model as file_model
import app.recipe.steps.validator.PostRecipeStep as validator_PostRecipeStep
import app.recipe.steps.validator.PutRecipeStep as validator_PutRecipeStep
import app.recipe.steps.validator.DeleteRecipeStep as validator_DeleteRecipeStep
import app.recipe.steps.factory.PostRecipeStep as factory_PostRecipeStep
import app.recipe.steps.factory.PutRecipeStep as factory_PutRecipeStep

recipe_steps_api = Blueprint('recipe_steps_api', __name__)

steps = steps_model.Steps()
file = file_model.File()

post_recipe_step_validator = validator_PostRecipeStep.Validator()
put_recipe_step_validator = validator_PutRecipeStep.Validator()
delete_recipe_step_validator = validator_DeleteRecipeStep.Validator()
post_recipe_step_factory = factory_PostRecipeStep.Factory()
put_recipe_step_factory = factory_PutRecipeStep.Factory()


@recipe_steps_api.route('/recipe/<_id>/step', methods=['POST'])
def post_recipe_step(_id):
    """
    @api {post} /recipe/<_id>/step PostRecipeStep
    @apiGroup RecipeSteps
    @apiDescription Create a recipe's step. Can specify where to add the step

    @apiParam (Query param) {String} _id Recipe's ObjectId
    @apiParam (Query param) {String} [with_files] if "true", add recipe's files
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
    HTTPS 201
    {
        'codeMsg': 'cookbook.recipe_steps.success.created',
        'codeStatus': 201,
        'data': {'_id': '5e68acb9e067528c70c75f3c', 'cooking_time': 0, 'level': 0, 'nb_people': 0, 'note': '',
                 'preparation_time': 0, 'resume': '', title': 'qa_rhr', 'slug': '', 'categories': [],
                 'steps': [{'_id': '5e68acb97b0ead079be3cef7', 'step': 'new_step'}]}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe_steps.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an integer', 'param': 'position', 'value': 'invalid'}
    }
    """
    """ check param enrichment """
    with_files = post_recipe_step_validator.is_string_boolean(with_files=request.args.get('with_files'))[1]
    """ check param _id """
    post_recipe_step_validator.is_object_id_valid(_id=_id)
    """ check body """
    body = post_recipe_step_factory.clean_body(data=request.json)
    post_recipe_step_validator.is_body_valid(_id=_id, data=body)
    """ insert step """
    data = steps.insert(_id=_id, data=body)
    """ add enrichment if needed """
    if with_files:
        data.add_enrichment_file_for_one()
    """ return response """
    return server.ServerResponse().return_response(data=data.get_result(), api="recipe_steps", code=201)


@recipe_steps_api.route('/recipe/<_id_recipe>/step/<_id_step>', methods=['PUT'])
def put_recipe_step(_id_recipe, _id_step):
    """
    @api {put} /recipe/<_id_recipe>/step/<_id_step>  PutRecipeStep
    @apiGroup RecipeSteps
    @apiDescription Update a recipe's step

    @apiParam (Query param) {String} _id_recipe Recipe's ObjectId
    @apiParam (Query param) {String} _id_step Step's ObjectId
    @apiParam (Query param) {String} [with_files] if "true", add recipe's files
    @apiParam (Body param) {String} step Step's value to add

    @apiExample {json} Example usage:
    PUT http://127.0.0.1:5000/recipe/<_id_recipe>/step/<_id_step>
    {
        'step': <step>
    }

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.recipe_steps.success.ok',
        'codeStatus': 200,
        'data': {'_id': '5e68acb9e067528c70c75f3c', 'cooking_time': 0, 'level': 0, 'nb_people': 0, 'note': '',
                 'preparation_time': 0, 'resume': '', title': 'qa_rhr', 'slug': '', 'categories': [],
                 'steps': [{'_id': '5e68acb97b0ead079be3cef7', 'step': 'updated_step'}]}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe_steps.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an integer', 'param': 'position', 'value': 'invalid'}
    }
    """
    """ check param enrichment """
    with_files = put_recipe_step_validator.is_string_boolean(with_files=request.args.get('with_files'))[1]
    """ check param _id """
    put_recipe_step_validator.is_object_id_valid_recipe(_id=_id_recipe)
    put_recipe_step_validator.is_object_id_valid_steps(_id_recipe=_id_recipe, _id_step=_id_step)
    """ check body """
    body = put_recipe_step_factory.clean_body(data=request.json)
    put_recipe_step_validator.is_body_valid(data=body)
    """ update step """
    data = steps.update(_id_recipe=_id_recipe, _id_step=_id_step, data=body)
    """ add enrichment if needed """
    if with_files:
        data.add_enrichment_file_for_one()
    """ return response """
    return server.ServerResponse().return_response(data=data.get_result(), api="recipe_steps", code=200)


@recipe_steps_api.route('/recipe/<_id_recipe>/step/<_id_step>', methods=['DELETE'])
def delete_recipe_step(_id_recipe, _id_step):
    """
    @api {delete} /recipe/<_id_recipe>/step/<_id_step>  DeleteRecipeStep
    @apiGroup RecipeSteps
    @apiDescription Delete a recipe's step

    @apiParam (Query param) {String} _id_recipe Recipe's ObjectId
    @apiParam (Query param) {String} _id_step Step's ObjectId
    @apiParam (Query param) {String} [with_files] if "true", add recipe's files

    @apiExample {json} Example usage:
    DELETE http://127.0.0.1:5000/recipe/<_id_recipe>/step/<_id_step>

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.recipe_steps.success.ok',
        'codeStatus': 200,
        'data': {'_id': '5e68acb9e067528c70c75f3c', 'cooking_time': 0, 'level': 0, 'nb_people': 0, 'note': '',
                 'preparation_time': 0, 'resume': '', title': 'qa_rhr', 'slug': '', 'categories': [],
                 'steps': [{'_id': '5e68acb97b0ead079be3cef7', 'step': 'another_previous_step'}]}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe_steps.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an integer', 'param': 'position', 'value': 'invalid'}
    }
    """
    """ check param enrichment """
    with_files = delete_recipe_step_validator.is_string_boolean(with_files=request.args.get('with_files'))[1]
    """ check param _id """
    delete_recipe_step_validator.is_object_id_valid_recipe(_id=_id_recipe)
    delete_recipe_step_validator.is_object_id_valid_steps(_id_recipe=_id_recipe, _id_step=_id_step)
    """ clean files """
    file.clean_file_by_id_parent(_id_parent=_id_step)
    """ delete step """
    data = steps.delete(_id_recipe=_id_recipe, _id_step=_id_step)
    """ add enrichment if needed """
    if with_files:
        data.add_enrichment_file_for_one()
    """ return response """
    return server.ServerResponse().return_response(data=data.get_result(), api="recipe_steps", code=200)


@recipe_steps_api.errorhandler(400)
def validator_failed(error):
    """" abort 400 """
    return server.ServerResponse().return_response(data=error.description, api="recipe_steps", code=400)


@recipe_steps_api.errorhandler(404)
def not_found(error):
    """" abort 404 """
    return server.ServerResponse().return_response(data=error.description, api="recipe_steps", code=404)
