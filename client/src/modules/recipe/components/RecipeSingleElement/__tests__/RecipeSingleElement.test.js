import React from 'react'
import { shallow } from 'enzyme'

import RecipeSingleElement from '../RecipeSingleElement.component'
import { recipes } from 'modules/recipe/mocks/recipes.mock'

describe('RecipeSingleElement.component', () => {
  it('should render recipeSingleElement', () => {
    const wrapper = shallow(<RecipeSingleElement recipe={recipes.content[0]} />)

    expect(wrapper.find('.recipeSingleElement').length).toEqual(1)
    expect(wrapper.find('.recipeSingleElement_image').length).toEqual(1)
    expect(wrapper.find('.recipeSingleElement_mainCategorie').length).toEqual(1)
    expect(wrapper.find('.recipeSingleElement_details').length).toEqual(1)
  })

  it('should render recipeSingleElement with others data', () => {
    const wrapper = shallow(<RecipeSingleElement recipe={recipes.content[1]} />)

    expect(wrapper.find('.recipeSingleElement').length).toEqual(1)
    expect(wrapper.find('.recipeSingleElement_image').length).toEqual(1)
    expect(wrapper.find('.recipeSingleElement_mainCategorie').length).toEqual(1)
    expect(wrapper.find('.recipeSingleElement_details').length).toEqual(1)
  })
})
