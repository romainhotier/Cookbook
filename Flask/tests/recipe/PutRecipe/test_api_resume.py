import unittest
import requests

import utils
import tests.recipe.PutRecipe.api as api
import tests.recipe.model as recipe_model

server = utils.Server()
api = api.PutRecipe()
recipe = recipe_model.RecipeTest()


class PutRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest."""
        recipe.clean()

    def test_resume_without(self):
        """ BodyParameter resume is missing.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail("body", msg=server.detail_must_contain_at_least_one_key, value=body)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_resume_none(self):
        """ BodyParameter resume is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_resume: None}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_resume, msg=server.detail_must_be_a_string, 
                                   value=body[api.param_resume])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_resume_empty(self):
        """ BodyParameter resume is an empty string.

        Return
            200 - Updated Recipe.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_resume: ""}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe.check_bdd_data()

    def test_resume_string(self):
        """ BodyParameter resume is a string.

        Return
            200 - Updated Recipe.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_resume: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe.check_bdd_data()

    def test_resume_tab(self):
        """ BodyParameter resume is an empty tab.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_resume: []}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_resume, msg=server.detail_must_be_a_string, 
                                   value=body[api.param_resume])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_resume_object(self):
        """ BodyParameter resume is an empty object.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_resume: {}}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_resume, msg=server.detail_must_be_a_string, 
                                   value=body[api.param_resume])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PutRecipe())


if __name__ == '__main__':
    unittest.main()
