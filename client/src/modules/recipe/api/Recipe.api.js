export const fetchAllRecipesURL = () => `${process.env.REACT_APP_API_URL}/recipe`

export const fetchRecipeURL = slug => `${process.env.REACT_APP_API_URL}/recipe/${slug}?with_files=true`

export const createRecipeURL = () => `${process.env.REACT_APP_API_URL}/recipe`

export const updateRecipeURL = id_recipe => `${process.env.REACT_APP_API_URL}/recipe/${id_recipe}`

export const createFileRecipeURL = id_recipe => `${process.env.REACT_APP_API_URL}/files/recipe/${id_recipe}`

export const deleteFileRecipeURL = path => `${process.env.REACT_APP_API_URL}/files/${path}`
