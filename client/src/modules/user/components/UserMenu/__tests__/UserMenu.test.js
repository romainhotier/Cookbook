import React from 'react'
import { shallow } from 'enzyme'

import UserMenu from '../UserMenu.component'

describe('UserMenu.component', () => {
  it('should if MenuItem are present', () => {
    const wrapper = shallow(<UserMenu />)

    expect(wrapper.find('MenuItem').length).toEqual(3)
    expect(wrapper.find('NavLink').length).toEqual(3)
  })
})
