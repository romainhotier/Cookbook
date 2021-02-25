import React from 'react'
import { shallow } from 'enzyme'
import Carousel from '../Carousel.component'

const files = ['folders/img_1.jpg', 'folders/img_2.jpg']

describe('Carousel.component', () => {
  it('should if Carousel is present in the page', () => {
    const wrapper = shallow(<Carousel files={files} />)

    expect(wrapper.find('.carousel_img').length).toEqual(2)
  })
})
