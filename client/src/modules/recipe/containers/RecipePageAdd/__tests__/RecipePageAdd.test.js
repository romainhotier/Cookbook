import React from 'react'
import { shallow } from 'enzyme'

import { RecipePageAdd } from '../RecipePageAdd.container'

describe('RecipePageDetails.container', () => {
  it('should if h2 and RecipeForm are render', () => {
    const wrapper = shallow(<RecipePageAdd postRecipe={jest.fn()} />)

    expect(wrapper.find('h2').length).toEqual(1)
    expect(wrapper.find('RecipeForm').length).toEqual(1)
  })
})
