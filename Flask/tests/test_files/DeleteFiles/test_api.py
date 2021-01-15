import unittest
import requests

import utils
import tests.test_files.DeleteFiles.api as api
import tests.test_recipe.model as recipe_model
import tests.test_files.model as files_model

server = utils.Server()
api = api.DeleteFiles()
recipe = recipe_model.RecipeTest()
file = files_model.FilesTest()

file_paths = utils.PathExplorer().get_files_path_for_test()


class DeleteFiles(unittest.TestCase):

    def setUp(self):
        """ Clean all FileTest and RecipeTest """
        recipe.clean()
        file.clean()

    def test_api_ok_text(self):
        """ Default case with text

        Return
            200 - FileTest.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_file1 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[0]).insert()
        tc_file2 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[1]).insert()
        tc_recipe.add_files_recipe(files=[tc_file1, tc_file2])
        tc_recipe.display()
        """ param """
        tc_path = tc_file1.path
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_path
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.delete_files_recipe(files=[tc_file1])
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], tc_path)
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check files """
        tc_file1.check_file_not_exist()
        tc_file2.check_file_exist()
        tc_recipe.check_bdd_data()

    def test_api_ok_image(self):
        """ Default case with image

        Return
            200 - FileTest.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_file1 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[0]).insert()
        tc_file2 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[1]).insert()
        tc_recipe.add_files_recipe(files=[tc_file1], mongo=True)
        tc_recipe.add_files_recipe(files=[tc_file2], mongo=True)
        """ param """
        tc_path = tc_file2.path
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_path
        response = requests.delete(url, verify=False)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "image/png")

    def test_api_ok_more_param(self):
        """ Default case with more parameter.

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
        url = server.main_url + "/" + api.url + "/" + tc_path + "?invalid=invalid"
        response = requests.delete(url, verify=False)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "text/plain; charset=utf-8")
        self.assertEqual(response.text, "Text file exemple !")

    def test_api_url_not_found(self):
        """ Wrong url.

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
        tc_path = tc_file1.path
        """ call api """
        url = server.main_url + "/" + api.url + "x/" + tc_path
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)

    @classmethod
    def tearDownClass(cls):
        #cls.setUp(DeleteFiles())
        pass


if __name__ == '__main__':
    unittest.main()
