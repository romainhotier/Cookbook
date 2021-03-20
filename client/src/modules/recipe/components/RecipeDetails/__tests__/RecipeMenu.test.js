import React from 'react'
import { shallow } from 'enzyme'

import { RecipeMenu } from '../RecipeMenu.component'

describe('RecipeMenu.component', () => {
  it('should if Menu and Menu.Item are render', () => {
    const wrapper = shallow(<RecipeMenu slug="pancake" showModal={jest.fn()} />)

    expect(wrapper.find('Menu').length).toEqual(1)
    expect(wrapper.find('MenuItem').length).toEqual(2)
  })
})
