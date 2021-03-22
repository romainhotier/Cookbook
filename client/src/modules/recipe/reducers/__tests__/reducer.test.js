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
  putRecipeSuccess,
  putRecipeFailed,
  deleteRecipeRequest,
  deleteRecipeSuccess,
  deleteRecipeFailed,
  postFileRecipeRequest,
  postFileRecipeSuccess,
  postFileRecipeFailed,
  postFileRecipeStepRequest,
  postFileRecipeStepSuccess,
  postFileRecipeStepFailed,
  deleteFileRecipeRequest,
  deleteFileRecipeSuccess,
  deleteFileRecipeFailed,
  deleteFileRecipeStepRequest,
  deleteFileRecipeStepSuccess,
  deleteFileRecipeStepFailed,
} from 'modules/recipe/actions'

import { recipes, fileRecipe, fileRecipeStep } from 'modules/recipe/mocks/recipes.mock'

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

  it('should putRecipeSuccess return expected state', () => {
    const newState = setRecipes(initialStateImmutable, [recipes.content[0]])

    const updateRecipe = { ...recipes.content[0], nb_people: '40' }
    const putRecipeSuccessState = RecipeReducer(newState, putRecipeSuccess(updateRecipe)).toJS()

    const expectedState = {
      content: [updateRecipe],
      loadingPostRecipe: false,
    }

    expect(putRecipeSuccessState).toMatchObject(expectedState)
  })

  it('should putRecipeSuccess without data return state', () => {
    const updateRecipe = { ...recipes.content[0], title: 'Banane Jaune' }
    const putRecipeSuccessState = RecipeReducer(initialStateImmutable, putRecipeSuccess(updateRecipe)).toJS()

    const expectedState = {
      content: [],
      loadingPostRecipe: false,
    }

    expect(putRecipeSuccessState).toMatchObject(expectedState)
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

  /*
   ** POST FILES RECIPE STEP
   */
  it('should postFileRecipeStepRequest return expected state', () => {
    const postFileRecipeStepRequestState = RecipeReducer(initialStateImmutable, postFileRecipeStepRequest()).toJS()

    const expectedState = initialState

    expect(postFileRecipeStepRequestState).toMatchObject(expectedState)
  })

  it('should postFileRecipeStepSuccess return expected state', () => {
    const newState = setRecipes(initialStateImmutable, [recipes.content[0]])

    const postFileRecipeStepSuccessState = RecipeReducer(newState, postFileRecipeStepSuccess(fileRecipeStep)).toJS()

    const expectedState = {
      content: [
        {
          ...recipes.content[0],
          steps: [
            {
              _id: '5fdf4387e29e317ae857b5e2',
              files: [
                '123.jpg',
                '456.jpg',
                'recipe/5fdf4387e29e317ae857b5e6/steps/5fdf4387e29e317ae857b5e2/pancake-banane.jpg',
              ],
              description:
                "Ecraser les bananes en purée et mélanger tous les ingrédients, jusqu'à l'obtention d'une pâte lisse. ",
            },
            {
              _id: '5fdf4387e29e317ae857b5e3',
              description:
                "Chauffer une poêle à feu moyen. Si la poêle n'est pas anti-adhésive, badigeonnez-la d'huile de coco (ou autres matières grasses). ",
            },
          ],
        },
      ],
    }

    expect(postFileRecipeStepSuccessState).toMatchObject(expectedState)
  })

  it('should postFileRecipeStepSuccess without good recipe id return expected state', () => {
    const newState = setRecipes(initialStateImmutable, [recipes.content[0]])
    const action = 'recipes/123/steps:456/test.jpg'

    const postFileRecipeStepSuccessState = RecipeReducer(newState, postFileRecipeStepSuccess(action)).toJS()

    expect(postFileRecipeStepSuccessState).toMatchObject(newState.toJS())
  })

  it('should postFileRecipeStepFailed return expected state', () => {
    const postFileRecipeStepFailedState = RecipeReducer(
      initialStateImmutable,
      postFileRecipeStepFailed('new error')
    ).toJS()

    const expectedState = {
      error: 'new error',
    }

    expect(postFileRecipeStepFailedState).toMatchObject(expectedState)
  })

  /*
   ** DELETE FILES IN RECIPE
   */
  it('should deleteFileRecipeStepRequest return expected state', () => {
    const deleteFileRecipeStepRequestState = RecipeReducer(initialStateImmutable, deleteFileRecipeStepRequest()).toJS()

    const expectedState = initialState

    expect(deleteFileRecipeStepRequestState).toMatchObject(expectedState)
  })

  it('should deleteFileRecipeStepSuccess return expected state', () => {
    const newState = setRecipes(initialStateImmutable, [{ ...recipes.content[0] }])
    const action = fileRecipeStep[0]

    const deleteFileRecipeStepSuccessState = RecipeReducer(newState, deleteFileRecipeStepSuccess(action)).toJS()

    const expectedState = {
      content: [
        {
          ...recipes.content[0],
          steps: [
            {
              _id: '5fdf4387e29e317ae857b5e2',
              description:
                "Ecraser les bananes en purée et mélanger tous les ingrédients, jusqu'à l'obtention d'une pâte lisse. ",
              files: ['123.jpg', '456.jpg'],
            },
            {
              _id: '5fdf4387e29e317ae857b5e3',
              description:
                "Chauffer une poêle à feu moyen. Si la poêle n'est pas anti-adhésive, badigeonnez-la d'huile de coco (ou autres matières grasses). ",
            },
          ],
        },
      ],
    }

    expect(deleteFileRecipeStepSuccessState).toMatchObject(expectedState)
  })

  it('should deleteFileRecipeStepSuccess without good recipe id return expected state', () => {
    const newState = setRecipes(initialStateImmutable, [{ ...recipes.content[0], files: fileRecipe }])
    const action = 'recipes/123/steps/abc/test.jpg'

    const deleteFileRecipeStepSuccessState = RecipeReducer(newState, deleteFileRecipeStepSuccess(action)).toJS()

    expect(deleteFileRecipeStepSuccessState).toMatchObject(newState.toJS())
  })

  it('should deleteFileRecipeStepFailed return expected state', () => {
    const deleteFileRecipeStepFailedState = RecipeReducer(
      initialStateImmutable,
      deleteFileRecipeStepFailed('new error')
    ).toJS()

    const expectedState = {
      error: 'new error',
    }

    expect(deleteFileRecipeStepFailedState).toMatchObject(expectedState)
  })
})
