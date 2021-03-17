export const fetchAllIngredientsURL = () => `${process.env.REACT_APP_API_URL}/ingredient`

export const postIngredientURL = () => `${process.env.REACT_APP_API_URL}/ingredient`

export const putIngredientURL = id => `${process.env.REACT_APP_API_URL}/ingredient/${id}`

export const deleteIngredientURL = id => `${process.env.REACT_APP_API_URL}/ingredient/${id}`

export const searchIngredientsURL = () => `${process.env.REACT_APP_API_URL}/ingredient/search`
