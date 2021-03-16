import React from 'react'
import { shallow } from 'enzyme'
import { Select } from '../Select.component'

const options = [
  {
    label: 'Pour 100 grammes',
    value: 'g',
  },
  {
    label: 'Pour 100 millilitres',
    value: 'ml',
  },
]

describe('Select.component', () => {
  it('should if FormItem is present in the page', () => {
    const wrapper = shallow(<Select label={'my select'} />)
    expect(wrapper.find('FormItem').length).toEqual(1)
    expect(wrapper.find('Option').length).toEqual(0)
  })
  it('should if FormItem and Option are present in the page', () => {
    const wrapper = shallow(<Select label={'my select'} options={options} />)
    expect(wrapper.find('FormItem').length).toEqual(1)
    expect(wrapper.find('Option').length).toEqual(2)
  })
})
