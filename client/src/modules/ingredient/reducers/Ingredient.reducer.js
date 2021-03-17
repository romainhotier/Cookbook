import { handleActions } from 'redux-actions'
import findKey from 'lodash/findKey'
import { List } from 'immutable'

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

import {
  IngredientStateFactory,
  getAllIngredients,
  findIngredientEntry,
  removeFileInIngredient,
  updateFilesInIngredient,
  setIngredients,
} from './Ingredient.store'

export const defaultInitialState = IngredientStateFactory()

const IngredientReducer = handleActions(
  {
    /*
     ** GET ALL INGREDIENTS
     */
    [getAllIngredientsRequest](state) {
      return state.set('loadingFetchIngredient', true)
    },

    [getAllIngredientsSuccess](state, action) {
      return state.set('loadingFetchIngredient', false).set('content', List(action.payload))
    },

    [getAllIngredientsFailed](state) {
      return state.set('loadingFetchIngredient', false).set('error', true)
    },

    /*
     ** POST INGREDIENT
     */
    [postIngredientRequest](state) {
      return state.set('loadingPostIngredient', true)
    },

    [postIngredientSuccess](state, action) {
      const newIngredients = getAllIngredients(state).push(action.payload.data)
      return state.set('loadingPostIngredient', false).set('content', List(newIngredients))
    },

    [postIngredientFailed](state) {
      return state.set('loadingPostIngredient', false).set('error', true)
    },

    /*
     ** PUT INGREDIENT
     */
    [putIngredientRequest](state) {
      return state.set('loadingPutIngredient', true)
    },

    [putIngredientSuccess](state, action) {
      const ingredient = action.payload.data

      const index = findIngredientEntry(state, ingredient._id)
      if (index < 0) {
        return state.set('loadingPutIngredient', false)
      }

      const newIngredients = getAllIngredients(state).updateIn([index], ing => ({ ...ing, ...ingredient }))
      return state.set('loadingPutIngredient', false).set('content', List(newIngredients))
    },

    [putIngredientFailed](state, action) {
      return state.set('loadingPutIngredient', false).set('error', `${action.payload}`)
    },

    /*
     ** DELETE INGREDIENT
     */
    [deleteIngredientRequest](state) {
      return state.set('loadingDeleteIngredient', true)
    },

    [deleteIngredientSuccess](state, action) {
      const ingredientId = action.payload

      const index = findIngredientEntry(state, ingredientId)
      if (index < 0) {
        return state.set('loadingDeleteIngredient', false)
      }

      const newIngredients = getAllIngredients(state).removeIn([index])
      return state.set('loadingDeleteIngredient', false).set('content', List(newIngredients))
    },

    [deleteIngredientFailed](state, action) {
      return state.set('loadingDeleteIngredient', false).set('error', `${action.payload}`)
    },

    /*
     ** SEARCH INGREDIENT
     */
    [searchIngredientsRequest](state) {
      return state.set('error', null)
    },

    [searchIngredientsSuccess](state, action) {
      return state.set('content', List(action.payload))
    },

    [searchIngredientsFailed](state, action) {
      return state.set('error', `${action.payload}`)
    },
  },
  defaultInitialState
)

export default IngredientReducer
