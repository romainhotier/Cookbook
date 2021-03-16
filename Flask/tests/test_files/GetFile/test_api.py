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

    def test_api_ok_text(self):
        """ Default case with recipe .txt

        Return
            200 - FileTest.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
        tc_file1 = FileTest(filename="text.txt").insert(short_path="recipe/{0}".format(tc_recipe.get_id()))
        tc_file2 = FileTest(filename="image.png").insert(short_path="recipe/{0}".format(tc_recipe.get_id()))
        tc_recipe.add_files_recipe(files=[tc_file1, tc_file2], add_in_mongo=True)
        """ param """
        tc_path = tc_file1.get_short_path_url()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_path
        response = requests.get(url, verify=False)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "text/plain; charset=utf-8")
        self.assertEqual(response.text, "Text file exemple !")

    def test_api_ok_image(self):
        """ Default case with recipe .png

        Return
            200 - FileTest.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
        tc_file1 = FileTest(filename="text.txt").insert(short_path="recipe/{0}".format(tc_recipe.get_id()))
        tc_file2 = FileTest(filename="image.png").insert(short_path="recipe/{0}".format(tc_recipe.get_id()))
        tc_recipe.add_files_recipe(files=[tc_file1, tc_file2], add_in_mongo=True)
        """ param """
        tc_path = tc_file2.get_short_path_url()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_path
        response = requests.get(url, verify=False)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "image/png")

    def test_api_ok_more_param(self):
        """ Default case with more parameter.

        Return
            200 - FileTest.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
        tc_file1 = FileTest(filename="text.txt").insert(short_path="recipe/{0}".format(tc_recipe.get_id()))
        tc_file2 = FileTest(filename="image.png").insert(short_path="recipe/{0}".format(tc_recipe.get_id()))
        tc_recipe.add_files_recipe(files=[tc_file1, tc_file2], add_in_mongo=True)
        """ param """
        tc_path = tc_file1.get_short_path_url()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_path + "?invalid=invalid"
        response = requests.get(url, verify=False)
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
        tc_recipe = RecipeTest().insert()
        tc_file1 = FileTest(filename="text.txt").insert(short_path="recipe/{0}".format(tc_recipe.get_id()))
        tc_file2 = FileTest(filename="image.png").insert(short_path="recipe/{0}".format(tc_recipe.get_id()))
        tc_recipe.add_files_recipe(files=[tc_file1, tc_file2], add_in_mongo=True)
        """ param """
        tc_path = tc_file1.get_short_path_url()
        """ call api """
        url = server.main_url + "/" + api.url + "x/" + tc_path
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        self.assertEqual(response_body["detail"], rep.detail_url_not_found)

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestGetFile())


if __name__ == '__main__':
    unittest.main()
