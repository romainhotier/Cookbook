import unittest
import requests

import utils
import tests.user.PostUserLogin.api as api
import tests.user.model as user_model

server = utils.Server
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
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertRegex(response_body[api.rep_data]['token'], api.data_regex)

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
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertRegex(response_body[api.rep_data]['token'], api.data_regex)

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
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)

    def test_2_email_without(self):
        tc_user = user_model.UserTest().insert()
        body = {api.param_password: tc_user.password}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_email, server.detail_is_required, "missing")
        self.assertEqual(response_body[api.rep_detail], detail)

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
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_email, server.detail_must_be_a_string, body[api.param_email])
        self.assertEqual(response_body[api.rep_detail], detail)

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
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_email, server.detail_must_be_not_empty, body[api.param_email])
        self.assertEqual(response_body[api.rep_detail], detail)

    def test_3_password_without(self):
        tc_user = user_model.UserTest().insert()
        body = {api.param_email: tc_user.email}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_password, server.detail_is_required, "missing")
        self.assertEqual(response_body[api.rep_detail], detail)

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
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_password, server.detail_must_be_a_string, body[api.param_password])
        self.assertEqual(response_body[api.rep_detail], detail)

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
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_password, server.detail_must_be_not_empty, body[api.param_password])
        self.assertEqual(response_body[api.rep_detail], detail)

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostUserLogin())


if __name__ == '__main__':
    unittest.main()
