import unittest
import requests

from tests import server, rep
from tests.test_user import UserTest
from tests.test_user.PostUserSignup import api


class TestPostUserSignup(unittest.TestCase):

    def setUp(self):
        """ Clean UserTest."""
        UserTest().clean()

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
        tc_user = UserTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = rep.json_schema_check(data=response_body["data"], schema=api.create_schema(user=tc_user))
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))
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
        tc_user = UserTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = rep.json_schema_check(data=response_body["data"], schema=api.create_schema(user=tc_user))
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))
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
        tc_user = UserTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        self.assertEqual(response_body["detail"], rep.detail_url_not_found)
        """ check """
        tc_user.check_doesnt_exist_by_email()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestPostUserSignup())


if __name__ == '__main__':
    unittest.main()
