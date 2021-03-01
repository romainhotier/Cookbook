import React from 'react'
import { shallow } from 'enzyme'
import configureStore from 'redux-mock-store'
import { Provider } from 'react-redux'

import { defaultState } from 'modules/recipe/reducers/Recipe.reducer'
import UserPageSaveRecipes from '../UserPageSaveRecipes.container'

describe('UserPageSaveRecipes.container', () => {
  it('should if UserContent is present', () => {
    const mockStore = configureStore()
    const store = mockStore({ recipes: defaultState })
    const wrapper = shallow(
      <Provider store={store}>
        <UserPageSaveRecipes fetchAllRecipe={jest.fn()} className="UserPageSaveRecipes" />
      </Provider>
    )

    expect(wrapper.find('.UserPageSaveRecipes').length).toEqual(1)
  })
})
