import React from 'react'
import { shallow } from 'enzyme'

import { RecipeLayout } from '../RecipeLayout'

describe('RecipeLayout', () => {
  it('should RecipeLayout exist', () => {
    const wrapper = shallow(<RecipeLayout />)
    expect(wrapper.find('Switch').length).toEqual(1)
    expect(wrapper.find('Route').length).toEqual(4)
  })
})
