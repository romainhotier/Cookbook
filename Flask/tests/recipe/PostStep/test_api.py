import unittest
import requests

import utils
import tests.recipe.PostStep.api as api

server = utils.Server
api = api.PostStep()


class PostStep(unittest.TestCase):

    def test_0_api_ok(self):
        body = {api.param_step: "step_information"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_data(response_body[api.rep_data]), api.format_response(body))

    def test_0_api_ok_more_param(self):
        body = {api.param_step: "step_information",
                "invalid": "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_data(response_body[api.rep_data]), api.format_response(body))

    def test_1_url_not_found(self):
        body = {api.param_step: "step_information"}
        """ call api """
        url = server.main_url + "/" + api.url + "x"
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 405)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_405)
        self.assertEqual(response_body[api.rep_detail], server.detail_method_not_allowed)

    def test_2_step_without(self):
        body = {}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_step, server.detail_is_required, "missing")
        self.assertEqual(response_body[api.rep_detail], detail)

    def test_2_step_null(self):
        body = {api.param_step: None}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_step, server.detail_must_be_a_string, body[api.param_step])
        self.assertEqual(response_body[api.rep_detail], detail)

    def test_2_step_empty(self):
        body = {api.param_step: ""}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_step, server.detail_must_be_not_empty, body[api.param_step])
        self.assertEqual(response_body[api.rep_detail], detail)

    def test_2_step_string(self):
        body = {api.param_step: "step_information"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_data(response_body[api.rep_data]), api.format_response(body))


if __name__ == '__main__':
    unittest.main()
