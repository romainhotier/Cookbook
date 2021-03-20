import React from 'react'
import { shallow } from 'enzyme'

import SwitchTheme from '../SwitchTheme.component'

describe('SwitchTheme.component', () => {
  it('should if SwitchTheme is present in the page', () => {
    const wrapper = shallow(<SwitchTheme />)
    expect(wrapper.find('ContextConsumer').length).toEqual(1)
  })
})
