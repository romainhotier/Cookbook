import unittest
import requests

import utils
import tests.test_file_mongo.GetFile.api as api
import tests.test_file_mongo.model as file_model

server = utils.Server()
api = api.GetFile()
file = file_model.FileMongoTest()


class GetFile(unittest.TestCase):

    def setUp(self):
        """ Clean all FileMongoTest """
        file.clean()

    def test_api_ok(self):
        """ Default case

        Return
            200 - Get raw file.
        """
        """ env """
        tc_file = file_model.FileMongoTest().insert()
        """ param """
        tc_id = tc_file.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.get(url, verify=False)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/plain', response.headers["Content-Type"])
        self.assertEqual(response.text, tc_file.get_data())

    def test_api_url_not_found(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        tc_file = file_model.FileMongoTest().insert()
        """ param """
        tc_id = tc_file.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "x/" + tc_id
        response = requests.get(url, verify=False)
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
        cls.setUp(GetFile())


if __name__ == '__main__':
    unittest.main()
