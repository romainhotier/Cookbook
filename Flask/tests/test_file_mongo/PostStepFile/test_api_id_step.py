import unittest
import requests

import utils
import tests.test_file_mongo.PostStepFile.api as api
import tests.test_recipe.model as recipe_model
import tests.test_file_mongo.model as file_model

server = utils.Server()
api = api.PostStepFile()
recipe = recipe_model.RecipeTest()
file = file_model.FileMongoTest()

file_path = utils.PathExplorer().get_file_path_for_test()


class PostStepFile(unittest.TestCase):

    def setUp(self):
        """ Clean all FileMongoTest and RecipeTest """
        recipe.clean()
        file.clean()

    def test_id_step_without(self):
        """ QueryParameter _id_step is missing.

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
        tc_id_step = ""
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
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

    def test_id_step_string(self):
        """ QueryParameter _id_step is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step b")
        tc_recipe.insert()
        """ param """
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "invalid"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id_step, msg=server.detail_must_be_an_object_id, value=tc_id_step)
        self.assertEqual(response_body["detail"], detail)
        """ check file """
        file_model.FileMongoTest().custom_id_from_body(data=body).check_doesnt_exist_by_filename()

    def test_id_step_object_id_invalid(self):
        """ QueryParameter _id_step is a nok ObjectId.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step b")
        tc_recipe.insert()
        """ param """
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "aaaaaaaaaaaaaaaaaaaaaaaa"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id_step, msg=server.detail_doesnot_exist, value=tc_id_step)
        self.assertEqual(response_body["detail"], detail)
        """ check file """
        file_model.FileMongoTest().custom_id_from_body(data=body).check_doesnt_exist_by_filename()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostStepFile())


if __name__ == '__main__':
    unittest.main()
