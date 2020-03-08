import { handleActions } from 'redux-actions'

import {
  getAllCategoriesRequest,
  getAllCategoriesSuccess,
  getAllCategoriesFailed,
} from 'redux/category/actions'

const defaultState = {
  content: {},
  isFetching: false,
  error: null,
  success: null
}

const categoryReducer = handleActions(
  {
    /*
    ** GET ALL Categories
    */
    [getAllCategoriesRequest](state, action) {
      return {
        ...state,
        isFetching: true,
        error: null,
        success: null,
      }
    },

    [getAllCategoriesSuccess](state, action) {
      let categories = {}
      action.payload.forEach((category) => {
        categories[category.id] = {
          ...category
        }
      })

      return {
        ...state,
        content: categories,
        isFetching: false,
        success: true,
      }
    },

    [getAllCategoriesFailed](state, action) {
      return {
        ...state,
        isFetching: false,
        error: true,
        success: false,
      }
    },
  },
  defaultState
)

export default categoryReducer
