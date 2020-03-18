import unittest
import requests

from server import factory as factory
import app.recipe.recipe.model as recipe_model
import app.recipe.recipe.test.PostRecipe.api as api

server = factory.Server()
api = api.PostRecipe()
recipe = recipe_model.RecipeTest()


class PostRecipe(unittest.TestCase):

    def setUp(self):
        recipe.clean()

    def test_0_api_ok(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        """ refacto """
        tc_recipe.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_0_api_ok_more_param(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                "invalid": "invalid"}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        """ refacto """
        tc_recipe.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_1_url_not_found(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url + "x"
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        tc_recipe.select_nok_by_title()

    def test_2_title_without(self):
        body = {api.param_slug: "slug"}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_title, server.detail_is_required, "missing")
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_2_title_none(self):
        body = {api.param_title: None,
                api.param_slug: "slug"}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_title, server.detail_must_be_a_string, body[api.param_title])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_2_title_empty(self):
        body = {api.param_title: "",
                api.param_slug: "slug"}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_title, server.detail_must_be_not_empty, body[api.param_title])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_2_title_string(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        """ refacto """
        tc_recipe.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_2_title_tab(self):
        body = {api.param_title: []}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_title, server.detail_must_be_a_string, body[api.param_title])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_2_title_object(self):
        body = {api.param_title: {}}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_title, server.detail_must_be_a_string, body[api.param_title])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_3_level_without(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        """ refacto """
        tc_recipe.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_3_level_none(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: None}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_level, server.detail_must_be_an_integer, body[api.param_level])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_3_level_empty(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: ""}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_level, server.detail_must_be_an_integer, body[api.param_level])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_3_level_string(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: "invalid"}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_level, server.detail_must_be_an_integer, body[api.param_level])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_3_level_integer_min_over(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: 5}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_level, server.detail_must_be_between + " 0 and 3", body[api.param_level])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_3_level_integer_min(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: 0}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        """ refacto """
        tc_recipe.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_3_level_integer_max(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: 3}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        """ refacto """
        tc_recipe.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_3_level_integer_max_over(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: 4}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_level, server.detail_must_be_between + " 0 and 3", body[api.param_level])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_3_level_tab(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: []}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_level, server.detail_must_be_an_integer, body[api.param_level])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_3_level_object(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: {}}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_level, server.detail_must_be_an_integer, body[api.param_level])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_4_resume_without(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        """ refacto """
        tc_recipe.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_4_resume_none(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_resume: None}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_resume, server.detail_must_be_a_string, body[api.param_resume])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_4_resume_empty(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_resume: ""}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        """ refacto """
        tc_recipe.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_4_resume_string(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_resume: "invalid"}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        """ refacto """
        tc_recipe.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_4_resume_tab(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_resume: []}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_resume, server.detail_must_be_a_string, body[api.param_resume])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_4_resume_object(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_resume: {}}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_resume, server.detail_must_be_a_string, body[api.param_resume])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_5_cooking_time_without(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"
                }
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        """ refacto """
        tc_recipe.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_5_cooking_time_none(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_cooking_time: None}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_cooking_time, server.detail_must_be_an_integer,
                                   body[api.param_cooking_time])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_5_cooking_time_empty(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_cooking_time: ""}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_cooking_time, server.detail_must_be_an_integer,
                                   body[api.param_cooking_time])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_5_cooking_time_string(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_cooking_time: "invalid"}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_cooking_time, server.detail_must_be_an_integer,
                                   body[api.param_cooking_time])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_5_cooking_time_integer(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_cooking_time: 5}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        """ refacto """
        tc_recipe.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_5_cooking_time_tab(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_cooking_time: []}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_cooking_time, server.detail_must_be_an_integer,
                                   body[api.param_cooking_time])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_5_cooking_time_object(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_cooking_time: {}}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_cooking_time, server.detail_must_be_an_integer,
                                   body[api.param_cooking_time])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_6_preparation_time_without(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        """ refacto """
        tc_recipe.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_6_preparation_time_none(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_preparation_time: None}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_preparation_time, server.detail_must_be_an_integer,
                                   body[api.param_preparation_time])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_6_preparation_time_empty(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_preparation_time: ""}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_preparation_time, server.detail_must_be_an_integer,
                                   body[api.param_preparation_time])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_6_preparation_time_string(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_preparation_time: "invalid"}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_preparation_time, server.detail_must_be_an_integer,
                                   body[api.param_preparation_time])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_6_preparation_time_integer(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_preparation_time: 5}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        """ refacto """
        tc_recipe.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_6_preparation_time_tab(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_preparation_time: []}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_preparation_time, server.detail_must_be_an_integer,
                                   body[api.param_preparation_time])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_6_preparation_time_object(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_preparation_time: {}}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_preparation_time, server.detail_must_be_an_integer,
                                   body[api.param_preparation_time])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_7_nb_people_without(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        """ refacto """
        tc_recipe.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_7_nb_people_none(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_nb_people: None}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_nb_people, server.detail_must_be_an_integer, body[api.param_nb_people])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_7_nb_people_empty(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_nb_people: ""}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_nb_people, server.detail_must_be_an_integer, body[api.param_nb_people])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_7_nb_people_string(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_nb_people: "invalid"}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_nb_people, server.detail_must_be_an_integer, body[api.param_nb_people])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_7_nb_people_integer(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_nb_people: 5}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        """ refacto """
        tc_recipe.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_7_nb_people_tab(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_nb_people: []}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_nb_people, server.detail_must_be_an_integer, body[api.param_nb_people])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_7_nb_people_object(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_nb_people: {}}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_nb_people, server.detail_must_be_an_integer, body[api.param_nb_people])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_8_note_without(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        """ refacto """
        tc_recipe.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_8_note_none(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_note: None}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_note, server.detail_must_be_a_string, body[api.param_note])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_8_note_empty(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_note: ""}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        """ refacto """
        tc_recipe.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_8_note_string(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_note: "invalid"}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        """ refacto """
        tc_recipe.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_8_note_tab(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_note: []}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_note, server.detail_must_be_a_string, body[api.param_note])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_8_note_object(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_note: {}}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_note, server.detail_must_be_a_string, body[api.param_note])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_9_steps_without(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        """ refacto """
        tc_recipe.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_9_steps_none(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_steps: None}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_steps, server.detail_must_be_an_array, body[api.param_steps])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_9_steps_empty(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_steps: ""}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_steps, server.detail_must_be_an_array, body[api.param_steps])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_9_steps_string(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_steps: "invalid"}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_steps, server.detail_must_be_an_array, body[api.param_steps])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_9_steps_tab(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_steps: []}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        """ refacto """
        tc_recipe.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_9_steps_object(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_steps: {}}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_steps, server.detail_must_be_an_array, body[api.param_steps])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_10_categories_without(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        """ refacto """
        tc_recipe.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_10_categories_none(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_categories: None}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_categories, server.detail_must_be_an_array, body[api.param_categories])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_10_categories_empty(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_categories: ""}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_categories, server.detail_must_be_an_array, body[api.param_categories])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_10_categories_string(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_categories: "invalid"}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_categories, server.detail_must_be_an_array, body[api.param_categories])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_10_categories_tab(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_categories: []}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        """ refacto """
        tc_recipe.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_10_categories_object(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_categories: {}}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_categories, server.detail_must_be_an_array, body[api.param_categories])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_11_slug_without(self):
        body = {api.param_title: "qa_rhr_title"}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_slug, server.detail_is_required, "missing")
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_11_slug_none(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: None}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_slug, server.detail_must_be_a_string, body[api.param_slug])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_11_slug_empty(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: ""}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_slug, server.detail_must_be_not_empty, body[api.param_slug])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_11_slug_string(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        """ refacto """
        tc_recipe.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_11_slug_tab(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: []}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_slug, server.detail_must_be_a_string, body[api.param_slug])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_11_slug_object(self):
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: {}}
        tc_recipe = recipe_model.RecipeTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_slug, server.detail_must_be_a_string, body[api.param_slug])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_nok_by_title()

    def test_12_title_already_exist(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        body = {api.param_title: tc_recipe.get_data_value("title"),
                api.param_slug: "slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_title, server.detail_already_exist, body[api.param_title])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostRecipe())


if __name__ == '__main__':
    unittest.main()
