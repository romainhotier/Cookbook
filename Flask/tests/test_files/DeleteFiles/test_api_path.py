import unittest
import requests

import utils
import tests.test_recipe.PutRecipe.api as api
import tests.test_recipe.model as recipe_model
import tests.test_files.model as files_model

server = utils.Server()
api = api.PutRecipe()
recipe = recipe_model.RecipeTest()
files = files_model.FilesTest()


file_paths = utils.PathExplorer().get_files_path_for_test()


class PutRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest."""
        recipe.clean()
        files.clean()

    def test_files_without(self):
        """ BodyParameter categories is missing.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_file1 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[0]).insert()
        tc_file2 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[1]).insert()
        tc_recipe.add_files_recipe(files=[tc_file1, tc_file2], mongo=True)
        """ param """
        tc_id = tc_recipe.get_id()
        body = {}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param="body", msg=server.detail_must_contain_at_least_one_key, value=body)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()
        tc_file1.check_file_exist()
        tc_file2.check_file_exist()

    def test_files_none(self):
        """ BodyParameter categories is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_file1 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[0]).insert()
        tc_file2 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[1]).insert()
        tc_recipe.add_files_recipe(files=[tc_file1, tc_file2], mongo=True)
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_files: None}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_files, msg=server.detail_must_be_an_array,
                                   value=body[api.param_files])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()
        tc_file1.check_file_exist()
        tc_file2.check_file_exist()

    def test_files_empty(self):
        """ BodyParameter categories is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_file1 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[0]).insert()
        tc_file2 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[1]).insert()
        tc_recipe.add_files_recipe(files=[tc_file1, tc_file2], mongo=True)
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_files: ""}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_files, msg=server.detail_must_be_an_array,
                                   value=body[api.param_files])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()
        tc_file1.check_file_exist()
        tc_file2.check_file_exist()

    def test_files_string(self):
        """ BodyParameter categories is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_file1 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[0]).insert()
        tc_file2 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[1]).insert()
        tc_recipe.add_files_recipe(files=[tc_file1, tc_file2], mongo=True)
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_files: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_files, msg=server.detail_must_be_an_array,
                                   value=body[api.param_files])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()
        tc_file1.check_file_exist()
        tc_file2.check_file_exist()

    def test_files_tab(self):
        """ BodyParameter categories is an empty tab.

        Return
            200 - Updated Recipe.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_file1 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[0]).insert()
        tc_file2 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[1]).insert()
        tc_recipe.add_files_recipe(files=[tc_file1, tc_file2], mongo=True)
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_files: ["invalid", tc_file2.path]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.custom(body).custom({"files": [tc_file2.path]})
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe.check_bdd_data()
        tc_file1.check_file_not_exist()
        tc_file2.check_file_exist()

    def test_files_object(self):
        """ BodyParameter categories is an empty object.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_file1 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[0]).insert()
        tc_file2 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[1]).insert()
        tc_recipe.add_files_recipe(files=[tc_file1, tc_file2], mongo=True)
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_files: {}}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_files, msg=server.detail_must_be_an_array,
                                   value=body[api.param_files])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()
        tc_file1.check_file_exist()
        tc_file2.check_file_exist()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PutRecipe())


if __name__ == '__main__':
    unittest.main()
