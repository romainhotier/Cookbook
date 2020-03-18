from flask import make_response
import json

from server import mongo_config as mongo_conf

json_format = mongo_conf.JSONEncoder()


class Server(object):

    def __init__(self):
        self.secure = 'http'
        self.ip = '127.0.0.1'
        self.port = '5000'
        self.main_url = "{0}://{1}:{2}".format(self.secure, self.ip, self.port)
        self.rep_code_msg_ok = "cookbook.xxx.success.ok"
        self.rep_code_msg_created = "cookbook.xxx.success.created"
        self.rep_code_msg_error_400 = "cookbook.xxx.error.bad_request"
        self.rep_code_msg_error_404 = "cookbook.xxx.error.not_found"
        self.rep_code_msg_error_405 = "The method is not allowed for the requested URL."
        self.detail_is_required = "Is required"
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


class ServerResponse(object):

    def __init__(self):
        self.body = {"codeStatus": "",
                     "codeMsg": ""
                     }

    def return_response(self, data, api, code, **optional):
        """ return an HTTPResponse """
        if code in [400, 404, 405, 500]:
            body = self.format_body(api=api, http_code=code, data=None, detail=data)
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
        self.body["codeStatus"] = http_code
        self.body["codeMsg"] = self.select_code_msg(http_code=http_code, api_category=api)
        self.add_data_detail(data, detail)
        return self.body

    @staticmethod
    def select_code_msg(http_code, api_category):
        """ return correct code msg linked with a htttp_code """
        if http_code == 200:
            return "cookbook.{}.success.ok".format(api_category)
        elif http_code == 201:
            return "cookbook.{}.success.created".format(api_category)
        elif http_code == 400:
            return "cookbook.{}.error.bad_request".format(api_category)
        elif http_code == 404:
            return "cookbook.{}.error.not_found".format(api_category)
        elif http_code == 405:
            return "cookbook.{}.error.method_not_allowed".format(api_category)
        elif http_code == 500:
            return "cookbook.{}.error.internal_error".format(api_category)

    def add_data_detail(self, data, detail):
        """ add data or detail """
        if data is not None:
            self.body["data"] = data
        if detail is not None:
            self.body["detail"] = detail
