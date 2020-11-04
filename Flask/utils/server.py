from flask import make_response

import logging

logFormatter = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(format=logFormatter, level=logging.INFO)


class Server(object):

    def __init__(self):
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
        self.detail_must_be_an_array = "Must be an array"
        self.detail_must_be_an_object = "Must be an object"
        self.detail_must_be_a_boolean = "Must be a boolean"
        self.detail_must_be_not_empty = "Must be not empty"
        self.detail_must_be_between = "Must be between"
        self.detail_must_be_in = "Must be in"
        self.detail_must_contain_at_least_one_key = "Must contain at least one key"
        self.detail_already_exist = "Already exist"
        self.detail_doesnot_exist = "Doesn't exist"
        self.detail_url_not_found = "The requested URL was not found on the server. " \
                                    "If you entered the URL manually please check your spelling and try again."
        self.detail_method_not_allowed = "The method is not allowed for the requested URL."

    def return_response(self, data, api, code, **optional):
        """ return an HTTPResponse """
        if code in [400, 404, 405, 500]:
            body = self.format_body(api=api, http_code=code, data=None, detail=data)
            return self.format_response(body=body, code=code)
        elif code in [401]:
            body = self.format_body(api=api, http_code=code, data=None, detail=self.format_detail_token(t=data))
            return self.format_response(body=body, code=code)
        elif code in [403]:
            body = self.format_body(api=api, http_code=code, data=None, detail=self.detail_forbidden)
            return self.format_response(body=body, code=code)
        elif code == 204:
            body = ""
            return self.format_response(body=body, code=code)
        elif code in [200, 201]:
            if "detail" in optional.keys():
                body = self.format_body(api=api, http_code=code, data=data, detail=optional["detail"])
                return self.format_response(body=body, code=code)
            else:
                body = self.format_body(api=api, http_code=code, data=data, detail=None)
                return self.format_response(body=body, code=code)

    def format_response(self, body, code):
        response = self.format_headers(make_response(body, code))
        return response

    @staticmethod
    def format_headers(response):
        response.headers['Content-Type'] = 'application/json'
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    def format_body(self, api, http_code, data, detail):
        body = {"codeStatus": http_code, "codeMsg": self.select_code_msg(http_code=http_code, api_category=api)}
        if data is not None:
            body["data"] = data
        if detail is not None:
            body["detail"] = detail
        return body

    def select_code_msg(self, http_code, api_category):
        """ return correct code msg linked with a htttp_code """
        if http_code == 200:
            return self.rep_code_msg_ok.replace("xxx", api_category)
        elif http_code == 201:
            return self.rep_code_msg_created.replace("xxx", api_category)
        elif http_code == 400:
            return self.rep_code_msg_error_400.replace("xxx", api_category)
        elif http_code == 401:
            return self.rep_code_msg_error_401.replace("xxx", api_category)
        elif http_code == 403:
            return self.rep_code_msg_error_403.replace("xxx", api_category)
        elif http_code == 404:
            return self.rep_code_msg_error_404.replace("xxx", api_category)
        elif http_code == 405:
            return self.rep_code_msg_error_405.replace("xxx", api_category)
        elif http_code == 500:
            return self.rep_code_msg_error_500.replace("xxx", api_category)

    def format_detail_token(self, t):
        if t == "expired":
            return {'msg': self.detail_has_expired, 'param': 'token'}
        elif t == "invalid":
            return {'msg': self.detail_was_wrong, 'param': 'token'}
        elif t == "missing":
            return {'msg': self.detail_is_required, 'param': 'token'}

    @staticmethod
    def get_backend_options(args):
        for arg in args:
            if arg in ["test", "dev", "prod"]:
                if arg == "test":
                    return {"env": "development", "debug": True, "testing": True}
                elif arg == "dev":
                    return {"env": "development", "debug": True, "testing": False}
                elif arg == "prod":
                    return {"env": "production", "debug": False, "testing": False}
            else:
                return {"env": "production", "debug": False, "testing": False}
