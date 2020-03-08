import {
  getAllRecipesRequest,
  getAllRecipesSuccess,
  getAllRecipesFailed,
  getAllIngredientsOfRecipeRequest,
  getAllIngredientsOfRecipeSuccess,
  getAllIngredientsOfRecipeFailed,
  getRecipeRequest,
  getRecipeSuccess,
  getRecipeFailed,
  addRecipeRequest,
  addRecipeSuccess,
  addRecipeFailed,
  editRecipeRequest,
  editRecipeSuccess,
  editRecipeFailed,
  uploadPictureRecipeRequest,
  uploadPictureRecipeSuccess,
  uploadPictureRecipeFailed,
} from '../actions'

const cookServerUrl = process.env.REACT_APP_API_URL + '/recipe'

export const getAllRecipes = () => {
  return dispatch => {
    dispatch(getAllRecipesRequest());
    fetch(`${cookServerUrl}`)
    .then(res => res.json())
    .then(res => {
      console.log(res)
      if(res.error) {
        throw(res.error);
      }
      dispatch(getAllRecipesSuccess(res.data));
      return res.recipes;
    })
    .catch(error => {
      dispatch(getAllRecipesFailed(error));
    })
  }
}

export const getRecipe = (data) => {
  return (dispatch) => {
    dispatch(getRecipeRequest());
    fetch(`${cookServerUrl}/${data}`)
    .then(res => res.json())
    .then(res => {
      if(res.error) {
        throw(res.error);
      }
      dispatch(getRecipeSuccess(res.recipe));
      return res.recipes;
    })
    .catch(error => {
      dispatch(getRecipeFailed(error));
    })
  }
}

export const getAllIngredientsOfRecipe = (data) => {
  return (dispatch) => {
    dispatch(getAllIngredientsOfRecipeRequest());
    fetch(`${cookServerUrl}/${data}/ingredients`)
    .then(res => res.json())
    .then(res => {
      if(res.error) {
        throw(res.error);
      }
      dispatch(getAllIngredientsOfRecipeSuccess(res.recipe));
      return res.recipes;
    })
    .catch(error => {
      dispatch(getAllIngredientsOfRecipeFailed(error));
    })
  }
}

export const addRecipe = (data) => {
  return (dispatch) => {
    dispatch(addRecipeRequest());
    return new Promise((resolve, reject) => {
      fetch(`${cookServerUrl}/add`, {
        method: 'POST',
        headers: new Headers({
          'Content-Type': 'application/json'
        }),
        body: JSON.stringify(data)
      })
      .then(response => {
        if (response.ok) {
          dispatch(addRecipeSuccess(resolve(response.json())));
        } else {
          response.json().then(json => { reject(json) })
        }
      })
      .catch(error => {
        dispatch(addRecipeFailed(error));
      })
    })
  }
}

export const uploadDocument = (form) => {
  return (dispatch) => {
    if(form.image === undefined) {
      dispatch(uploadPictureRecipeSuccess())
      return;
    }
    const data = new FormData()
    data.append('file', form.image)
    data.append('filename', form.image.uid)

    dispatch(uploadPictureRecipeRequest());
    return new Promise((resolve, reject) => {
      fetch(`${cookServerUrl}/files`, {
        method: 'POST',
        body: data
      })
      .then(response => {
        if (response.ok) {
          dispatch(uploadPictureRecipeSuccess())
          resolve(response.json())
        } else {
          response.json().then(json => { reject(json) })
        }
      })
      .catch(error => {
        dispatch(uploadPictureRecipeFailed(error))
      })
    })
  }
}

export const editRecipe = (data) => {
  return (dispatch) => {
    dispatch(editRecipeRequest());
    return new Promise((resolve, reject) => {
      fetch(`${cookServerUrl}/edit`, {
        method: 'PUT',
        headers: new Headers({
          'Content-Type': 'application/json'
        }),
        body: JSON.stringify(data)
      })
      .then(response => {
        if (response.ok) {
          dispatch(editRecipeSuccess(resolve(response.json())));
        } else {
          response.json().then(json => { reject(json) })
        }
      })
      .catch(error => {
        dispatch(editRecipeFailed(error));
      })
    })
  }
}
