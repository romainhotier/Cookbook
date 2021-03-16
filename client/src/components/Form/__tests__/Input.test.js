import React from 'react'
import { shallow } from 'enzyme'
import { Input } from '../Input.component'

describe('Input.component', () => {
  it('should if FormItem is present in the page', () => {
    const wrapper = shallow(<Input label={'my Input'} />)
    expect(wrapper.find('FormItem').length).toEqual(1)
    expect(wrapper.find('Input').length).toEqual(1)
  })
})
