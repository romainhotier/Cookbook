import { handleActions } from 'redux-actions'

import {
  getAllIngredientsRequest,
  getAllIngredientsSuccess,
  getAllIngredientsFailed,
  postIngredientRequest,
  postIngredientSuccess,
  postIngredientFailed,
  deleteIngredientRequest,
  deleteIngredientSuccess,
  deleteIngredientFailed,
} from './../actions'

const defaultState = {
  content: {},
  loadingFetchIngredients: false,
  loadingDeleteIngredient: false,
  loadingPostIngredient: false,
  error: null,
}

const IngredientReducer = handleActions(
  {
    /*
     ** GET ALL INGREDIENTS
     */
    [getAllIngredientsRequest](state, action) {
      return {
        ...state,
        loadingFetchIngredients: true,
        error: null,
      }
    },

    [getAllIngredientsSuccess](state, action) {
      let data = {}
      action.payload.forEach(ing => {
        data[ing.slug] = {
          ...ing,
        }
      })

      return {
        ...state,
        content: data,
        loadingFetchIngredients: false,
      }
    },

    [getAllIngredientsFailed](state, action) {
      return {
        ...state,
        loadingFetchIngredients: false,
        error: true,
      }
    },

    /*
     ** POST INGREDIENT
     */
    [postIngredientRequest](state, action) {
      return {
        ...state,
        loadingPostIngredient: true,
        error: null,
      }
    },

    [postIngredientSuccess](state, action) {
      let { content } = state
      const { data } = action.payload

      return {
        ...state,
        content: {
          ...content,
          [data.slug]: data,
        },
        loadingPostIngredient: false,
      }
    },

    [postIngredientFailed](state, action) {
      return {
        ...state,
        loadingPostIngredient: false,
        error: true,
      }
    },

    /*
     ** DELETE INGREDIENT
     */
    [deleteIngredientRequest](state, action) {
      return {
        ...state,
        loadingDeleteIngredient: true,
        error: null,
      }
    },

    [deleteIngredientSuccess](state, action) {
      let { content } = state
      const { id } = action.payload

      console.log('content', content)
      console.log('id', id)
      return {
        ...state,
        content: {
          ...content,
        },
        loadingDeleteIngredient: false,
      }
    },

    [deleteIngredientFailed](state, action) {
      return {
        ...state,
        loadingDeleteIngredient: false,
        error: true,
      }
    },
  },
  defaultState
)

export default IngredientReducer
