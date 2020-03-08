import { combineReducers } from 'redux'
import recipes from './recipe/reducers/recipeReducer'
import categories from './category/reducers/categoryReducer'

const rootReducer = combineReducers({
    recipes,
    categories,
})

export default rootReducer
