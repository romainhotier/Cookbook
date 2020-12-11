export const fetchAllRecipesURL = () => `${process.env.REACT_APP_API_URL}/recipe?with_files=true`

export const fetchRecipeURL = (slug) => `${process.env.REACT_APP_API_URL}/recipe/${slug}?with_files=true`

export const createRecipeURL = () => `${process.env.REACT_APP_API_URL}/recipe`

export const updateRecipeURL = (id_recipe) => `${process.env.REACT_APP_API_URL}/recipe/${id_recipe}`
