
import {
    getAllRecipesRequest,
    getAllRecipesSuccess,
    getAllRecipesFailed,
    getRecipeRequest,
    getRecipeSuccess,
    getRecipeFailed,
} from '../actions'

import {
    fetchAllRecipesURL,
    fetchRecipeURL
} from '../api/Recipe.api'

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

export const fetchRecipe = (id) => (dispatch => {
    dispatch(getRecipeRequest());

    fetch(fetchRecipeURL(id))
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