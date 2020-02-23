from flask import make_response
import json

import mongo_config as mongo_conf

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
        self.detail_must_be_not_empty = "Must be not empty"
        self.detail_must_be_between = "Must be between"
        self.detail_already_exist = "Already exist"
        self.detail_url_not_found = "The requested URL was not found on the server. " \
                                    "If you entered the URL manually please check your spelling and try again."


class ServerResponse(object):

    def __init__(self):
        self.body = {"codeStatus": "",
                     "codeMsg": ""
                     }

    def format_response(self, data, api, is_mongo, code):
        """ return an HTTPResponse """
        if code == 400:
            body = self.set_response_body(api=api, http_code=code, data=None, detail=data)
            return make_response(body, code)
        elif code == 404:
            body = self.set_response_body(api=api, http_code=code, data=None, detail=data)
            return make_response(body, code)
        elif code == 405:
            body = self.set_response_body(api=api, http_code=code, data=None, detail=data)
            return make_response(body, code)
        elif code == 500:
            body = self.set_response_body(api=api, http_code=code, data=None, detail=data)
            return make_response(body, code)
        elif code == 204:
            response = make_response("", code)
            response.headers['Content-Type'] = 'application/json'
            return response
        elif code in [200, 201]:
            if is_mongo:
                body = self.set_response_body(api=api, http_code=code,
                                              data=self.get_data_result_mongo(data), detail=None)
                return make_response(body, code)
            else:
                body = self.set_response_body(api=api, http_code=code, data=self.get_data_object(data), detail=None)
                return make_response(body, code)

    def set_response_body(self, api, http_code, data, detail):
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
            if isinstance(data, str):
                self.body["data"] = json.loads(data)
            else:
                self.body["data"] = data
        if detail is not None:
            self.body["detail"] = detail

    @staticmethod
    def get_data_result_mongo(result):
        """ format data from a cursor mongodb """
        if result.count() == 1:
            """ case cursor has only one document """
            data = result[0]
            return json_format.encode(data)
        else:
            """ case cursor has only one document """
            data = []
            for r in result:
                data.append(r)
            return json_format.encode(data)

    @staticmethod
    def get_data_object(obj):
        """ format data from a ingredient object"""
        #data = obj.get_data_stringify_object_id()
        #return data
        return obj
