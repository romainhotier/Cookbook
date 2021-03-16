import { recipes, fileRecipe } from 'modules/recipe/mocks/mock.recipes'

import {
  RecipeStateFactory,
  getAllRecipes,
  setRecipes,
  getloadingFetchRecipe,
  getloadingPostRecipe,
  getloadingPutRecipe,
} from '../Recipe.store'

export const defaultInitialState = RecipeStateFactory()

describe('Recipe Store', () => {
  it('should return the initial state', () => {
    expect(defaultInitialState.toJS()).toMatchObject({
      content: {},
      loading: false,
      loadingFetchRecipe: false,
      loadingPostRecipe: false,
      loadingPutRecipe: false,
      error: null,
    })
  })

  /* GET ALL RECIPES */
  it('should getAllRecipes return content state', () => {
    expect(getAllRecipes(defaultInitialState).toJS()).toMatchObject({})

    const newState = setRecipes(defaultInitialState, [recipes.content[0], recipes.content[1]])
    expect(getAllRecipes(newState).toJS()).toMatchObject([recipes.content[0], recipes.content[1]])
  })

  /* GET loading Fetch Recipe */
  it('should getloadingFetchRecipe return loadingFetchRecipe state', () => {
    expect(getloadingFetchRecipe(defaultInitialState)).toEqual(false)
  })

  /* GET loading Post Recipe */
  it('should getloadingPostRecipe return loadingPostRecipe state', () => {
    expect(getloadingPostRecipe(defaultInitialState)).toEqual(false)
  })

  /* GET loading Put Recipe */
  it('should getloadingPutRecipe return loadingPutRecipe state', () => {
    expect(getloadingPutRecipe(defaultInitialState)).toEqual(false)
  })
})
