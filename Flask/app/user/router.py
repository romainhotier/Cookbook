from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity

from app import utils
from app.auth import Auth
from app.user import User
import app.user.factory as factory
import app.user.validator as validator

apis = Blueprint('user', __name__, url_prefix='/user')


@apis.route('/me', methods=['GET'])
@Auth.login_required
def get_me():
    """
    @api {get} /user/me  GetMyUser
    @apiGroup User
    @apiDescription Get my user

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/user/me

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.user.success.ok',
        'codeStatus': 200,
        'data': {'_id': '5f6a0327e9fea33b5861445c', 'display_name': 'qa_rhr_display_name', 'email': 'qa@rhr.com',
                 'status': []}
    }

    @apiErrorExample {json} Error response:
    HTTPS 401
    {
        'codeMsg': 'cookbook.user.error.bad_request',
        'codeStatus': 401,
        'detail': {'msg': 'Is required', 'param': 'token'}}
    }
    """
    """ get user """
    data = User().select_me(_id=get_jwt_identity())
    """ return response """
    return utils.ResponseMaker().return_response(data=data.result, api=apis.name, http_code=200)


@apis.route('/login', methods=['POST'])
def login():
    """
    @api {post} /user/login  PostUserLogin
    @apiGroup User
    @apiDescription Log in an user

    @apiParam (Body param) {String} email User's email
    @apiParam (Body param) {String} password User's password

    @apiExample {json} Example usage:
    POST http://127.0.0.1:5000/user/login
    {
        'email': <email>,
        'password': <password>
    }

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.user.success.created',
        'codeStatus': 200,
        'data': {'token': '...'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.user.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Is required', 'param': 'email'}}
    }
    """
    api = factory.PostUserLogin.Factory()
    validation = validator.PostUserLogin.Validator()
    """ check body """
    body = api.clean_body(data=request.json)
    validation.is_body_valid(data=body)
    """ check password """
    if api.check_password(data=body):
        """ return response """
        access_token = api.create_token(email=body[api.param_email])
        return utils.ResponseMaker().return_response(data={"token": access_token}, api=apis.name, http_code=200)
    else:
        """ return response """
        return utils.ResponseMaker().return_response(data="Invalid email/password", api=apis.name, http_code=401)


@apis.route('/signup', methods=['POST'])
def signup():
    """
    @api {post} /user/signup  PostUserSignup
    @apiGroup User
    @apiDescription Create an user

    @apiParam (Body param) {String} display_name User's name in UI
    @apiParam (Body param) {String} email User's email to login
    @apiParam (Body param) {String} password User's password

    @apiExample {json} Example usage:
    POST http://127.0.0.1:5000/user/singup
    {
        'display_name': <display_name>,
        'email': <email>,
        'password': <password>
    }

    @apiSuccessExample {json} Success response:
    HTTPS 201
    {
        'codeMsg': 'cookbook.user.success.created',
        'codeStatus': 201,
        'data': {'_id': '5e5840e63ed55d9119064649', 'display_name': 'display_name_qa_rhr', 'email': 'qa@rhr.com'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.user.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Is required', 'param': 'display_name'}}
    }
    """
    api = factory.PostUserSignup.Factory()
    validation = validator.PostUserSignup.Validator()
    """ check body """
    body = api.clean_body(data=request.json)
    validation.is_body_valid(data=body)
    """ add user """
    data = User().insert(data=body)
    """ return response """
    return utils.ResponseMaker().return_response(data=data.result, api=apis.name, http_code=201)


@apis.errorhandler(400)
def validator_failed(err):
    """ Return a response for bad request.

    Parameters
    ----------
    err
        Error from Flask.

    Returns
    -------
    Any
        Server response.
    """
    return utils.ResponseMaker().return_response(data=err.description, api=apis.name, http_code=400)


@apis.errorhandler(403)
def forbidden(err):
    """ Return a response for forbidden access.

    Parameters
    ----------
    err
        Error from Flask.

    Returns
    -------
    Any
        Server response.
    """
    return utils.ResponseMaker().return_response(data=err, api=apis.name, http_code=403)


@apis.errorhandler(404)
def not_found(err):
    """ Return a response for url not found.

    Parameters
    ----------
    err
        Error from Flask.

    Returns
    -------
    Any
        Server response.
    """
    return utils.ResponseMaker().return_response(data=err, api=apis.name, http_code=404)
