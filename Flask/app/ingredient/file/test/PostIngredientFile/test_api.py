import unittest
import requests

from server import factory as factory
import app.ingredient.ingredient.model as ingredient_model
import app.ingredient.file.test.PostIngredientFile.api as api

server = factory.Server()
api = api.PostIngredientFile()
ingredient = ingredient_model.IngredientTest()


class PostIngredientFile(unittest.TestCase):

    def setUp(self):
        ingredient.clean()

    def test_0_api_ok(self):
        #tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        """ cal api """
        #url = server.main_url + "/" + api.url
        url = "http://127.0.0.1:5000/ingredient/file/5e5d28ea9fcb21764e83fe0e"
        #url = "http://127.0.0.1:5000/ingredient/file/5e5d3055efd0e8b78ba4d80d"
        #response = requests.post(url, json=body, verify=False)
        response = requests.get(url, verify=False)
        print(response)
        print(response.status_code)
        print(response.headers)
        print(response.text)
        #response_body = response.json()
        """ assert """
        #self.assertEqual(response.status_code, 201)
        #self.assertEqual(response.headers["Content-Type"], 'application/json')
        #self.assertEqual(response_body[api.rep_code_status], 201)
        #self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        #self.assertEqual(api.format_response(response_body[api.rep_data]), tc_ingredient.get_data_without_id())
        """ refacto """
        #tc_ingredient.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

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
        cls.setUp(PostIngredientFile())


if __name__ == '__main__':
    unittest.main()
