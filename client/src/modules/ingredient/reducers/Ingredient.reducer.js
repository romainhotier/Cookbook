import { handleActions } from 'redux-actions'
import omitBy from 'lodash/omitBy'
import findKey from 'lodash/findKey'

import {
  getAllIngredientsRequest,
  getAllIngredientsSuccess,
  getAllIngredientsFailed,
  postIngredientRequest,
  postIngredientSuccess,
  postIngredientFailed,
  putIngredientRequest,
  putIngredientSuccess,
  putIngredientFailed,
  deleteIngredientRequest,
  deleteIngredientSuccess,
  deleteIngredientFailed,
  searchIngredientsRequest,
  searchIngredientsSuccess,
  searchIngredientsFailed,
} from './../actions'

const defaultState = {
  content: {},
  loadingFetchIngredients: false,
  loadingDeleteIngredient: false,
  loadingPostIngredient: false,
  loadingPutIngredient: false,
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
        error: `${action.payload}`,
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
        error: `${action.payload}`,
      }
    },

    /*
     ** PUT INGREDIENT
     */
    [putIngredientRequest](state, action) {
      return {
        ...state,
        loadingPutIngredient: true,
        error: null,
      }
    },

    [putIngredientSuccess](state, action) {
      let { content } = state
      let { data } = action.payload

      const newContent = omitBy(content, recipe => recipe._id === data._id)

      return {
        ...state,
        content: {
          ...newContent,
          [data.slug]: data,
        },
        loadingPutIngredient: false,
      }
    },

    [putIngredientFailed](state, action) {
      return {
        ...state,
        loadingPutIngredient: false,
        error: `${action.payload}`,
      }
    },

    /*
     ** DELETE INGREDIENT
     */
    [deleteIngredientRequest](state) {
      return {
        ...state,
        loadingDeleteIngredient: true,
        error: null,
      }
    },

    [deleteIngredientSuccess](state, action) {
      let { content } = state

      const ingSlug = findKey(content, ing => ing._id === action.payload)
      delete content[ingSlug]

      return {
        ...state,
        content,
        loadingDeleteIngredient: false,
      }
    },

    [deleteIngredientFailed](state, action) {
      return {
        ...state,
        loadingDeleteIngredient: false,
        error: `${action.payload}`,
      }
    },

    /*
     ** SEARCH INGREDIENT
     */
    [searchIngredientsRequest](state, action) {
      return {
        ...state,
        error: null,
      }
    },

    [searchIngredientsSuccess](state, action) {
      let data = {}
      action.payload.forEach(ing => {
        data[ing.slug] = {
          ...ing,
        }
      })

      return {
        ...state,
        content: data,
      }
    },

    [searchIngredientsFailed](state, action) {
      return {
        ...state,
        error: `${action.payload}`,
      }
    },
  },
  defaultState
)

export default IngredientReducer
