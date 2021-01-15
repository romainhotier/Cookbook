import unittest
import requests

from tests import server, rep
from tests.test_ingredient import IngredientTest
from tests.test_ingredient.GetIngredient import api


class TestGetIngredient(unittest.TestCase):

    def setUp(self):
        """ Clean IngredientTest. """
        IngredientTest().clean()

    def test_id_without(self):
        """ QueryParameter _id is missing.

        Return
            200 - Go to GetAllIngredient.
        """
        """ env """
        tc_ingredient1 = IngredientTest().insert()
        tc_ingredient2 = IngredientTest().insert()
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(ingredient=tc_ingredient1), response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient2), response_body["data"])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    def test_id_string(self):
        """ QueryParameter _id is a string.

        Return
            400 - Bad request.
        """
        """ env """
        IngredientTest().insert()
        """ param """
        tc_id = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_id, msg=rep.detail_must_be_an_object_id, value=tc_id)
        self.assertEqual(response_body["detail"], detail)

    def test_id_object_id_invalid(self):
        """ QueryParameter _id is a nok ObjectId.

        Return
            400 - Bad request.
        """
        """ env """
        IngredientTest().insert()
        """ param """
        tc_id = "aaaaaaaaaaaaaaaaaaaaaaaa"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_id, msg=rep.detail_doesnot_exist, value=tc_id)
        self.assertEqual(response_body["detail"], detail)

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestGetIngredient())


if __name__ == '__main__':
    unittest.main()
