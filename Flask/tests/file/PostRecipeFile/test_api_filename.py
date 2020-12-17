import unittest
import requests

import utils
import tests.file.PostRecipeFile.api as api
import tests.recipe.model as recipe_model
import tests.file.model as file_model

server = utils.Server()
api = api.PostRecipeFile()
recipe = recipe_model.RecipeTest()
file = file_model.FileTest()

file_path = api.get_file_path_for_test()


class PostRecipeFile(unittest.TestCase):

    def setUp(self):
        """ Clean all FileTest and RecipeTest """
        recipe.clean()
        file.clean()

    def test_filename_without(self):
        """ BodyParameter filename is missing.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_path: file_path,
                api.param_is_main: False}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_filename, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)

    def test_filename_null(self):
        """ BodyParameter filename is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_path: file_path,
                api.param_filename: None,
                api.param_is_main: False}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_filename, msg=server.detail_must_be_a_string, 
                                   value=body[api.param_filename])
        self.assertEqual(response_body["detail"], detail)
        """ check file """
        file_model.FileTest().custom_id_from_body(data=body).check_doesnt_exist_by_filename()

    def test_filename_empty(self):
        """ BodyParameter filename is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "",
                api.param_is_main: False}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_filename, msg=server.detail_must_be_not_empty, 
                                   value=body[api.param_filename])
        self.assertEqual(response_body["detail"], detail)
        """ check file """
        file_model.FileTest().custom_id_from_body(data=body).check_doesnt_exist_by_filename()

    def test_filename_string(self):
        """ BodyParameter filename is a string.

        Return
            201 - RecipeTest and FileTests.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        new_id = api.return_new_file_id(response_body)
        tc_file = tc_recipe.add_file_recipe(filename=body[api.param_filename], is_main=body[api.param_is_main],
                                            identifier=new_id)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(new_id=new_id))
        """ check file """
        tc_file.check_bdd_data()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostRecipeFile())


if __name__ == '__main__':
    unittest.main()
