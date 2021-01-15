import unittest
import requests

from tests import server, rep
from tests.test_recipe import RecipeTest
from tests.test_files import FileTest
from tests.test_files.DeleteFile import api


class TestDeleteFile(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest."""
        RecipeTest().clean()
        FileTest().clean()

    def test_path_without(self):
        """ QueryParameter path is missing.

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
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        self.assertEqual(response_body["detail"], rep.detail_url_not_found)
        """ check """
        tc_recipe.check_bdd_data()
        tc_file1.check_file_exist()
        tc_file2.check_file_exist()

    def test_path_invalid(self):
        """ QueryParameter path is a string.

        Return
            400 - Bad request.
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
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_path, msg=rep.detail_must_be_a_path, value=tc_path)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()
        tc_file1.check_file_exist()
        tc_file2.check_file_exist()

    def test_path_invalid_len(self):
        """ QueryParameter path len is nok.

        Return
            400 - Bad request.
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
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], "")
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))
        """ check """
        tc_recipe.check_bdd_data()
        tc_file1.check_file_exist()
        tc_file2.check_file_exist()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestDeleteFile())


if __name__ == '__main__':
    unittest.main()
