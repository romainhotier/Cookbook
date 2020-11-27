import unittest
import requests

import utils
import tests.ingredient.SearchIngredient.api as api
import tests.ingredient.model as ingredient_model
import tests.file.model as file_model

server = utils.Server()
api = api.SearchIngredient()
ingredient = ingredient_model.IngredientTest()
file = file_model.FileTest()


class SearchIngredient(unittest.TestCase):

    def setUp(self):
        """ Clean IngredientTest and FileTest."""
        ingredient.clean()
        file.clean()

    def test_0_no_param(self):
        """ Default case.

        Return
            200 - Go to GetIngredient.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        """ call api """
        url = server.main_url + "/" + api.url + "?"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(ingredient=tc_ingredient1), response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient2), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_0_more_param(self):
        """ Default case with more parameters.

        Return
            200 - Go to GetIngredient.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"invalid": "invalid"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        """ call api """
        url = server.main_url + "/" + api.url + "?" + "invalid=invalid"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(ingredient=tc_ingredient1), response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient2), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_1_url_not_found(self):
        """ Wrong url.

        Return
            400 - Go to GetIngredient.
        """
        """ env """
        ingredient_model.IngredientTest().custom({"name": "qa_rhr_a"}).insert()
        """ param """
        tc_name = "qa"
        """ call api """
        url = server.main_url + "/" + api.url + "x" + "?" + api.param_name + "=" + tc_name
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param="_id", msg=server.detail_must_be_an_object_id, value="searchx")
        self.assertEqual(response_body["detail"], detail)

    def test_2_name_empty(self):
        """ QueryParameter name is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        ingredient_model.IngredientTest().custom({"name": "qa_rhr_a"}).insert()
        """ param """
        tc_name = ""
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_name + "=" + tc_name
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_name, msg=server.detail_must_be_not_empty, value=tc_name)
        self.assertEqual(response_body["detail"], detail)

    def test_2_name_invalid(self):
        """ QueryParameter name is a string.

        Return
            200 - Get Ingredient.
        """
        """ env """
        ingredient_model.IngredientTest().custom({"name": "qa_rhr_a"}).insert()
        """ param """
        tc_name = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_name + "=" + tc_name
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertCountEqual(response_body["data"], [])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_2_name_exact(self):
        """ QueryParameter name is exact.

        Return
            200 - Get Ingredient.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_a"}).insert()
        ingredient_model.IngredientTest().custom({"name": "qa_rhr_b"}).insert()
        """ param """
        tc_name = tc_ingredient1.name
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_name + "=" + tc_name
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertCountEqual(response_body["data"], [api.data_expected(ingredient=tc_ingredient1)])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_2_name_partial(self):
        """ QueryParameter name is partial.

        Return
            200 - Get Ingredient.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_a"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_b"}).insert()
        """ param """
        tc_name = "qa_rhr"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_name + "=" + tc_name
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertCountEqual(response_body["data"], [api.data_expected(ingredient=tc_ingredient1),
                                                      api.data_expected(ingredient=tc_ingredient2)])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        
    def test_3_slug_empty(self):
        """ QueryParameter slug is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        ingredient_model.IngredientTest().custom({"slug": "qa_rhr_a"}).insert()
        """ param """
        tc_slug = ""
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_slug + "=" + tc_slug
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_slug, msg=server.detail_must_be_not_empty, value=tc_slug)
        self.assertEqual(response_body["detail"], detail)

    def test_3_slug_invalid(self):
        """ QueryParameter slug is a string.

        Return
            200 - Get Ingredient.
        """
        """ env """
        ingredient_model.IngredientTest().custom({"slug": "qa_rhr_a"}).insert()
        """ param """
        tc_slug = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_slug + "=" + tc_slug
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertCountEqual(response_body["data"], [])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_3_slug_exact(self):
        """ QueryParameter slug is exact.

        Return
            200 - Get Ingredient.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"slug": "qa_rhr_a"}).insert()
        ingredient_model.IngredientTest().custom({"slug": "qa_rhr_b"}).insert()
        """ param """
        tc_slug = tc_ingredient1.slug
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_slug + "=" + tc_slug
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertCountEqual(response_body["data"], [api.data_expected(ingredient=tc_ingredient1)])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_3_slug_partial(self):
        """ QueryParameter slug is partial.

        Return
            200 - Get Ingredient.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"slug": "qa_rhr_a"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom({"slug": "qa_rhr_b"}).insert()
        """ param """
        tc_slug = "qa_rhr"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_slug + "=" + tc_slug
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertCountEqual(response_body["data"], [api.data_expected(ingredient=tc_ingredient1),
                                                      api.data_expected(ingredient=tc_ingredient2)])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        
    def test_4_categories_empty(self):
        """ QueryParameter category is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        ingredient_model.IngredientTest().custom({"categories": ["qa_rhr_a"]}).insert()
        """ param """
        tc_categories = ""
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_categories + "=" + tc_categories
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_categories, msg=server.detail_must_be_not_empty, value=tc_categories)
        self.assertEqual(response_body["detail"], detail)

    def test_4_categories_invalid(self):
        """ QueryParameter category is a string.

        Return
            200 - Get Ingredient.
        """
        """ env """
        ingredient_model.IngredientTest().custom({"categories": ["qa_rhr_a"]}).insert()
        """ param """
        tc_categories = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_categories + "=" + tc_categories
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertCountEqual(response_body["data"], [])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_4_categories_exact(self):
        """ QueryParameter category is exact.

        Return
            200 - Get Ingredient.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"categories": ["qa_rhr_a"]}).insert()
        ingredient_model.IngredientTest().custom({"categories": ["qa_rhr_b"]}).insert()
        """ param """
        tc_categories = tc_ingredient1.categories[0]
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_categories + "=" + tc_categories
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertCountEqual(response_body["data"], [api.data_expected(ingredient=tc_ingredient1)])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_4_categories_partial(self):
        """ QueryParameter category is partial.

        Return
            200 - Get Ingredient.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"categories": ["qa_rhr_a"]}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom({"categories": ["qa_rhr_b"]}).insert()
        """ param """
        tc_categories = "qa_rhr"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_categories + "=" + tc_categories
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertCountEqual(response_body["data"], [api.data_expected(ingredient=tc_ingredient1),
                                                      api.data_expected(ingredient=tc_ingredient2)])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_5_with_files_without(self):
        """ QueryParameter with_files is missing.

        Return
            200 - Get Ingredient.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_a"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_b"}).insert()
        """ param """
        tc_name = "qa_rhr"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_name + "=" + tc_name
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertCountEqual(response_body["data"], [api.data_expected(ingredient=tc_ingredient1), 
                                                      api.data_expected(ingredient=tc_ingredient2)])
        self.assertIn(api.data_expected(ingredient=tc_ingredient2), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_5_with_files_empty(self):
        """ QueryParameter with_files is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_a"}).insert()
        ingredient_model.IngredientTest().custom({"name": "qa_rhr_b"}).insert()
        """ param """
        tc_name = tc_ingredient1.name
        tc_with_files = ""
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_name + "=" + tc_name + "&" + \
            api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_files, msg=server.detail_must_be_in + api.rep_detail_true_false,
                                   value=tc_with_files)
        self.assertEqual(response_body["detail"], detail)

    def test_5_with_files_string(self):
        """ QueryParameter with_files is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_a"}).insert()
        ingredient_model.IngredientTest().custom({"name": "qa_rhr_b"}).insert()
        tc_name = tc_ingredient1.name
        tc_with_files = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_name + "=" + tc_name + "&" + \
            api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_files, msg=server.detail_must_be_in + api.rep_detail_true_false,
                                   value=tc_with_files)
        self.assertEqual(response_body["detail"], detail)

    def test_5_with_files_string_false(self):
        """ QueryParameter with_files is false.

        Return
            200 - Get Ingredient.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_a"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_b"}).insert()
        tc_ingredient1.add_file(filename="qa_rhr_1", is_main=False)
        tc_ingredient1.add_file(filename="qa_rhr_2", is_main=True)
        tc_ingredient2.add_file(filename="qa_rhr_3", is_main=False)
        """ param """
        tc_name = "qa_rhr"
        tc_with_files = "false"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_name + "=" + tc_name + "&" + \
            api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertCountEqual(response_body["data"], [api.data_expected(ingredient=tc_ingredient1),
                                                      api.data_expected(ingredient=tc_ingredient2)])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_5_with_files_string_true(self):
        """ QueryParameter with_files is true.

        Return
            200 - Get Ingredient with Files.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_a"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_b"}).insert()
        tc_file1 = tc_ingredient1.add_file(filename="qa_rhr_1", is_main=False)
        tc_file2 = tc_ingredient1.add_file(filename="qa_rhr_2", is_main=True)
        tc_file3 = tc_ingredient2.add_file(filename="qa_rhr_3", is_main=False)
        """ param """
        tc_name = "qa_rhr"
        tc_with_files = "true"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_name + "=" + tc_name + "&" + \
            api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertCountEqual(response_body["data"], [api.data_expected(ingredient=tc_ingredient1,
                                                                        files=[tc_file1, tc_file2]),
                                                      api.data_expected(ingredient=tc_ingredient2,
                                                                        files=[tc_file3])])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    @classmethod
    def tearDownClass(cls):
        cls.setUp(SearchIngredient())


if __name__ == '__main__':
    unittest.main()
