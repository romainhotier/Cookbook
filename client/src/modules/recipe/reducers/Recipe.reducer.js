import { handleActions } from 'redux-actions'

import {
  getAllRecipesRequest,
  getAllRecipesSuccess,
  getAllRecipesFailed,
  getRecipeRequest,
  getRecipeSuccess,
  getRecipeFailed,
} from './../actions'

const defaultState = {
  content: {},
  loadingFetchRecipes: false,
  error: null
}

const RecipeReducer = handleActions(
  {
    /*
     ** GET ALL RECIPES
     */
    [getAllRecipesRequest](state, action) {
      return {
        ...state,
        loadingFetchRecipes: true,
        error: null,
      }
    },

    [getAllRecipesSuccess](state, action) {
      let data = {}
      action.payload.forEach((recipe) => {
        data[recipe.slug] = {
          ...recipe,
        }
      })

      return {
        ...state,
        content: data,
        loadingFetchRecipes: false,
      }
    },

    [getAllRecipesFailed](state, action) {
      return {
        ...state,
        loadingFetchRecipes: false,
        error: true,
      }
    },

     /*
     ** GET RECIPE
     */
    [getRecipeRequest](state, action) {
      return {
        ...state,
        loadingFetchRecipes: true,
        error: null,
      }
    },

    [getRecipeSuccess](state, action) {
      let data = {}
      const recipe = action.payload

      data[recipe.slug] = {
        ...recipe,
      }

      return {
        ...state,
        content: data,
        loadingFetchRecipes: false,
      }
    },

    [getRecipeFailed](state, action) {
      return {
        ...state,
        loadingFetchRecipes: false,
        error: true,
      }
    },
  },
  defaultState
)

export default RecipeReducer
