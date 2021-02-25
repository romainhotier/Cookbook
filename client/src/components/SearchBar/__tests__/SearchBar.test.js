import React from 'react'
import { shallow } from 'enzyme'

import SearchBar from '../SearchBar.component'

describe('SearchBar.component', () => {
  it('should if Search is present', () => {
    const wrapper = shallow(<SearchBar />)
    expect(wrapper.find('.searchBar').length).toEqual(1)
    expect(wrapper.find('Search').length).toEqual(1)
  })
})
