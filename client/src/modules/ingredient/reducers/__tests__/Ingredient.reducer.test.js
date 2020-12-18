import {
  getAllIngredientsRequest,
  getAllIngredientsSuccess,
  getAllIngredientsFailed,
  postIngredientRequest,
  postIngredientSuccess,
  postIngredientFailed,
  putIngredientRequest,
  putIngredientSuccess,
  putIngredientFailed,
  deleteIngredientRequest,
  deleteIngredientSuccess,
  deleteIngredientFailed,
} from '../../actions'

import IngredientReducer from '../Ingredient.reducer'
import { ingredientsList, ingredient } from 'modules/ingredient/__mocks__/ingredients.mock'

describe('Ingredient Reducer', () => {
  it('should return the initial state', () => {
    expect(IngredientReducer(undefined, {})).toMatchObject({
      content: {},
      loadingFetchIngredients: false,
      loadingDeleteIngredient: false,
      loadingPostIngredient: false,
      loadingPutIngredient: false,
      error: null,
    })
  })

  // GET ALL
  it('should handle getAllIngredientsRequest', () => {
    const initialState = {
      content: {},
      loadingFetchIngredients: false,
      error: null,
    }
    const expectedState = {
      content: {},
      loadingFetchIngredients: true,
      error: null,
    }
    expect(IngredientReducer(initialState, getAllIngredientsRequest())).toMatchObject(expectedState)
  })

  it('should handle getAllIngredientsSuccess', () => {
    const initialState = {
      content: {},
      loadingFetchIngredients: false,
      error: null,
    }
    const expectedState = {
      content: {
        banane: {
          id: '5fdb8dbdc0749c35c039b43f',
          name: 'Banane',
          nutriments: {
            calories: '89',
            carbohydrates: '23',
            fats: '0.3',
            portion: '120',
            proteins: '1.1',
          },
          slug: 'banane',
          unit: 'g',
        },
        farine: {
          id: '6gtr48dc0749c35c039b43f',
          name: 'Farine',
          nutriments: {
            calories: '89',
            carbohydrates: '23',
            fats: '0.3',
            portion: '120',
            proteins: '1.1',
          },
          slug: 'farine',
          unit: 'g',
        },
      },
      loadingFetchIngredients: false,
      error: null,
    }

    expect(IngredientReducer(initialState, getAllIngredientsSuccess(ingredientsList))).toMatchObject(expectedState)
  })

  it('should handle getAllIngredientsFailed', () => {
    const initialState = {
      content: {},
      loadingFetchIngredients: false,
      error: null,
    }
    const expectedState = {
      content: {},
      loadingFetchIngredients: false,
      error: `Error: Error msg`,
    }
    expect(IngredientReducer(initialState, getAllIngredientsFailed(new Error('Error msg')))).toMatchObject(
      expectedState
    )
  })

  // POST
  it('should handle postIngredientRequest', () => {
    const initialState = {
      content: {},
      loadingPostIngredient: false,
      error: null,
    }
    const expectedState = {
      content: {},
      loadingPostIngredient: true,
      error: null,
    }
    expect(IngredientReducer(initialState, postIngredientRequest())).toMatchObject(expectedState)
  })

  it('should handle postIngredientSuccess', () => {
    const initialState = {
      content: {},
      loadingPostIngredient: false,
      error: null,
    }
    const expectedState = {
      content: {
        banane: {
          id: '5fdb8dbdc0749c35c039b43f',
          name: 'Banane',
          nutriments: {
            calories: '89',
            carbohydrates: '23',
            fats: '0.3',
            portion: '120',
            proteins: '1.1',
          },
          slug: 'banane',
          unit: 'g',
        },
      },
      loadingPostIngredient: false,
      error: null,
    }

    expect(IngredientReducer(initialState, postIngredientSuccess({ data: ingredient }))).toMatchObject(expectedState)
  })

  it('should handle postIngredientFailed', () => {
    const initialState = {
      content: {},
      loadingPostIngredient: false,
      error: null,
    }
    const expectedState = {
      content: {},
      loadingPostIngredient: false,
      error: `Error: Error msg`,
    }
    expect(IngredientReducer(initialState, postIngredientFailed(new Error('Error msg')))).toMatchObject(expectedState)
  })

  // PUT
  it('should handle putIngredientRequest', () => {
    const initialState = {
      content: {},
      loadingPutIngredient: false,
      error: null,
    }
    const expectedState = {
      content: {},
      loadingPutIngredient: true,
      error: null,
    }
    expect(IngredientReducer(initialState, putIngredientRequest())).toMatchObject(expectedState)
  })

  it('should handle putIngredientSuccess', () => {
    const initialState = {
      content: {
        banane: {
          id: '5fdb8dbdc0749c35c039b43f',
          name: 'Banane',
          nutriments: {
            calories: '50',
            carbohydrates: '18',
            fats: '0.3',
            portion: '120',
            proteins: '1.1',
          },
          slug: 'banane',
          unit: 'ml',
        },
      },
      loadingPutIngredient: false,
      error: null,
    }
    const expectedState = {
      content: {
        banane: {
          id: '5fdb8dbdc0749c35c039b43f',
          name: 'Banane',
          nutriments: {
            calories: '89',
            carbohydrates: '23',
            fats: '0.3',
            portion: '120',
            proteins: '1.1',
          },
          slug: 'banane',
          unit: 'g',
        },
      },
      loadingPutIngredient: false,
      error: null,
    }

    expect(IngredientReducer(initialState, putIngredientSuccess({ data: ingredient }))).toMatchObject(expectedState)
  })

  it('should handle putIngredientFailed', () => {
    const initialState = {
      content: {},
      loadingPutIngredient: false,
      error: null,
    }
    const expectedState = {
      content: {},
      loadingPutIngredient: false,
      error: `Error: Error msg`,
    }
    expect(IngredientReducer(initialState, putIngredientFailed(new Error('Error msg')))).toMatchObject(expectedState)
  })

  // DELETE
  it('should handle deleteIngredientRequest', () => {
    const initialState = {
      content: {},
      loadingDeleteIngredient: false,
      error: null,
    }
    const expectedState = {
      content: {},
      loadingDeleteIngredient: true,
      error: null,
    }
    expect(IngredientReducer(initialState, deleteIngredientRequest())).toMatchObject(expectedState)
  })

  it('should handle deleteIngredientSuccess', () => {
    const initialState = {
      content: {
        banane: {
          id: '5fdb8dbdc0749c35c039b43f',
          name: 'Banane',
          nutriments: {
            calories: '50',
            carbohydrates: '18',
            fats: '0.3',
            portion: '120',
            proteins: '1.1',
          },
          slug: 'banane',
          unit: 'ml',
        },
      },
      loadingDeleteIngredient: false,
      error: null,
    }
    const expectedState = {
      content: {},
      loadingDeleteIngredient: false,
      error: null,
    }

    expect(IngredientReducer(initialState, deleteIngredientSuccess('5fdb8dbdc0749c35c039b43f'))).toMatchObject(
      expectedState
    )
  })

  it('should handle deleteIngredientFailed', () => {
    const initialState = {
      content: {},
      loadingDeleteIngredient: false,
      error: null,
    }
    const expectedState = {
      content: {},
      loadingDeleteIngredient: false,
      error: `Error: Error msg`,
    }
    expect(IngredientReducer(initialState, deleteIngredientFailed(new Error('Error msg')))).toMatchObject(expectedState)
  })
})
