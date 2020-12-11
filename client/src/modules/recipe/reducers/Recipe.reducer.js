import { handleActions } from 'redux-actions'

import {
  getAllRecipesRequest,
  getAllRecipesSuccess,
  getAllRecipesFailed,
  getRecipeRequest,
  getRecipeSuccess,
  getRecipeFailed,
  postRecipeRequest,
  postRecipeSuccess,
  postRecipeFailed,
  putRecipeRequest,
  putRecipeSuccess,
  putRecipeFailed,
} from './../actions'

const defaultState = {
  content: {},
  loadingFetchRecipes: false,
  loadingPostRecipes: false,
  loadingPutRecipes: false,
  error: null,
}

const RecipeReducer = handleActions(
  {
    /*
     ** GET ALL RECIPES
     */
    [getAllRecipesRequest](state) {
      return {
        ...state,
        loadingFetchRecipes: true,
        error: null,
      }
    },

    [getAllRecipesSuccess](state, action) {
      let data = {}
      action.payload.forEach(recipe => {
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

    [getAllRecipesFailed](state) {
      return {
        ...state,
        loadingFetchRecipes: false,
        error: true,
      }
    },

    /*
     ** GET RECIPE
     */
    [getRecipeRequest](state) {
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

    [getRecipeFailed](state) {
      return {
        ...state,
        loadingFetchRecipes: false,
        error: true,
      }
    },

    /*
     ** POST RECIPE
     */
    [postRecipeRequest](state) {
      return {
        ...state,
        loadingPostRecipes: true,
        error: null,
      }
    },

    [postRecipeSuccess](state, action) {
      let data = {}
      const recipe = action.payload

      data[recipe.slug] = {
        ...recipe,
      }

      return {
        ...state,
        content: data,
        loadingPostRecipes: false,
      }
    },

    [postRecipeFailed](state) {
      return {
        ...state,
        loadingPostRecipes: false,
        error: true,
      }
    },

    /*
     ** PUT RECIPE
     */
    [putRecipeRequest](state) {
      return {
        ...state,
        loadingPutRecipes: true,
        error: null,
      }
    },

    [putRecipeSuccess](state, action) {
      let data = {}
      const recipe = action.payload

      data[recipe.slug] = {
        ...recipe,
      }

      return {
        ...state,
        content: data,
        loadingPutRecipes: false,
      }
    },

    [putRecipeFailed](state) {
      return {
        ...state,
        loadingPutRecipes: false,
        error: true,
      }
    },
  },
  defaultState
)

export default RecipeReducer
