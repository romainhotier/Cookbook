import { notification } from 'antd'
import get from 'lodash/get'

import {
  postFileRecipeRequest,
  postFileRecipeSuccess,
  postFileRecipeFailed,
  postFileRecipeStepRequest,
  postFileRecipeStepSuccess,
  postFileRecipeStepFailed,
  deleteFileRecipeRequest,
  deleteFileRecipeSuccess,
  deleteFileRecipeFailed,
  deleteFileRecipeStepRequest,
  deleteFileRecipeStepSuccess,
  deleteFileRecipeStepFailed,
} from '../actions'

import { createFileRecipeURL, deleteFileRecipeURL, createFileRecipeStepURL } from '../api/Recipe.api'

import { codeMsg } from 'constants/codeMsg.constants'
import { slugifyResponse } from 'constants/functions.constants'

export const postFileRecipe = (id, data) => dispatch => {
  dispatch(postFileRecipeRequest())

  fetch(createFileRecipeURL(id), {
    method: 'POST',
    body: data,
  })
    .then(res => res.json())
    .then(response => {
      if (response.codeStatus === 201) {
        dispatch(postFileRecipeSuccess(response.data))
        notification['success']({
          message: 'Image ajoutée !',
        })
      } else {
        dispatch(dispatch(postFileRecipeFailed(response.detail)))

        const errorFormat = get(codeMsg, `${response.codeMsg}.${slugifyResponse(response.detail.msg)}`)
        notification['error']({
          message: 'Oooh une erreur',
          description: `${errorFormat(response.detail.value)}`,
        })
      }
    })
    .catch(error => {
      dispatch(postFileRecipeFailed(error))
    })
}

export const deleteFileRecipe = path => dispatch => {
  dispatch(deleteFileRecipeRequest())

  fetch(deleteFileRecipeURL(path), {
    method: 'DELETE',
  })
    .then(res => res.json())
    .then(response => {
      if (response.codeStatus === 200) {
        dispatch(deleteFileRecipeSuccess(response.data))
        notification['success']({
          message: 'Image supprimée !',
        })
      } else {
        dispatch(dispatch(deleteFileRecipeFailed(response.detail)))

        const errorFormat = get(codeMsg, `${response.codeMsg}.${slugifyResponse(response.detail.msg)}`)
        notification['error']({
          message: 'Oooh une erreur',
          description: `${errorFormat(response.detail.value)}`,
        })
      }
    })
    .catch(error => {
      dispatch(deleteFileRecipeFailed(error))
    })
}

export const postFileRecipeStep = ({ id_recipe, id_step, data }) => dispatch => {
  dispatch(postFileRecipeStepRequest())

  fetch(createFileRecipeStepURL(id_recipe, id_step), {
    method: 'POST',
    body: data,
  })
    .then(res => res.json())
    .then(response => {
      if (response.codeStatus === 201) {
        dispatch(postFileRecipeStepSuccess(response.data))
        notification['success']({
          message: 'Image ajoutée !',
        })
      } else {
        dispatch(dispatch(postFileRecipeStepFailed(response.detail)))

        const errorFormat = get(codeMsg, `${response.codeMsg}.${slugifyResponse(response.detail.msg)}`)
        notification['error']({
          message: 'Oooh une erreur',
          description: `${errorFormat(response.detail.value)}`,
        })
      }
    })
    .catch(error => {
      dispatch(postFileRecipeFailed(error))
    })
}

export const deleteFileRecipeStep = path => dispatch => {
  dispatch(deleteFileRecipeStepRequest())

  fetch(deleteFileRecipeURL(path), {
    method: 'DELETE',
  })
    .then(res => res.json())
    .then(response => {
      if (response.codeStatus === 200) {
        dispatch(deleteFileRecipeStepSuccess(response.data))
        notification['success']({
          message: 'Image supprimée !',
        })
      } else {
        dispatch(dispatch(deleteFileRecipeStepFailed(response.detail)))

        const errorFormat = get(codeMsg, `${response.codeMsg}.${slugifyResponse(response.detail.msg)}`)
        notification['error']({
          message: 'Oooh une erreur',
          description: `${errorFormat(response.detail.value)}`,
        })
      }
    })
    .catch(error => {
      dispatch(deleteFileRecipeStepFailed(error))
    })
}
