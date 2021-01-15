import unittest
import requests
import time

from tests import server, rep
from tests.test_user import UserTest
from tests.test_user.GetMe import api

auth = UserTest()


class TestGetMe(unittest.TestCase):

    @auth.login
    def setUp(self, **kwargs):
        """ Login and store info."""
        self.user = kwargs["user"]
        self.headers = kwargs["headers"]

    def test_api_ok(self):
        """ Default case.

        Return
            200 - Get User.
        """
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.get(url, headers=self.headers, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(user=self.user))
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    def test_api_header_deprecated(self):
        """ Header is deprecated.

        Return
            401 - Unauthorized".
        """
        """ env """
        time.sleep(6)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.get(url, headers=self.headers, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 401)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_401)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param="token", msg=rep.detail_has_expired)
        self.assertEqual(response_body["detail"], detail)

    def test_api_header_nok(self):
        """ Header is nok.

        Return
            401 - Unauthorized".
        """
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.get(url, headers={"Authorization": "aaa"}, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 401)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_401)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param="token", msg=rep.detail_was_wrong)
        self.assertEqual(response_body["detail"], detail)

    def test_api_without_header(self):
        """ Header is missing.

        Return
            401 - Unauthorized".
        """
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 401)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_401)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param="token", msg=rep.detail_is_required)
        self.assertEqual(response_body["detail"], detail)

    def tearDown(self):
        """ Clean UserTest."""
        UserTest().clean()

    @classmethod
    def tearDownClass(cls):
        """ Clean UserTest."""
        UserTest.clean()


if __name__ == '__main__':
    unittest.main()
