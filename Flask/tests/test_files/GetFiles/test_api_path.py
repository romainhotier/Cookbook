import unittest
import requests

import utils
import tests.test_files.GetFiles.api as api
import tests.test_recipe.model as recipe_model
import tests.test_files.model as files_model

server = utils.Server()
api = api.GetFiles()
recipe = recipe_model.RecipeTest()
file = files_model.FilesTest()

file_paths = utils.PathExplorer().get_files_path_for_test()


class GetFiles(unittest.TestCase):

    def setUp(self):
        """ Clean all FileTest and RecipeTest """
        recipe.clean()
        file.clean()
        pass

    def test_path_without(self):
        """ PathParameter path is missing.

        Return
            404 - Url not found.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_file1 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[0]).insert()
        tc_file2 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[1]).insert()
        tc_recipe.add_files_recipe(files=[tc_file1, tc_file2], mongo=True)
        """ param """
        """ call api """
        url = server.main_url + "/" + api.url + "/"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)

    def test_path_empty(self):
        """ PathParameter path is an empty string.

        Return
            404 - Url not found.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_file1 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[0]).insert()
        tc_file2 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[1]).insert()
        tc_recipe.add_files_recipe(files=[tc_file1, tc_file2], mongo=True)
        """ param """
        tc_path = ""
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_path
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)

    def test_path_invalid(self):
        """ PathParameter path is a invalid string.

        Return
            404 - Url not found.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_file1 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[0]).insert()
        tc_file2 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[1]).insert()
        tc_recipe.add_files_recipe(files=[tc_file1, tc_file2], mongo=True)
        """ param """
        tc_path = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_path
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url_files)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)

    def test_path_valid(self):
        """ PathParameter path is a valid string.

        Return
            200 - FileTest.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_file1 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[0]).insert()
        tc_file2 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[1]).insert()
        tc_recipe.add_files_recipe(files=[tc_file1, tc_file2], mongo=True)
        """ param """
        tc_path = tc_file1.path
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_path
        response = requests.get(url, verify=False)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "text/plain; charset=utf-8")
        self.assertEqual(response.text, "Text file exemple !")

    @classmethod
    def tearDownClass(cls):
        cls.setUp(GetFiles())


if __name__ == '__main__':
    unittest.main()
