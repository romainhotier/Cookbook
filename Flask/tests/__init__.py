""" Server and Response """

import jsonschema


class Server(object):

    def __init__(self):
        """ Server to be tested
        """
        self.secure = 'http'
        self.ip = 'localhost'
        self.port = '5000'
        self.main_url = "{0}://{1}:{2}".format(self.secure, self.ip, self.port)


class Response(object):

    def __init__(self):
        """ Response settings """
        self.code_msg_ok = "cookbook.xxx.success.ok"
        self.code_msg_created = "cookbook.xxx.success.created"
        self.code_msg_error_400 = "cookbook.xxx.error.bad_request"
        self.code_msg_error_401 = "cookbook.xxx.error.unauthorized"
        self.code_msg_error_403 = "cookbook.xxx.error.forbidden"
        self.code_msg_error_404 = "cookbook.xxx.error.not_found"
        self.code_msg_error_405 = "cookbook.xxx.error.method_not_allowed"
        self.code_msg_error_500 = "cookbook.xxx.error.internal"
        self.detail_has_expired = "Has expired"
        self.detail_was_wrong = "Was wrong"
        self.detail_is_required = "Is required"
        self.detail_forbidden = "Forbidden action - Admin only"
        self.detail_must_be_an_object_id = "Must be an ObjectId"
        self.detail_must_be_a_string = "Must be a string"
        self.detail_must_be_a_path = "Must be a path with '/'"
        self.detail_must_be_an_integer = "Must be an integer"
        self.detail_must_be_a_float = "Must be a float"
        self.detail_must_be_an_array = "Must be an array"
        self.detail_must_be_an_array_of_string = "Must be an array of string"
        self.detail_must_be_an_array_of_object = "Must be an array of object"
        self.detail_must_be_an_object = "Must be an object"
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
    def check_not_present(value, response):
        """ Check if data/detail is not present in Server's response.

        Parameters
        ----------
        value : str
            Tested value.
        response : dict
            Server's response.

        Returns
        -------
        bool
        """
        if value in response:
            return False
        else:
            return True

    @staticmethod
    def json_schema_check(data, schema):
        """ check schema.

        Parameters
        ----------
        data : dict
            Server's response.
        schema : dict
            Schema.

        Returns
        -------
        dict
            Result and err if exist.
        """
        try:
            jsonschema.validate(instance=data, schema=schema)
            return {"result": True, "error": None}
        except jsonschema.exceptions.ValidationError as err:
            return {"result": False, "error": err}


server = Server()
rep = Response()
