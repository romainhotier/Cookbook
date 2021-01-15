import unittest
import requests

from tests import server, rep
from tests.test_ingredient import IngredientTest
from tests.test_ingredient.PutIngredient import api


class TestPutIngredient(unittest.TestCase):

    def setUp(self):
        """ Clean IngredientTest."""
        IngredientTest().clean()

    def test_id_without(self):
        """ QueryParameter _id is missing.

        Return
            404 - Url not found.
        """
        """ env """
        tc_ingredient = IngredientTest().insert()
        """ param """
        body = {api.param_name: "qa_rhr_name_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/"
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        self.assertEqual(response_body["detail"], rep.detail_url_not_found)
        """ check """
        tc_ingredient.check_bdd_data()

    def test_id_string(self):
        """ QueryParameter _id is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = IngredientTest().insert()
        """ param """
        tc_id = "invalid"
        body = {api.param_name: "qa_rhr_name_update"}
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
        detail = rep.format_detail(param=api.param_id, msg=rep.detail_must_be_an_object_id, value=tc_id)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_bdd_data()

    def test_id_object_id_invalid(self):
        """ QueryParameter _id is a nok ObjectId.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = IngredientTest().insert()
        """ param """
        tc_id = "aaaaaaaaaaaaaaaaaaaaaaaa"
        body = {api.param_name: "qa_rhr_name_update"}
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
        detail = rep.format_detail(param=api.param_id, msg=rep.detail_doesnot_exist, value=tc_id)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_bdd_data()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestPutIngredient())


if __name__ == '__main__':
    unittest.main()
