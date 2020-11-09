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


export const postIngredientRequest = createAction(
  'POST_INGREDIENT_REQUEST'
)
export const postIngredientSuccess = createAction(
  'POST_INGREDIENT_SUCCESS'
)
export const postIngredientFailed = createAction(
  'POST_INGREDIENT_FAILED'
)
