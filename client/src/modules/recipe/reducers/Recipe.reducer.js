import { handleActions } from 'redux-actions'
import { List } from 'immutable'

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
  deleteRecipeRequest,
  deleteRecipeSuccess,
  deleteRecipeFailed,
  postFileRecipeRequest,
  postFileRecipeSuccess,
  postFileRecipeFailed,
  deleteFileRecipeRequest,
  deleteFileRecipeSuccess,
  deleteFileRecipeFailed,
  postFileRecipeStepRequest,
  postFileRecipeStepSuccess,
  postFileRecipeStepFailed,
  deleteFileRecipeStepRequest,
  deleteFileRecipeStepSuccess,
  deleteFileRecipeStepFailed,
} from './../actions'

import {
  RecipeStateFactory,
  getAllRecipes,
  findRecipeEntry,
  removeFileInRecipe,
  updateFilesInRecipe,
  setRecipes,
  updateFilesRecipeStep,
  removeFileRecipeStep,
} from './Recipe.store'

export const defaultInitialState = RecipeStateFactory()

const RecipeReducer = handleActions(
  {
    /*
     ** GET ALL RECIPES
     */
    [getAllRecipesRequest](state) {
      return state.set('loadingFetchRecipe', true)
    },

    [getAllRecipesSuccess](state, action) {
      return state.set('loadingFetchRecipe', false).set('content', List(action.payload))
    },

    [getAllRecipesFailed](state) {
      return state.set('loadingFetchRecipe', false).set('error', true)
    },

    /*
     ** GET RECIPE
     */
    [getRecipeRequest](state) {
      return state.set('loadingFetchRecipe', true)
    },

    [getRecipeSuccess](state, action) {
      return state.set('loadingFetchRecipe', false).set('content', List([action.payload]))
    },

    [getRecipeFailed](state) {
      return state.set('loadingFetchRecipe', false).set('error', true)
    },

    /*
     ** POST RECIPE
     */
    [postRecipeRequest](state) {
      return state.set('loadingPostRecipe', true)
    },

    [postRecipeSuccess](state, action) {
      const newRecipes = getAllRecipes(state).push(action.payload)
      return state.set('loadingPostRecipe', false).set('content', List(newRecipes))
    },

    [postRecipeFailed](state) {
      return state.set('loadingPostRecipe', false).set('error', true)
    },

    /*
     ** PUT RECIPE
     */
    [putRecipeRequest](state) {
      return state.set('loadingPutRecipe', true)
    },

    [putRecipeSuccess](state, action) {
      const recipeEdited = action.payload
      const index = findRecipeEntry(state, recipeEdited._id)

      if (index < 0) {
        return state.set('loadingPutRecipe', false)
      }

      const newRecipes = getAllRecipes(state).updateIn([index], recipe => ({ ...recipe, ...recipeEdited }))
      return state.set('loadingPutRecipe', false).set('content', List(newRecipes))
    },

    [putRecipeFailed](state) {
      return state.set('loadingPutRecipe', false).set('error', true)
    },

    /*
     ** DELETE RECIPE
     */
    [deleteRecipeRequest](state) {
      return state.set('loading', true)
    },

    [deleteRecipeSuccess](state, action) {
      const recipeId = action.payload

      const index = findRecipeEntry(state, recipeId)
      if (index < 0) {
        return state.set('loading', false)
      }

      const newRecipes = getAllRecipes(state).removeIn([index])
      return state.set('loading', false).set('content', List(newRecipes))
    },

    [deleteRecipeFailed](state) {
      return state.set('loading', false).set('error', true)
    },

    /*
     ** POST FILES IN RECIPE
     */
    [postFileRecipeRequest](state) {
      return state.set('error', null)
    },

    [postFileRecipeSuccess](state, { payload }) {
      const url = payload[0]
      const splitUrl = url.split('/')
      const id = splitUrl[1]

      const index = findRecipeEntry(state, id)
      if (index < 0) {
        return state
      }
      const updatedRecipesList = updateFilesInRecipe(state, index, payload)

      return setRecipes(state, updatedRecipesList)
    },

    [postFileRecipeFailed](state, { payload }) {
      return state.set('error', payload)
    },

    /*
     ** DELETE FILES IN RECIPE
     */
    [deleteFileRecipeRequest](state) {
      return state.set('error', null)
    },

    [deleteFileRecipeSuccess](state, { payload }) {
      const splitUrl = payload.split('/')
      const id = splitUrl[1]

      const index = findRecipeEntry(state, id)
      if (index < 0) {
        return state
      }

      const updatedRecipesList = removeFileInRecipe(state, index, payload)
      return setRecipes(state, updatedRecipesList)
    },

    [deleteFileRecipeFailed](state, { payload }) {
      return state.set('error', payload)
    },

    /*
     ** POST FILES RECIPE STEP
     */
    [postFileRecipeStepRequest](state) {
      return state.set('error', null)
    },

    [postFileRecipeStepSuccess](state, { payload }) {
      const url = payload[0]
      const splitUrl = url.split('/')
      const recipe_id = splitUrl[1]
      const step_id = splitUrl[3]

      const index = findRecipeEntry(state, recipe_id)
      if (index < 0) {
        return state
      }
      const updatedRecipesList = updateFilesRecipeStep(state, index, step_id, payload)

      return setRecipes(state, updatedRecipesList)
    },

    [postFileRecipeStepFailed](state, { payload }) {
      return state.set('error', payload)
    },

    /*
     ** DELETE FILES RECIPE STEP
     */
    [deleteFileRecipeStepRequest](state) {
      return state.set('error', null)
    },

    [deleteFileRecipeStepSuccess](state, { payload }) {
      const splitUrl = payload.split('/')
      const recipe_id = splitUrl[1]
      const step_id = splitUrl[3]

      const index = findRecipeEntry(state, recipe_id)
      if (index < 0) {
        return state
      }

      const updatedRecipesList = removeFileRecipeStep(state, index, step_id, payload)
      return setRecipes(state, updatedRecipesList)
    },

    [deleteFileRecipeStepFailed](state, { payload }) {
      return state.set('error', payload)
    },
  },
  defaultInitialState
)

export default RecipeReducer
