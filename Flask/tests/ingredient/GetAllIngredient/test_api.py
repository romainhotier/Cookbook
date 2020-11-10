import unittest
import requests

import utils
import tests.ingredient.GetAllIngredient.api as api
import tests.ingredient.model as ingredient_model
#import tests.file.model as file_model

server = utils.Server()
api = api.GetAllIngredient()
ingredient = ingredient_model.IngredientTest()
#file = file_model.FileTest()


class GetAllIngredient(unittest.TestCase):

    def setUp(self):
        ingredient.clean()
        #file.clean()

    def test_0_api_okaaaaa(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_a"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_b"}).insert()
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.get(url, verify=False)
        response_body = response.json()
        print(response_body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(ingredient=tc_ingredient1), response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient2), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_0_api_ok(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_a"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_b"}).insert()
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(ingredient=tc_ingredient1), response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient2), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_0_api_ok_more_param(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_a"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_b"}).insert()
        """ call api """
        url = server.main_url + "/" + api.url + "?invalid=invalid"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(ingredient=tc_ingredient1), response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient2), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_1_url_not_found(self):
        ingredient_model.IngredientTest().custom({"name": "qa_rhr_a"}).insert()
        ingredient_model.IngredientTest().custom({"name": "qa_rhr_b"}).insert()
        """ call api """
        url = server.main_url + "/" + api.url + "x"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)

    def test_2_with_files_without(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_a"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_b"}).insert()
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(ingredient=tc_ingredient1), response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient2), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_2_with_files_empty(self):
        ingredient_model.IngredientTest().custom({"name": "qa_rhr_a"}).insert()
        ingredient_model.IngredientTest().custom({"name": "qa_rhr_b"}).insert()
        tc_with_files = ""
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_files, msg=server.detail_must_be_in + " [true, false]",
                                   value=tc_with_files)
        self.assertEqual(response_body["detail"], detail)

    def test_2_with_files_string(self):
        ingredient_model.IngredientTest().custom({"name": "qa_rhr_a"}).insert()
        ingredient_model.IngredientTest().custom({"name": "qa_rhr_b"}).insert()
        tc_with_files = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_files, msg=server.detail_must_be_in + " [true, false]",
                                   value=tc_with_files)
        self.assertEqual(response_body["detail"], detail)

    def test_2_with_files_string_false(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_a"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_b"}).insert()
        tc_ingredient1.add_file(filename="qa_rhr_1", is_main=False)
        tc_ingredient1.add_file(filename="qa_rhr_2", is_main=True)
        tc_ingredient2.add_file(filename="qa_rhr_3", is_main=False)
        tc_with_files = "false"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(ingredient=tc_ingredient1), response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient2), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_2_with_files_string_true(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_a"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_b"}).insert()
        tc_file1 = tc_ingredient1.add_file(filename="qa_rhr_1", is_main=False)
        tc_file2 = tc_ingredient1.add_file(filename="qa_rhr_2", is_main=True)
        tc_file3 = tc_ingredient2.add_file(filename="qa_rhr_3", is_main=False)
        tc_with_files = "true"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(ingredient=tc_ingredient1, files=[tc_file1, tc_file2]), response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient2, files=[tc_file3]), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    @classmethod
    def tearDownClass(cls):
        cls.setUp(GetAllIngredient())


if __name__ == '__main__':
    unittest.main()
