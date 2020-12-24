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

    def test_display_name_without(self):
        """ BodyParameter display_name is missing.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_email: "qa_rhr@a.com",
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
        detail = api.create_detail(param=api.param_display_name, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_user.check_doesnt_exist_by_email()

    def test_display_name_none(self):
        """ BodyParameter display_name is null.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_display_name: None,
                api.param_email: "qa_rhr@a.com",
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
        detail = api.create_detail(param=api.param_display_name, msg=server.detail_must_be_a_string,
                                   value=body[api.param_display_name])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_user.check_doesnt_exist_by_email()

    def test_display_name_empty(self):
        """ BodyParameter display_name is an empty string.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_display_name: "",
                api.param_email: "qa_rhr@a.com",
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
        detail = api.create_detail(param=api.param_display_name, msg=server.detail_must_be_not_empty,
                                   value=body[api.param_display_name])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_user.check_doesnt_exist_by_email()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostUserSignup())


if __name__ == '__main__':
    unittest.main()
