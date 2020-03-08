import {
  getAllCategoriesRequest,
  getAllCategoriesSuccess,
  getAllCategoriesFailed,
} from '../actions'

const cookServerUrl = process.env.REACT_APP_API_URL

export const getAllCategories = () => {
  return dispatch => {
    dispatch(getAllCategoriesRequest());
    fetch(`${cookServerUrl}/categories`)
    .then(res => res.json())
    .then(res => {
      if(res.error) {
        throw(res.error);
      }
      dispatch(getAllCategoriesSuccess(res.categories));
      return res.recipes;
    })
    .catch(error => {
      dispatch(getAllCategoriesFailed(error));
    })
  }
}
