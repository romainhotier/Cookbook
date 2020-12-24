import unittest
import requests

import utils
import tests.test_ingredient.GetIngredient.api as api
import tests.test_ingredient.model as ingredient_model
import tests.test_file.model as file_model

server = utils.Server()
api = api.GetIngredient()
ingredient = ingredient_model.IngredientTest()
file = file_model.FileTest()


class GetIngredient(unittest.TestCase):

    def setUp(self):
        """ Clean IngredientTest and FileTest."""
        ingredient.clean()
        file.clean()

    def test_with_files_without(self):
        """ QueryParameter with_files is missing.

        Return
            200 - One Ingredient.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_ingredient.add_file(filename="qa_rhr_1_1", is_main=False)
        tc_ingredient.add_file(filename="qa_rhr_1_2", is_main=True)
        """ param """
        tc_id = tc_ingredient.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(ingredient=tc_ingredient))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_with_files_empty(self):
        """ QueryParameter with_files is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_ingredient.add_file(filename="qa_rhr_1_1", is_main=False)
        tc_ingredient.add_file(filename="qa_rhr_1_2", is_main=True)
        """ param """
        tc_id = tc_ingredient.get_id()
        tc_with_files = ""
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_files, msg=server.detail_must_be_in + api.detail_with_files,
                                   value=tc_with_files)
        self.assertEqual(response_body["detail"], detail)

    def test_with_files_invalid(self):
        """ QueryParameter with_files is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_ingredient.add_file(filename="qa_rhr_1_1", is_main=False)
        tc_ingredient.add_file(filename="qa_rhr_1_2", is_main=True)
        """ param """
        tc_id = tc_ingredient.get_id()
        tc_with_files = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_files, msg=server.detail_must_be_in + api.detail_with_files,
                                   value=tc_with_files)
        self.assertEqual(response_body["detail"], detail)

    def test_with_files_false(self):
        """ QueryParameter with_files is false.

        Return
           200 - One Ingredient.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_ingredient.add_file(filename="qa_rhr_1_1", is_main=False)
        tc_ingredient.add_file(filename="qa_rhr_1_2", is_main=True)
        """ param """
        tc_id = tc_ingredient.get_id()
        tc_with_files = "false"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(ingredient=tc_ingredient))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_with_files_true(self):
        """ QueryParameter with_files is true.

        Return
            200 - One Ingredient with files.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_file1 = tc_ingredient.add_file(filename="qa_rhr_1_1", is_main=False)
        tc_file2 = tc_ingredient.add_file(filename="qa_rhr_1_2", is_main=True)
        """ param """
        tc_id = tc_ingredient.get_id()
        tc_with_files = "true"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(ingredient=tc_ingredient, files=[tc_file1, tc_file2]))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    @classmethod
    def tearDownClass(cls):
        cls.setUp(GetIngredient())
        pass


if __name__ == '__main__':
    unittest.main()
