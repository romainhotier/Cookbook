from flask import Blueprint, make_response, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, \
    get_raw_jwt

from flask import current_app as app
import datetime

import utils
import app.user.factory as factory
import app.user.validator as validator
import app.user as user_model

api = Blueprint('user', __name__, url_prefix='/user')


@api.route('/signup', methods=['POST'])
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
    body = factory.FactoryPostUserSignup.clean_body(data=request.json)
    validator.ValidatorPostUserSignup.is_body_valid(data=body)
    """ add user """
    data = user_model.UserModel.insert(data=body)
    """ return response """
    return utils.Server.return_response(data=data.json, api=api.name, code=201)


@api.route('/login', methods=['POST'])
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
    body = factory.FactoryPostUserLogin.clean_body(data=request.json)
    validator.ValidatorPostUserLogin.is_body_valid(data=body)
    """ check password """
    user_id = factory.FactoryPostUserLogin.check_password(data=body)[1]
    """ create token """
    expires = datetime.timedelta(hours=app.config["EXPIRATION_TOKEN"])
    access_token = create_access_token(identity=str(user_id), expires_delta=expires)
    data = factory.FactoryPostUserLogin.data_information(token=access_token)
    """ return response """
    return utils.Server.return_response(data=data, api=api.name, code=200)


@api.errorhandler(400)
def validator_failed(error):
    """" abort 400 """
    return utils.Server.return_response(data=error.description, api=api.name, code=400)


@api.errorhandler(401)
def unauthorized(error):
    """" abort 401 """
    return utils.Server.return_response(data=error.description, api=api.name, code=401)


@api.errorhandler(404)
def not_found(error):
    """" abort 404 """
    return utils.Server.return_response(data=error.description, api=api.name, code=404)
