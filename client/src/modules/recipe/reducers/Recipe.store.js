import { Record, List } from 'immutable'
import remove from 'lodash/remove'

export const RecipeStateFactory = Record({
  content: List.of(),
  loading: false,
  loadingFetchRecipe: false,
  loadingPostRecipe: false,
  loadingPutRecipe: false,
  error: null,
})

// GET
export const getAllRecipes = state => state.get('content')
export const getloadingFetchRecipe = state => state.get('loadingFetchRecipe')
export const getloadingPutRecipe = state => state.get('loadingPutRecipe')
export const getloadingPostRecipe = state => state.get('loadingPostRecipe')

// SET
export const findRecipeEntry = (state, recipeId) => {
  const entry = getAllRecipes(state).findEntry(({ _id }) => _id === recipeId)

  if (!entry) {
    return [-1, null]
  }
  return { index: entry[0], value: entry[1] }
}

export function setRecipes(state, recipes) {
  return !recipes ? state : state.set('content', List(recipes))
}

export const updateFilesInRecipe = (state, index, file) =>
  getAllRecipes(state).updateIn([index], recipe => ({
    ...recipe,
    files: [...recipe.files, ...file],
  }))

export const removeFileInRecipe = (state, index, urlFile) =>
  getAllRecipes(state).updateIn([index], recipe => {
    const newfiles = remove(recipe.files, file => file !== urlFile)
    return {
      ...recipe,
      files: newfiles,
    }
  })
