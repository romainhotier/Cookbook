import { handleActions } from 'redux-actions'

import {
  getAllRecipesRequest,
  getAllRecipesSuccess,
  getAllRecipesFailed,
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
  },
  defaultState
)

export default RecipeReducer
