import unittest
import requests

import utils
import tests.test_user.PostUserLogin.api as api
import tests.test_user.model as user_model

server = utils.Server()
api = api.PostUserLogin()
user = user_model.UserTest()


class PostUserLogin(unittest.TestCase):

    def setUp(self):
        """ Clean UserTest."""
        user.clean()

    def test_email_without(self):
        """ BodyParameter email is missing.

        Return
            400 - Bad request.
        """
        """ env """
        tc_user = user_model.UserTest().insert()
        """ param """
        body = {api.param_password: tc_user.password}
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
        detail = api.create_detail(param=api.param_email, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)

    def test_email_null(self):
        """ BodyParameter email is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_user = user_model.UserTest().insert()
        """ param """
        body = {api.param_email: None,
                api.param_password: tc_user.password}
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
        detail = api.create_detail(param=api.param_email, msg=server.detail_must_be_a_string,
                                   value=body[api.param_email])
        self.assertEqual(response_body["detail"], detail)

    def test_email_empty(self):
        """ BodyParameter email is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_user = user_model.UserTest().insert()
        """ param """
        body = {api.param_email: "",
                api.param_password: tc_user.password}
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
        detail = api.create_detail(param=api.param_email, msg=server.detail_must_be_not_empty,
                                   value=body[api.param_email])
        self.assertEqual(response_body["detail"], detail)

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostUserLogin())


if __name__ == '__main__':
    unittest.main()
