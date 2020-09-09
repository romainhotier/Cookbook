import unittest
import requests

import utils
import tests.user.PostUserSignup.api as api
import tests.user.model as user_model

server = utils.Server
api = api.PostUserSignup()
user = user_model.UserTest()


class PostUserSignup(unittest.TestCase):

    def setUp(self):
        user.clean()

    def test_0_api_ok(self):
        body = {api.param_display_name: "qa_rhr_display_name",
                api.param_email: "qa_rhr@a.com",
                api.param_password: "admin"}
        tc_user = user_model.UserTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_user)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ refacto """
        tc_user.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_0_api_ok_more_param(self):
        body = {api.param_display_name: "qa_rhr_display_name",
                api.param_email: "qa_rhr@a.com",
                api.param_password: "admin",
                "invalid": "invalid"}
        tc_user = user_model.UserTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_user)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ refacto """
        tc_user.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_1_url_not_found(self):
        body = {api.param_display_name: "qa_rhr_display_name",
                api.param_email: "qa_rhr@a.com",
                api.param_password: "admin"}
        tc_user = user_model.UserTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url + "x"
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        tc_user.select_nok_by_email()

    def test_2_display_name_without(self):
        body = {api.param_email: "qa_rhr@a.com",
                api.param_password: "admin"}
        tc_user = user_model.UserTest().custom(body)
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
        detail = api.create_detail(param=api.param_display_name, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        tc_user.select_nok_by_email()

    def test_2_display_name_none(self):
        body = {api.param_display_name: None,
                api.param_email: "qa_rhr@a.com",
                api.param_password: "admin"}
        tc_user = user_model.UserTest().custom(body)
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
        detail = api.create_detail(param=api.param_display_name, msg=server.detail_must_be_a_string,
                                   value=body[api.param_display_name])
        self.assertEqual(response_body["detail"], detail)
        tc_user.select_nok_by_email()

    def test_2_display_name_empty(self):
        body = {api.param_display_name: "",
                api.param_email: "qa_rhr@a.com",
                api.param_password: "admin"}
        tc_user = user_model.UserTest().custom(body)
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
        detail = api.create_detail(param=api.param_display_name, msg=server.detail_must_be_not_empty,
                                   value=body[api.param_display_name])
        self.assertEqual(response_body["detail"], detail)
        tc_user.select_nok_by_email()

    def test_3_email_without(self):
        body = {api.param_display_name: "qa_rhr_display_name",
                api.param_password: "admin"}
        tc_user = user_model.UserTest().custom(body)
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
        tc_user.select_nok_by_display_name()

    def test_3_email_null(self):
        body = {api.param_display_name: "qa_rhr_display_name",
                api.param_email: None,
                api.param_password: "admin"}
        tc_user = user_model.UserTest().custom(body)
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
        tc_user.select_nok_by_display_name()

    def test_3_email_empty(self):
        body = {api.param_display_name: "qa_rhr_display_name",
                api.param_email: "",
                api.param_password: "admin"}
        tc_user = user_model.UserTest().custom(body)
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
        tc_user.select_nok_by_display_name()

    def test_4_password_without(self):
        body = {api.param_display_name: "qa_rhr_display_name",
                api.param_email: "qa_rhr@a.com"}
        tc_user = user_model.UserTest().custom(body)
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
        tc_user.select_nok_by_email()

    def test_4_password_null(self):
        body = {api.param_display_name: "qa_rhr_display_name",
                api.param_email: "qa_rhr@a.com",
                api.param_password: None}
        tc_user = user_model.UserTest().custom(body)
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
        tc_user.select_nok_by_email()

    def test_4_password_empty(self):
        body = {api.param_display_name: "qa_rhr_display_name",
                api.param_email: "qa_rhr@a.com",
                api.param_password: ""}
        tc_user = user_model.UserTest().custom(body)
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
        tc_user.select_nok_by_email()

    def test_5_email_already_exist(self):
        tc_user = user_model.UserTest().insert()
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
        tc_user.select_ok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostUserSignup())


if __name__ == '__main__':
    unittest.main()
