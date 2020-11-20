
import {
  getAllIngredientsRequest,
  getAllIngredientsSuccess,
  getAllIngredientsFailed,
  postIngredientRequest,
  postIngredientSuccess,
  postIngredientFailed,
} from '../actions'

import {
  fetchAllIngredientsURL,
  postIngredientURL,
} from '../api/Ingredient.api'

import { notification } from 'antd'
import get from 'lodash/get'
import { codeMsg } from 'constants/codeMsg.constants'
import { slugifyResponse } from 'constants/functions.constants'

export const fetchAllIngredients = () => (dispatch => {
  dispatch(getAllIngredientsRequest());

  fetch(fetchAllIngredientsURL())
  .then(res => res.json())
  .then(res => {
      if(res.error) {
      throw(res.error);
      }
      dispatch(getAllIngredientsSuccess(res.data));
      return res.recipes;
  })
  .catch(error => {
      dispatch(getAllIngredientsFailed(error));
  })
})

export const postIngredient = (data) => (dispatch => {
  dispatch(postIngredientRequest());

  fetch(postIngredientURL(), {
    method: 'POST',
    headers: new Headers({
      'Content-Type': 'application/json'
    }),
    body: JSON.stringify(data)
  })
  .then(res => res.json())
  .then(response => {
    if(response.codeStatus === 201) {
      dispatch(
        postIngredientSuccess(response)
      );
      console.log()
      notification['success']({
        message: 'Ingrédient créé !',
        description:
          `${get(codeMsg, `${response.codeMsg}`)}`
      });
    } else {
      dispatch(
        dispatch(postIngredientFailed(response.detail))
      );

      const errorFormat = get(codeMsg, `${response.codeMsg}.${slugifyResponse(response.detail.msg)}`);
      notification['error']({
        message: 'Oooh une erreur',
        description:
        `${errorFormat(response.detail.value)}`
      });
    }
  })
  .catch(error => {
    dispatch(postIngredientFailed(error));
  })

})
