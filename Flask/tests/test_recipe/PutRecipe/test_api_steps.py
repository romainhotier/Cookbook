import unittest
import requests

import utils
import tests.test_recipe.PutRecipe.api as api
import tests.test_recipe.model as recipe_model

server = utils.Server()
api = api.PutRecipe()
recipe = recipe_model.RecipeTest()


class PutRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest."""
        recipe.clean()

    def test_steps_without(self):
        """ BodyParameter steps is missing.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
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
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param="body", msg=server.detail_must_contain_at_least_one_key, value=body)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_steps_null(self):
        """ BodyParameter steps is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_steps: None}
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
        detail = api.create_detail(param=api.param_steps, msg=server.detail_must_be_an_array,
                                   value=body[api.param_steps])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_steps_empty(self):
        """ BodyParameter steps is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_steps: ""}
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
        detail = api.create_detail(param=api.param_steps, msg=server.detail_must_be_an_array,
                                   value=body[api.param_steps])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_steps_invalid(self):
        """ BodyParameter steps is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_steps: ""}
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
        detail = api.create_detail(param=api.param_steps, msg=server.detail_must_be_an_array,
                                   value=body[api.param_steps])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_steps_object(self):
        """ BodyParameter steps is an object.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_steps: {}}
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
        detail = api.create_detail(param=api.param_steps, msg=server.detail_must_be_an_array,
                                   value=body[api.param_steps])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_steps_tab(self):
        """ BodyParameter steps is a tab.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_steps: []}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.custom(api.clean_body(data=body))
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(api.response_without_steps(data=response_body["data"]),
                         api.data_expected_without_steps(recipe=tc_recipe))
        api.check_steps(recipe=tc_recipe, response_data=response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe.check_bdd_data()

    def test_steps_tab_reset(self):
        """ BodyParameter steps is a tab reset.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="aaaaaaaaaaaaaaaaaaaaaaaa", description="step")
        tc_recipe.insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_steps: []}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.custom(api.clean_body(data=body))
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(api.response_without_steps(data=response_body["data"]),
                         api.data_expected_without_steps(recipe=tc_recipe))
        api.check_steps(recipe=tc_recipe, response_data=response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe.check_bdd_data()

    def test_steps_tab_null(self):
        """ BodyParameter steps is a tab null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_steps: [None]}
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
        detail = api.create_detail(param=api.param_steps, msg=server.detail_must_be_an_array_of_object,
                                   value=body[api.param_steps])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_steps_tab_empty(self):
        """ BodyParameter steps is a tab empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_steps: [""]}
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
        detail = api.create_detail(param=api.param_steps, msg=server.detail_must_be_an_array_of_object,
                                   value=body[api.param_steps])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_steps_tab_invalid(self):
        """ BodyParameter steps is a tab string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_steps: ["invalid"]}
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
        detail = api.create_detail(param=api.param_steps, msg=server.detail_must_be_an_array_of_object,
                                   value=body[api.param_steps])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_steps_id_without(self):
        """ BodyParameter step.id is missing.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_steps: [{api.param_step_description: "step"}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.custom(api.clean_body(data=body))
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(api.response_without_steps(data=response_body["data"]),
                         api.data_expected_without_steps(recipe=tc_recipe))
        api.check_steps(recipe=tc_recipe, response_data=response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe.check_bdd_data()

    def test_steps_id_null(self):
        """ BodyParameter step.id is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_steps: [{api.param_step_id: None,
                                   api.param_step_description: "step"}]}
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
        detail = api.create_detail(param=api.param_steps+"."+api.param_step_id, msg=server.detail_must_be_an_object_id,
                                   value=body[api.param_steps][0][api.param_step_id])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_steps_id_empty(self):
        """ BodyParameter step.id is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_steps: [{api.param_step_id: "",
                                   api.param_step_description: "step"}]}
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
        detail = api.create_detail(param=api.param_steps+"."+api.param_step_id, msg=server.detail_must_be_an_object_id,
                                   value=body[api.param_steps][0][api.param_step_id])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_steps_id_invalid(self):
        """ BodyParameter step.id is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_steps: [{api.param_step_id: "invalid",
                                   api.param_step_description: "step"}]}
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
        detail = api.create_detail(param=api.param_steps+"."+api.param_step_id, msg=server.detail_must_be_an_object_id,
                                   value=body[api.param_steps][0][api.param_step_id])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_steps_id_object_id(self):
        """ BodyParameter step.id is an ObjectId.

        Return
            200 - Updated Recipe.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_steps: [{api.param_step_id: "aaaaaaaaaaaaaaaaaaaaaaaa",
                                   api.param_step_description: "step"}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(api.response_without_steps(data=response_body["data"]),
                         api.data_expected_without_steps(recipe=tc_recipe))
        api.check_steps(recipe=tc_recipe, response_data=response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe.check_bdd_data()

    def test_steps_description_without(self):
        """ BodyParameter step.description is missing.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_steps: [{api.param_step_id: "aaaaaaaaaaaaaaaaaaaaaaaa"}]}
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
        detail = api.create_detail(param=api.param_steps+"."+api.param_step_description, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_steps_description_null(self):
        """ BodyParameter step.description is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_steps: [{api.param_step_id: "aaaaaaaaaaaaaaaaaaaaaaaa",
                                   api.param_step_description: None}]}
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
        detail = api.create_detail(param=api.param_step+"."+api.param_step_description,
                                   msg=server.detail_must_be_a_string,
                                   value=body[api.param_steps][0][api.param_step_description])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_steps_description_empty(self):
        """ BodyParameter step.description is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_steps: [{api.param_step_id: "aaaaaaaaaaaaaaaaaaaaaaaa",
                                   api.param_step_description: ""}]}
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
        detail = api.create_detail(param=api.param_step+"."+api.param_step_description,
                                   msg=server.detail_must_be_not_empty,
                                   value=body[api.param_steps][0][api.param_step_description])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_steps_description_invalid(self):
        """ BodyParameter step.description is a string.

        Return
            200 - Updated Recipe.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_steps: [{api.param_step_id: "aaaaaaaaaaaaaaaaaaaaaaaa",
                                   api.param_step_description: "step"}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(api.response_without_steps(data=response_body["data"]),
                         api.data_expected_without_steps(recipe=tc_recipe))
        api.check_steps(recipe=tc_recipe, response_data=response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe.check_bdd_data()

    def test_steps_complexe(self):
        """ Special case : complexe update

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="aaaaaaaaaaaaaaaaaaaaaaaa", description="step1")
        tc_recipe.add_step(_id_step="bbbbbbbbbbbbbbbbbbbbbbbb", description="step2")
        tc_recipe.insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_steps: [{api.param_step_id: "aaaaaaaaaaaaaaaaaaaaaaaa",
                                   api.param_step_description: "step1"},
                                  {api.param_step_description: "step_new"},
                                  {api.param_step_id: "cccccccccccccccccccccccc",
                                   api.param_step_description: "step_new_fake"},
                                  {api.param_step_id: "bbbbbbbbbbbbbbbbbbbbbbbb",
                                   api.param_step_description: "step2_update"}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(api.response_without_steps(data=response_body["data"]),
                         api.data_expected_without_steps(recipe=tc_recipe))
        api.check_steps(recipe=tc_recipe, response_data=response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe.check_bdd_data()

    def test_steps_clean_files(self):
        """ Special case : File to be cleaned

        Return
            200 - Updated Recipe.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="aaaaaaaaaaaaaaaaaaaaaaaa", description="step1")
        tc_recipe.add_step(_id_step="bbbbbbbbbbbbbbbbbbbbbbbb", description="step2")
        tc_recipe.insert()
        tc_file1 = tc_recipe.add_file_mongo_step(_id_step="aaaaaaaaaaaaaaaaaaaaaaaa", filename="file11", is_main=False)
        tc_file2 = tc_recipe.add_file_mongo_step(_id_step="aaaaaaaaaaaaaaaaaaaaaaaa", filename="file12", is_main=False)
        tc_file3 = tc_recipe.add_file_mongo_step(_id_step="bbbbbbbbbbbbbbbbbbbbbbbb", filename="file2", is_main=False)
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_steps: [{api.param_step_description: "step_new"},
                                  {api.param_step_id: "bbbbbbbbbbbbbbbbbbbbbbbb",
                                   api.param_step_description: "step2up"}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(api.response_without_steps(data=response_body["data"]),
                         api.data_expected_without_steps(recipe=tc_recipe))
        api.check_steps(recipe=tc_recipe, response_data=response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe.check_bdd_data()
        tc_file1.check_doesnt_exist_by_id()
        tc_file2.check_doesnt_exist_by_id()
        tc_file3.check_bdd_data()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PutRecipe())


if __name__ == '__main__':
    unittest.main()
