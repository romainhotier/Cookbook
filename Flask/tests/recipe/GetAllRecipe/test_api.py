import unittest
import requests

import utils
import tests.recipe.GetAllRecipe.api as api
import tests.recipe.model as recipe_model
import tests.file.model as file_model

server = utils.Server
api = api.GetAllRecipe()
recipe = recipe_model.RecipeTest()
file = file_model.FileTest()


class GetAllRecipe(unittest.TestCase):

    def setUp(self):
        recipe.clean()
        file.clean()

    def test_0_api_ok(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "qa_rhr_a"}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"title": "qa_rhr_b"}).insert()
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertIn(tc_recipe1.get_stringify(), response_body[api.rep_data])
        self.assertIn(tc_recipe2.get_stringify(), response_body[api.rep_data])

    def test_0_api_ok_more_param(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "qa_rhr_a"}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"title": "qa_rhr_b"}).insert()
        """ call api """
        url = server.main_url + "/" + api.url + "?invalid=invalid"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertIn(tc_recipe1.get_stringify(), response_body[api.rep_data])
        self.assertIn(tc_recipe2.get_stringify(), response_body[api.rep_data])

    def test_1_url_not_found(self):
        recipe_model.RecipeTest().custom({"title": "qa_rhr_a"}).insert()
        recipe_model.RecipeTest().custom({"title": "qa_rhr_b"}).insert()
        """ call api """
        url = server.main_url + "/" + api.url + "x"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)

    def test_2_with_files_without(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "qa_rhr_a"}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"title": "qa_rhr_b"}).insert()
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertIn(tc_recipe1.get_stringify(), response_body[api.rep_data])
        self.assertIn(tc_recipe2.get_stringify(), response_body[api.rep_data])

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
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_with_files, server.detail_must_be_in + " [true, false]", tc_with_files)
        self.assertEqual(response_body[api.rep_detail], detail)

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
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_with_files, server.detail_must_be_in + " [true, false]", tc_with_files)
        self.assertEqual(response_body[api.rep_detail], detail)

    def test_2_with_files_string_false(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "qa_rhr_a"})
        tc_recipe2 = recipe_model.RecipeTest().custom({"title": "qa_rhr_b"})
        tc_recipe1.add_step(_id_step="111111111111111111111111", step="step recipe 1 - 1st")
        tc_recipe1.add_step(_id_step="222222222222222222222222", step="step recipe 1 - 2nd")
        tc_recipe2.add_step(_id_step="333333333333333333333333", step="step recipe 2 - 1st")
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
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertIn(tc_recipe1.get_stringify(), response_body[api.rep_data])
        self.assertIn(tc_recipe2.get_stringify(), response_body[api.rep_data])

    def test_2_with_files_string_true(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "qa_rhr_a"})
        tc_recipe2 = recipe_model.RecipeTest().custom({"title": "qa_rhr_b"})
        tc_recipe1.add_step(_id_step="111111111111111111111111", step="step recipe 1 - 1st")
        tc_recipe1.add_step(_id_step="222222222222222222222222", step="step recipe 1 - 2nd")
        tc_recipe2.add_step(_id_step="333333333333333333333333", step="step recipe 2 - 1st")
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
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        r1 = tc_recipe1.get_stringify_with_file(files_recipe=[tc_file_recipe11, tc_file_recipe12],
                                                files_steps={"111111111111111111111111": [tc_file_step111],
                                                             "222222222222222222222222": [tc_file_step121,
                                                                                          tc_file_step122]})
        r2 = tc_recipe2.get_stringify_with_file(files_recipe=[tc_file_recipe2],
                                                files_steps={"333333333333333333333333": [tc_file_step211,
                                                                                          tc_file_step212]})
        self.assertIn(r1, response_body[api.rep_data])
        self.assertIn(r2, response_body[api.rep_data])

    @classmethod
    def tearDownClass(cls):
        cls.setUp(GetAllRecipe())


if __name__ == '__main__':
    unittest.main()
