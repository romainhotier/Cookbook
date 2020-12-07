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
} from './../actions'

const defaultState = {
  content: {},
  loadingFetchRecipes: false,
  loadingPostRecipes: false,
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
  },
  defaultState
)

export default RecipeReducer
