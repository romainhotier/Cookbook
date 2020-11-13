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
        user.clean()

    def test_0_api_ok(self):
        tc_user = user_model.UserTest().insert()
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

    def test_0_api_ok_more_param(self):
        tc_user = user_model.UserTest().insert()
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

    def test_1_url_not_found(self):
        tc_user = user_model.UserTest().insert()
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

    def test_2_email_without(self):
        tc_user = user_model.UserTest().insert()
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

    def test_2_email_null(self):
        tc_user = user_model.UserTest().insert()
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

    def test_2_email_empty(self):
        tc_user = user_model.UserTest().insert()
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

    def test_3_password_without(self):
        tc_user = user_model.UserTest().insert()
        body = {api.param_email: tc_user.email}
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
        detail = api.create_detail(param=api.param_password, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)

    def test_3_password_null(self):
        tc_user = user_model.UserTest().insert()
        body = {api.param_email: tc_user.email,
                api.param_password: None}
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
        detail = api.create_detail(param=api.param_password, msg=server.detail_must_be_a_string,
                                   value=body[api.param_password])
        self.assertEqual(response_body["detail"], detail)

    def test_3_password_empty(self):
        tc_user = user_model.UserTest().insert()
        body = {api.param_email: tc_user.email,
                api.param_password: ""}
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
        detail = api.create_detail(param=api.param_password, msg=server.detail_must_be_not_empty,
                                   value=body[api.param_password])
        self.assertEqual(response_body["detail"], detail)

    def tearDown(self):
        user.clean()

    @classmethod
    def tearDownClass(cls):
        user.clean()


if __name__ == '__main__':
    unittest.main()
