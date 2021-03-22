import {
  fetchAllRecipesURL,
  fetchRecipeURL,
  createRecipeURL,
  updateRecipeURL,
  deleteRecipeURL,
  createFileRecipeURL,
  createFileRecipeStepURL,
  deleteFileRecipeURL,
} from '../Recipe.api'

describe('Ingredient.api', () => {
  it('should render goods urls', () => {
    const fetchAllRecipes = fetchAllRecipesURL()
    expect(fetchAllRecipes).toEqual(`${process.env.REACT_APP_API_URL}/recipe?with_calories=true`)

    const fetchRecipe = fetchRecipeURL('pancake')
    expect(fetchRecipe).toEqual(`${process.env.REACT_APP_API_URL}/recipe/pancake?with_calories=true`)

    const createRecipe = createRecipeURL('123')
    expect(createRecipe).toEqual(`${process.env.REACT_APP_API_URL}/recipe`)

    const updateRecipe = updateRecipeURL('123')
    expect(updateRecipe).toEqual(`${process.env.REACT_APP_API_URL}/recipe/123`)

    const deleteRecipe = deleteRecipeURL('123')
    expect(deleteRecipe).toEqual(`${process.env.REACT_APP_API_URL}/recipe/123`)

    const createFileRecipe = createFileRecipeURL('123')
    expect(createFileRecipe).toEqual(`${process.env.REACT_APP_API_URL}/files/recipe/123`)

    const deleteFileRecipe = deleteFileRecipeURL('123')
    expect(deleteFileRecipe).toEqual(`${process.env.REACT_APP_API_URL}/files/123`)

    const createFileRecipeStep = createFileRecipeStepURL('123', 'ABC')
    expect(createFileRecipeStep).toEqual(`${process.env.REACT_APP_API_URL}/files/recipe/123/step/ABC`)
  })
})
