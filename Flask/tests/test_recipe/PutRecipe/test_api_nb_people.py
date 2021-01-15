import unittest
import requests

from tests import server, rep
from tests.test_recipe import RecipeTest
from tests.test_recipe.PutRecipe import api


class TestPutRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest."""
        RecipeTest().clean()

    def test_nb_people_without(self):
        """ BodyParameter nb_people is missing.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
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
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param="body", msg=rep.detail_must_contain_at_least_one_key, value=body)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_nb_people_none(self):
        """ BodyParameter nb_people is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_nb_people: None}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_nb_people, msg=rep.detail_must_be_an_integer,
                                   value=body[api.param_nb_people])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_nb_people_empty(self):
        """ BodyParameter nb_people is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_nb_people: ""}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_nb_people, msg=rep.detail_must_be_an_integer,
                                   value=body[api.param_nb_people])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_nb_people_string(self):
        """ BodyParameter nb_people is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_nb_people: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_nb_people, msg=rep.detail_must_be_an_integer,
                                   value=body[api.param_nb_people])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_nb_people_integer(self):
        """ BodyParameter nb_people is a number.

        Return
            200 - Updated Recipe.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_nb_people: 5}
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
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))
        """ check """
        tc_recipe.check_bdd_data()

    def test_nb_people_tab(self):
        """ BodyParameter nb_people is an empty tab.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_nb_people: []}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_nb_people, msg=rep.detail_must_be_an_integer,
                                   value=body[api.param_nb_people])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_nb_people_object(self):
        """ BodyParameter nb_people is an empty object.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_nb_people: {}}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_nb_people, msg=rep.detail_must_be_an_integer,
                                   value=body[api.param_nb_people])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestPutRecipe())


if __name__ == '__main__':
    unittest.main()
