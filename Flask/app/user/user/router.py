from flask import Blueprint, make_response, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, \
    get_raw_jwt

from flask import current_app as app
import datetime

import server.server as server
import app.user.user.model as user_model

import app.user.user.factory.PostUserSignup as factory_PostUserSignup
import app.user.user.validator.PostUserSignup as validator_PostUserSignup
import app.user.user.factory.PostUserLogin as factory_PostUserLogin
import app.user.user.validator.PostUserLogin as validator_PostUserLogin

user_api = Blueprint('user_api', __name__)

user = user_model.User()
post_user_signup_factory = factory_PostUserSignup.Factory()
post_user_signup_validator = validator_PostUserSignup.Validator()
post_user_login_factory = factory_PostUserLogin.Factory()
post_user_login_validator = validator_PostUserLogin.Validator()


@user_api.route('/user/signup', methods=['POST'])
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
    """ check body """
    body = post_user_signup_factory.clean_body(data=request.json)
    post_user_signup_validator.is_body_valid(data=body)
    """ add user """
    data = user.insert(data=body)
    """ return response """
    return server.ServerResponse().return_response(data=data.get_result(), api="user", code=201)


@user_api.route('/user/login', methods=['POST'])
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
    """ check body """
    body = post_user_login_factory.clean_body(data=request.json)
    post_user_login_validator.is_body_valid(data=body)
    """ check password """
    user_id = post_user_login_factory.check_password(data=body)[1]
    """ create token """
    expires = datetime.timedelta(hours=app.config["EXPIRATION_TOKEN"])
    access_token = create_access_token(identity=str(user_id), expires_delta=expires)
    data = post_user_login_factory.data_information(token=access_token)
    """ return response """
    return server.ServerResponse().return_response(data=data, api="user", code=200)


@user_api.errorhandler(400)
def validator_failed(error):
    """" abort 400 """
    return server.ServerResponse().return_response(data=error.description, api="user", code=400)


@user_api.errorhandler(401)
def unauthorized(error):
    """" abort 401 """
    return server.ServerResponse().return_response(data=error.description, api="user", code=401)


@user_api.errorhandler(404)
def not_found(error):
    """" abort 404 """
    return server.ServerResponse().return_response(data=error.description, api="user", code=404)
