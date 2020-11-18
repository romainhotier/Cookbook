import unittest
import requests

import utils
import tests.recipe.GetRecipe.api as api
import tests.recipe.model as recipe_model
import tests.file.model as file_model

server = utils.Server()
api = api.GetRecipe()
recipe = recipe_model.RecipeTest()
file = file_model.FileTest()


class GetRecipe(unittest.TestCase):

    def setUp(self):
        recipe.clean()
        file.clean()

    def test_0_api_ok(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "qa_rhr_a"}).insert()
        recipe_model.RecipeTest().custom({"title": "qa_rhr_b"}).insert()
        tc_slug = tc_recipe1.slug
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_slug
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe1))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_0_api_ok_more_param(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "qa_rhr_a"}).insert()
        recipe_model.RecipeTest().custom({"title": "qa_rhr_b"}).insert()
        tc_slug = tc_recipe1.slug
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_slug + "?invalid=invalid"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe1))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_1_url_not_found(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "qa_rhr_a"}).insert()
        recipe_model.RecipeTest().custom({"title": "qa_rhr_b"}).insert()
        tc_slug = tc_recipe1.slug
        """ call api """
        url = server.main_url + "/" + api.url + "x/" + tc_slug
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)

    def test_2_slug_without(self):
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
        self.assertIn(api.data_expected(recipe=tc_recipe1), response_body["data"])
        self.assertIn(api.data_expected(recipe=tc_recipe2), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_2_slug_string(self):
        recipe_model.RecipeTest().custom({"title": "qa_rhr_a"}).insert()
        tc_slug = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_slug
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_slug, msg=server.detail_doesnot_exist, value=tc_slug)
        self.assertEqual(response_body["detail"], detail)

    def test_3_with_files_without(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "qa_rhr_a"}).insert()
        recipe_model.RecipeTest().custom({"title": "qa_rhr_b"}).insert()
        tc_slug = tc_recipe1.slug
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_slug
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe1))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_3_with_files_empty(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "qa_rhr_a"}).insert()
        recipe_model.RecipeTest().custom({"title": "qa_rhr_b"}).insert()
        tc_slug = tc_recipe1.slug
        tc_with_files = ""
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_slug + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_files, msg=server.detail_must_be_in + " ['true', 'false']", 
                                   value=tc_with_files)
        self.assertEqual(response_body["detail"], detail)

    def test_3_with_files_string(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "qa_rhr_a"}).insert()
        recipe_model.RecipeTest().custom({"title": "qa_rhr_b"}).insert()
        tc_slug = tc_recipe1.slug
        tc_with_files = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_slug + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_files, msg=server.detail_must_be_in + " ['true', 'false']", 
                                   value=tc_with_files)
        self.assertEqual(response_body["detail"], detail)

    def test_4_with_files_string_false(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "qa_rhr_a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step recipe 1 - 2nd")
        tc_recipe.insert()
        tc_recipe.add_file_recipe(filename="qa_rhr_1", is_main=True)
        tc_recipe.add_file_recipe(filename="qa_rhr_2", is_main=False)
        tc_recipe.add_file_step(_id_step="111111111111111111111111", filename="qa_rhr_11", is_main=False)
        tc_recipe.add_file_step(_id_step="222222222222222222222222", filename="qa_rhr_21", is_main=False)
        tc_recipe.add_file_step(_id_step="222222222222222222222222", filename="qa_rhr_22", is_main=True)
        tc_slug = tc_recipe.slug
        tc_with_files = "false"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_slug + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_4_with_files_string_true(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "qa_rhr_a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step recipe 1 - 2nd")
        tc_recipe.insert()
        tc_file_recipe11 = tc_recipe.add_file_recipe(filename="qa_rhr_1", is_main=True)
        tc_file_recipe12 = tc_recipe.add_file_recipe(filename="qa_rhr_2", is_main=False)
        tc_file_step111 = tc_recipe.add_file_step(_id_step="111111111111111111111111", filename="qa_rhr_11",
                                                  is_main=False)
        tc_file_step121 = tc_recipe.add_file_step(_id_step="222222222222222222222222", filename="qa_rhr_21",
                                                  is_main=False)
        tc_file_step122 = tc_recipe.add_file_step(_id_step="222222222222222222222222", filename="qa_rhr_22",
                                                  is_main=True)
        tc_slug = tc_recipe.slug
        tc_with_files = "true"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_slug + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"],
                         api.data_expected(recipe=tc_recipe,
                                           files={"recipe": [tc_file_recipe11, tc_file_recipe12],
                                                  "steps": {"111111111111111111111111": [tc_file_step111],
                                                            "222222222222222222222222": [tc_file_step121,
                                                                                         tc_file_step122]}}))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    @classmethod
    def tearDownClass(cls):
        cls.setUp(GetRecipe())


if __name__ == '__main__':
    unittest.main()
