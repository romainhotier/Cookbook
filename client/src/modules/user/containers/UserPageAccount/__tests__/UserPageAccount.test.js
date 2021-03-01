import React from 'react'
import { shallow } from 'enzyme'

import UserPageAccount from '../UserPageAccount.container'

describe('UserPageAccount.container', () => {
  it('should if UserContent is present', () => {
    const wrapper = shallow(<UserPageAccount />)
    expect(wrapper.find('UserContent').length).toEqual(1)
  })
})
