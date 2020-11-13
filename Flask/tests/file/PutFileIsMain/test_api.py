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
        file.clean()

    def test_0_api_ok(self):
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
        tc_id = tc_file3.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, verify=False)
        response_body = response.json()
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
        tc_file1.select_ok()
        tc_file2.select_ok()
        tc_file3.select_ok()
        tc_file4.select_ok()

    def test_1_url_not_found(self):
        tc_file = file_model.FileTest().insert()
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

    def test_2_id_without(self):
        file_model.FileTest().insert()
        tc_id = ""
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)

    def test_2_id_string(self):
        file_model.FileTest().insert()
        tc_id = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id, msg=server.detail_must_be_an_object_id, value=tc_id)
        self.assertEqual(response_body["detail"], detail)

    def test_2_id_object_id_invalid(self):
        file_model.FileTest().insert()
        tc_id = "aaaaaaaaaaaaaaaaaaaaaaaa"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id, msg=server.detail_doesnot_exist, value=tc_id)
        self.assertEqual(response_body["detail"], detail)

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PutFileIsMain())


if __name__ == '__main__':
    unittest.main()
