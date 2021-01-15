import unittest
import requests

from tests import server, rep
from tests.test_user import UserTest
from tests.test_user.PostUserLogin import api


class TestPostUserLogin(unittest.TestCase):

    def setUp(self):
        """ Clean UserTest."""
        UserTest().clean()

    def test_email_without(self):
        """ BodyParameter email is missing.

        Return
            400 - Bad request.
        """
        """ env """
        tc_user = UserTest().insert()
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
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_email, msg=rep.detail_is_required)
        self.assertEqual(response_body["detail"], detail)

    def test_email_null(self):
        """ BodyParameter email is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_user = UserTest().insert()
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
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_email, msg=rep.detail_must_be_a_string, value=body[api.param_email])
        self.assertEqual(response_body["detail"], detail)

    def test_email_empty(self):
        """ BodyParameter email is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_user = UserTest().insert()
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
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_email, msg=rep.detail_must_be_not_empty, value=body[api.param_email])
        self.assertEqual(response_body["detail"], detail)

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestPostUserLogin())


if __name__ == '__main__':
    unittest.main()
