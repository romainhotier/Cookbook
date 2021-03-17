import { ingredientsList as ingredientsListMock } from 'modules/ingredient/mocks/ingredients.mock'

import {
  IngredientStateFactory,
  getAllIngredients,
  setIngredients,
  getloadingFetchIngredient,
  getloadingPutIngredient,
  getloadingPostIngredient,
} from '../Ingredient.store'

export const defaultInitialState = IngredientStateFactory()

describe('Ingredient Store', () => {
  it('should return the initial state', () => {
    expect(defaultInitialState.toJS()).toMatchObject({
      content: {},
      loadingFetchIngredient: false,
      loadingDeleteIngredient: false,
      loadingPostIngredient: false,
      loadingPutIngredient: false,
      error: null,
    })
  })

  /* GET ALL INGREDIENTS */
  it('should getAllIngredients return content state', () => {
    expect(getAllIngredients(defaultInitialState).toJS()).toMatchObject({})

    const newState = setIngredients(defaultInitialState, ingredientsListMock)
    expect(getAllIngredients(newState).toJS()).toMatchObject(ingredientsListMock)
  })

  /* GET loading Fetch Ingredient */
  it('should getloadingFetchIngredient return loadingFetchIngredient state', () => {
    expect(getloadingFetchIngredient(defaultInitialState)).toEqual(false)
  })

  /* GET loading Post Ingredient */
  it('should getloadingPostIngredient return loadingPostIngredient state', () => {
    expect(getloadingPostIngredient(defaultInitialState)).toEqual(false)
  })

  /* GET loading Put Ingredient */
  it('should getloadingPutIngredient return loadingPutIngredient state', () => {
    expect(getloadingPutIngredient(defaultInitialState)).toEqual(false)
  })
})
