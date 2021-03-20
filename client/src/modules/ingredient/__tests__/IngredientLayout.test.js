import React from 'react'
import { shallow } from 'enzyme'

import { IngredientLayout } from '../IngredientLayout'

describe('IngredientLayout', () => {
  it('should IngredientLayout exist', () => {
    const wrapper = shallow(<IngredientLayout />)
    expect(wrapper.find('Switch').length).toEqual(1)
    expect(wrapper.find('Route').length).toEqual(1)
  })
})
