import React from 'react'
import { shallow } from 'enzyme'
import CategoryTag from '../CategoryTag.component'

describe('CategoryTag.component', () => {
  it('should if tag is present', () => {
    const wrapper = shallow(<CategoryTag category={'Salée'} />)

    expect(wrapper.find('.categoryTag').length).toEqual(1)
  })
})
