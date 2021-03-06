import { createAction } from 'redux-actions'

export const getAllIngredientsRequest = createAction('GET_ALL_INGREDIENTS_REQUEST')
export const getAllIngredientsSuccess = createAction('GET_ALL_INGREDIENTS_SUCCESS')
export const getAllIngredientsFailed = createAction('GET_ALL_INGREDIENTS_FAILED')

export const postIngredientRequest = createAction('POST_INGREDIENT_REQUEST')
export const postIngredientSuccess = createAction('POST_INGREDIENT_SUCCESS')
export const postIngredientFailed = createAction('POST_INGREDIENT_FAILED')

export const putIngredientRequest = createAction('PUT_INGREDIENT_REQUEST')
export const putIngredientSuccess = createAction('PUT_INGREDIENT_SUCCESS')
export const putIngredientFailed = createAction('PUT_INGREDIENT_FAILED')

export const deleteIngredientRequest = createAction('DELETE_INGREDIENT_REQUEST')
export const deleteIngredientSuccess = createAction('DELETE_INGREDIENT_SUCCESS')
export const deleteIngredientFailed = createAction('DELETE_INGREDIENT_FAILED')

export const searchIngredientsRequest = createAction('SEARCH_INGREDIENTS_REQUEST')
export const searchIngredientsSuccess = createAction('SEARCH_INGREDIENTS_SUCCESS')
export const searchIngredientsFailed = createAction('SEARCH_INGREDIENTS_FAILED')
