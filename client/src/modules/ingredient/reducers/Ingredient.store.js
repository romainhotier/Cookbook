import { Record, List } from 'immutable'

export const IngredientStateFactory = Record({
  content: List.of(),
  loadingFetchIngredient: false,
  loadingDeleteIngredient: false,
  loadingPostIngredient: false,
  loadingPutIngredient: false,
  error: null,
})

// GET
export const getAllIngredients = state => state.get('content')
export const getloadingFetchIngredient = state => state.get('loadingFetchIngredient')
export const getloadingPutIngredient = state => state.get('loadingPutIngredient')
export const getloadingPostIngredient = state => state.get('loadingPostIngredient')

// SET
export const findIngredientEntry = (state, IngredientId) => {
  const entry = getAllIngredients(state).findEntry(({ _id }) => _id === IngredientId)

  if (!entry) {
    return -1
  }
  return entry[0]
}

export function setIngredients(state, ingredients) {
  return !ingredients ? state : state.set('content', List(ingredients))
}
