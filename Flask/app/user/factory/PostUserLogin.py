from flask import abort

import app.user as user_model


class Factory(object):

    def __init__(self):
        self.list_param = ["email", "password"]

    def clean_body(self, data):
        cleaned = self.remove_foreign_key(data)
        return cleaned

    def remove_foreign_key(self, data):
        clean_data = {}
        for i, j in data.items():
            if i in self.list_param:
                clean_data[i] = j
        return clean_data

    @staticmethod
    def check_password(data):
        user = user_model.UserModel.select_one_by_email(email=data["email"]).json
        authorized = user_model.UserModel.check_password(true_password=user["password"],
                                                         password_attempt=data["password"])
        if not authorized:
            detail = "Invalid email/password"
            return abort(401, description=detail)
        return True, user["_id"]

    @staticmethod
    def data_information(token):
        return {"token": token}
