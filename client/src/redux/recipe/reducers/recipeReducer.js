import { handleActions } from 'redux-actions'

import {
  getAllRecipesRequest,
  getAllRecipesSuccess,
  getAllRecipesFailed,
  getAllIngredientsOfRecipeRequest,
  getAllIngredientsOfRecipeSuccess,
  getAllIngredientsOfRecipeFailed,
  getRecipeRequest,
  getRecipeSuccess,
  getRecipeFailed,
  addRecipeRequest,
  addRecipeSuccess,
  addRecipeFailed,
  editRecipeRequest,
  editRecipeSuccess,
  editRecipeFailed,
  uploadPictureRecipeRequest,
  uploadPictureRecipeSuccess,
  uploadPictureRecipeFailed,
} from 'redux/recipe/actions'

const defaultState = {
  content: {},
  fetchRecipes: false,
  submitRecipe: false,
  submittingIsSuccess: null,
  upload: false,
  fetchIngredients: false,
  error: null,
}

const recipeReducer = handleActions(
  {
    /*
     ** GET ALL RECIPES
     */
    [getAllRecipesRequest](state, action) {
      return {
        ...state,
        fetchRecipes: true,
        submittingIsSuccess: null,
        error: null,
      }
    },

    [getAllRecipesSuccess](state, action) {
      console.log(action)
      console.log(state)
      let recipes = {}
      action.payload.forEach((recipe) => {
        recipes[recipe.id] = {
          ...recipe,
        }
      })

      return {
        ...state,
        content: recipes,
        fetchRecipes: false,
      }
    },

    [getAllRecipesFailed](state, action) {
      return {
        ...state,
        fetchRecipes: false,
        error: true,
      }
    },

    /*
     ** GET ALL INGREDIENTS OF RECIPE
     */
    [getAllIngredientsOfRecipeRequest](state, action) {
      return {
        ...state,
        fetchIngredients: true,
        error: null,
      }
    },

    [getAllIngredientsOfRecipeSuccess](state, action) {
      let recipes = { ...state.content }
      const ingredients = Object.values(action.payload)
      const idRecipe = ingredients[0].idRecipes
      recipes[idRecipe] = {
        ...recipes[idRecipe],
        ingredients: ingredients,
      }

      return {
        ...state,
        content: recipes,
        fetchIngredients: false,
      }
    },

    [getAllIngredientsOfRecipeFailed](state, action) {
      return {
        ...state,
        fetchIngredients: false,
        error: true,
      }
    },

    /*
     ** GET RECIPE
     */
    [getRecipeRequest](state, action) {
      return {
        ...state,
        fetchRecipes: true,
        error: null,
      }
    },

    [getRecipeSuccess](state, action) {
      let recipes = { ...state.content }
      const recipe = action.payload[0]
      recipes[recipe.id] = {
        ...recipe,
      }

      return {
        ...state,
        content: recipes,
        fetchRecipes: false,
      }
    },

    [getRecipeFailed](state, action) {
      return {
        ...state,
        fetchRecipes: false,
        error: true,
      }
    },

    /*
     ** ADD RECIPE
     */
    [addRecipeRequest](state, action) {
      return {
        ...state,
        submitRecipe: true,
        submittingIsSuccess: null,
        error: null,
      }
    },

    [addRecipeSuccess](state, action) {
      return {
        ...state,
        submitRecipe: false,
        submittingIsSuccess: true,
      }
    },

    [addRecipeFailed](state, action) {
      return {
        ...state,
        submitRecipe: false,
        submittingIsSuccess: false,
        error: true,
      }
    },

    /*
     ** EDIT RECIPE
     */
    [editRecipeRequest](state, action) {
      return {
        ...state,
        submitRecipe: true,
        submittingIsSuccess: null,
        error: null,
      }
    },

    [editRecipeSuccess](state, action) {
      return {
        ...state,
        submitRecipe: false,
        submittingIsSuccess: true,
      }
    },

    [editRecipeFailed](state, action) {
      return {
        ...state,
        submitRecipe: false,
        submittingIsSuccess: false,
        error: true,
      }
    },

    /*
     ** UPLOAD DOCUMENT RECIPE
     */
    [uploadPictureRecipeRequest](state, action) {
      return {
        ...state,
        upload: true,
        error: null,
      }
    },

    [uploadPictureRecipeSuccess](state, action) {
      console.log(state)
      console.log(action)
      return {
        ...state,

        upload: false,
      }
    },

    [uploadPictureRecipeFailed](state, action) {
      return {
        ...state,
        upload: false,
        error: true,
      }
    },
  },
  defaultState
)

export default recipeReducer
