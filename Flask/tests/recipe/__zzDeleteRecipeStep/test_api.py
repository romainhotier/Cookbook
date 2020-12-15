import unittest
import requests

import utils
import tests.recipe.DeleteRecipeStep.api as api
import tests.recipe.model as recipe_model
import tests.file.model as file_model

server = utils.Server()
api = api.DeleteRecipeStep()
recipe = recipe_model.RecipeTest()
file = file_model.FileTest()


class DeleteRecipeStep(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest and FileTest."""
        recipe.clean()
        file.clean()

    def test_0_api_ok(self):
        """ Default case.

        Return
            200 - Recipe.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step recipe 1 - 2nd")
        tc_recipe.insert()
        """ param """
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.remove_step(position=0)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe.select_ok()

    def test_0_api_ok_more_param(self):
        """ Default case with more parameters.

        Return
            200 - Recipe.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step recipe 1 - 2nd")
        tc_recipe.insert()
        """ param """
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step + \
            "?invalid=invalid"
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.remove_step(position=0)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe.select_ok()

    def test_1_url_not_found_1(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step recipe 1 - 2nd")
        tc_recipe.insert()
        """ param """
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        """ call api """
        url = server.main_url + "/" + api.url1 + "x/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        """ check """
        tc_recipe.select_ok()

    def test_1_url_not_found_2(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step recipe 1 - 2nd")
        tc_recipe.insert()
        """ param """
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/x" + api.url2 + "/" + tc_id_step
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        """ check """
        tc_recipe.select_ok()

    def test_2_id_recipe_without(self):
        """ QueryParameter _id_recipe is missing.

        Return
            405 - Method not allowed.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step recipe 1 - 2nd")
        tc_recipe.insert()
        """ param """
        tc_id_recipe = ""
        tc_id_step = "111111111111111111111111"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 405)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_405)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_method_not_allowed)
        """ check """
        tc_recipe.select_ok()

    def test_2_id_recipe_string(self):
        """ QueryParameter _id_recipe is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step recipe 1 - 2nd")
        tc_recipe.insert()
        """ param """
        tc_id_recipe = "invalid"
        tc_id_step = "111111111111111111111111"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id_recipe, msg=server.detail_must_be_an_object_id,
                                   value=tc_id_recipe)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.select_ok()

    def test_2_id_recipe_object_id_invalid(self):
        """ QueryParameter _id_recipe is a nok ObjectId.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step recipe 1 - 2nd")
        tc_recipe.insert()
        """ param """
        tc_id_recipe = "aaaaaaaaaaaaaaaaaaaaaaaa"
        tc_id_step = "111111111111111111111111"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id_recipe, msg=server.detail_doesnot_exist, value=tc_id_recipe)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.select_ok()

    def test_3_id_step_without(self):
        """ QueryParameter _id_step is missing.

        Return
            404 - Url not found.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step recipe 1 - 2nd")
        tc_recipe.insert()
        """ param """
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = ""
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        """ check """
        tc_recipe.select_ok()

    def test_3_id_step_string(self):
        """ QueryParameter _id_step is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step recipe 1 - 2nd")
        tc_recipe.insert()
        """ param """
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id_step, msg=server.detail_must_be_an_object_id, value=tc_id_step)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.select_ok()

    def test_3_id_step_object_id_invalid(self):
        """ QueryParameter _id_step is a nok ObjectId.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step recipe 1 - 2nd")
        tc_recipe.insert()
        """ param """
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "aaaaaaaaaaaaaaaaaaaaaaaa"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id_step, msg=server.detail_doesnot_exist, value=tc_id_step)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.select_ok()

    def test_4_with_files_without(self):
        """ QueryParameter with_files is missing.

        Return
            200 - Recipe.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step recipe 1 - 2nd")
        tc_recipe.insert()
        """ param """
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.remove_step(position=0)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe.select_ok()

    def test_4_with_files_empty(self):
        """ QueryParameter with_files is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step recipe 1 - 2nd")
        tc_recipe.insert()
        """ param """
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        tc_with_files = ""
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step + "?"\
            + api.param_with_files + "=" + tc_with_files
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_files, msg=server.detail_must_be_in + api.rep_detail_true_false,
                                   value=tc_with_files)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.select_ok()

    def test_4_with_files_string(self):
        """ QueryParameter with_files is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step recipe 1 - 2nd")
        tc_recipe.insert()
        """ param """
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        tc_with_files = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step + "?"\
            + api.param_with_files + "=" + tc_with_files
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_files, msg=server.detail_must_be_in + api.rep_detail_true_false,
                                   value=tc_with_files)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.select_ok()

    def test_4_with_files_string_false(self):
        """ QueryParameter with_files is false.

        Return
            200 - Recipe.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step recipe 1 - 2nd")
        tc_recipe.insert()
        tc_recipe.add_file_recipe(filename="qa_rhr_1", is_main=True)
        tc_recipe.add_file_recipe(filename="qa_rhr_2", is_main=False)
        tc_recipe.add_file_step(_id_step="111111111111111111111111", filename="qa_rhr_11", is_main=False)
        tc_recipe.add_file_step(_id_step="222222222222222222222222", filename="qa_rhr_21", is_main=False)
        tc_recipe.add_file_step(_id_step="222222222222222222222222", filename="qa_rhr_22", is_main=True)
        """ param """
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        tc_with_files = "false"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step + "?" \
            + api.param_with_files + "=" + tc_with_files
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.remove_step(position=0)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe.select_ok()

    def test_4_with_files_string_true(self):
        """ QueryParameter with_files is true.

        Return
            200 - Recipe with File.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step recipe 1 - 2nd")
        tc_recipe.insert()
        tc_file_recipe11 = tc_recipe.add_file_recipe(filename="qa_rhr_1", is_main=True)
        tc_file_recipe12 = tc_recipe.add_file_recipe(filename="qa_rhr_2", is_main=False)
        tc_recipe.add_file_step(_id_step="111111111111111111111111", filename="qa_rhr_11", is_main=False)
        tc_file_step121 = tc_recipe.add_file_step(_id_step="222222222222222222222222", filename="qa_rhr_21",
                                                  is_main=False)
        tc_file_step122 = tc_recipe.add_file_step(_id_step="222222222222222222222222", filename="qa_rhr_22",
                                                  is_main=True)
        """ param """
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        tc_with_files = "true"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step + "?" \
            + api.param_with_files + "=" + tc_with_files
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.remove_step(position=0)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"],
                         api.data_expected(recipe=tc_recipe,
                                           files={"recipe": [tc_file_recipe11, tc_file_recipe12],
                                                  "steps": {"222222222222222222222222": [tc_file_step121,
                                                                                         tc_file_step122]}}))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe.select_ok()

    def test_5_clean_file(self):
        """ File associated cleaned.

        Return
            200 - Recipe.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step recipe 1 - 2nd")
        tc_recipe.insert()
        tc_file_step111 = tc_recipe.add_file_step(_id_step="111111111111111111111111", filename="qa_rhr_1",
                                                  is_main=False)
        tc_file_step121 = tc_recipe.add_file_step(_id_step="222222222222222222222222", filename="qa_rhr_2",
                                                  is_main=False)
        tc_file_step122 = tc_recipe.add_file_step(_id_step="222222222222222222222222", filename="qa_rhr_3",
                                                  is_main=True)
        """ param """
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.remove_step(position=0)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_file_step111.select_nok()
        tc_file_step121.select_ok()
        tc_file_step122.select_ok()
        tc_recipe.select_ok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(DeleteRecipeStep())


if __name__ == '__main__':
    unittest.main()
