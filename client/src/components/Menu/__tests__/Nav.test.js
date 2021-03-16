import React from 'react'
import { shallow } from 'enzyme'

import { Nav } from '../Nav.component'

describe('Nav.component', () => {
  it('should if NavLink are present', () => {
    const wrapper = shallow(<Nav />)
    expect(wrapper.find('NavLink').length).toEqual(3)
  })
})
