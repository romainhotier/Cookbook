import {createAction} from 'redux-actions'

export const getAllRecipesRequest = createAction(
  'GET_ALL_RECIPES_REQUEST'
)
export const getAllRecipesSuccess = createAction(
  'GET_ALL_RECIPES_SUCCESS'
)
export const getAllRecipesFailed = createAction(
  'GET_ALL_RECIPES_FAILED'
)
