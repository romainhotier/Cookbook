from flask import Blueprint, request

from server import factory as factory
import app.recipe.steps.model as steps_model
import app.file.file.model as file_model
import app.steps.steps.validator.PostStep as validator_PostStep
import app.steps.steps.factory.PostStep as factory_PostStep

steps_api = Blueprint('steps_api', __name__)

steps = steps_model.Steps()
file = file_model.File()

post_step_validator = validator_PostStep.Validator()
post_step_factory = factory_PostStep.Factory()


@steps_api.route('/step', methods=['POST'])
def post_step():
    """
    @api {post} /step PostStep
    @apiGroup Steps
    @apiDescription Return en step to add in param 'steps' for PostRecipe

    @apiParam (Body param) {String} step Step's value

    @apiExample {json} Example usage:
    POST http://127.0.0.1:5000/step
    {
        'step': <step>,
    }

    @apiSuccessExample {json} Success response:
    HTTPS 201
    {
        'codeMsg': 'cookbook.step.success.created',
        'codeStatus': 201,
        'data': {'_id': '5e68acb9e067528c70c75f3c', 'step': ''}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.step.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be not empty', 'param': 'step', 'value': ''}
    }
    """
    """ check body """
    body = post_step_factory.clean_body(data=request.json)
    post_step_validator.is_body_valid(data=body)
    """ insert step """
    data = post_step_factory.create_step(data=body)
    """ return response """
    return factory.ServerResponse().return_response(data=data, api="step", code=201)


@steps_api.errorhandler(400)
def validator_failed(error):
    """" abort 400 """
    return factory.ServerResponse().return_response(data=error.description, api="step", code=400)


@steps_api.errorhandler(404)
def not_found(error):
    """" abort 404 """
    return factory.ServerResponse().return_response(data=error.description, api="step", code=404)
