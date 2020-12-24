import unittest
import requests

import utils
import tests.test_user.PostUserSignup.api as api
import tests.test_user.model as user_model

server = utils.Server()
api = api.PostUserSignup()
user = user_model.UserTest()


class PostUserSignup(unittest.TestCase):

    def setUp(self):
        """ Clean UserTest."""
        user.clean()

    def test_email_without(self):
        """ BodyParameter email is missing.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_display_name: "qa_rhr_display_name",
                api.param_password: "admin"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_user = user_model.UserTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_email, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_user.check_doesnt_exist_by_display_name()

    def test_email_null(self):
        """ BodyParameter email is null.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_display_name: "qa_rhr_display_name",
                api.param_email: None,
                api.param_password: "admin"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_user = user_model.UserTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_email, msg=server.detail_must_be_a_string,
                                   value=body[api.param_email])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_user.check_doesnt_exist_by_display_name()

    def test_email_empty(self):
        """ BodyParameter email is an empty string.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_display_name: "qa_rhr_display_name",
                api.param_email: "",
                api.param_password: "admin"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_user = user_model.UserTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_email, msg=server.detail_must_be_not_empty,
                                   value=body[api.param_email])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_user.check_doesnt_exist_by_display_name()

    def test_email_already_exist(self):
        """ BodyParameter email already exist.

        Return
            400 - Bad request.
        """
        """ env """
        tc_user = user_model.UserTest().insert()
        """ param """
        body = {api.param_display_name: "qa_rhr_display_name_2",
                api.param_email: tc_user.email,
                api.param_password: "admin2"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_email, msg=server.detail_already_exist, value=body[api.param_email])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_user.check_bdd_data()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostUserSignup())


if __name__ == '__main__':
    unittest.main()
