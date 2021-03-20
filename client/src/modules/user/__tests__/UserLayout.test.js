import React from 'react'
import { shallow } from 'enzyme'

import { UserLayout } from '../UserLayout'

describe('UserLayout', () => {
  it('should UserLayout exist', () => {
    const wrapper = shallow(<UserLayout />)
    expect(wrapper.find('Switch').length).toEqual(1)
    expect(wrapper.find('Route').length).toEqual(3)
    expect(wrapper.find('.UserMenu').length).toEqual(1)
  })
})
