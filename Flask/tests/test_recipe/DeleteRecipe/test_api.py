import unittest
import requests

from tests import server, rep
from tests.test_files import FileTest
from tests.test_recipe import RecipeTest
from tests.test_recipe.DeleteRecipe import api


class TestDeleteRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest."""
        RecipeTest().clean()
        FileTest().clean()

    def test_api_ok(self):
        """ Default case.

        Return
            200 - Recipe Deleted.
        """
        """ env """
        tc_recipe1 = RecipeTest().insert()
        tc_recipe2 = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], tc_id)
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))
        """ check """
        tc_recipe1.check_doesnt_exist_by_id()
        tc_recipe2.check_bdd_data()

    def test_api_url_not_found(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        tc_recipe1 = RecipeTest().insert()
        tc_recipe2 = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "x/" + tc_id
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        self.assertEqual(response_body["detail"], rep.detail_url_not_found)
        """ check """
        tc_recipe1.check_bdd_data()
        tc_recipe2.check_bdd_data()

    def test_api_clean_file(self):
        """ File associated cleaned.

        Return
            200 - Recipe Deleted.
        """
        """ env """
        tc_recipe1 = RecipeTest().insert()
        tc_recipe2 = RecipeTest().insert()
        """ file recipe1 """
        tc_file11 = FileTest(filename="text.txt").insert(short_path="recipe/{0}".format(tc_recipe1.get_id()))
        tc_file12 = FileTest(filename="image.png").insert(short_path="recipe/{0}".format(tc_recipe1.get_id()))
        tc_recipe1.add_files_recipe(files=[tc_file11, tc_file12], add_in_mongo=True)
        """ file recipe2 """
        tc_file21 = FileTest(filename="text.txt").insert(short_path="recipe/{0}".format(tc_recipe2.get_id()))
        tc_file22 = FileTest(filename="image.png").insert(short_path="recipe/{0}".format(tc_recipe2.get_id()))
        tc_recipe2.add_files_recipe(files=[tc_file21, tc_file22], add_in_mongo=True)
        """ param """
        tc_id = tc_recipe1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], tc_id)
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))
        """ check recipe1 """
        tc_file11.check_file_not_exist()
        tc_file12.check_file_not_exist()
        tc_recipe1.check_doesnt_exist_by_id()
        """ check recipe2 """
        tc_file21.check_file_exist()
        tc_file22.check_file_exist()
        tc_recipe2.check_bdd_data()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestDeleteRecipe())


if __name__ == '__main__':
    unittest.main()
