import unittest
import requests

import utils
import tests.file.PostStepFile.api as api
import tests.recipe.model as recipe_model
import tests.file.model as file_model

server = utils.Server()
api = api.PostStepFile()
recipe = recipe_model.RecipeTest()
file = file_model.FileTest()

file_path = api.get_file_path_for_test()


class PostStepFile(unittest.TestCase):

    def setUp(self):
        """ Clean all FileTest and RecipeTest """
        recipe.clean()
        file.clean()

    def test_api_ok(self):
        """ Default case

        Return
            201 - RecipeTest and FileTests.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step b")
        tc_recipe.insert()
        """ param """
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        new_id = api.return_new_file_id(response_body)
        tc_file = tc_recipe.add_file_step(_id_step="111111111111111111111111",
                                          filename=body[api.param_filename],
                                          is_main=body[api.param_is_main],
                                          identifier=new_id)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(new_id=new_id))
        """ check file """
        tc_file.check_bdd_data()

    def test_api_ok_more_param(self):
        """ Default case with more parameter.

        Return
            201 - RecipeTest and FileTests.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step b")
        tc_recipe.insert()
        """ param """
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False,
                "invalid": "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        new_id = api.return_new_file_id(response_body)
        tc_file = tc_recipe.add_file_step(_id_step="111111111111111111111111",
                                          filename=body[api.param_filename],
                                          is_main=body[api.param_is_main],
                                          identifier=new_id)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(new_id=new_id))
        """ check file """
        tc_file.check_bdd_data()

    def test_api_url_not_found_1(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step b")
        tc_recipe.insert()
        """ param """
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False}
        """ call api """
        url = server.main_url + "/" + api.url1 + "x/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        """ check file """
        file_model.FileTest().custom_id_from_body(data=body).check_doesnt_exist_by_filename()

    def test_api_url_not_found_2(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step b")
        tc_recipe.insert()
        """ param """
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/x" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        """ check file """
        file_model.FileTest().custom_id_from_body(data=body).check_doesnt_exist_by_filename()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostStepFile())


if __name__ == '__main__':
    unittest.main()
