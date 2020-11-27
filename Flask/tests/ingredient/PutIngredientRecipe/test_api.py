import unittest
import requests

import utils
import tests.ingredient.PutIngredientRecipe.api as api
import tests.ingredient.model as ingredient_model

server = utils.Server()
api = api.PutIngredientRecipe()
link = ingredient_model.IngredientRecipeTest()


class PutIngredientRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean IngredientRecipeTest."""
        link.clean()

    def test_0_api_ok(self):
        """ Default case.

        Return
            200 - Updated IngredientRecipe.
        """
        """ env """
        tc_link = ingredient_model.IngredientRecipeTest().insert()
        """ param """  
        tc_id = tc_link.get_id()
        body = {api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit_up"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(link=tc_link))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_link.select_ok()

    def test_0_api_ok_more_param(self):
        """ Default case with more parameters.

        Return
            200 - Updated IngredientRecipe.
        """
        """ env """
        tc_link = ingredient_model.IngredientRecipeTest().insert()
        """ param """        
        tc_id = tc_link.get_id()
        body = {api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit_up",
                "invalid": "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(link=tc_link))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_link.select_ok()

    def test_1_url_not_found(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        tc_link = ingredient_model.IngredientRecipeTest().insert()
        """ param """        
        tc_id = tc_link.get_id()
        body = {api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit_up"}
        """ call api """
        url = server.main_url + "/x" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        """ check """
        tc_link.select_ok()

    def test_2_id_without(self):
        """ QueryParameter _id is missing.

        Return
            404 - Url not found.
        """
        """ env """
        tc_link = ingredient_model.IngredientRecipeTest().insert()
        """ param """
        body = {api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit_up"}
        """ call api """
        url = server.main_url + "/" + api.url + "/"
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        """ check """
        tc_link.select_ok()

    def test_2_id_string(self):
        """ QueryParameter _id is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_link = ingredient_model.IngredientRecipeTest().insert()
        """ param """
        tc_id = "invalid"
        body = {api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit_up"}
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
        detail = api.create_detail(param=api.param_id, msg=server.detail_must_be_an_object_id, value=tc_id)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_ok()

    def test_2_id_object_id_invalid(self):
        """ QueryParameter _id is a nok ObjectId.

        Return
            400 - Bad request.
        """
        """ env """
        tc_link = ingredient_model.IngredientRecipeTest().insert()
        """ param """
        tc_id = "aaaaaaaaaaaaaaaaaaaaaaaa"
        body = {api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit_up"}
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
        detail = api.create_detail(param=api.param_id, msg=server.detail_doesnot_exist, value=tc_id)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_ok()

    def test_3_quantity_without(self):
        """ BodyParameter quantity is missing.

        Return
            200 - Updated IngredientRecipe.
        """
        """ env """
        tc_link = ingredient_model.IngredientRecipeTest().insert()
        """ param """        
        tc_id = tc_link.get_id()
        body = {api.param_unit: "qa_rhr_unit_up"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(link=tc_link))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_link.select_ok()

    def test_3_quantity_null(self):
        """ BodyParameter quantity is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_link = ingredient_model.IngredientRecipeTest().insert()
        """ param """        
        tc_id = tc_link.get_id()
        body = {api.param_quantity: None,
                api.param_unit: "qa_rhr_unit_up"}
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
        detail = api.create_detail(param=api.param_quantity, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_quantity])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_ok()

    def test_3_quantity_empty(self):
        """ BodyParameter quantity is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_link = ingredient_model.IngredientRecipeTest().insert()
        """ param """        
        tc_id = tc_link.get_id()
        body = {api.param_quantity: "",
                api.param_unit: "qa_rhr_unit_up"}
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
        detail = api.create_detail(param=api.param_quantity, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_quantity])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_ok()

    def test_3_quantity_string(self):
        """ BodyParameter quantity is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_link = ingredient_model.IngredientRecipeTest().insert()
        """ param """        
        tc_id = tc_link.get_id()
        body = {api.param_quantity: "invalid",
                api.param_unit: "qa_rhr_unit_up"}
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
        detail = api.create_detail(param=api.param_quantity, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_quantity])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_ok()

    def test_4_unit_without(self):
        """ BodyParameter unit is missing.

        Return
            200 - Updated IngredientRecipe.
        """
        """ env """
        tc_link = ingredient_model.IngredientRecipeTest().insert()
        """ param """        
        tc_id = tc_link.get_id()
        body = {api.param_quantity: 5}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(link=tc_link))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_link.select_ok()

    def test_4_unit_null(self):
        """ BodyParameter unit is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_link = ingredient_model.IngredientRecipeTest().insert()
        """ param """        
        tc_id = tc_link.get_id()
        body = {api.param_quantity: 5,
                api.param_unit: None}
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
        detail = api.create_detail(param=api.param_unit, msg=server.detail_must_be_a_string, value=body[api.param_unit])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_ok()

    def test_4_unit_empty(self):
        """ BodyParameter unit is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_link = ingredient_model.IngredientRecipeTest().insert()
        """ param """        
        tc_id = tc_link.get_id()
        body = {api.param_quantity: 5,
                api.param_unit: ""}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(link=tc_link))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_link.select_ok()

    def test_4_unit_string(self):
        """ BodyParameter unit is string.

        Return
            200 - Updated IngredientRecipe.
        """
        """ env """
        tc_link = ingredient_model.IngredientRecipeTest().insert()
        """ param """        
        tc_id = tc_link.get_id()
        body = {api.param_quantity: 5,
                api.param_unit: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(link=tc_link))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_link.select_ok()

    def test_5_without_nothing(self):
        """ BodyParameter no one.

        Return
            400 - Bad request.
        """
        """ env """
        tc_link = ingredient_model.IngredientRecipeTest().insert()
        """ param """        
        tc_id = tc_link.get_id()
        body = {}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail("body", msg=server.detail_must_contain_at_least_one_key, value=body)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_ok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PutIngredientRecipe())


if __name__ == '__main__':
    unittest.main()
