import { createAction } from 'redux-actions'

// RECIPE
export const postFileRecipeRequest = createAction('POST_FILE_IN_RECIPE_REQUEST')
export const postFileRecipeSuccess = createAction('POST_FILE_IN_RECIPE_SUCCESS')
export const postFileRecipeFailed = createAction('POST_FILE_IN_RECIPE_FAILED')

export const deleteFileRecipeRequest = createAction('REMOVE_FILE_RECIPE_REQUEST')
export const deleteFileRecipeSuccess = createAction('REMOVE_FILE_RECIPE_SUCCESS')
export const deleteFileRecipeFailed = createAction('REMOVE_FILE_RECIPE_FAILED')

// RECIPE STEP
export const postFileRecipeStepRequest = createAction('POST_FILE_RECIPE_STEP_REQUEST')
export const postFileRecipeStepSuccess = createAction('POST_FILE_RECIPE_STEP_SUCCESS')
export const postFileRecipeStepFailed = createAction('POST_FILE_RECIPE_STEP_FAILED')

export const deleteFileRecipeStepRequest = createAction('REMOVE_FILE_RECIPE_STEP_REQUEST')
export const deleteFileRecipeStepSuccess = createAction('REMOVE_FILE_RECIPE_STEP_SUCCESS')
export const deleteFileRecipeStepFailed = createAction('REMOVE_FILE_RECIPE_STEP_FAILED')
