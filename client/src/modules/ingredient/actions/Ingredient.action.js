import { createAction } from 'redux-actions'

export const getAllIngredientsRequest = createAction('GET_ALL_INGREDIENTS_REQUEST')
export const getAllIngredientsSuccess = createAction('GET_ALL_INGREDIENTS_SUCCESS')
export const getAllIngredientsFailed = createAction('GET_ALL_INGREDIENTS_FAILED')

export const postIngredientRequest = createAction('POST_INGREDIENT_REQUEST')
export const postIngredientSuccess = createAction('POST_INGREDIENT_SUCCESS')
export const postIngredientFailed = createAction('POST_INGREDIENT_FAILED')

export const deleteIngredientRequest = createAction('DELETE_INGREDIENT_REQUEST')
export const deleteIngredientSuccess = createAction('DELETE_INGREDIENT_SUCCESS')
export const deleteIngredientFailed = createAction('DELETE_INGREDIENT_FAILED')

export const postIngredientsRecipeRequest = createAction('POST_INGREDIENTS_RECIPE_REQUEST')
export const postIngredientsRecipeSuccess = createAction('POST_INGREDIENTS_RECIPE_SUCCESS')
export const postIngredientsRecipeFailed = createAction('POST_INGREDIENTS_RECIPE_FAILED')
