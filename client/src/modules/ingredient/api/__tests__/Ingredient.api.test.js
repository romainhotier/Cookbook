import {
  fetchAllIngredientsURL,
  postIngredientURL,
  putIngredientURL,
  deleteIngredientURL,
  searchIngredientsURL,
} from '../Ingredient.api'

describe('Ingredient.api', () => {
  it('should render goods urls', () => {
    const fetchAllIngredients = fetchAllIngredientsURL()
    expect(fetchAllIngredients).toEqual(`${process.env.REACT_APP_API_URL}/ingredient`)

    const postIngredient = postIngredientURL()
    expect(postIngredient).toEqual(`${process.env.REACT_APP_API_URL}/ingredient`)

    const putIngredient = putIngredientURL('123')
    expect(putIngredient).toEqual(`${process.env.REACT_APP_API_URL}/ingredient/123`)

    const deleteIngredient = deleteIngredientURL('123')
    expect(deleteIngredient).toEqual(`${process.env.REACT_APP_API_URL}/ingredient/123`)

    const searchIngredients = searchIngredientsURL('123')
    expect(searchIngredients).toEqual(`${process.env.REACT_APP_API_URL}/ingredient/search`)
  })
})
