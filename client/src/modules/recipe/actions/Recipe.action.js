import { createAction } from 'redux-actions'

export const getAllRecipesRequest = createAction('GET_ALL_RECIPES_REQUEST')
export const getAllRecipesSuccess = createAction('GET_ALL_RECIPES_SUCCESS')
export const getAllRecipesFailed = createAction('GET_ALL_RECIPES_FAILED')

export const getRecipeRequest = createAction('GET_RECIPE_REQUEST')
export const getRecipeSuccess = createAction('GET_RECIPE_SUCCESS')
export const getRecipeFailed = createAction('GET_RECIPE_FAILED')

export const postRecipeRequest = createAction('POST_RECIPE_REQUEST')
export const postRecipeSuccess = createAction('POST_RECIPE_SUCCESS')
export const postRecipeFailed = createAction('POST_RECIPE_FAILED')

export const putRecipeRequest = createAction('PUT_RECIPE_REQUEST')
export const putRecipeSuccess = createAction('PUT_RECIPE_SUCCESS')
export const putRecipeFailed = createAction('PUT_RECIPE_FAILED')
