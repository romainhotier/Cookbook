import unittest
import requests

import utils
import tests.ingredient.PostIngredient.api as api
import tests.ingredient.model as ingredient_model
import tests.file.model as file_model

server = utils.Server()
api = api.PostIngredient()
ingredient = ingredient_model.IngredientTest()
file = file_model.FileTest()


class PostIngredient(unittest.TestCase):

    def setUp(self):
        ingredient.clean()

    def test_0_api_ok(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ refacto """
        tc_ingredient.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_0_api_ok_more_param(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                "invalid": "invalid",
                api.param_nutriments: {api.param_calories: 0,
                                       api.param_carbohydrates: 0,
                                       api.param_fats: 0,
                                       api.param_proteins: 0,
                                       api.param_info: "per 100g",
                                       "invalid": "invalid"}
                }
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ refacto """
        tc_ingredient.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_1_url_not_found(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug"}
        """ call api """
        url = server.main_url + "/" + api.url + "x"
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        tc_ingredient.select_nok_by_name()

    def test_2_name_without(self):
        body = {api.param_slug: "qa_rhr_slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_name, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_2_name_none(self):
        body = {api.param_name: None,
                api.param_slug: "qa_rhr_slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_name, msg=server.detail_must_be_a_string, value=body[api.param_name])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_2_name_empty(self):
        body = {api.param_name: "",
                api.param_slug: "qa_rhr_slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_name, msg=server.detail_must_be_not_empty,
                                   value=body[api.param_name])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_2_name_string(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ refacto """
        tc_ingredient.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_3_name_already_exist(self):
        tc_ingredient = ingredient_model.IngredientTest().insert()
        body = {api.param_name: tc_ingredient.name,
                api.param_slug: "qa_rhr_slug_2nd"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_name, msg=server.detail_already_exist, value=body[api.param_name])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_ok()

    def test_4_slug_without(self):
        body = {api.param_name: "qa_rhr_name"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_slug, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_4_slug_none(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: None}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_slug, msg=server.detail_must_be_a_string, value=body[api.param_slug])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_4_slug_empty(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: ""}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_slug, msg=server.detail_must_be_not_empty,
                                   value=body[api.param_slug])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_4_slug_string(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ refacto """
        tc_ingredient.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_4_slug_already_exist(self):
        tc_ingredient = ingredient_model.IngredientTest().insert()
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
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_slug, msg=server.detail_already_exist, value=body[api.param_slug])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_ok()

    def test_5_categories_without(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ refacto """
        tc_ingredient.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_5_categories_none(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_categories: None}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_categories, msg=server.detail_must_be_an_array,
                                   value=body[api.param_categories])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_5_categories_empty(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_categories: ""}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_categories, msg=server.detail_must_be_an_array,
                                   value=body[api.param_categories])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_5_categories_string(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_categories: "qa_rhr_category"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_categories, msg=server.detail_must_be_an_array,
                                   value=body[api.param_categories])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_5_categories_tab(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_categories: []}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ refacto """
        tc_ingredient.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_5_categories_tab_2(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_categories: [None, "", "invalid"]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ refacto """
        tc_ingredient.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_6_nutriments_without(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ refacto """
        tc_ingredient.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_6_nutriments_null(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: None}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
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
        tc_ingredient.select_nok_by_name()

    def test_6_nutriments_empty(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: ""}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
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
        tc_ingredient.select_nok_by_name()

    def test_6_nutriments_invalid(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
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
        tc_ingredient.select_nok_by_name()

    def test_6_nutriments_tab(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: []}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
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
        tc_ingredient.select_nok_by_name()

    def test_6_nutriments_object(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_calories, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_7_nutriments_calories_without(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_carbohydrates: 0,
                                       api.param_fats: 0,
                                       api.param_proteins: 0}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_calories, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_7_nutriments_calories_null(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: None,
                                       api.param_carbohydrates: 0,
                                       api.param_fats: 0,
                                       api.param_proteins: 0}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_calories, msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_calories])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_7_nutriments_calories_empty(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: "",
                                       api.param_carbohydrates: 0,
                                       api.param_fats: 0,
                                       api.param_proteins: 0}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_calories, msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_calories])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_7_nutriments_calories_invalid(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: "invalid",
                                       api.param_carbohydrates: 0,
                                       api.param_fats: 0,
                                       api.param_proteins: 0}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_calories, msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_calories])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_7_nutriments_calories_string_number(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: "1.1",
                                       api.param_carbohydrates: 0,
                                       api.param_fats: 0,
                                       api.param_proteins: 0}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ refacto """
        tc_ingredient.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_7_nutriments_calories_number(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: 1.1,
                                       api.param_carbohydrates: 0,
                                       api.param_fats: 0,
                                       api.param_proteins: 0}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ refacto """
        tc_ingredient.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_8_nutriments_carbohydrates_without(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: 0,
                                       api.param_fats: 0,
                                       api.param_proteins: 0}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_carbohydrates, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_8_nutriments_carbohydrates_null(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: 0,
                                       api.param_carbohydrates: None,
                                       api.param_fats: 0,
                                       api.param_proteins: 0}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_carbohydrates, msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_carbohydrates])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_8_nutriments_carbohydrates_empty(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: 0,
                                       api.param_carbohydrates: "",
                                       api.param_fats: 0,
                                       api.param_proteins: 0}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_carbohydrates, msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_carbohydrates])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_8_nutriments_carbohydrates_invalid(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: 0,
                                       api.param_carbohydrates: "invalid",
                                       api.param_fats: 0,
                                       api.param_proteins: 0}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_carbohydrates, msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_carbohydrates])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_8_nutriments_carbohydrates_string_number(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: 0,
                                       api.param_carbohydrates: "1.1",
                                       api.param_fats: 0,
                                       api.param_proteins: 0}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ refacto """
        tc_ingredient.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_8_nutriments_carbohydrates_number(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: 0,
                                       api.param_carbohydrates: 1.1,
                                       api.param_fats: 0,
                                       api.param_proteins: 0}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ refacto """
        tc_ingredient.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_9_nutriments_fats_without(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: 0,
                                       api.param_carbohydrates: 0,
                                       api.param_proteins: 0}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_fats, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_9_nutriments_fats_null(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: 0,
                                       api.param_carbohydrates: 0,
                                       api.param_fats: None,
                                       api.param_proteins: 0}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_fats, msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_fats])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_9_nutriments_fats_empty(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: 0,
                                       api.param_carbohydrates: 0,
                                       api.param_fats: "",
                                       api.param_proteins: 0}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_fats, msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_fats])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_9_nutriments_fats_invalid(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: 0,
                                       api.param_carbohydrates: 0,
                                       api.param_fats: "invalid",
                                       api.param_proteins: 0}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_fats, msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_fats])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_9_nutriments_fats_string_number(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: 0,
                                       api.param_carbohydrates: 0,
                                       api.param_fats: "1.1",
                                       api.param_proteins: 0}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ refacto """
        tc_ingredient.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_9_nutriments_fats_number(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: 0,
                                       api.param_carbohydrates: 0,
                                       api.param_fats: 1.1,
                                       api.param_proteins: 0}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ refacto """
        tc_ingredient.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_10_nutriments_proteins_without(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: 0,
                                       api.param_carbohydrates: 0,
                                       api.param_fats: 0}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_proteins, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_10_nutriments_proteins_null(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: 0,
                                       api.param_carbohydrates: 0,
                                       api.param_fats: 0,
                                       api.param_proteins: None}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_proteins, msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_proteins])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_10_nutriments_proteins_empty(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: 0,
                                       api.param_carbohydrates: 0,
                                       api.param_fats: 0,
                                       api.param_proteins: ""}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_proteins, msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_proteins])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_10_nutriments_proteins_invalid(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: 0,
                                       api.param_carbohydrates: 0,
                                       api.param_fats: 0,
                                       api.param_proteins: "invalid"}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_proteins, msg=server.detail_must_be_a_float,
                                   value=body[api.param_nutriments][api.param_proteins])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_10_nutriments_proteins_string_number(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: 0,
                                       api.param_carbohydrates: 0,
                                       api.param_fats: 0,
                                       api.param_proteins: "1.1"}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ refacto """
        tc_ingredient.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_10_nutriments_proteins_number(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: 0,
                                       api.param_carbohydrates: 0,
                                       api.param_fats: 0,
                                       api.param_proteins: 1.1}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ refacto """
        tc_ingredient.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_11_nutriments_info_without(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: 0,
                                       api.param_carbohydrates: 0,
                                       api.param_fats: 0,
                                       api.param_proteins: 0}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ refacto """
        tc_ingredient.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_11_nutriments_info_null(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: 0,
                                       api.param_carbohydrates: 0,
                                       api.param_fats: 0,
                                       api.param_proteins: 0,
                                       api.param_info: None}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_info, msg=server.detail_must_be_a_string,
                                   value=body[api.param_nutriments][api.param_info])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_11_nutriments_info_empty(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: 0,
                                       api.param_carbohydrates: 0,
                                       api.param_fats: 0,
                                       api.param_proteins: 0,
                                       api.param_info: ""}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_info, msg=server.detail_must_be_not_empty,
                                   value=body[api.param_nutriments][api.param_info])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_11_nutriments_info_invalid(self):
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug",
                api.param_nutriments: {api.param_calories: 0,
                                       api.param_carbohydrates: 0,
                                       api.param_fats: 0,
                                       api.param_proteins: 0,
                                       api.param_info: "invalid"}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ refacto """
        tc_ingredient.custom({"_id": response_body["data"]["_id"]}).select_ok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostIngredient())


if __name__ == '__main__':
    unittest.main()
