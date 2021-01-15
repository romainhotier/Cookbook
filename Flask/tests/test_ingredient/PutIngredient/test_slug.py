import unittest
import requests

from tests import server, rep
from tests.test_ingredient import IngredientTest
from tests.test_ingredient.PutIngredient import api


class TestPutIngredient(unittest.TestCase):

    def setUp(self):
        """ Clean IngredientTest."""
        IngredientTest().clean()

    def test_slug_without(self):
        """ BodyParameter slug is missing.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient.get_id()
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
        tc_ingredient.check_bdd_data()

    def test_slug_none(self):
        """ BodyParameter slug is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_slug: None}
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
        detail = rep.format_detail(param=api.param_slug, msg=rep.detail_must_be_a_string, value=body[api.param_slug])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_bdd_data()

    def test_slug_empty(self):
        """ BodyParameter slug is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_slug: ""}
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
        detail = rep.format_detail(param=api.param_slug, msg=rep.detail_must_be_not_empty, value=body[api.param_slug])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_bdd_data()

    def test_slug_string(self):
        """ BodyParameter slug is a string.

        Return
            200 - Updated Ingredient.
        """
        """ env """
        tc_ingredient = IngredientTest().custom({"slug": "qa_rhr_slug"}).insert()
        tc_id = tc_ingredient.get_id()
        """ param """
        body = {api.param_slug: "qa_rhr_slug_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(ingredient=tc_ingredient))
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))
        """ check """
        tc_ingredient.check_bdd_data()

    def test_slug_already_exist(self):
        """ BodyParameter slug already exist.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient1 = IngredientTest().custom({"slug": "qa_rhr_a"}).insert()
        tc_ingredient2 = IngredientTest().custom({"slug": "qa_rhr_b"}).insert()
        """ param """        
        tc_id = tc_ingredient1.get_id()
        body = {api.param_slug: tc_ingredient2.slug}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        detail = rep.format_detail(param=api.param_slug, msg=rep.detail_already_exist, value=body[api.param_slug])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient1.check_bdd_data()
        tc_ingredient2.check_bdd_data()

    def test_slug_already_exist_coherent(self):
        """ BodyParameter slug already exist but it's coherent.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient1 = IngredientTest().custom({"slug": "qa_rhr_a"}).insert()
        tc_ingredient2 = IngredientTest().custom({"slug": "qa_rhr_b"}).insert()
        """ param """
        tc_id = tc_ingredient1.get_id()
        body = {api.param_slug: tc_ingredient1.slug}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient1.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(ingredient=tc_ingredient1))
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))
        """ check """
        tc_ingredient1.check_bdd_data()
        tc_ingredient2.check_bdd_data()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestPutIngredient())


if __name__ == '__main__':
    unittest.main()
