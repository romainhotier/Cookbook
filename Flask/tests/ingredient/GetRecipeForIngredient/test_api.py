import unittest
import requests

import utils
import tests.ingredient.GetRecipeForIngredient.api as api
import tests.ingredient.model as ingredient_model
import tests.recipe.model as recipe_model

server = utils.Server()
api = api.GetRecipeForIngredient()
ingredient = ingredient_model.IngredientTest()
recipe = recipe_model.RecipeTest()
link = ingredient_model.IngredientRecipeTest()


class GetRecipeForIngredient(unittest.TestCase):

    def setUp(self):
        """ Clean IngredientTest, RecipeTest and IngredientRecipeTest."""
        ingredient.clean()
        recipe.clean()
        link.clean()

    def test_0_api_ok(self):
        """ Default case.

        Return
            200 - Get Ingredients associated to a Recipe.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_recipe2 = recipe_model.RecipeTest().insert()
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        tc_ingredient3 = ingredient_model.IngredientTest().insert()
        tc_link1 = ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                                   "_id_ingredient": tc_ingredient1._id}).insert()
        tc_link2 = ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe2._id,
                                                                   "_id_ingredient": tc_ingredient1._id}).insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                        "_id_ingredient": tc_ingredient2._id}).insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe2._id,
                                                        "_id_ingredient": tc_ingredient3._id}).insert()
        """ param """
        tc_id_ingredient = tc_ingredient1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_ingredient + "/" + api.url2
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
        tc_id_ingredient = tc_recipe.get_id()
        """ call api """
        url = server.main_url + "/x" + api.url1 + "/" + tc_id_ingredient + "/" + api.url2
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
        tc_id_ingredient = tc_recipe.get_id()
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_ingredient + "/x" + api.url2
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)

    def test_2_id_ingredient_without(self):
        """ QueryParameter _id_ingredient is missing.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe._id,
                                                        "_id_ingredient": tc_ingredient._id}).insert()
        """ param """
        tc_id_ingredient = ""
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_ingredient + "/" + api.url2
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param="_id", msg=server.detail_must_be_an_object_id, value=api.url2)
        self.assertEqual(response_body["detail"], detail)

    def test_2_id_ingredient_string(self):
        """ QueryParameter _id_ingredient is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe._id,
                                                        "_id_ingredient": tc_ingredient._id}).insert()
        """ param """
        tc_id_ingredient = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_ingredient + "/" + api.url2
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id_ingredient, msg=server.detail_must_be_an_object_id,
                                   value=tc_id_ingredient)
        self.assertEqual(response_body["detail"], detail)

    def test_2_id_ingredient_object_id_invalid(self):
        """ QueryParameter _id_ingredient is a nok ObjectId.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe._id,
                                                        "_id_ingredient": tc_ingredient._id}).insert()
        """ param """
        tc_id_ingredient = "aaaaaaaaaaaaaaaaaaaaaaaa"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_ingredient + "/" + api.url2
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id_ingredient, msg=server.detail_doesnot_exist,
                                   value=tc_id_ingredient)
        self.assertEqual(response_body["detail"], detail)

    def test_3_with_titles_without(self):
        """ QueryParameter with_titles is missing.

        Return
            200 - Get Ingredients associated to a Recipe.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "r1"}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"title": "r2"}).insert()
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_link1 = ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                                   "_id_ingredient": tc_ingredient1._id}).insert()
        tc_link2 = ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe2._id,
                                                                   "_id_ingredient": tc_ingredient1._id}).insert()
        """ param """
        tc_id_ingredient = tc_ingredient1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_ingredient + "/" + api.url2
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

    def test_3_with_titles_empty(self):
        """ QueryParameter with_titles is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "r1"}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"title": "r2"}).insert()
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                        "_id_ingredient": tc_ingredient1._id}).insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe2._id,
                                                        "_id_ingredient": tc_ingredient1._id}).insert()
        """ param """
        tc_id_ingredient = tc_ingredient1.get_id()
        tc_with_titles = ""
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_ingredient + "/" + api.url2 + "?" + \
            api.param_with_titles + "=" + tc_with_titles
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_titles, msg=server.detail_must_be_in+api.rep_detail_true_false,
                                   value=tc_with_titles)
        self.assertEqual(response_body["detail"], detail)

    def test_3_with_titles_string(self):
        """ QueryParameter with_titles is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "r1"}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"title": "r2"}).insert()
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                        "_id_ingredient": tc_ingredient1._id}).insert()
        ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe2._id,
                                                        "_id_ingredient": tc_ingredient1._id}).insert()
        """ param """
        tc_id_ingredient = tc_ingredient1.get_id()
        tc_with_titles = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_ingredient + "/" + api.url2 + "?" + \
            api.param_with_titles + "=" + tc_with_titles
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_titles, msg=server.detail_must_be_in+api.rep_detail_true_false,
                                   value=tc_with_titles)
        self.assertEqual(response_body["detail"], detail)

    def test_3_with_titles_string_false(self):
        """ QueryParameter with_titles is false.

        Return
            200 - Get Ingredients associated to a Recipe.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "r1"}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"title": "r2"}).insert()
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_link1 = ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                                   "_id_ingredient": tc_ingredient1._id}).insert()
        tc_link2 = ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe2._id,
                                                                   "_id_ingredient": tc_ingredient1._id}).insert()
        """ param """
        tc_id_ingredient = tc_ingredient1.get_id()
        tc_with_titles = "false"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_ingredient + "/" + api.url2 + "?" + \
            api.param_with_titles + "=" + tc_with_titles
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

    def test_3_with_titles_string_true(self):
        """ QueryParameter with_titles is true.

        Return
            200 - Get Ingredients associated to a Recipe with title's Recipe.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "r1"}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"title": "r2"}).insert()
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_link1 = ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe1._id,
                                                                   "_id_ingredient": tc_ingredient1._id}).insert()
        tc_link2 = ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe2._id,
                                                                   "_id_ingredient": tc_ingredient1._id}).insert()
        """ param """
        tc_id_ingredient = tc_ingredient1.get_id()
        tc_with_titles = "true"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_ingredient + "/" + api.url2 + "?" + \
            api.param_with_titles + "=" + tc_with_titles
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertCountEqual(response_body["data"], [api.data_expected(link=tc_link1, title=True),
                                                      api.data_expected(link=tc_link2, title=True)])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    @classmethod
    def tearDownClass(cls):
        cls.setUp(GetRecipeForIngredient())


if __name__ == '__main__':
    unittest.main()
