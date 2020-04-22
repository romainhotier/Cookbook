import os
import platform
from functools import wraps
from flask_jwt_extended import verify_jwt_in_request


class Auth(object):

    def __init__(self):
        self.path_config = self.get_path()
        self.auth_needed = self.is_auth_needed()

    def display(self):
        print(self.__dict__)

    def login_required(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if self.auth_needed:
                verify_jwt_in_request()
            return f(*args, **kwargs)
        return wrapper

    @staticmethod
    def get_path():
        current_path = os.getcwd()
        if platform.system() == "Windows":
            path = current_path + "\\config.py"
            return path
        elif platform.system() in ["Linux", "Darwin"]:
            path = current_path + "/config.py"
            return path

    def is_auth_needed(self):
        with open(self.path_config, "r") as f:
            for line in f:
                a = line.rstrip('\n').split(" = ")
                k = a[0]
                v = a[1]
                if k == "ENV":
                    if v == '"testing"':
                        return False
                    else:
                        return True
