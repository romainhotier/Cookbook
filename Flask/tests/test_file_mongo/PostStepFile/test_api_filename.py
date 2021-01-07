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

    def test_filename_without(self):
        """ BodyParameter filename is missing.

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
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: file_path,
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
        detail = api.create_detail(param=api.param_filename, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)

    def test_filename_null(self):
        """ BodyParameter filename is null.

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
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: file_path,
                api.param_filename: None,
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
        detail = api.create_detail(param=api.param_filename, msg=server.detail_must_be_a_string,
                                   value=body[api.param_filename])
        self.assertEqual(response_body["detail"], detail)
        """ check file """
        file_model.FileMongoTest().custom_id_from_body(data=body).check_doesnt_exist_by_filename()

    def test_filename_empty(self):
        """ BodyParameter filename is an empty string.

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
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: file_path,
                api.param_filename: "",
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
        detail = api.create_detail(param=api.param_filename, msg=server.detail_must_be_not_empty,
                                   value=body[api.param_filename])
        self.assertEqual(response_body["detail"], detail)
        """ check file """
        file_model.FileMongoTest().custom_id_from_body(data=body).check_doesnt_exist_by_filename()

    def test_filename_string(self):
        """ BodyParameter filename is a string.

        Return
            201 - RecipeTest and FileMongoTests.
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
        tc_file = tc_recipe.add_file_mongo_step(_id_step="111111111111111111111111",
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

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostStepFile())


if __name__ == '__main__':
    unittest.main()
