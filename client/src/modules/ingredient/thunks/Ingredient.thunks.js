
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
      'Accept': '*',
      'Content-Type': 'application/json'
    }),
    body: JSON.stringify(data)
  })
  .then(res => res.json())
  .then(response => {
    console.log('response', response)
    // if (response.ok) {
    //   dispatch(addRecipeSuccess(resolve(response.json())));
    // } else {
    //   response.json().then(json => { reject(json) })
    // }
  })
  .catch(error => {
      dispatch(postIngredientFailed(error));
  })

})
