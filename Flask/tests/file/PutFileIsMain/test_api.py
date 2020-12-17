import unittest
import requests
from bson import ObjectId

import utils
import tests.file.PutFileIsMain.api as api
import tests.file.model as file_model

server = utils.Server()
api = api.PutFileIsMain()
file = file_model.FileTest()


class PutFileIsMain(unittest.TestCase):

    def setUp(self):
        """ Clean all FileTest"""
        file.clean()

    def test_api_ok(self):
        """ Default case

        Return
            200 - Update information.
        """
        """ env """
        tc_file1 = file_model.FileTest().custom({"metadata": {"kind": "kind_file",
                                                              "_id_parent": ObjectId("111111111111111111111111"),
                                                              "is_main": True}}).insert()
        tc_file2 = file_model.FileTest().custom({"metadata": {"kind": "kind_file",
                                                              "_id_parent": ObjectId("111111111111111111111111"),
                                                              "is_main": False}}).insert()
        tc_file3 = file_model.FileTest().custom({"metadata": {"kind": "kind_file",
                                                              "_id_parent": ObjectId("111111111111111111111111"),
                                                              "is_main": False}}).insert()
        tc_file4 = file_model.FileTest().custom({"metadata": {"kind": "kind_file",
                                                              "_id_parent": ObjectId("222222222222222222222222"),
                                                              "is_main": True}}).insert()
        """ param """
        tc_id = tc_file3.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, verify=False)
        response_body = response.json()
        """ change """
        tc_file1.custom_is_main(False)
        tc_file3.custom_is_main(True)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(_id_file=tc_id,
                                                                  _id_parent="111111111111111111111111"))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check files """
        tc_file1.check_bdd_data()
        tc_file2.check_bdd_data()
        tc_file3.check_bdd_data()
        tc_file4.check_bdd_data()

    def test_api_url_not_found(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        tc_file = file_model.FileTest().insert()
        """ param """
        tc_id = tc_file.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "x/" + tc_id
        response = requests.put(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        """ check file """
        tc_file.check_bdd_data()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PutFileIsMain())


if __name__ == '__main__':
    unittest.main()
