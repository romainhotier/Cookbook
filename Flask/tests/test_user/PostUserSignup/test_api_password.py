import unittest
import requests

from tests import server, rep
from tests.test_user import UserTest
from tests.test_user.PostUserSignup import api


class TestPostUserSignup(unittest.TestCase):

    def setUp(self):
        """ Clean UserTest."""
        UserTest().clean()

    def test_password_without(self):
        """ BodyParameter password is missing.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_display_name: "qa_rhr_display_name",
                api.param_email: "qa_rhr@a.com"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_user = UserTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_password, msg=rep.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_user.check_doesnt_exist_by_email()

    def test_password_null(self):
        """ BodyParameter password is null.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_display_name: "qa_rhr_display_name",
                api.param_email: "qa_rhr@a.com",
                api.param_password: None}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_user = UserTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_password, msg=rep.detail_must_be_a_string,
                                   value=body[api.param_password])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_user.check_doesnt_exist_by_email()

    def test_password_empty(self):
        """ BodyParameter password is an empty string.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_display_name: "qa_rhr_display_name",
                api.param_email: "qa_rhr@a.com",
                api.param_password: ""}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_user = UserTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_password, msg=rep.detail_must_be_not_empty,
                                   value=body[api.param_password])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_user.check_doesnt_exist_by_email()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestPostUserSignup())


if __name__ == '__main__':
    unittest.main()
