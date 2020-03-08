import {createAction} from 'redux-actions'

export const getAllCategoriesRequest = createAction(
  'GET_ALL_CATEGORIES_REQUEST'
)
export const getAllCategoriesSuccess = createAction(
  'GET_ALL_CATEGORIES_SUCCESS'
)
export const getAllCategoriesFailed = createAction(
  'GET_ALL_CATEGORIES_FAILED'
)
