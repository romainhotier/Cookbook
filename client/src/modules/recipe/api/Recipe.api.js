export const fetchAllRecipesURL = () => `${process.env.REACT_APP_API_URL}/recipe?with_calories=true`

export const fetchRecipeURL = slug => `${process.env.REACT_APP_API_URL}/recipe/${slug}?with_calories=true`

export const createRecipeURL = () => `${process.env.REACT_APP_API_URL}/recipe`

export const updateRecipeURL = id_recipe => `${process.env.REACT_APP_API_URL}/recipe/${id_recipe}`

export const deleteRecipeURL = id_recipe => `${process.env.REACT_APP_API_URL}/recipe/${id_recipe}`

// FILE RECIPE
export const createFileRecipeURL = id_recipe => `${process.env.REACT_APP_API_URL}/files/recipe/${id_recipe}`

export const deleteFileRecipeURL = path => `${process.env.REACT_APP_API_URL}/files/${path}`

// FILE RECIPE STEP
export const createFileRecipeStepURL = (id_recipe, id_step) =>
  `${process.env.REACT_APP_API_URL}/files/recipe/${id_recipe}/step/${id_step}`
