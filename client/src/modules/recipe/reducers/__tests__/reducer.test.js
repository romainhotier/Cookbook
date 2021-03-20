import {
  getAllRecipesRequest,
  getAllRecipesSuccess,
  getAllRecipesFailed,
  getRecipeRequest,
  getRecipeSuccess,
  getRecipeFailed,
  postRecipeRequest,
  postRecipeSuccess,
  postRecipeFailed,
  putRecipeRequest,
  putRecipeFailed,
  deleteRecipeRequest,
  deleteRecipeSuccess,
  deleteRecipeFailed,
  postFileRecipeRequest,
  postFileRecipeSuccess,
  postFileRecipeFailed,
  deleteFileRecipeRequest,
  deleteFileRecipeSuccess,
  deleteFileRecipeFailed,
} from 'modules/recipe/actions'

import { recipes, fileRecipe } from 'modules/recipe/mocks/recipes.mock'

import { setRecipes } from '../Recipe.store'
import RecipeReducer from '../Recipe.reducer'

const initialStateImmutable = RecipeReducer(undefined, {})
const initialState = RecipeReducer(undefined, {}).toJS()

describe('Recipe Reducer', () => {
  it('should return the initial state', () => {
    expect(initialState).toMatchObject({
      content: {},
      loading: false,
      loadingFetchRecipe: false,
      loadingPostRecipe: false,
      loadingPutRecipe: false,
      error: null,
    })
  })

  /*
   ** GET ALL RECIPES
   */
  it('should getAllRecipesRequest return expected state', () => {
    const getAllRecipesRequestState = RecipeReducer(initialStateImmutable, getAllRecipesRequest()).toJS()

    const expectedState = {
      content: {},
      loadingFetchRecipe: true,
    }

    expect(getAllRecipesRequestState).toMatchObject(expectedState)
  })

  it('should getAllRecipesSuccess return expected state', () => {
    const action = recipes.content
    const getAllRecipesSuccessState = RecipeReducer(initialStateImmutable, getAllRecipesSuccess(action)).toJS()

    const expectedState = {
      content: recipes.content,
      loadingFetchRecipe: false,
    }

    expect(getAllRecipesSuccessState).toMatchObject(expectedState)
  })

  it('should getAllRecipesFailed return expected state', () => {
    const getAllRecipesFailedState = RecipeReducer(initialStateImmutable, getAllRecipesFailed()).toJS()

    const expectedState = {
      loadingFetchRecipe: false,
      error: true,
    }

    expect(getAllRecipesFailedState).toMatchObject(expectedState)
  })

  /*
   ** GET RECIPE
   */
  it('should getRecipeRequest return expected state', () => {
    const getRecipeRequestState = RecipeReducer(initialStateImmutable, getRecipeRequest()).toJS()

    const expectedState = {
      content: {},
      loadingFetchRecipe: true,
    }

    expect(getRecipeRequestState).toMatchObject(expectedState)
  })

  it('should getRecipeSuccess return expected state', () => {
    const action = recipes.content[0]
    const getRecipeSuccessState = RecipeReducer(initialStateImmutable, getRecipeSuccess(action)).toJS()

    const expectedState = {
      content: [action],
      loadingFetchRecipe: false,
    }

    expect(getRecipeSuccessState).toMatchObject(expectedState)
  })

  it('should getRecipeFailed return expected state', () => {
    const getRecipeFailedState = RecipeReducer(initialStateImmutable, getRecipeFailed()).toJS()

    const expectedState = {
      loadingFetchRecipe: false,
      error: true,
    }

    expect(getRecipeFailedState).toMatchObject(expectedState)
  })

  /*
   ** POST RECIPE
   */
  it('should postRecipeRequest return expected state', () => {
    const postRecipeRequestState = RecipeReducer(initialStateImmutable, postRecipeRequest()).toJS()

    const expectedState = {
      content: {},
      loadingPostRecipe: true,
    }

    expect(postRecipeRequestState).toMatchObject(expectedState)
  })

  it('should postRecipeSuccess return expected state', () => {
    const action = recipes.content[0]
    const postRecipeSuccessState = RecipeReducer(initialStateImmutable, postRecipeSuccess(action)).toJS()

    const expectedState = {
      content: [action],
      loadingPostRecipe: false,
    }

    expect(postRecipeSuccessState).toMatchObject(expectedState)
  })

  it('should postRecipeFailed return expected state', () => {
    const postRecipeFailedState = RecipeReducer(initialStateImmutable, postRecipeFailed()).toJS()

    const expectedState = {
      loadingPostRecipe: false,
      error: true,
    }

    expect(postRecipeFailedState).toMatchObject(expectedState)
  })

  /*
   ** PUT RECIPE
   */
  it('should putRecipeRequest return expected state', () => {
    const putRecipeRequestState = RecipeReducer(initialStateImmutable, putRecipeRequest()).toJS()

    const expectedState = {
      loadingPutRecipe: true,
    }

    expect(putRecipeRequestState).toMatchObject(expectedState)
  })

  it('should putRecipeFailed return expected state', () => {
    const putRecipeFailedState = RecipeReducer(initialStateImmutable, putRecipeFailed()).toJS()

    const expectedState = {
      loadingPutRecipe: false,
      error: true,
    }

    expect(putRecipeFailedState).toMatchObject(expectedState)
  })

  /*
   ** DELETE RECIPE
   */
  it('should deleteRecipeRequest return expected state', () => {
    const deleteRecipeRequestState = RecipeReducer(initialStateImmutable, deleteRecipeRequest()).toJS()

    const expectedState = {
      content: {},
      loading: true,
    }

    expect(deleteRecipeRequestState).toMatchObject(expectedState)
  })

  it('should deleteRecipeSuccess without good id return expected state', () => {
    const action = recipes.content[0]._id
    const deleteRecipeSuccessState = RecipeReducer(initialStateImmutable, deleteRecipeSuccess(action)).toJS()

    const expectedState = {
      content: {},
      loading: false,
    }

    expect(deleteRecipeSuccessState).toMatchObject(expectedState)
  })

  it('should deleteRecipeSuccess return expected state', () => {
    const newState = setRecipes(initialStateImmutable, [recipes.content[0], recipes.content[1]])

    const action = recipes.content[0]._id
    const deleteRecipeSuccessState = RecipeReducer(newState, deleteRecipeSuccess(action)).toJS()

    const expectedState = {
      content: [recipes.content[1]],
      loading: false,
    }

    expect(deleteRecipeSuccessState).toMatchObject(expectedState)
  })

  it('should deleteRecipeFailed return expected state', () => {
    const deleteRecipeFailedState = RecipeReducer(initialStateImmutable, deleteRecipeFailed()).toJS()

    const expectedState = {
      loading: false,
      error: true,
    }

    expect(deleteRecipeFailedState).toMatchObject(expectedState)
  })

  /*
   ** POST FILES IN RECIPE
   */
  it('should postFileRecipeRequest return expected state', () => {
    const postFileRecipeRequestState = RecipeReducer(initialStateImmutable, postFileRecipeRequest()).toJS()

    const expectedState = initialState

    expect(postFileRecipeRequestState).toMatchObject(expectedState)
  })

  it('should postFileRecipeSuccess return expected state', () => {
    const newState = setRecipes(initialStateImmutable, [recipes.content[0]])
    const action = fileRecipe

    const postFileRecipeSuccessState = RecipeReducer(newState, postFileRecipeSuccess(action)).toJS()

    const expectedState = {
      content: [{ ...recipes.content[0], files: fileRecipe }],
    }

    expect(postFileRecipeSuccessState).toMatchObject(expectedState)
  })

  it('should postFileRecipeSuccess without good recipe id return expected state', () => {
    const newState = setRecipes(initialStateImmutable, [recipes.content[0]])
    const action = 'recipes/123/test.jpg'

    const postFileRecipeSuccessState = RecipeReducer(newState, postFileRecipeSuccess(action)).toJS()

    expect(postFileRecipeSuccessState).toMatchObject(newState.toJS())
  })

  it('should postFileRecipeFailed return expected state', () => {
    const postFileRecipeFailedState = RecipeReducer(initialStateImmutable, postFileRecipeFailed('new error')).toJS()

    const expectedState = {
      error: 'new error',
    }

    expect(postFileRecipeFailedState).toMatchObject(expectedState)
  })

  /*
   ** DELETE FILES IN RECIPE
   */
  it('should deleteFileRecipeRequest return expected state', () => {
    const deleteFileRecipeRequestState = RecipeReducer(initialStateImmutable, deleteFileRecipeRequest()).toJS()

    const expectedState = initialState

    expect(deleteFileRecipeRequestState).toMatchObject(expectedState)
  })

  it('should deleteFileRecipeSuccess return expected state', () => {
    const newState = setRecipes(initialStateImmutable, [{ ...recipes.content[0], files: fileRecipe }])
    const action = fileRecipe[0]

    const deleteFileRecipeSuccessState = RecipeReducer(newState, deleteFileRecipeSuccess(action)).toJS()

    const expectedState = {
      content: [{ ...recipes.content[0], files: [] }],
    }

    expect(deleteFileRecipeSuccessState).toMatchObject(expectedState)
  })

  it('should deleteFileRecipeSuccess without good recipe id return expected state', () => {
    const newState = setRecipes(initialStateImmutable, [{ ...recipes.content[0], files: fileRecipe }])
    const action = 'recipes/123/test.jpg'

    const deleteFileRecipeSuccessState = RecipeReducer(newState, deleteFileRecipeSuccess(action)).toJS()

    expect(deleteFileRecipeSuccessState).toMatchObject(newState.toJS())
  })

  it('should deleteFileRecipeFailed return expected state', () => {
    const deleteFileRecipeFailedState = RecipeReducer(initialStateImmutable, deleteFileRecipeFailed('new error')).toJS()

    const expectedState = {
      error: 'new error',
    }

    expect(deleteFileRecipeFailedState).toMatchObject(expectedState)
  })
})
