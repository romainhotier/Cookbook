import copy
import json
import jsonpickle
import re

from flask import make_response
from app import utils


class ResponseBody(object):

    code_msg_ok = "cookbook.xxx.success.ok"
    code_msg_created = "cookbook.xxx.success.created"
    code_msg_error_400 = "cookbook.xxx.error.bad_request"
    code_msg_error_401 = "cookbook.xxx.error.unauthorized"
    code_msg_error_403 = "cookbook.xxx.error.forbidden"
    code_msg_error_404 = "cookbook.xxx.error.not_found"
    code_msg_error_405 = "cookbook.xxx.error.method_not_allowed"
    code_msg_error_500 = "cookbook.xxx.error.internal"
    detail_has_expired = "Has expired"
    detail_was_wrong = "Was wrong"
    detail_is_required = "Is required"
    detail_forbidden = "Forbidden action - Admin only"
    detail_url_not_found = "The requested URL was not found on the server"
    detail_method_not_allowed = "The method is not allowed for the requested URL."

    def __init__(self):
        """ ResponseBody model.

        - codeStatus = Api's http code status
        - codeMsg = App section
        - data = Data (optional)
        - detail = Data for error (optional)

        Returns
        -------
        ResponseBody
        """
        self.codeStatus = None
        self.codeMsg = None
        self.data = None
        self.detail = None

    def format(self, api, http_code, **kwargs):
        """ Format the response's body.

        Parameters
        ----------
        api : str
            Api's family name.
        http_code : int
            HttpCode.
        kwargs : Any
            Can be in ['data', 'detail'].

        Returns
        -------
        ResponseBody
        """
        self.codeStatus = http_code
        self.codeMsg = self.format_code_msg(api=api, http_code=http_code)
        if "data" in kwargs:
            self.data = self.deserialize(kwargs["data"])
        if "detail" in kwargs:
            self.detail = self.format_detail(http_code=http_code, detail=kwargs["detail"])
        return self

    # use in format
    def format_code_msg(self, api, http_code):
        """ Return a code message linked with http code and api category.

        Parameters
        ----------
        api: str
            Name of the api category ("ingredient", "recipe", etc).
        http_code: int
            Http code of the response.


        Returns
        -------
        str
            A correct code_msg.
        """
        if http_code == 200:
            return self.code_msg_ok.replace("xxx", api)
        elif http_code == 201:
            return self.code_msg_created.replace("xxx", api)
        elif http_code == 400:
            return self.code_msg_error_400.replace("xxx", api)
        elif http_code == 401:
            return self.code_msg_error_401.replace("xxx", api)
        elif http_code == 403:
            return self.code_msg_error_403.replace("xxx", api)
        elif http_code == 404:
            return self.code_msg_error_404.replace("xxx", api)
        elif http_code == 405:
            return self.code_msg_error_405.replace("xxx", api)
        elif http_code == 500:
            return self.code_msg_error_500.replace("xxx", api)

    # use in format
    def format_detail(self, http_code, detail):
        """ Format the detail's body.

        Parameters
        ----------
        http_code : int
            HttpCode.
        detail : Any
            err or Validator().

        Returns
        -------
        Any
        """
        if http_code in [401, 403, 404, 405]:
            return self.format_default_detail(http_code=http_code, detail=detail)
        else:
            return self.deserialize(detail)

    # use in format_detail
    def format_default_detail(self, http_code, detail):
        """ Format the detail's body for default http code.

        Parameters
        ----------
        http_code : int
            HttpCode.
        detail : Any
            Error.

        Returns
        -------
        Json
        """
        if http_code in [405]:
            return self.detail_method_not_allowed
        elif http_code in [404]:
            return self.detail_url_not_found
        elif http_code in [401]:
            if isinstance(detail, dict):
                validation = utils.Validator(param="token", msg=self.detail_has_expired)
                return validation.__dict__
            elif re.compile("Bad Authorization header", re.IGNORECASE).search(detail) is not None:
                validation = utils.Validator(param="token", msg=self.detail_was_wrong)
                return validation.__dict__
            elif re.compile("Missing Authorization Header", re.IGNORECASE).search(detail) is not None:
                validation = utils.Validator(param="token", msg=self.detail_is_required)
                return validation.__dict__
        elif http_code in [403]:
            return self.detail_forbidden

    # use in format
    @staticmethod
    def deserialize(data):
        """ Convert to PythonObj to Json.

        Parameters
        ----------
        data : Any

        Returns
        -------
        Any
            Json
        """
        if isinstance(data, str):
            return data
        elif isinstance(data, list):
            return [json.loads(jsonpickle.encode(obj, unpicklable=False)) for obj in data]
        else:
            return json.loads(jsonpickle.encode(data, unpicklable=False))


class Response(object):
    """ Server's response.
    """

    @staticmethod
    def remove_none_data(data):
        """ Remove None value from ResponseBody.

        Parameters
        ----------
        data : Any

        Returns
        -------
        Any
        """
        result = copy.deepcopy(data.__dict__)
        for key, value in data.__dict__.items():
            if value is None:
                result.pop(key)
        return result

    def sent(self, api, http_code, **kwargs):
        """ Sent response.

        Parameters
        ----------
        api : str
            Api's family name.
        http_code : int
            HttpCode.
        kwargs : Any
            Can be in ['data', 'detail'].

        Returns
        -------
        Any
        """
        if "file" in kwargs:
            response = make_response(kwargs["data"].read(), http_code)
            response.mimetype = kwargs["data"].content_type
        else:
            body = ResponseBody().format(api, http_code, **kwargs)
            response = make_response(self.remove_none_data(body), http_code)
            response.headers['Content-Type'] = 'application/json'
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
