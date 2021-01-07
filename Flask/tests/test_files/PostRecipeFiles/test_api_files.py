import unittest
import requests

import utils
import tests.test_files.PostRecipeFiles.api as api
import tests.test_recipe.model as recipe_model
import tests.test_files.model as files_model

server = utils.Server()
api = api.PostRecipeFiles()
recipe = recipe_model.RecipeTest()
file = files_model.FilesTest()

file_paths = utils.PathExplorer().get_files_path_for_test()


class PostRecipeFiles(unittest.TestCase):

    def setUp(self):
        """ Clean all FileTest and RecipeTest """
        recipe.clean()
        file.clean()
        pass

    def test_files_without(self):
        """ MultiPart Without.

        Return
            201 - FileTests..
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_file1 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[0]).insert()
        tc_recipe.add_files_recipe(files=[tc_file1], mongo=True)
        """ param """
        tc_id = tc_recipe.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], [])
        """ check recipe """
        tc_recipe.check_bdd_data()
        """ check files """
        tc_file1.check_file_exist()

    def test_files_invalid(self):
        """ MultiPart invalid.

        Return
            201 - FileTests.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_file1 = files_model.FilesTest().set_short_path(kind="recipe", _id=tc_recipe.get_id(),
                                                          path=file_paths[0]).insert()
        tc_recipe.add_files_recipe(files=[tc_file1], mongo=True)
        """ param """
        tc_id = tc_recipe.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        body = {"invalid": "invalid"}
        response = requests.post(url, json=body, files={"invalid": "invalid"}, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], [])
        """ check recipe """
        tc_recipe.check_bdd_data()
        """ check files """
        tc_file1.check_file_exist()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostRecipeFiles())


if __name__ == '__main__':
    unittest.main()
