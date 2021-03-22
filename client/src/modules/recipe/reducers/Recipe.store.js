import { Record, List } from 'immutable'
import remove from 'lodash/remove'
import find from 'lodash/find'

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
    return -1
  }

  return entry[0]
}

export function setRecipes(state, recipes) {
  return !recipes ? state : state.set('content', List(recipes))
}

export const updateFilesInRecipe = (state, index, file) =>
  getAllRecipes(state).updateIn([index], recipe => ({
    ...recipe,
    files: [...recipe.files, ...file],
  }))

export const updateFilesRecipeStep = (state, index, step_id, file) =>
  getAllRecipes(state).updateIn([index], recipe => {
    const step = find(recipe.steps, step => step._id === step_id)
    const stepsExist = step.files === undefined ? [] : step.files
    step.files = [...stepsExist, ...file]

    return {
      ...recipe,
      steps: [...recipe.steps],
    }
  })

export const removeFileInRecipe = (state, index, urlFile) =>
  getAllRecipes(state).updateIn([index], recipe => {
    const newfiles = remove(recipe.files, file => file !== urlFile)
    return {
      ...recipe,
      files: newfiles,
    }
  })

export const removeFileRecipeStep = (state, index, step_id, urlFile) =>
  getAllRecipes(state).updateIn([index], recipe => {
    const step = find(recipe.steps, step => step._id === step_id)
    const newfiles = remove(step.files, file => file !== urlFile)

    step.files = newfiles

    return {
      ...recipe,
      steps: [...recipe.steps],
    }
  })
