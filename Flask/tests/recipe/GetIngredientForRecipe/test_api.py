import unittest
import requests

import utils
import tests.recipe.GetIngredientForRecipe.api as api
import tests.ingredient.model as ingredient_model
import tests.recipe.model as recipe_model

server = utils.Server()
api = api.GetIngredientForRecipe()
ingredient = ingredient_model.IngredientTest()
recipe = recipe_model.RecipeTest()
link = ingredient_model.IngredientRecipeTest()


class GetIngredientForRecipe(unittest.TestCase):

    def setUp(self):
        ingredient.clean()
        recipe.clean()
        link.clean()

    def test_0_api_ok(self):
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_recipe2 = recipe_model.RecipeTest().insert()
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        tc_ingredient3 = ingredient_model.IngredientTest().insert()
        tc_link11 = ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                                    "_id_ingredient": tc_ingredient1._id}).insert()
        tc_link12 = ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                                    "_id_ingredient": tc_ingredient2._id}).insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe2._id,
                                                        "_id_ingredient": tc_ingredient2._id}).insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe2._id,
                                                        "_id_ingredient": tc_ingredient3._id}).insert()
        tc_id_recipe = tc_recipe1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertCountEqual(response_body["data"], [api.data_expected(link=tc_link11),
                                                      api.data_expected(link=tc_link12)])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_1_url_not_found_1(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe._id,
                                                        "_id_ingredient": tc_ingredient._id}).insert()
        tc_id_recipe = tc_recipe.get_id()
        """ call api """
        url = server.main_url + "/x" + api.url1 + "/" + tc_id_recipe + "/" + api.url2
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        
    def test_1_url_not_found_2(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe._id,
                                                        "_id_ingredient": tc_ingredient._id}).insert()
        tc_id_recipe = tc_recipe.get_id()
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/x" + api.url2
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)

    def test_2_id_recipe_without(self):
        """ go to GetRecipe """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe._id,
                                                        "_id_ingredient": tc_ingredient._id}).insert()
        tc_id_recipe = ""
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param="slug", msg=server.detail_doesnot_exist, value=api.url2)
        self.assertEqual(response_body["detail"], detail)

    def test_2_id_recipe_string(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe._id,
                                                        "_id_ingredient": tc_ingredient._id}).insert()
        tc_id_recipe = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id, msg=server.detail_must_be_an_object_id,
                                   value=tc_id_recipe)
        self.assertEqual(response_body["detail"], detail)

    def test_2_id_recipe_object_id_invalid(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe._id,
                                                        "_id_ingredient": tc_ingredient._id}).insert()
        tc_id_recipe = "aaaaaaaaaaaaaaaaaaaaaaaa"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id, msg=server.detail_doesnot_exist, value=tc_id_recipe)
        self.assertEqual(response_body["detail"], detail)

    def test_3_with_name_without(self):
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "i1_qa_rhr"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom({"name": "i2_qa_rhr"}).insert()
        tc_link1 = ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                                   "_id_ingredient": tc_ingredient1._id}).insert()
        tc_link2 = ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                                   "_id_ingredient": tc_ingredient2._id}).insert()
        tc_id_recipe = tc_recipe1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertCountEqual(response_body["data"], [api.data_expected(link=tc_link1),
                                                      api.data_expected(link=tc_link2)])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_3_with_name_empty(self):
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "i1_qa_rhr"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom({"name": "i2_qa_rhr"}).insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                        "_id_ingredient": tc_ingredient1._id}).insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                        "_id_ingredient": tc_ingredient2._id}).insert()
        tc_id_recipe = tc_recipe1.get_id()
        tc_with_name = ""
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "?" + \
            api.param_with_name + "=" + tc_with_name
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_name, msg=server.detail_must_be_in + " [true, false]",
                                   value=tc_with_name)
        self.assertEqual(response_body["detail"], detail)

    def test_3_with_name_string(self):
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "i1_qa_rhr"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom({"name": "i2_qa_rhr"}).insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                        "_id_ingredient": tc_ingredient1._id}).insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                        "_id_ingredient": tc_ingredient2._id}).insert()
        tc_id_recipe = tc_recipe1.get_id()
        tc_with_name = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "?" + \
            api.param_with_name + "=" + tc_with_name
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_name, msg=server.detail_must_be_in + " [true, false]",
                                   value=tc_with_name)
        self.assertEqual(response_body["detail"], detail)

    def test_3_with_name_string_false(self):
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "i1_qa_rhr"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom({"name": "i2_qa_rhr"}).insert()
        tc_link1 = ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                                   "_id_ingredient": tc_ingredient1._id}).insert()
        tc_link2 = ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                                   "_id_ingredient": tc_ingredient2._id}).insert()
        tc_id_recipe = tc_recipe1.get_id()
        tc_with_name = "false"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "?" + \
            api.param_with_name + "=" + tc_with_name
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], [api.data_expected(link=tc_link1),
                                                 api.data_expected(link=tc_link2)])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_3_with_name_string_true(self):
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "i1_qa_rhr"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom({"name": "i2_qa_rhr"}).insert()
        tc_link1 = ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                                   "_id_ingredient": tc_ingredient1._id}).insert()
        tc_link2 = ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                                   "_id_ingredient": tc_ingredient2._id}).insert()
        tc_id_recipe = tc_recipe1.get_id()
        tc_with_name = "true"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "?" + \
            api.param_with_name + "=" + tc_with_name
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], [api.data_expected(link=tc_link1, names=True),
                                                 api.data_expected(link=tc_link2, names=True)])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    @classmethod
    def tearDownClass(cls):
        cls.setUp(GetIngredientForRecipe())


if __name__ == '__main__':
    unittest.main()
