import unittest
import requests

import utils
import tests.ingredient.PostIngredient.api as api
import tests.ingredient.model as ingredient_model

server = utils.Server()
api = api.PostIngredient()
ingredient = ingredient_model.IngredientTest()


class PostIngredient(unittest.TestCase):

    def setUp(self):
        """ Clean IngredientTest."""
        ingredient.clean()

    def test_nutriments_without(self):
        """ BodyParameter nutriments is missing.

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
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_ingredient.custom_id_from_body(data=response_body).check_bdd_data()

    def test_nutriments_null(self):
        """ BodyParameter nutriments is null.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: None}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nutriments, msg=server.detail_must_be_an_object,
                                   value=body[api.param_nutriments])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_nutriments_empty(self):
        """ BodyParameter nutriments is an empty string.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: ""}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nutriments, msg=server.detail_must_be_an_object,
                                   value=body[api.param_nutriments])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_nutriments_invalid(self):
        """ BodyParameter nutriments is a string.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nutriments, msg=server.detail_must_be_an_object,
                                   value=body[api.param_nutriments])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_nutriments_tab(self):
        """ BodyParameter nutriments is an empty tab.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: []}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nutriments, msg=server.detail_must_be_an_object,
                                   value=body[api.param_nutriments])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_nutriments_object(self):
        """ BodyParameter nutriments is an object.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nutriments+"."+api.param_nutriments_calories, 
                                   msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_nutriments_calories_without(self):
        """ BodyParameter nutriments.calories is missing.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_carbohydrates: 0,
                                       api.param_nutriments_fats: 0,
                                       api.param_nutriments_proteins: 0,
                                       api.param_nutriments_portion: 1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nutriments+"."+api.param_nutriments_calories, 
                                   msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_nutriments_calories_null(self):
        """ BodyParameter nutriments.calories is null.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: None,
                                       api.param_nutriments_carbohydrates: 0,
                                       api.param_nutriments_fats: 0,
                                       api.param_nutriments_proteins: 0,
                                       api.param_nutriments_portion: 1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nutriments+"."+api.param_nutriments_calories,
                                   msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_nutriments_calories])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_nutriments_calories_empty(self):
        """ BodyParameter nutriments.calories is an empty string.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: "",
                                       api.param_nutriments_carbohydrates: 0,
                                       api.param_nutriments_fats: 0,
                                       api.param_nutriments_proteins: 0,
                                       api.param_nutriments_portion: 1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nutriments+"."+api.param_nutriments_calories,
                                   msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_nutriments_calories])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_nutriments_calories_invalid(self):
        """ BodyParameter nutriments.calories is a string.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: "invalid",
                                       api.param_nutriments_carbohydrates: 0,
                                       api.param_nutriments_fats: 0,
                                       api.param_nutriments_proteins: 0,
                                       api.param_nutriments_portion: 1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nutriments+"."+api.param_nutriments_calories,
                                   msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_nutriments_calories])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_nutriments_calories_string_number(self):
        """ BodyParameter nutriments.calories is a string number.

        Return
            201 - Inserted Ingredient.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: "1.1",
                                       api.param_nutriments_carbohydrates: 0,
                                       api.param_nutriments_fats: 0,
                                       api.param_nutriments_proteins: 0,
                                       api.param_nutriments_portion: 1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_ingredient.custom_id_from_body(data=response_body).check_bdd_data()

    def test_nutriments_calories_number(self):
        """ BodyParameter nutriments.calories is a number.

        Return
            201 - Inserted Ingredient.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: 1.1,
                                       api.param_nutriments_carbohydrates: 0,
                                       api.param_nutriments_fats: 0,
                                       api.param_nutriments_proteins: 0,
                                       api.param_nutriments_portion: 1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_ingredient.custom_id_from_body(data=response_body).check_bdd_data()

    def test_nutriments_carbohydrates_without(self):
        """ BodyParameter nutriments.carbohydrates is missing.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: 0,
                                       api.param_nutriments_fats: 0,
                                       api.param_nutriments_proteins: 0,
                                       api.param_nutriments_portion: 1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nutriments+"."+api.param_nutriments_carbohydrates,
                                   msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_nutriments_carbohydrates_null(self):
        """ BodyParameter nutriments.carbohydrates is null.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: 0,
                                       api.param_nutriments_carbohydrates: None,
                                       api.param_nutriments_fats: 0,
                                       api.param_nutriments_proteins: 0,
                                       api.param_nutriments_portion: 1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nutriments+"."+api.param_nutriments_carbohydrates,
                                   msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_nutriments_carbohydrates])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_nutriments_carbohydrates_empty(self):
        """ BodyParameter nutriments.carbohydrates is an empty string.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: 0,
                                       api.param_nutriments_carbohydrates: "",
                                       api.param_nutriments_fats: 0,
                                       api.param_nutriments_proteins: 0,
                                       api.param_nutriments_portion: 1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nutriments+"."+api.param_nutriments_carbohydrates,
                                   msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_nutriments_carbohydrates])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_nutriments_carbohydrates_invalid(self):
        """ BodyParameter nutriments.carbohydrates is a string.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: 0,
                                       api.param_nutriments_carbohydrates: "invalid",
                                       api.param_nutriments_fats: 0,
                                       api.param_nutriments_proteins: 0,
                                       api.param_nutriments_portion: 1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nutriments+"."+api.param_nutriments_carbohydrates,
                                   msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_nutriments_carbohydrates])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_nutriments_carbohydrates_string_number(self):
        """ BodyParameter nutriments.carbohydrates is a string number.

        Return
            201 - Inserted Ingredient.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: 0,
                                       api.param_nutriments_carbohydrates: "1.1",
                                       api.param_nutriments_fats: 0,
                                       api.param_nutriments_proteins: 0,
                                       api.param_nutriments_portion: 1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_ingredient.custom_id_from_body(data=response_body).check_bdd_data()

    def test_nutriments_carbohydrates_number(self):
        """ BodyParameter nutriments.carbohydrates is a number.

        Return
            201 - Inserted Ingredient.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: 0,
                                       api.param_nutriments_carbohydrates: 1.1,
                                       api.param_nutriments_fats: 0,
                                       api.param_nutriments_proteins: 0,
                                       api.param_nutriments_portion: 1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_ingredient.custom_id_from_body(data=response_body).check_bdd_data()

    def test_nutriments_fats_without(self):
        """ BodyParameter nutriments.fats is missing.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: 0,
                                       api.param_nutriments_carbohydrates: 0,
                                       api.param_nutriments_proteins: 0,
                                       api.param_nutriments_portion: 1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nutriments+"."+api.param_nutriments_fats,
                                   msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_nutriments_fats_null(self):
        """ BodyParameter nutriments.fats is null.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: 0,
                                       api.param_nutriments_carbohydrates: 0,
                                       api.param_nutriments_fats: None,
                                       api.param_nutriments_proteins: 0,
                                       api.param_nutriments_portion: 1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nutriments+"."+api.param_nutriments_fats,
                                   msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_nutriments_fats])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_nutriments_fats_empty(self):
        """ BodyParameter nutriments.fats is an empty string.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: 0,
                                       api.param_nutriments_carbohydrates: 0,
                                       api.param_nutriments_fats: "",
                                       api.param_nutriments_proteins: 0,
                                       api.param_nutriments_portion: 1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nutriments+"."+api.param_nutriments_fats,
                                   msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_nutriments_fats])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_nutriments_fats_invalid(self):
        """ BodyParameter nutriments.fats is a string.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: 0,
                                       api.param_nutriments_carbohydrates: 0,
                                       api.param_nutriments_fats: "invalid",
                                       api.param_nutriments_proteins: 0,
                                       api.param_nutriments_portion: 1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nutriments+"."+api.param_nutriments_fats,
                                   msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_nutriments_fats])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_nutriments_fats_string_number(self):
        """ BodyParameter nutriments.fats is a string number.

        Return
            201 - Inserted Ingredient.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: 0,
                                       api.param_nutriments_carbohydrates: 0,
                                       api.param_nutriments_fats: "1.1",
                                       api.param_nutriments_proteins: 0,
                                       api.param_nutriments_portion: 1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_ingredient.custom_id_from_body(data=response_body).check_bdd_data()

    def test_nutriments_fats_number(self):
        """ BodyParameter nutriments.fats is a number.

        Return
            201 - Inserted Ingredient.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: 0,
                                       api.param_nutriments_carbohydrates: 0,
                                       api.param_nutriments_fats: 1.1,
                                       api.param_nutriments_proteins: 0,
                                       api.param_nutriments_portion: 1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        print(response_body)
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_ingredient.custom_id_from_body(data=response_body).check_bdd_data()

    def test_nutriments_proteins_without(self):
        """ BodyParameter nutriments.proteins is missing.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: 0,
                                       api.param_nutriments_carbohydrates: 0,
                                       api.param_nutriments_fats: 0,
                                       api.param_nutriments_portion: 1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nutriments+"."+api.param_nutriments_proteins,
                                   msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_nutriments_proteins_null(self):
        """ BodyParameter nutriments.proteins is null.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: 0,
                                       api.param_nutriments_carbohydrates: 0,
                                       api.param_nutriments_fats: 0,
                                       api.param_nutriments_proteins: None,
                                       api.param_nutriments_portion: 1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nutriments+"."+api.param_nutriments_proteins,
                                   msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_nutriments_proteins])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_nutriments_proteins_empty(self):
        """ BodyParameter nutriments.proteins is an empty string.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: 0,
                                       api.param_nutriments_carbohydrates: 0,
                                       api.param_nutriments_fats: 0,
                                       api.param_nutriments_proteins: "",
                                       api.param_nutriments_portion: 1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nutriments+"."+api.param_nutriments_proteins,
                                   msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_nutriments_proteins])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_nutriments_proteins_invalid(self):
        """ BodyParameter nutriments.proteins is a string.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: 0,
                                       api.param_nutriments_carbohydrates: 0,
                                       api.param_nutriments_fats: 0,
                                       api.param_nutriments_proteins: "invalid",
                                       api.param_nutriments_portion: 1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nutriments+"."+api.param_nutriments_proteins,
                                   msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_nutriments_proteins])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_nutriments_proteins_string_number(self):
        """ BodyParameter nutriments.proteins is a string number.

        Return
            201 - Inserted Ingredient.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: 0,
                                       api.param_nutriments_carbohydrates: 0,
                                       api.param_nutriments_fats: 0,
                                       api.param_nutriments_proteins: "1.1",
                                       api.param_nutriments_portion: 1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_ingredient.custom_id_from_body(data=response_body).check_bdd_data()

    def test_nutriments_proteins_number(self):
        """ BodyParameter nutriments.proteins is a number.

        Return
            201 - Inserted Ingredient.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: 0,
                                       api.param_nutriments_carbohydrates: 0,
                                       api.param_nutriments_fats: 0,
                                       api.param_nutriments_proteins: 1.1,
                                       api.param_nutriments_portion: 1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_ingredient.custom_id_from_body(data=response_body).check_bdd_data()

    def test_nutriments_portion_without(self):
        """ BodyParameter nutriments.portion is missing.

        Return
            201 - Inserted Ingredient.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: 0,
                                       api.param_nutriments_carbohydrates: 0,
                                       api.param_nutriments_fats: 0,
                                       api.param_nutriments_proteins: 0}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nutriments+"."+api.param_nutriments_portion,
                                   msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_nutriments_portion_null(self):
        """ BodyParameter nutriments.portion is null.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: 0,
                                       api.param_nutriments_carbohydrates: 0,
                                       api.param_nutriments_fats: 0,
                                       api.param_nutriments_proteins: 0,
                                       api.param_nutriments_portion: None}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nutriments+"."+api.param_nutriments_portion,
                                   msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_nutriments_portion])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_nutriments_portion_empty(self):
        """ BodyParameter nutriments.portion is an empty string.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: 0,
                                       api.param_nutriments_carbohydrates: 0,
                                       api.param_nutriments_fats: 0,
                                       api.param_nutriments_proteins: 0,
                                       api.param_nutriments_portion: ""}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nutriments+"."+api.param_nutriments_portion,
                                   msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_nutriments_portion])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_nutriments_portion_invalid(self):
        """ BodyParameter nutriments.portion is a string.

        Return
            201 - Inserted Ingredient.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: 0,
                                       api.param_nutriments_carbohydrates: 0,
                                       api.param_nutriments_fats: 0,
                                       api.param_nutriments_proteins: 0,
                                       api.param_nutriments_portion: "invalid"}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nutriments+"."+api.param_nutriments_portion,
                                   msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_nutriments_portion])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()
        
    def test_nutriments_portion_string_number(self):
        """ BodyParameter nutriments.portion is a string number.

        Return
            201 - Inserted Ingredient.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: 0,
                                       api.param_nutriments_carbohydrates: 0,
                                       api.param_nutriments_fats: 0,
                                       api.param_nutriments_proteins: 0,
                                       api.param_nutriments_portion: "1.1"}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_ingredient.custom_id_from_body(data=response_body).check_bdd_data()
        
    def test_nutriments_portion_number(self):
        """ BodyParameter nutriments.portion is a number.

        Return
            201 - Inserted Ingredient.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_nutriments_calories: 0,
                                       api.param_nutriments_carbohydrates: 0,
                                       api.param_nutriments_fats: 0,
                                       api.param_nutriments_proteins: 0,
                                       api.param_nutriments_portion: 1.1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_ingredient.custom_id_from_body(data=response_body).check_bdd_data()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostIngredient())


if __name__ == '__main__':
    unittest.main()
