import React from 'react'
import { shallow } from 'enzyme'

import UserContent from '../UserContent.component'

describe('UserContent.component', () => {
  it('should if h2 is present', () => {
    const wrapper = shallow(<UserContent title="My Title" />)

    expect(wrapper.find('h2').length).toEqual(1)
  })
})
