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

    def test_is_main_without(self):
        """ BodyParameter is_main is missing.

        Return
            201 - RecipeTest and FileMongoTests.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        new_id = api.return_new_file_id(response_body)
        tc_file = tc_recipe.add_file_mongo_recipe(filename=body[api.param_filename], is_main=False, identifier=new_id)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(new_id=new_id))
        """ check file """
        tc_file.check_bdd_data()

    def test_is_main_null(self):
        """ BodyParameter is_main is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: None}
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
        detail = api.create_detail(param=api.param_is_main, msg=server.detail_must_be_a_boolean,
                                   value=body[api.param_is_main])
        self.assertEqual(response_body["detail"], detail)
        """ check file """
        file_model.FileMongoTest().custom_id_from_body(data=body).check_doesnt_exist_by_filename()

    def test_is_main_empty(self):
        """ BodyParameter is_main is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: ""}
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
        detail = api.create_detail(param=api.param_is_main, msg=server.detail_must_be_a_boolean,
                                   value=body[api.param_is_main])
        self.assertEqual(response_body["detail"], detail)
        """ check file """
        file_model.FileMongoTest().custom_id_from_body(data=body).check_doesnt_exist_by_filename()

    def test_is_main_string(self):
        """ BodyParameter is_main is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: "invalid"}
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
        detail = api.create_detail(param=api.param_is_main, msg=server.detail_must_be_a_boolean,
                                   value=body[api.param_is_main])
        self.assertEqual(response_body["detail"], detail)
        """ check file """
        file_model.FileMongoTest().custom_id_from_body(data=body).check_doesnt_exist_by_filename()

    def test_is_main_false(self):
        """ BodyParameter is_main is False.

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

    def test_is_main_true(self):
        """ BodyParameter is_main is True.

        Return
            201 - RecipeTest and FileMongoTests.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: True}
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

    def test_is_main_true_already_exist(self):
        """ BodyParameter is_main is True and another True exist.

        Return
            201 - RecipeTest and FileMongoTests.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_file1 = tc_recipe.add_file_mongo_recipe(filename="qa_rhr_filename", is_main=True)
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename_new",
                api.param_is_main: True}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_file1.custom_is_main(False)
        new_id = api.return_new_file_id(response_body)
        tc_file2 = tc_recipe.add_file_mongo_recipe(filename=body[api.param_filename], is_main=body[api.param_is_main],
                                                   identifier=new_id)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(new_id=new_id))
        """ check file """
        tc_file1.check_bdd_data()
        tc_file2.custom_id_from_body(data=body).check_bdd_data()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostRecipeFile())


if __name__ == '__main__':
    unittest.main()
