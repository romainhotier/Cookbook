const cookServerUrl = 'http://192.168.1.84:5000'

export const fetchAllRecipesURL = () => `${cookServerUrl}/recipe?with_files=true`

export const fetchRecipeURL = (slug) => `${cookServerUrl}/recipe/${slug}?with_files=true`
