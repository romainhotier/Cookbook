from flask import make_response
import re

import logging

logFormatter = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(format=logFormatter, level=logging.INFO)


class Server(object):

    def __init__(self):
        """ All server settings, message, etc...
        """
        self.logger = logging.getLogger(__name__)
        self.secure = 'http'
        self.ip = 'localhost'
        self.port = '5000'
        self.main_url = "{0}://{1}:{2}".format(self.secure, self.ip, self.port)
        self.rep_code_msg_ok = "cookbook.xxx.success.ok"
        self.rep_code_msg_created = "cookbook.xxx.success.created"
        self.rep_code_msg_error_400 = "cookbook.xxx.error.bad_request"
        self.rep_code_msg_error_401 = "cookbook.xxx.error.unauthorized"
        self.rep_code_msg_error_403 = "cookbook.xxx.error.forbidden"
        self.rep_code_msg_error_404 = "cookbook.xxx.error.not_found"
        self.rep_code_msg_error_405 = "cookbook.xxx.error.method_not_allowed"
        self.rep_code_msg_error_500 = "cookbook.xxx.error.internal"
        self.detail_has_expired = "Has expired"
        self.detail_was_wrong = "Was wrong"
        self.detail_is_required = "Is required"
        self.detail_forbidden = "Forbidden action - Admin only"
        self.detail_must_be_an_object_id = "Must be an ObjectId"
        self.detail_must_be_a_string = "Must be a string"
        self.detail_must_be_an_integer = "Must be an integer"
        self.detail_must_be_a_float = "Must be a float"
        self.detail_must_be_an_array = "Must be an array"
        self.detail_must_be_an_array_of_string = "Must be an array of string"
        self.detail_must_be_an_array_of_object = "Must be an array of object"
        self.detail_must_be_an_object = "Must be an object"
        self.detail_must_be_an_object_or_string = "Must be an object or a string"
        self.detail_must_be_a_boolean = "Must be a boolean"
        self.detail_must_be_not_empty = "Must be not empty"
        self.detail_must_be_between = "Must be between"
        self.detail_must_be_in = "Must be in"
        self.detail_must_contain_at_least_one_key = "Must contain at least one key"
        self.detail_already_exist = "Already exist"
        self.detail_doesnot_exist = "Doesn't exist"
        self.detail_must_be_unique = "Must be unique"
        self.detail_url_not_found = "The requested URL was not found on the server"
        self.detail_method_not_allowed = "The method is not allowed for the requested URL."

    def return_response(self, data, api, http_code, **kwargs):
        """ Return a Server response.

        Parameters
        ----------
        data:
            Information asked, errors, etc.
        api: str
            Name of the api category ("ingredient", "recipe", etc).
        http_code: int
            Http_code for the response.
        kwargs: optional
            Detail: If an optional detail is needed.

        Returns
        -------
        Any
            Server response.
        """
        if "file" in kwargs:
            response = make_response(data.read(), http_code)
            response.mimetype = data.content_type
        else:
            body = self.format_body(data, api, http_code, **kwargs)
            response = make_response(body, http_code)
            response.headers['Content-Type'] = 'application/json'
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    # use in return response
    def format_body(self, data, api, http_code, **kwargs):
        """ Make a json response.

        Parameters
        ----------
        data
            Information asked, errors, etc.
        api: str
            Name of the api category ("ingredient", "recipe", etc).
        http_code: int
            Http_code for the response.
        kwargs: optional
            Detail: If a optional detail is needed.

        Returns
        -------
        Dict
            Server body response.
        """
        body = {"codeStatus": http_code, "codeMsg": self.format_code_msg(http_code=http_code, api=api)}
        if http_code in [400, 500]:
            body["detail"] = data
        elif http_code in [405]:
            body["detail"] = self.detail_method_not_allowed
        elif http_code in [404]:
            body["detail"] = self.detail_url_not_found
        elif http_code in [401]:
            if isinstance(data, dict):
                body["detail"] = {'msg': self.detail_has_expired, 'param': 'token'}
            elif re.compile("Bad Authorization header", re.IGNORECASE).search(data) is not None:
                body["detail"] = {'msg': self.detail_was_wrong, 'param': 'token'}
            elif re.compile("Missing Authorization Header", re.IGNORECASE).search(data) is not None:
                body["detail"] = {'msg': self.detail_is_required, 'param': 'token'}
        elif http_code in [403]:
            body["detail"] = self.detail_forbidden
        elif http_code == 204:
            body = ""
        elif http_code in [200, 201]:
            body["data"] = data
            if "detail" in kwargs:
                body["detail"] = kwargs["detail"]
        return body

    # use in format_body
    def format_code_msg(self, http_code, api):
        """ Return a code message linked with http code and api category.

        Parameters
        ----------
        http_code: int
            Http code of the response.
        api: str
            Name of the api category ("ingredient", "recipe", etc).

        Returns
        -------
        str
            A correct code_msg.
        """
        if http_code == 200:
            return self.rep_code_msg_ok.replace("xxx", api)
        elif http_code == 201:
            return self.rep_code_msg_created.replace("xxx", api)
        elif http_code == 400:
            return self.rep_code_msg_error_400.replace("xxx", api)
        elif http_code == 401:
            return self.rep_code_msg_error_401.replace("xxx", api)
        elif http_code == 403:
            return self.rep_code_msg_error_403.replace("xxx", api)
        elif http_code == 404:
            return self.rep_code_msg_error_404.replace("xxx", api)
        elif http_code == 405:
            return self.rep_code_msg_error_405.replace("xxx", api)
        elif http_code == 500:
            return self.rep_code_msg_error_500.replace("xxx", api)

    @staticmethod
    def format_detail(param, msg, **kwargs):
        """ Return detail object.

        Parameters
        ----------
        param: str
            Name of the parameter.
        msg: str
            Message to explain the issue.
        kwargs: optional
            Value: Actual defect value.

        Returns
        -------
        dict
            All information about an issue.
        """
        detail = {"param": param, "msg": msg}
        if "value" in kwargs:
            detail["value"] = kwargs["value"]
        return detail

    @staticmethod
    def get_backend_options(args):
        """ Catch command line options.

        Parameters
        ----------
        args: list
            All arguments in the command line.
            1st can be ["test", "dev", "prod"].

        Returns
        -------
        dict
            Set env / debug / testing to update server config.
        """
        try:
            mode = args[1]
            if mode == "test":
                return {"env": "development", "debug": True, "testing": True}
            elif mode == "dev":
                return {"env": "development", "debug": True, "testing": False}
            elif mode == "prod":
                return {"env": "production", "debug": False, "testing": False}
            else:
                return {"env": "production", "debug": False, "testing": False}
        except IndexError:
            return {"env": "production", "debug": False, "testing": False}
