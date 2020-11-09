import {createAction} from 'redux-actions'

export const getAllIngredientsRequest = createAction(
  'GET_ALL_INGREDIENTS_REQUEST'
)
export const getAllIngredientsSuccess = createAction(
  'GET_ALL_INGREDIENTS_SUCCESS'
)
export const getAllIngredientsFailed = createAction(
  'GET_ALL_INGREDIENTS_FAILED'
)
