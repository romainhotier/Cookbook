import unittest
import requests

import utils
import tests.recipe.SearchRecipe.api as api
import tests.recipe.model as recipe_model
import tests.file.model as file_model

server = utils.Server()
api = api.SearchRecipe()
recipe = recipe_model.RecipeTest()
file = file_model.FileTest()


class SearchRecipe(unittest.TestCase):

    def setUp(self):
        recipe.clean()
        file.clean()

    def test_0_api_ok(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "qa_rhr_a"}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"title": "qa_rhr_b"}).insert()
        tc_title = "qa_rhr"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_title + "=" + tc_title
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(recipe=tc_recipe1), response_body["data"])
        self.assertIn(api.data_expected(recipe=tc_recipe2), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_0_api_ok_more_param(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "qa_rhr_a"}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"title": "qa_rhr_b"}).insert()
        tc_title = "qa_rhr"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_title + "=" + tc_title + "&invalid=invalid"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(tc_recipe1.get_stringify(), response_body["data"])
        self.assertIn(tc_recipe2.get_stringify(), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_0_api_no_param(self):
        """ similar to getAll"""
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_recipe2 = recipe_model.RecipeTest().insert()
        """ call api """
        url = server.main_url + "/" + api.url + "?"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(tc_recipe1.get_stringify(), response_body["data"])
        self.assertIn(tc_recipe2.get_stringify(), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_0_api_multi_param(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "qa_rhr_a", "level": 5}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"title": "qa_rhr_b", "level": 5}).insert()
        tc_recipe3 = recipe_model.RecipeTest().custom({"title": "qa_rhr_a", "level": 6}).insert()
        tc_title = "qa_rhr_a"
        tc_level = "5"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_title + "=" + tc_title + "&" + \
            api.param_level + "=" + tc_level
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(tc_recipe1.get_stringify(), response_body["data"])
        self.assertNotIn(tc_recipe2.get_stringify(), response_body["data"])
        self.assertNotIn(tc_recipe3.get_stringify(), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_1_url_not_found(self):
        """ go to getRecipe """
        recipe_model.RecipeTest().insert()
        tc_title = "qa_rhr"
        """ call api """
        url = server.main_url + "/" + api.url + "x" + "?" + api.param_title + "=" + tc_title
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        detail = api.create_detail(param="slug", msg=server.detail_doesnot_exist, value="searchx")
        self.assertEqual(response_body["detail"], detail)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))

    def test_2_title_empty(self):
        recipe_model.RecipeTest().insert()
        tc_title = ""
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_title + "=" + tc_title
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        detail = api.create_detail(param=api.param_title, msg=server.detail_must_be_not_empty, value=tc_title)
        self.assertEqual(response_body["detail"], detail)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))

    def test_2_title_invalid(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "qa_rhr_a"}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"title": "qa_rhr_b"}).insert()
        tc_title = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_title + "=" + tc_title
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertNotIn(tc_recipe1.get_stringify(), response_body["data"])
        self.assertNotIn(tc_recipe2.get_stringify(), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_2_title_ok(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "qa_rhra"}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"title": "qa_rhrb"}).insert()
        tc_title = "qa_rhra"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_title + "=" + tc_title
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(tc_recipe1.get_stringify(), response_body["data"])
        self.assertNotIn(tc_recipe2.get_stringify(), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_3_slug_empty(self):
        recipe_model.RecipeTest().insert()
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
        detail = api.create_detail(param=api.param_slug, msg=server.detail_must_be_not_empty, value=tc_slug)
        self.assertEqual(response_body["detail"], detail)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))

    def test_3_slug_invalid(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"slug": "qa_rhr_a"}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"slug": "qa_rhr_b"}).insert()
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
        self.assertNotIn(tc_recipe1.get_stringify(), response_body["data"])
        self.assertNotIn(tc_recipe2.get_stringify(), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_3_slug_ok(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"slug": "qa_rhra"}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"slug": "qa_rhrb"}).insert()
        tc_slug = "qa_rhra"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_slug + "=" + tc_slug
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(tc_recipe1.get_stringify(), response_body["data"])
        self.assertNotIn(tc_recipe2.get_stringify(), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_4_level_empty(self):
        recipe_model.RecipeTest().insert()
        tc_level = ""
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_level + "=" + tc_level
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        detail = api.create_detail(param=api.param_level, msg=server.detail_must_be_an_integer, value=tc_level)
        self.assertEqual(response_body["detail"], detail)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))

    def test_4_level_invalid(self):
        recipe_model.RecipeTest().insert()
        tc_level = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_level + "=" + tc_level
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        detail = api.create_detail(param=api.param_level, msg=server.detail_must_be_an_integer, value=tc_level)
        self.assertEqual(response_body["detail"], detail)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))

    def test_4_level_ok(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"level": 5}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"level": 6}).insert()
        tc_level = "5"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_level + "=" + tc_level
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(tc_recipe1.get_stringify(), response_body["data"])
        self.assertNotIn(tc_recipe2.get_stringify(), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_5_cooking_time_empty(self):
        recipe_model.RecipeTest().insert()
        tc_cooking_time = ""
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_cooking_time + "=" + tc_cooking_time
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        detail = api.create_detail(param=api.param_cooking_time, msg=server.detail_must_be_an_integer,
                                   value=tc_cooking_time)
        self.assertEqual(response_body["detail"], detail)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))

    def test_5_cooking_time_invalid(self):
        recipe_model.RecipeTest().insert()
        tc_cooking_time = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_cooking_time + "=" + tc_cooking_time
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        detail = api.create_detail(param=api.param_cooking_time, msg=server.detail_must_be_an_integer,
                                   value=tc_cooking_time)
        self.assertEqual(response_body["detail"], detail)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))

    def test_5_cooking_time_ok(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"cooking_time": 5}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"cooking_time": 6}).insert()
        tc_cooking_time = "5"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_cooking_time + "=" + tc_cooking_time
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(tc_recipe1.get_stringify(), response_body["data"])
        self.assertNotIn(tc_recipe2.get_stringify(), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_6_preparation_time_empty(self):
        recipe_model.RecipeTest().insert()
        tc_preparation_time = ""
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_preparation_time + "=" + tc_preparation_time
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        detail = api.create_detail(param=api.param_preparation_time, msg=server.detail_must_be_an_integer,
                                   value=tc_preparation_time)
        self.assertEqual(response_body["detail"], detail)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))

    def test_6_preparation_time_invalid(self):
        recipe_model.RecipeTest().insert()
        tc_preparation_time = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_preparation_time + "=" + tc_preparation_time
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        detail = api.create_detail(param=api.param_preparation_time, msg=server.detail_must_be_an_integer,
                                   value=tc_preparation_time)
        self.assertEqual(response_body["detail"], detail)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))

    def test_6_preparation_time_ok(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"preparation_time": 5}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"preparation_time": 6}).insert()
        tc_preparation_time = "5"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_preparation_time + "=" + tc_preparation_time
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(tc_recipe1.get_stringify(), response_body["data"])
        self.assertNotIn(tc_recipe2.get_stringify(), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_7_nb_people_empty(self):
        recipe_model.RecipeTest().insert()
        tc_nb_people = ""
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_nb_people + "=" + tc_nb_people
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        detail = api.create_detail(param=api.param_nb_people, msg=server.detail_must_be_an_integer, value=tc_nb_people)
        self.assertEqual(response_body["detail"], detail)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))

    def test_7_nb_people_invalid(self):
        recipe_model.RecipeTest().insert()
        tc_nb_people = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_nb_people + "=" + tc_nb_people
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        detail = api.create_detail(param=api.param_nb_people, msg=server.detail_must_be_an_integer, value=tc_nb_people)
        self.assertEqual(response_body["detail"], detail)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))

    def test_7_nb_people_ok(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"nb_people": 5}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"nb_people": 6}).insert()
        tc_nb_people = "5"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_nb_people + "=" + tc_nb_people
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(tc_recipe1.get_stringify(), response_body["data"])
        self.assertNotIn(tc_recipe2.get_stringify(), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_8_categories_empty(self):
        recipe_model.RecipeTest().insert()
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
        detail = api.create_detail(param=api.param_categories, msg=server.detail_must_be_not_empty, value=tc_categories)
        self.assertEqual(response_body["detail"], detail)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))

    def test_8_categories_invalid(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"categories": ["qa_rhr_", "qa_rhr_b", "qa_rhr_c"]}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"categories": ["qa_rhr_a", "qa_rhr_c"]}).insert()
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
        self.assertNotIn(tc_recipe1.get_stringify(), response_body["data"])
        self.assertNotIn(tc_recipe2.get_stringify(), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_8_categories_ok(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"categories": ["qa_rhr_", "qa_rhr_b", "qa_rhr_c"]}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"categories": ["qa_rhr_a", "qa_rhr_c"]}).insert()
        tc_categories = "qa_rhr_b"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_categories + "=" + tc_categories
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(tc_recipe1.get_stringify(), response_body["data"])
        self.assertNotIn(tc_recipe2.get_stringify(), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_2_with_files_without(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "qa_rhr_a"}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"title": "qa_rhr_b"}).insert()
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(tc_recipe1.get_stringify(), response_body["data"])
        self.assertIn(tc_recipe2.get_stringify(), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_2_with_files_empty(self):
        recipe_model.RecipeTest().custom({"title": "qa_rhr_a"}).insert()
        recipe_model.RecipeTest().custom({"title": "qa_rhr_b"}).insert()
        tc_with_files = ""
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_files, msg=server.detail_must_be_in + " [true, false]",
                                   value=tc_with_files)
        self.assertEqual(response_body["detail"], detail)

    def test_2_with_files_string(self):
        recipe_model.RecipeTest().custom({"title": "qa_rhr_a"}).insert()
        recipe_model.RecipeTest().custom({"title": "qa_rhr_b"}).insert()
        tc_with_files = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_files, msg=server.detail_must_be_in + " [true, false]",
                                   value=tc_with_files)
        self.assertEqual(response_body["detail"], detail)

    def test_2_with_files_string_false(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "qa_rhr_a"})
        tc_recipe2 = recipe_model.RecipeTest().custom({"title": "qa_rhr_b"})
        tc_recipe1.add_step(_id_step="111111111111111111111111", description="step recipe 1 - 1st")
        tc_recipe1.add_step(_id_step="222222222222222222222222", description="step recipe 1 - 2nd")
        tc_recipe2.add_step(_id_step="333333333333333333333333", description="step recipe 2 - 1st")
        tc_recipe1.insert()
        tc_recipe2.insert()
        tc_recipe1.add_file_recipe(filename="qa_rhr_1", is_main=True)
        tc_recipe1.add_file_recipe(filename="qa_rhr_2", is_main=False)
        tc_recipe2.add_file_recipe(filename="qa_rhr_3", is_main=False)
        tc_recipe1.add_file_step(_id_step="111111111111111111111111", filename="qa_rhr_1", is_main=False)
        tc_recipe1.add_file_step(_id_step="222222222222222222222222", filename="qa_rhr_21", is_main=False)
        tc_recipe1.add_file_step(_id_step="222222222222222222222222", filename="qa_rhr_22", is_main=True)
        tc_recipe2.add_file_step(_id_step="333333333333333333333333", filename="qa_rhr_31", is_main=True)
        tc_recipe2.add_file_step(_id_step="333333333333333333333333", filename="qa_rhr_32", is_main=False)
        tc_with_files = "false"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(tc_recipe1.get_stringify(), response_body["data"])
        self.assertIn(tc_recipe2.get_stringify(), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_2_with_files_string_true(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "qa_rhr_a"})
        tc_recipe2 = recipe_model.RecipeTest().custom({"title": "qa_rhr_b"})
        tc_recipe1.add_step(_id_step="111111111111111111111111", description="step recipe 1 - 1st")
        tc_recipe1.add_step(_id_step="222222222222222222222222", description="step recipe 1 - 2nd")
        tc_recipe2.add_step(_id_step="333333333333333333333333", description="step recipe 2 - 1st")
        tc_recipe1.insert()
        tc_recipe2.insert()
        tc_file_recipe11 = tc_recipe1.add_file_recipe(filename="qa_rhr_1", is_main=True)
        tc_file_recipe12 = tc_recipe1.add_file_recipe(filename="qa_rhr_2", is_main=False)
        tc_file_recipe2 = tc_recipe2.add_file_recipe(filename="qa_rhr_3", is_main=False)
        tc_file_step111 = tc_recipe1.add_file_step(_id_step="111111111111111111111111", filename="qa_rhr_11",
                                                   is_main=False)
        tc_file_step121 = tc_recipe1.add_file_step(_id_step="222222222222222222222222", filename="qa_rhr_21",
                                                   is_main=False)
        tc_file_step122 = tc_recipe1.add_file_step(_id_step="222222222222222222222222", filename="qa_rhr_22",
                                                   is_main=True)
        tc_file_step211 = tc_recipe2.add_file_step(_id_step="333333333333333333333333", filename="qa_rhr_31",
                                                   is_main=True)
        tc_file_step212 = tc_recipe2.add_file_step(_id_step="333333333333333333333333", filename="qa_rhr_32",
                                                   is_main=False)
        tc_with_files = "true"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(recipe=tc_recipe1,
                                        files={"recipe": [tc_file_recipe11, tc_file_recipe12],
                                               "steps": {"111111111111111111111111": [tc_file_step111],
                                                         "222222222222222222222222": [tc_file_step121,
                                                                                      tc_file_step122]}}),
                      response_body["data"])
        self.assertIn(api.data_expected(recipe=tc_recipe2,
                                        files={"recipe": [tc_file_recipe2],
                                               "steps": {"333333333333333333333333": [tc_file_step211,
                                                                                      tc_file_step212]}}),
                      response_body["data"],)
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    @classmethod
    def tearDownClass(cls):
        cls.setUp(SearchRecipe())


if __name__ == '__main__':
    unittest.main()
