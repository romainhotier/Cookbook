import { combineReducers } from 'redux'

import { RecipeReducer } from './recipe/reducers'
import { IngredientReducer } from './ingredient/reducers'

const rootReducer = combineReducers({
  recipes: RecipeReducer,
  ingredients: IngredientReducer,
})

export default rootReducer
