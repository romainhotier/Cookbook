import {
  getAllIngredientsRequest,
  getAllIngredientsSuccess,
  getAllIngredientsFailed,
  postIngredientRequest,
  postIngredientSuccess,
  postIngredientFailed,
  deleteIngredientRequest,
  deleteIngredientSuccess,
  deleteIngredientFailed,
  putIngredientRequest,
  putIngredientSuccess,
  putIngredientFailed,
  searchIngredientsRequest,
  searchIngredientsSuccess,
  searchIngredientsFailed,
} from '../actions'

import {
  fetchAllIngredientsURL,
  postIngredientURL,
  deleteIngredientURL,
  putIngredientURL,
  searchIngredientsURL,
} from '../api/Ingredient.api'

import { notification } from 'antd'
import get from 'lodash/get'
import { codeMsg } from 'constants/codeMsg.constants'
import { slugifyResponse } from 'constants/functions.constants'

export const fetchAllIngredients = () => dispatch => {
  dispatch(getAllIngredientsRequest())

  fetch(fetchAllIngredientsURL())
    .then(res => res.json())
    .then(res => {
      if (res.error) {
        throw res.error
      }
      return dispatch(getAllIngredientsSuccess(res.data))
    })
    .catch(error => {
      dispatch(getAllIngredientsFailed(error))
    })
}

export const postIngredient = data => dispatch => {
  dispatch(postIngredientRequest())

  fetch(postIngredientURL(), {
    method: 'POST',
    headers: new Headers({
      'Content-Type': 'application/json',
    }),
    body: JSON.stringify(data),
  })
    .then(res => res.json())
    .then(response => {
      if (response.codeStatus === 201) {
        dispatch(postIngredientSuccess(response))
        notification['success']({
          message: 'Ingrédient créé !',
          description: `${get(codeMsg, `${response.codeMsg}`)}`,
        })
      } else {
        dispatch(dispatch(postIngredientFailed(response.detail)))

        const errorFormat = get(codeMsg, `${response.codeMsg}.${slugifyResponse(response.detail.msg)}`)
        notification['error']({
          message: 'Oooh une erreur',
          description: `${errorFormat(response.detail.value)}`,
        })
      }
    })
    .catch(error => {
      dispatch(postIngredientFailed(error))
    })
}

export const deleteIngredient = id => dispatch => {
  dispatch(deleteIngredientRequest())

  fetch(deleteIngredientURL(id), {
    method: 'DELETE',
  })
    .then(res => res.json())
    .then(response => {
      if (response.codeStatus === 200) {
        dispatch(deleteIngredientSuccess(response.data))
        notification['success']({
          message: 'Ingrédient Supprimé !',
        })
      } else {
        dispatch(dispatch(deleteIngredientFailed(response.detail)))

        const errorFormat = get(codeMsg, `${response.codeMsg}.${slugifyResponse(response.detail.msg)}`)
        notification['error']({
          message: 'Oooh une erreur',
          description: `${errorFormat(response.detail.value)}`,
        })
      }
    })
    .catch(error => {
      dispatch(deleteIngredientFailed(error))
    })
}

export const putIngredient = ({ data, id }) => dispatch => {
  dispatch(putIngredientRequest())

  fetch(putIngredientURL(id), {
    method: 'PUT',
    headers: new Headers({
      'Content-Type': 'application/json',
    }),
    body: JSON.stringify(data),
  })
    .then(res => res.json())
    .then(response => {
      if (response.codeStatus === 200) {
        dispatch(putIngredientSuccess(response))
        notification['success']({
          message: 'Ingrédient modifiée !',
          description: `${get(codeMsg, `${response.codeMsg}`)}`,
        })
      } else {
        dispatch(dispatch(putIngredientFailed(response.detail)))

        const errorFormat = get(codeMsg, `${response.codeMsg}.${slugifyResponse(response.detail.msg)}`)
        notification['error']({
          message: 'Oooh une erreur',
          description: `${errorFormat(response.detail.value)}`,
        })
      }
    })
    .catch(error => {
      dispatch(putIngredientFailed(error))
    })
}

export const searchIngredients = param => dispatch => {
  let params = new URLSearchParams(param)
  dispatch(searchIngredientsRequest())

  fetch(searchIngredientsURL() + '?' + params)
    .then(res => res.json())
    .then(res => {
      if (res.error) {
        throw res.error
      }
      return dispatch(searchIngredientsSuccess(res.data))
    })
    .catch(error => {
      dispatch(searchIngredientsFailed(error))
    })
}
