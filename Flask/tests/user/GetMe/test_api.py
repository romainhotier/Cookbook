import unittest
import requests
import time

import utils
import tests.user.GetMe.api as api
import tests.user.model as user_model

server = utils.Server()
api = api.GetMe()
user = user_model.UserTest()


class GetMe(unittest.TestCase):

    @user.login
    def setUp(self, **kwargs):
        self.user = kwargs["user"]
        self.headers = kwargs["headers"]

    def test_0_api_ok(self):
        url = server.main_url + "/" + api.url
        response = requests.get(url, headers=self.headers, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(user=self.user))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_0_api_header_deprecated(self):
        time.sleep(6)
        url = server.main_url + "/" + api.url
        response = requests.get(url, headers=self.headers, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 401)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_401)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param="token", msg=server.detail_has_expired)
        self.assertEqual(response_body["detail"], detail)

    def test_0_api_header_nok(self):
        url = server.main_url + "/" + api.url
        response = requests.get(url, headers={"Authorization": "aaa"}, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 401)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_401)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param="token", msg=server.detail_was_wrong)
        self.assertEqual(response_body["detail"], detail)

    def test_0_api_without_header(self):
        url = server.main_url + "/" + api.url
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 401)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_401)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param="token", msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)

    def tearDown(self):
        user.clean()

    @classmethod
    def tearDownClass(cls):
        user.clean()


if __name__ == '__main__':
    unittest.main()
