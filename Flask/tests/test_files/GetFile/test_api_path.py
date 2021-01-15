import unittest
import requests

from tests import server, rep
from tests.test_recipe import RecipeTest
from tests.test_files import FileTest
from tests.test_files.GetFile import api


class TestGetFile(unittest.TestCase):

    def setUp(self):
        """ Clean all FileTest and RecipeTest """
        RecipeTest().clean()
        FileTest().clean()

    def test_path_without(self):
        """ PathParameter path is missing.

        Return
            404 - Url not found.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
        tc_file1 = FileTest(filename="text.txt").insert(short_path="recipe/{0}".format(tc_recipe.get_id()))
        tc_file2 = FileTest(filename="image.png").insert(short_path="recipe/{0}".format(tc_recipe.get_id()))
        tc_recipe.add_files_recipe(files=[tc_file1, tc_file2], add_in_mongo=True)
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
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        self.assertEqual(response_body["detail"], rep.detail_url_not_found)

    def test_path_invalid(self):
        """ PathParameter path is a invalid string.

        Return
            404 - Url not found.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
        tc_file1 = FileTest(filename="text.txt").insert(short_path="recipe/{0}".format(tc_recipe.get_id()))
        tc_file2 = FileTest(filename="image.png").insert(short_path="recipe/{0}".format(tc_recipe.get_id()))
        tc_recipe.add_files_recipe(files=[tc_file1, tc_file2], add_in_mongo=True)
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
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        self.assertEqual(response_body["detail"], rep.detail_url_not_found)

    def test_path_invalid_len(self):
        """ PathParameter path len is nok.

        Return
            200 - FileTest.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
        tc_file1 = FileTest(filename="text.txt").insert(short_path="recipe/{0}".format(tc_recipe.get_id()))
        tc_file2 = FileTest(filename="image.png").insert(short_path="recipe/{0}".format(tc_recipe.get_id()))
        tc_recipe.add_files_recipe(files=[tc_file1, tc_file2], add_in_mongo=True)
        """ param """
        tc_path = "invalid/invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_path
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url_files)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        self.assertEqual(response_body["detail"], rep.detail_url_not_found)

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestGetFile())


if __name__ == '__main__':
    unittest.main()
