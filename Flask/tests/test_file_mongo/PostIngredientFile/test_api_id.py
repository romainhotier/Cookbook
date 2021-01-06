import unittest
import requests

import utils
import tests.test_file_mongo.PostIngredientFile.api as api
import tests.test_ingredient.model as ingredient_model
import tests.test_file_mongo.model as file_model

server = utils.Server()
api = api.PostIngredientFile()
ingredient = ingredient_model.IngredientTest()
file = file_model.FileMongoTest()

file_path = api.get_file_path_for_test()


class PostIngredientFile(unittest.TestCase):

    def setUp(self):
        """ Clean all FileMongoTest and IngredientTest """
        file.clean()
        ingredient.clean()

    def test_id_without(self):
        """ QueryParameter _id missing.

        Return
            404 - Url not found.
        """
        """ param """
        tc_id = ""
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        """ check file """
        file_model.FileMongoTest().custom_id_from_body(data=body).check_doesnt_exist_by_filename()

    def test_id_string(self):
        """ QueryParameter _id is a string.

        Return
            400 - Bad request.
        """
        """ param """
        tc_id = "invalid"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id, msg=server.detail_must_be_an_object_id, value=tc_id)
        self.assertEqual(response_body["detail"], detail)
        """ check file """
        file_model.FileMongoTest().custom_id_from_body(data=body).check_doesnt_exist_by_filename()

    def test_id_object_id_invalid(self):
        """ QueryParameter _id is a nok ObjectId.

        Return
            400 - Bad request.
        """
        """ param """
        tc_id = "aaaaaaaaaaaaaaaaaaaaaaaa"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id, msg=server.detail_doesnot_exist, value=tc_id)
        self.assertEqual(response_body["detail"], detail)
        """ check file """
        file_model.FileMongoTest().custom_id_from_body(data=body).check_doesnt_exist_by_filename()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostIngredientFile())


if __name__ == '__main__':
    unittest.main()
