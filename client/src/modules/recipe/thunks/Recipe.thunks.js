import { notification } from 'antd'
import get from 'lodash/get'

import {
    getAllRecipesRequest,
    getAllRecipesSuccess,
    getAllRecipesFailed,
    getRecipeRequest,
    getRecipeSuccess,
    getRecipeFailed,
    postRecipeRequest,
    postRecipeSuccess,
    postRecipeFailed,
    putRecipeRequest,
    putRecipeSuccess,
    putRecipeFailed,
} from '../actions'

import {
    fetchAllRecipesURL,
    fetchRecipeURL,
    createRecipeURL,
    updateRecipeURL,
} from '../api/Recipe.api'

import { codeMsg } from 'constants/codeMsg.constants'
import { slugifyResponse } from 'constants/functions.constants'

export const fetchAllRecipe = () => (dispatch => {
    dispatch(getAllRecipesRequest());

    fetch(fetchAllRecipesURL())
    .then(res => res.json())
    .then(res => {
        if(res.error) {
        throw(res.error);
        }
        dispatch(getAllRecipesSuccess(res.data));
        return res.recipes;
    })
    .catch(error => {
        dispatch(getAllRecipesFailed(error));
    })
})

export const fetchRecipe = (slug) => (dispatch => {
    dispatch(getRecipeRequest());

    fetch(fetchRecipeURL(slug))
    .then(res => res.json())
    .then(res => {
        if(res.error) {
        throw(res.error);
        }
        dispatch(getRecipeSuccess(res.data));
        return res.recipe;
    })
    .catch(error => {
        dispatch(getRecipeFailed(error));
    })
})

export const postRecipe = (data) => (dispatch => {
  dispatch(postRecipeRequest());

  fetch(createRecipeURL(), {
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
        postRecipeSuccess(response.data)
      );
      notification['success']({
        message: 'Recette créée !',
        description:
          `${get(codeMsg, `${response.codeMsg}`)}`
      });
    } else {
      dispatch(
        dispatch(postRecipeFailed(response.detail))
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
    dispatch(postRecipeFailed(error));
  })

})

export const putRecipe = (id, data, isComplete = false) => (dispatch => {
  dispatch(putRecipeRequest());

  fetch(updateRecipeURL(id), {
    method: 'PUT',
    headers: new Headers({
      'Content-Type': 'application/json'
    }),
    body: JSON.stringify(data)
  })
  .then(res => res.json())
  .then(response => {
    if(response.codeStatus === 201) {
      dispatch(
        putRecipeSuccess(response.data)
      );
      notification['success']({
        message: isComplete ? 'Recette complétée !' : 'Recette modifiée !',
        description:
          `${get(codeMsg, `${response.codeMsg}`)}`
      });
    } else {
      dispatch(
        dispatch(putRecipeFailed(response.detail))
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
    dispatch(putRecipeFailed(error));
  })

})
