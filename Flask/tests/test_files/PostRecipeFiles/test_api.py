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

file_paths = api.get_files_path_for_test()


class PostRecipeFiles(unittest.TestCase):

    def setUp(self):
        """ Clean all FileTest and RecipeTest """
        recipe.clean()
        file.clean()
        pass

    def test_api_ok(self):
        """ Default case

        Return
            201 - FileTests.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        tmp_files = api.format_files_multipart(paths=file_paths)
        tc_multipart = tmp_files[0]
        tc_files_open = tmp_files[1]
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, files=tc_multipart, verify=False)
        response_body = response.json()
        """ close files """
        api.close_files(files_open=tc_files_open)
        """ change """
        tc_file1 = files_model.FilesTest().set_path(kind="recipe", _id=tc_id, path=file_paths[0])
        tc_file2 = files_model.FilesTest().set_path(kind="recipe", _id=tc_id, path=file_paths[1])
        tc_file3 = files_model.FilesTest().set_path(kind="recipe", _id=tc_id, path=file_paths[2])
        tc_recipe.add_files_recipe(files=[tc_file1, tc_file2, tc_file3])
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(recipe_id=tc_id, file_paths=file_paths))
        """ check recipe """
        tc_recipe.check_bdd_data()
        """ check file """
        tc_file1.check_file_exist()
        tc_file2.check_file_exist()
        tc_file3.check_file_exist()

    def test_api_ok_more_param(self):
        """ Default case with more param

        Return
            201 - FileTests.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_file1 = files_model.FilesTest().set_path(kind="recipe", _id=tc_recipe.get_id(), path=file_paths[0]).insert()
        tc_recipe.add_files_recipe(files=[tc_file1], mongo=True)
        """ param """
        tc_id = tc_recipe.get_id()
        tmp_files = api.format_files_multipart(paths=file_paths[1:3])
        tc_multipart = tmp_files[0]
        tc_files_open = tmp_files[1]
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        body = {"invalid": "invalid"}
        response = requests.post(url, files=tc_multipart, verify=False)
        response_body = response.json()
        """ close files """
        api.close_files(files_open=tc_files_open)
        """ change """
        tc_file2 = files_model.FilesTest().set_path(kind="recipe", _id=tc_id, path=file_paths[1])
        tc_file3 = files_model.FilesTest().set_path(kind="recipe", _id=tc_id, path=file_paths[2])
        tc_recipe.add_files_recipe(files=[tc_file2, tc_file3])
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(recipe_id=tc_id, file_paths=file_paths[1:3]))
        """ check recipe """
        tc_recipe.check_bdd_data()
        """ check file """
        tc_file1.check_file_exist()
        tc_file2.check_file_exist()
        tc_file3.check_file_exist()
    #
    # def test_api_url_not_found(self):
    #     """ Wrong url.
    #
    #     Return
    #         404 - Url not found.
    #     """
    #     """ env """
    #     tc_recipe = recipe_model.RecipeTest().insert()
    #     """ param """
    #     tc_id = tc_recipe.get_id()
    #     body = {api.param_path: file_path,
    #             api.param_filename: "qa_rhr_filename",
    #             api.param_is_main: False}
    #     """ call api """
    #     url = server.main_url + "/" + api.url + "x/" + tc_id
    #     response = requests.post(url, json=body, verify=False)
    #     response_body = response.json()
    #     """ assert """
    #     self.assertEqual(response.status_code, 404)
    #     self.assertEqual(response.headers["Content-Type"], "application/json")
    #     self.assertEqual(response_body["codeStatus"], 404)
    #     self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
    #     self.assertTrue(api.check_not_present(value="data", rep=response_body))
    #     self.assertEqual(response_body["detail"], server.detail_url_not_found)
    #     """ check file """
    #     file_model.FileTest().custom_id_from_body(data=body).check_doesnt_exist_by_filename()

    @classmethod
    def tearDownClass(cls):
        #cls.setUp(PostRecipeFiles())
        pass


if __name__ == '__main__':
    unittest.main()
