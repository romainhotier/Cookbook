export const fetchAllRecipesURL = () => `${process.env.REACT_APP_API_URL}/recipe?with_files=true`

export const fetchRecipeURL = (slug) => `${process.env.REACT_APP_API_URL}/recipe/${slug}?with_files=true`
