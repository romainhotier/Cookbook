import unittest
import requests

from tests import server, rep
from tests.test_ingredient import IngredientTest
from tests.test_ingredient.PostIngredient import api


class TestPostIngredient(unittest.TestCase):

    def setUp(self):
        """ Clean IngredientTest."""
        IngredientTest().clean()

    def test_slug_without(self):
        """ BodyParameter slug is missing.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = IngredientTest().custom_from_body(data=body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_slug, msg=rep.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_slug_none(self):
        """ BodyParameter slug is null.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: None}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = IngredientTest().custom_from_body(data=body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_slug, msg=rep.detail_must_be_a_string, value=body[api.param_slug])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_slug_empty(self):
        """ BodyParameter slug is empty string.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: ""}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = IngredientTest().custom_from_body(data=body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_slug, msg=rep.detail_must_be_not_empty, value=body[api.param_slug])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_slug_string(self):
        """ BodyParameter slug is a string.

        Return
            201 - Inserted Ingredient.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = IngredientTest().custom_from_body(data=body)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = rep.json_schema_check(data=response_body["data"],
                                           schema=api.create_schema(ingredient=tc_ingredient))
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))
        """ check """
        tc_ingredient.custom_id_from_body(data=response_body).check_bdd_data()

    def test_slug_already_exist(self):
        """ BodyParameter slug already exist.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = IngredientTest().insert()
        """ param """
        body = {api.param_name: "qa_rhr_name_2nd",
                api.param_slug: tc_ingredient.slug}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_slug, msg=rep.detail_already_exist, value=body[api.param_slug])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_bdd_data()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestPostIngredient())


if __name__ == '__main__':
    unittest.main()
