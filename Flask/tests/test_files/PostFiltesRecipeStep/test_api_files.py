import unittest
import requests

from tests import server
from tests.test_recipe import RecipeTest
from tests.test_files import FileTest
from tests.test_files.PostFilesRecipe import api


class TestPostFilesRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean all FileTest and RecipeTest """
        RecipeTest().clean()
        FileTest().clean()

    def test_files_without(self):
        """ MultiPart Without.

        Return
            201 - FileTests.
        """
        """ env """
        tc_recipe = RecipeTest()
        tc_recipe.add_step(_id_step="aaaaaaaaaaaaaaaaaaaaaaaa", description="step1")
        tc_recipe.add_step(_id_step="bbbbbbbbbbbbbbbbbbbbbbbb", description="step2")
        tc_recipe.insert()
        tc_file1 = FileTest(filename="text.txt").insert(short_path="recipe/{0}/steps/aaaaaaaaaaaaaaaaaaaaaaaa".
                                                        format(tc_recipe.get_id()))
        tc_recipe.add_files_steps(_id_step="aaaaaaaaaaaaaaaaaaaaaaaa", files=[tc_file1], add_in_mongo=True)
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
        tc_recipe = RecipeTest()
        tc_recipe.add_step(_id_step="aaaaaaaaaaaaaaaaaaaaaaaa", description="step1")
        tc_recipe.add_step(_id_step="bbbbbbbbbbbbbbbbbbbbbbbb", description="step2")
        tc_recipe.insert()
        tc_file1 = FileTest(filename="text.txt").insert(short_path="recipe/{0}/steps/aaaaaaaaaaaaaaaaaaaaaaaa".
                                                        format(tc_recipe.get_id()))
        tc_recipe.add_files_steps(_id_step="aaaaaaaaaaaaaaaaaaaaaaaa", files=[tc_file1], add_in_mongo=True)
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
        cls.setUp(TestPostFilesRecipe())


if __name__ == '__main__':
    unittest.main()
