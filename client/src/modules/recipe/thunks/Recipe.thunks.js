
import {
    getAllRecipesRequest,
    getAllRecipesSuccess,
    getAllRecipesFailed
} from '../actions'

import {
    AllRecipesURL
} from '../api/Recipe.api'

export const fetchAllRecipe = () => (dispatch => {
    dispatch(getAllRecipesRequest());

    fetch(AllRecipesURL)
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