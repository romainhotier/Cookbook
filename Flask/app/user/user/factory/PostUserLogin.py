from flask import abort

import app.user.user.model as user_model

list_param_user = user_model.User().list_param
list_param_user.remove("display_name")


class Factory(object):

    def clean_body(self, data):
        cleaned = self.remove_foreign_key(data)
        return cleaned

    @staticmethod
    def remove_foreign_key(data):
        clean_data = {}
        for i, j in data.items():
            if i in list_param_user:
                clean_data[i] = j
        return clean_data

    @staticmethod
    def check_password(data):
        user = user_model.User().select_one_by_email(email=data["email"])
        authorized = user_model.User().check_password(true_password=user["password"], password_attempt=data["password"])
        if not authorized:
            detail = "Invalid email/password"
            return abort(401, description=detail)
        return True, user["_id"]

    @staticmethod
    def data_information(token):
        return {"token": token}
