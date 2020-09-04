import { combineReducers } from 'redux'

import {RecipeReducer} from './recipe/reducers'

const rootReducer = combineReducers({
    recipes: RecipeReducer
})

export default rootReducer
