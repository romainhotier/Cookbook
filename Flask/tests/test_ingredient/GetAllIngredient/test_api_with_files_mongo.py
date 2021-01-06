import unittest
import requests

import utils
import tests.test_ingredient.GetAllIngredient.api as api
import tests.test_ingredient.model as ingredient_model
import tests.test_file_mongo.model as file_mongo_model

server = utils.Server()
api = api.GetAllIngredient()
ingredient = ingredient_model.IngredientTest()
file_mongo = file_mongo_model.FileMongoTest()


class GetAllIngredient(unittest.TestCase):

    def setUp(self):
        """ Clean IngredientTest and FileMongoTest."""
        ingredient.clean()
        file_mongo.clean()

    def test_with_files_mongo_without(self):
        """ QueryParameter with_files_mongo is missing.

        Return
            200 - All Ingredient.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient1.add_file_mongo(filename="qa_rhr_1_1", is_main=False)
        tc_ingredient1.add_file_mongo(filename="qa_rhr_1_2", is_main=True)
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        tc_ingredient2.add_file_mongo(filename="qa_rhr_2_1", is_main=False)
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

    def test_with_files_mongo_empty(self):
        """ QueryParameter with_files_mongo is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient1.add_file_mongo(filename="qa_rhr_1_1", is_main=False)
        tc_ingredient1.add_file_mongo(filename="qa_rhr_1_2", is_main=True)
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        tc_ingredient2.add_file_mongo(filename="qa_rhr_2_1", is_main=False)
        """ param """
        tc_with_files_mongo = ""
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_with_files_mongo + "=" + tc_with_files_mongo
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_files_mongo,
                                   msg=server.detail_must_be_in + api.detail_with_files,
                                   value=tc_with_files_mongo)
        self.assertEqual(response_body["detail"], detail)

    def test_with_files_mongo_invalid(self):
        """ QueryParameter with_files_mongo is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient1.add_file_mongo(filename="qa_rhr_1_1", is_main=False)
        tc_ingredient1.add_file_mongo(filename="qa_rhr_1_2", is_main=True)
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        tc_ingredient2.add_file_mongo(filename="qa_rhr_2_1", is_main=False)
        """ param """
        tc_with_files_mongo = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_with_files_mongo + "=" + tc_with_files_mongo
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_files_mongo,
                                   msg=server.detail_must_be_in + api.detail_with_files,
                                   value=tc_with_files_mongo)
        self.assertEqual(response_body["detail"], detail)

    def test_with_files_mongo_false(self):
        """ QueryParameter with_files_mongo is false.

        Return
            200 - All Ingredient.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient1.add_file_mongo(filename="qa_rhr_1_1", is_main=False)
        tc_ingredient1.add_file_mongo(filename="qa_rhr_1_2", is_main=True)
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        tc_ingredient2.add_file_mongo(filename="qa_rhr_2_1", is_main=False)
        """ param """
        tc_with_files_mongo = "false"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_with_files_mongo + "=" + tc_with_files_mongo
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

    def test_with_files_mongo_true(self):
        """ QueryParameter with_files_mongo is true.

        Return
            200 - All Ingredient with files.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_file1 = tc_ingredient1.add_file_mongo(filename="qa_rhr_1_1", is_main=False)
        tc_file2 = tc_ingredient1.add_file_mongo(filename="qa_rhr_1_2", is_main=True)
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        tc_file3 = tc_ingredient2.add_file_mongo(filename="qa_rhr_2_1", is_main=False)
        """ param """
        tc_with_files_mongo = "true"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_with_files_mongo + "=" + tc_with_files_mongo
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(ingredient=tc_ingredient1, files_mongo=[tc_file1, tc_file2]),
                      response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient2, files_mongo=[tc_file3]), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    @classmethod
    def tearDownClass(cls):
        cls.setUp(GetAllIngredient())


if __name__ == '__main__':
    unittest.main()
