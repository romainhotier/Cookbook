import unittest
import requests

from tests import server, rep
from tests.test_recipe import RecipeTest
from tests.test_files import FileTest
from tests.test_files.PostFiltesRecipeStep import api


class TestPostFilesRecipeStep(unittest.TestCase):

    def setUp(self):
        """ Clean all FileTest and RecipeTest """
        RecipeTest().clean()
        FileTest().clean()

    def test_api_ok(self):
        """ Default case

        Return
            201 - FileTests.
        """
        """ env """
        tc_recipe = RecipeTest()
        tc_recipe.add_step(_id_step="aaaaaaaaaaaaaaaaaaaaaaaa", description="step1")
        tc_recipe.add_step(_id_step="bbbbbbbbbbbbbbbbbbbbbbbb", description="step2")
        tc_recipe.insert()
        """ param """
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "bbbbbbbbbbbbbbbbbbbbbbbb"
        tc_file = FileTest()
        tc_files = [('files', (tc_file.filename, tc_file.data, tc_file.mimetype))]
        """ call api """
        url = server.main_url + "/" + api.url_1 + "/" + tc_id_recipe + "/" + api.url_2 + "/" + tc_id_step
        response = requests.post(url, files=tc_files, verify=False)
        response_body = response.json()
        """ close files """
        tc_file.close()
        """ change """
        tc_file.set_file_path(short_path="recipe/{0}/steps/{1}".format(tc_id_recipe, tc_id_step))
        tc_recipe.add_files_steps(_id_step=tc_id_step, files=[tc_file])
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(files=[tc_file]))
        """ check recipe """
        tc_recipe.check_bdd_data()
        """ check file """
        tc_file.check_file_exist()

    def test_api_ok_more_param(self):
        """ Default case with more param

        Return
            201 - FileTests.
        """
        """ env """
        tc_recipe = RecipeTest()
        tc_recipe.add_step(_id_step="aaaaaaaaaaaaaaaaaaaaaaaa", description="step1")
        tc_recipe.add_step(_id_step="bbbbbbbbbbbbbbbbbbbbbbbb", description="step2")
        tc_recipe.insert()
        """ param """
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "bbbbbbbbbbbbbbbbbbbbbbbb"
        tc_file = FileTest()
        tc_files = [('files', (tc_file.filename, tc_file.data, tc_file.mimetype))]
        body = {"invalid": "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url_1 + "/" + tc_id_recipe + "/" + api.url_2 + "/" + tc_id_step
        response = requests.post(url, json=body, files=tc_files, verify=False)
        response_body = response.json()
        """ close files """
        tc_file.close()
        """ change """
        tc_file.set_file_path(short_path="recipe/{0}/steps/{1}".format(tc_id_recipe, tc_id_step))
        tc_recipe.add_files_steps(_id_step=tc_id_step, files=[tc_file])
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(files=[tc_file]))
        """ check recipe """
        tc_recipe.check_bdd_data()
        """ check file """
        tc_file.check_file_exist()

    def test_api_url_not_found_1(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        tc_recipe = RecipeTest()
        tc_recipe.add_step(_id_step="aaaaaaaaaaaaaaaaaaaaaaaa", description="step1")
        tc_recipe.insert()
        """ param """
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "aaaaaaaaaaaaaaaaaaaaaaaa"
        tc_file = FileTest()
        tc_files = [('files', (tc_file.filename, tc_file.data, tc_file.mimetype))]
        """ call api """
        url = server.main_url + "/" + api.url_1 + "x/" + tc_id_recipe + "/" + api.url_2 + "/" + tc_id_step
        response = requests.post(url, files=tc_files, verify=False)
        response_body = response.json()
        """ close files """
        tc_file.close()
        """ change """
        tc_file.set_file_path(short_path="recipe/{0}/steps/{1}".format(tc_id_recipe, tc_id_step))
        """ assert """
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 405)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_405)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        self.assertEqual(response_body["detail"], rep.detail_method_not_allowed)
        """ check recipe """
        tc_recipe.check_bdd_data()
        """ check files """
        tc_file.check_file_not_exist()

    def test_api_url_not_found_2(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        tc_recipe = RecipeTest()
        tc_recipe.add_step(_id_step="aaaaaaaaaaaaaaaaaaaaaaaa", description="step1")
        tc_recipe.insert()
        """ param """
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "aaaaaaaaaaaaaaaaaaaaaaaa"
        tc_file = FileTest()
        tc_files = [('files', (tc_file.filename, tc_file.data, tc_file.mimetype))]
        """ call api """
        url = server.main_url + "/" + api.url_1 + "/" + tc_id_recipe + "/x" + api.url_2 + "/" + tc_id_step
        response = requests.post(url, files=tc_files, verify=False)
        response_body = response.json()
        """ close files """
        tc_file.close()
        """ change """
        tc_file.set_file_path(short_path="recipe/{0}/steps/{1}".format(tc_id_recipe, tc_id_step))
        """ assert """
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 405)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_405)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        self.assertEqual(response_body["detail"], rep.detail_method_not_allowed)
        """ check recipe """
        tc_recipe.check_bdd_data()
        """ check files """
        tc_file.check_file_not_exist()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestPostFilesRecipeStep())


if __name__ == '__main__':
    unittest.main()
