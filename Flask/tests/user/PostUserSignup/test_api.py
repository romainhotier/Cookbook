import unittest
import requests

import utils
import tests.user.PostUserSignup.api as api
import tests.user.model as user_model

server = utils.Server()
api = api.PostUserSignup()
user = user_model.UserTest()


class PostUserSignup(unittest.TestCase):

    def setUp(self):
        """ Clean UserTest."""
        user.clean()

    def test_api_ok(self):
        """ Default case.

        Return
            201 - Inserted User.
        """
        """ param """
        body = {api.param_display_name: "qa_rhr_display_name",
                api.param_email: "qa_rhr@a.com",
                api.param_password: "admin"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_user = user_model.UserTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_user)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_user.custom_id_from_body(data=response_body).check_bdd_data()

    def test_api_ok_more_param(self):
        """ Default case with more parameters.

        Return
            201 - Inserted User.
        """
        """ param """
        body = {api.param_display_name: "qa_rhr_display_name",
                api.param_email: "qa_rhr@a.com",
                api.param_password: "admin",
                "invalid": "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_user = user_model.UserTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_user)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_user.custom_id_from_body(data=response_body).check_bdd_data()

    def test_api_url_not_found(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ param """
        body = {api.param_display_name: "qa_rhr_display_name",
                api.param_email: "qa_rhr@a.com",
                api.param_password: "admin"}
        """ call api """
        url = server.main_url + "/" + api.url + "x"
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_user = user_model.UserTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        """ check """
        tc_user.check_doesnt_exist_by_email()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostUserSignup())


if __name__ == '__main__':
    unittest.main()
