import unittest
import requests

import utils
import tests.recipe.PostRecipe.api as api
import tests.recipe.model as recipe_model

server = utils.Server()
api = api.PostRecipe()
recipe = recipe_model.RecipeTest()


class PostRecipe(unittest.TestCase):

    def setUp(self):
        recipe.clean()

    def test_0_api_ok(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_0_api_ok_more_param(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                "invalid": "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_1_url_not_found(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        """ call api """
        url = server.main_url + "/" + api.url + "x"
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        tc_recipe.select_nok_by_title()

    def test_2_title_without(self):
        body = {api.param_slug: "slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_title, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_2_title_none(self):
        body = {api.param_title: None,
                api.param_slug: "slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_title, msg=server.detail_must_be_a_string,
                                   value=body[api.param_title])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_2_title_empty(self):
        body = {api.param_title: "",
                api.param_slug: "slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_title, msg=server.detail_must_be_not_empty,
                                   value=body[api.param_title])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_2_title_string(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_2_title_tab(self):
        body = {api.param_title: []}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_title, msg=server.detail_must_be_a_string,
                                   value=body[api.param_title])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_2_title_object(self):
        body = {api.param_title: {}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_title, msg=server.detail_must_be_a_string,
                                   value=body[api.param_title])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_3_level_without(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_3_level_none(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: None}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_level, msg=server.detail_must_be_an_integer, 
                                   value=body[api.param_level])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_3_level_empty(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: ""}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_level, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_level])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_3_level_string(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_level, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_level])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_3_level_integer_min_over(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: 5}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_level, msg=server.detail_must_be_between + " 0 and 3",
                                   value=body[api.param_level])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_3_level_integer_min(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: 0}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_3_level_integer_max(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: 3}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_3_level_integer_max_over(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: 4}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_level, msg=server.detail_must_be_between + " 0 and 3",
                                   value=body[api.param_level])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_3_level_tab(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: []}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_level, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_level])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_3_level_object(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: {}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_level, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_level])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_4_resume_without(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_4_resume_none(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_resume: None}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_resume, msg=server.detail_must_be_a_string,
                                   value=body[api.param_resume])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_4_resume_empty(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_resume: ""}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_4_resume_string(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_resume: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_4_resume_tab(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_resume: []}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))

        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_resume, msg=server.detail_must_be_a_string,
                                   value=body[api.param_resume])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_4_resume_object(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_resume: {}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))

        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_resume, msg=server.detail_must_be_a_string,
                                   value=body[api.param_resume])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_5_cooking_time_without(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_5_cooking_time_none(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_cooking_time: None}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_cooking_time, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_cooking_time])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_5_cooking_time_empty(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_cooking_time: ""}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_cooking_time, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_cooking_time])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_5_cooking_time_string(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_cooking_time: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_cooking_time, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_cooking_time])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_5_cooking_time_integer(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_cooking_time: 5}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_5_cooking_time_tab(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_cooking_time: []}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_cooking_time, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_cooking_time])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_5_cooking_time_object(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_cooking_time: {}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_cooking_time, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_cooking_time])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_6_preparation_time_without(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_6_preparation_time_none(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_preparation_time: None}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_preparation_time, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_preparation_time])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_6_preparation_time_empty(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_preparation_time: ""}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_preparation_time, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_preparation_time])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_6_preparation_time_string(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_preparation_time: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_preparation_time, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_preparation_time])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_6_preparation_time_integer(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_preparation_time: 5}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_6_preparation_time_tab(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_preparation_time: []}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_preparation_time, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_preparation_time])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_6_preparation_time_object(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_preparation_time: {}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_preparation_time, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_preparation_time])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_7_nb_people_without(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_7_nb_people_none(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_nb_people: None}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))

        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nb_people, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_nb_people])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_7_nb_people_empty(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_nb_people: ""}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nb_people, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_nb_people])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_7_nb_people_string(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_nb_people: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nb_people, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_nb_people])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_7_nb_people_integer(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_nb_people: 5}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_7_nb_people_tab(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_nb_people: []}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nb_people, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_nb_people])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_7_nb_people_object(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_nb_people: {}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nb_people, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_nb_people])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_8_note_without(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_8_note_none(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_note: None}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_note, msg=server.detail_must_be_a_string, value=body[api.param_note])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_8_note_empty(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_note: ""}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_8_note_string(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_note: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_8_note_tab(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_note: []}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_note, msg=server.detail_must_be_a_string, value=body[api.param_note])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_8_note_object(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_note: {}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_note, msg=server.detail_must_be_a_string, value=body[api.param_note])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_9_status_without(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_9_status_none(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_status: None}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_status, msg=server.detail_must_be_in + api.rep_detail_status,
                                   value=body[api.param_status])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_9_status_empty(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_status: ""}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))

        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_status, msg=server.detail_must_be_in + api.rep_detail_status,
                                   value=body[api.param_status])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_9_status_string(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_status: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_status, msg=server.detail_must_be_in + api.rep_detail_status,
                                   value=body[api.param_status])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_9_status_in_progress(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_status: "in_progress"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_9_status_finished(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_status: "finished"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_10_categories_without(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_10_categories_none(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_categories: None}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_categories, msg=server.detail_must_be_an_array,
                                   value=body[api.param_categories])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_10_categories_empty(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_categories: ""}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_categories, msg=server.detail_must_be_an_array,
                                   value=body[api.param_categories])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_10_categories_string(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_categories: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_categories, msg=server.detail_must_be_an_array,
                                   value=body[api.param_categories])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_10_categories_tab(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_categories: []}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_10_categories_object(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_categories: {}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_categories, msg=server.detail_must_be_an_array,
                                   value=body[api.param_categories])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_11_slug_without(self):
        body = {api.param_title: "qa_rhr_title"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_slug, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_11_slug_none(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: None}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_slug, msg=server.detail_must_be_a_string, value=body[api.param_slug])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_11_slug_empty(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: ""}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_slug, msg=server.detail_must_be_not_empty,
                                   value=body[api.param_slug])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_11_slug_string(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_11_slug_tab(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: []}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_slug, msg=server.detail_must_be_a_string, value=body[api.param_slug])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_11_slug_object(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: {}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_slug, msg=server.detail_must_be_a_string, value=body[api.param_slug])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_nok_by_title()

    def test_12_title_already_exist(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        body = {api.param_title: tc_recipe.title,
                api.param_slug: "slug"}
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
        detail = api.create_detail(param=api.param_title, msg=server.detail_already_exist, value=body[api.param_title])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostRecipe())


if __name__ == '__main__':
    unittest.main()
