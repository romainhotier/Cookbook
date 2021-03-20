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
  searchIngredientsRequest,
  searchIngredientsSuccess,
  searchIngredientsFailed,
} from 'modules/ingredient/actions'

import {
  ingredient as ingredientMock,
  ingredientsList as ingredientsListMock,
} from 'modules/ingredient/mocks/ingredients.mock'

import IngredientReducer from '../Ingredient.reducer'
import { setIngredients } from '../Ingredient.store'

const initialStateImmutable = IngredientReducer(undefined, {})
const initialState = IngredientReducer(undefined, {}).toJS()

describe('Ingredient Reducer', () => {
  it('should return the initial state', () => {
    expect(initialState).toMatchObject({
      content: {},
      loadingFetchIngredient: false,
      loadingDeleteIngredient: false,
      loadingPostIngredient: false,
      loadingPutIngredient: false,
      error: null,
    })
  })

  /*
   ** GET ALL INGREDIENTS
   */
  it('should getAllIngredientsRequest return expected state', () => {
    const getAllIngredientsRequestState = IngredientReducer(initialStateImmutable, getAllIngredientsRequest()).toJS()

    const expectedState = {
      content: [],
      loadingFetchIngredient: true,
    }

    expect(getAllIngredientsRequestState).toMatchObject(expectedState)
  })

  it('should getAllIngredientsSuccess return expected state', () => {
    const getAllIngredientsSuccessState = IngredientReducer(
      initialStateImmutable,
      getAllIngredientsSuccess(ingredientsListMock)
    ).toJS()

    const expectedState = {
      content: ingredientsListMock,
      loadingFetchIngredient: false,
    }

    expect(getAllIngredientsSuccessState).toMatchObject(expectedState)
  })

  it('should getAllIngredientsFailed return expected state', () => {
    const getAllIngredientsFailedState = IngredientReducer(initialStateImmutable, getAllIngredientsFailed()).toJS()

    const expectedState = {
      loadingFetchIngredient: false,
      error: true,
    }

    expect(getAllIngredientsFailedState).toMatchObject(expectedState)
  })

  /*
   ** POST RECIPE
   */
  it('should postIngredientRequest return expected state', () => {
    const postIngredientRequestState = IngredientReducer(initialStateImmutable, postIngredientRequest()).toJS()

    const expectedState = {
      content: [],
      loadingPostIngredient: true,
    }

    expect(postIngredientRequestState).toMatchObject(expectedState)
  })

  it('should postIngredientSuccess return expected state', () => {
    const postIngredientSuccessState = IngredientReducer(
      initialStateImmutable,
      postIngredientSuccess({ data: ingredientMock })
    ).toJS()

    const expectedState = {
      content: [ingredientMock],
      loadingPostIngredient: false,
    }

    expect(postIngredientSuccessState).toMatchObject(expectedState)
  })

  it('should postIngredientFailed return expected state', () => {
    const postIngredientFailedState = IngredientReducer(initialStateImmutable, postIngredientFailed()).toJS()

    const expectedState = {
      loadingPostIngredient: false,
      error: true,
    }

    expect(postIngredientFailedState).toMatchObject(expectedState)
  })

  /*
   ** PUT INGREDIENT
   */
  it('should putIngredientRequest return expected state', () => {
    const putIngredientRequestState = IngredientReducer(initialStateImmutable, putIngredientRequest()).toJS()

    const expectedState = {
      loadingPutIngredient: true,
    }

    expect(putIngredientRequestState).toMatchObject(expectedState)
  })

  it('should putIngredientSuccess return expected state', () => {
    const newState = setIngredients(initialStateImmutable, [ingredientsListMock[0]])

    const updateIngredient = { ...ingredientsListMock[0], title: 'Banane Jaune' }
    const putIngredientSuccessState = IngredientReducer(
      newState,
      putIngredientSuccess({ data: updateIngredient })
    ).toJS()

    const expectedState = {
      content: [updateIngredient],
      loadingPostIngredient: false,
    }

    expect(putIngredientSuccessState).toMatchObject(expectedState)
  })

  it('should putIngredientSuccess without data return state', () => {
    const updateIngredient = { ...ingredientsListMock[0], title: 'Banane Jaune' }
    const putIngredientSuccessState = IngredientReducer(
      initialStateImmutable,
      putIngredientSuccess({ data: updateIngredient })
    ).toJS()

    const expectedState = {
      content: [],
      loadingPostIngredient: false,
    }

    expect(putIngredientSuccessState).toMatchObject(expectedState)
  })

  it('should putIngredientFailed return expected state', () => {
    const putIngredientFailedState = IngredientReducer(initialStateImmutable, putIngredientFailed('bad request')).toJS()

    const expectedState = {
      loadingPutIngredient: false,
      error: 'bad request',
    }

    expect(putIngredientFailedState).toMatchObject(expectedState)
  })

  /*
   ** DELETE INGREDIENT
   */
  it('should deleteIngredientRequest return expected state', () => {
    const deleteIngredientRequestState = IngredientReducer(initialStateImmutable, deleteIngredientRequest()).toJS()

    const expectedState = {
      content: {},
      loadingDeleteIngredient: true,
    }

    expect(deleteIngredientRequestState).toMatchObject(expectedState)
  })

  it('should deleteIngredientSuccess without good id return expected state', () => {
    const deleteIngredientSuccessState = IngredientReducer(
      initialStateImmutable,
      deleteIngredientSuccess(ingredientMock._id)
    ).toJS()

    const expectedState = {
      content: [],
      loadingDeleteIngredient: false,
    }

    expect(deleteIngredientSuccessState).toMatchObject(expectedState)
  })

  it('should deleteIngredientSuccess return expected state', () => {
    const newState = setIngredients(initialStateImmutable, [ingredientsListMock[0], ingredientsListMock[1]])

    const deleteIngredientSuccessState = IngredientReducer(
      newState,
      deleteIngredientSuccess(ingredientsListMock[0]._id)
    ).toJS()

    const expectedState = {
      content: [ingredientsListMock[1]],
      loadingDeleteIngredient: false,
    }

    expect(deleteIngredientSuccessState).toMatchObject(expectedState)
  })

  it('should deleteIngredientFailed return expected state', () => {
    const deleteIngredientFailedState = IngredientReducer(
      initialStateImmutable,
      deleteIngredientFailed('bad data')
    ).toJS()

    const expectedState = {
      loadingDeleteIngredient: false,
      error: 'bad data',
    }

    expect(deleteIngredientFailedState).toMatchObject(expectedState)
  })

  /*
   ** SEARCH INGREDIENT
   */
  it('should searchIngredientsRequest return expected state', () => {
    const searchIngredientsRequestState = IngredientReducer(initialStateImmutable, searchIngredientsRequest()).toJS()

    const expectedState = {
      content: [],
      error: null,
    }

    expect(searchIngredientsRequestState).toMatchObject(expectedState)
  })

  it('should searchIngredientsSuccess return expected state', () => {
    const searchIngredientsSuccessState = IngredientReducer(
      initialStateImmutable,
      searchIngredientsSuccess([ingredientsListMock[0]])
    ).toJS()

    const expectedState = {
      content: [ingredientsListMock[0]],
    }

    expect(searchIngredientsSuccessState).toMatchObject(expectedState)
  })

  it('should searchIngredientsFailed return expected state', () => {
    const searchIngredientsFailedState = IngredientReducer(
      initialStateImmutable,
      searchIngredientsFailed('bad data')
    ).toJS()

    const expectedState = {
      error: 'bad data',
    }

    expect(searchIngredientsFailedState).toMatchObject(expectedState)
  })
})
