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
        """ Clean IngredientTest, RecipeTest and IngredientRecipeTest."""
        ingredient.clean()
        recipe.clean()
        link.clean()

    def test_0_api_ok(self):
        """ Default case.

        Return
            200 - All Ingredients for a Recipe.
        """
        """ env """
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
        """ param """
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
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe._id,
                                                        "_id_ingredient": tc_ingredient._id}).insert()
        """ param """
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
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe._id,
                                                        "_id_ingredient": tc_ingredient._id}).insert()
        """ param """
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
        """ QueryParameter _id_recipe is missing.

        Return
            400 - Go to GetRecipe.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe._id,
                                                        "_id_ingredient": tc_ingredient._id}).insert()
        """ param """
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
        """ QueryParameter _id_recipe is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe._id,
                                                        "_id_ingredient": tc_ingredient._id}).insert()
        """ param """
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
        """ QueryParameter _id_recipe is a nok ObjectId.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe._id,
                                                        "_id_ingredient": tc_ingredient._id}).insert()
        """ param """
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

    def test_3_with_names_without(self):
        """ QueryParameter with_names is missing.

        Return
            200 - All Ingredients for a Recipe.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "i1_qa_rhr"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom({"name": "i2_qa_rhr"}).insert()
        tc_link1 = ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                                   "_id_ingredient": tc_ingredient1._id}).insert()
        tc_link2 = ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                                   "_id_ingredient": tc_ingredient2._id}).insert()
        """ param """
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

    def test_3_with_names_empty(self):
        """ QueryParameter with_names is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "i1_qa_rhr"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom({"name": "i2_qa_rhr"}).insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                        "_id_ingredient": tc_ingredient1._id}).insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                        "_id_ingredient": tc_ingredient2._id}).insert()
        """ param """
        tc_id_recipe = tc_recipe1.get_id()
        tc_with_names = ""
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "?" + \
            api.param_with_names + "=" + tc_with_names
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_names, msg=server.detail_must_be_in + api.detail_true_false,
                                   value=tc_with_names)
        self.assertEqual(response_body["detail"], detail)

    def test_3_with_names_string(self):
        """ QueryParameter with_names is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "i1_qa_rhr"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom({"name": "i2_qa_rhr"}).insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                        "_id_ingredient": tc_ingredient1._id}).insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                        "_id_ingredient": tc_ingredient2._id}).insert()
        """ param """
        tc_id_recipe = tc_recipe1.get_id()
        tc_with_names = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "?" + \
            api.param_with_names + "=" + tc_with_names
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_names, msg=server.detail_must_be_in + api.detail_true_false,
                                   value=tc_with_names)
        self.assertEqual(response_body["detail"], detail)

    def test_3_with_names_string_false(self):
        """ QueryParameter with_names is false.

        Return
            200 - All Ingredients for a Recipe.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "i1_qa_rhr"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom({"name": "i2_qa_rhr"}).insert()
        tc_link1 = ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                                   "_id_ingredient": tc_ingredient1._id}).insert()
        tc_link2 = ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                                   "_id_ingredient": tc_ingredient2._id}).insert()
        """ param """
        tc_id_recipe = tc_recipe1.get_id()
        tc_with_names = "false"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "?" + \
            api.param_with_names + "=" + tc_with_names
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

    def test_3_with_names_string_true(self):
        """ QueryParameter with_names is true.

        Return
            200 - All Ingredients with name for a Recipe.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "i1_qa_rhr"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom({"name": "i2_qa_rhr"}).insert()
        tc_link1 = ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                                   "_id_ingredient": tc_ingredient1._id}).insert()
        tc_link2 = ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                                   "_id_ingredient": tc_ingredient2._id}).insert()
        """ param """
        tc_id_recipe = tc_recipe1.get_id()
        tc_with_names = "true"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "?" + \
            api.param_with_names + "=" + tc_with_names
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
