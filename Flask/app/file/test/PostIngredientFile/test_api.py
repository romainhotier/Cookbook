import unittest
import requests
import pathlib

from server import factory as factory
import app.ingredient.ingredient.model as ingredient_model
import app.file.model as file_model
import app.file.test.PostIngredientFile.api as api

server = factory.Server()
api = api.PostIngredientFile()
ingredient = ingredient_model.IngredientTest()
file = file_model.FileTest()


default_path = str(pathlib.Path().absolute()).replace("PostIngredientFile", "file_exemple/text.txt")


class PostIngredientFile(unittest.TestCase):

    def setUp(self):
        ingredient.clean()
        file.clean()

    def test_0_api_ok(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: default_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ cal api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient.custom({"files": [{"_id": "", "is_main": body[api.param_is_main]}]})
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_ingredient.get_data_stringify_object_id())
        """ refacto """
        api.refacto_ingredient_with_file_id(ingredient=tc_ingredient, position=0, response=response_body).select_ok()
        #add check file ok dans la collection

    @unittest.skip('')
    def test_0_api_ok_more_param(self):
        body = {api.param_name: "qa_rhr_name",
                "invalid": "invalid"}
        tc_ingredient = ingredient_model.IngredientTest().custom(body)
        """ cal api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """

    @unittest.skip('')
    def test_1_url_not_found(self):
        body = {api.param_name: "qa_rhr_name"}
        tc_ingredient = ingredient_model.IngredientTest().custom(body)
        """ cal api """
        url = server.main_url + "/" + api.url + "x"
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        tc_ingredient.select_nok_by_name()

    @classmethod
    def tearDownClass(cls):
        #cls.setUp(PostIngredientFile())
        pass


if __name__ == '__main__':
    unittest.main()
