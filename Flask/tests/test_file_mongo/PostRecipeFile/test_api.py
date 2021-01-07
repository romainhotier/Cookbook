import unittest
import requests

import utils
import tests.test_file_mongo.PostRecipeFile.api as api
import tests.test_recipe.model as recipe_model
import tests.test_file_mongo.model as file_model

server = utils.Server()
api = api.PostRecipeFile()
recipe = recipe_model.RecipeTest()
file = file_model.FileMongoTest()

file_path = utils.PathExplorer().get_file_path_for_test()


class PostRecipeFile(unittest.TestCase):

    def setUp(self):
        """ Clean all FileMongoTest and RecipeTest """
        recipe.clean()
        file.clean()

    def test_api_ok(self):
        """ Default case

        Return
            201 - RecipeTest and FileMongoTests.
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
        tc_file = tc_recipe.add_file_mongo_recipe(filename=body[api.param_filename], is_main=body[api.param_is_main],
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
            201 - RecipeTest and FileMongoTests.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False,
                "invalid": "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        new_id = api.return_new_file_id(response_body)
        tc_file = tc_recipe.add_file_mongo_recipe(filename=body[api.param_filename], is_main=body[api.param_is_main],
                                                  identifier=new_id)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(new_id=new_id))
        """ check file """
        tc_file.check_bdd_data()

    def test_api_url_not_found(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False}
        """ call api """
        url = server.main_url + "/" + api.url + "x/" + tc_id
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
        file_model.FileMongoTest().custom_id_from_body(data=body).check_doesnt_exist_by_filename()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostRecipeFile())


if __name__ == '__main__':
    unittest.main()
