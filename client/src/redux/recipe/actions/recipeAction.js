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

export const getAllIngredientsOfRecipeRequest = createAction(
  'GET_ALL_INGREDIENTS_OF_RECIPE_REQUEST'
)
export const getAllIngredientsOfRecipeSuccess = createAction(
  'GET_ALL_INGREDIENTS_OF_RECIPE_SUCCESS'
)
export const getAllIngredientsOfRecipeFailed = createAction(
  'GET_ALL_INGREDIENTS_OF_RECIPE_FAILED'
)

export const getAllCategoriesOfRecipeRequest = createAction(
  'GET_ALL_CATEGORIES_OF_RECIPE_REQUEST'
)
export const getAllCategoriesOfRecipeSuccess = createAction(
  'GET_ALL_CATEGORIES_OF_RECIPE_SUCCESS'
)
export const getAllCategoriesOfRecipeFailed = createAction(
  'GET_ALL_CATEGORIES_OF_RECIPE_FAILED'
)

export const getRecipeRequest = createAction(
  'GET_RECIPE_REQUEST'
)
export const getRecipeSuccess = createAction(
  'GET_RECIPE_SUCCESS'
)
export const getRecipeFailed = createAction(
  'GET_RECIPE_FAILED'
)

export const addRecipeRequest = createAction(
  'ADD_RECIPE_REQUEST'
)
export const addRecipeSuccess = createAction(
  'ADD_RECIPE_SUCCESS'
)
export const addRecipeFailed = createAction(
  'ADD_RECIPE_FAILED'
)

export const editRecipeRequest = createAction(
  'EDIT_RECIPE_REQUEST'
)
export const editRecipeSuccess = createAction(
  'EDIT_RECIPE_SUCCESS'
)
export const editRecipeFailed = createAction(
  'EDIT_RECIPE_FAILED'
)

export const uploadPictureRecipeRequest = createAction(
  'UPLOAD_PICTURE_RECIPE_REQUEST'
)
export const uploadPictureRecipeSuccess = createAction(
  'UPLOAD_PICTURE_RECIPE_SUCCESS'
)
export const uploadPictureRecipeFailed = createAction(
  'UPLOAD_PICTURE_RECIPE_FAILED'
)
