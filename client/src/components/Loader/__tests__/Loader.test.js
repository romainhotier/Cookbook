import React from 'react'
import { shallow } from 'enzyme'
import Loader from '../Loader.component'

describe('Loader.component', () => {
  it('should if Loader is present in the page', () => {
    const wrapper = shallow(<Loader />)

    expect(wrapper.find('.page_loader').length).toEqual(1)
    expect(wrapper.find('Spin').length).toEqual(1)
  })
})
