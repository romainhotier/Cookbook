import unittest
import requests

import utils
import tests.user.PostUserLogin.api as api
import tests.user.model as user_model

server = utils.Server()
api = api.PostUserLogin()
user = user_model.UserTest()


class PostUserLogin(unittest.TestCase):

    def setUp(self):
        """ Clean UserTest."""
        user.clean()

    def test_api_ok(self):
        """ Default case.

        Return
            200 - Get Token.
        """
        """ env """
        tc_user = user_model.UserTest().insert()
        """ param """
        body = {api.param_email: tc_user.email,
                api.param_password: tc_user.password}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertRegex(response_body["data"]['token'], api.data_regex)
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_api_ok_more_param(self):
        """ Default case with more parameters.

        Return
            200 - Get Token.
        """
        """ env """
        tc_user = user_model.UserTest().insert()
        """ param """
        body = {api.param_email: tc_user.email,
                api.param_password: tc_user.password,
                "invalid": "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertRegex(response_body["data"]['token'], api.data_regex)
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_api_url_not_found(self):
        """ Wrong url.

        Return
            404 - url not found.
        """
        """ env """
        tc_user = user_model.UserTest().insert()
        """ param """
        body = {api.param_email: tc_user.email,
                api.param_password: tc_user.password}
        """ call api """
        url = server.main_url + "/x" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostUserLogin())


if __name__ == '__main__':
    unittest.main()
