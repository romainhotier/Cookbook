import unittest
import requests

import factory as factory
import recipe.recipe.model as recipe_model
import recipe.steps.test.DeleteRecipeStep.api as api

server = factory.Server()
api = api.DeleteRecipeStep()
recipe = recipe_model.RecipeTest()


class DeleteRecipeStep(unittest.TestCase):

    def setUp(self):
        recipe.clean()

    def test_0_api_ok(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        tc_step_index = "1"
        """ cal api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2 + "/" + tc_step_index
        response = requests.delete(url, verify=False)
        response_body = response.json()
        tc_recipe.custom({"steps": ["a"]})
        """ assert """
        print(response_body)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        # self.assertEqual(response_body[api.rep_code_status], 201)
        # self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        # self.assertEqual(response_body[api.rep_data], tc_recipe.get_data_stringify_object_id())
        tc_recipe.select_ok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(DeleteRecipeStep())


if __name__ == '__main__':
    unittest.main()
