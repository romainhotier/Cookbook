import React from 'react'
import { shallow } from 'enzyme'

import { RecipeImagesStep } from '../RecipeImagesStep.component'
import { recipeStep } from 'modules/recipe/mocks/recipes.mock'

describe('RecipeImagesStep.component', () => {
  it('should not render Image', () => {
    const wrapper = shallow(<RecipeImagesStep files={recipeStep[1].files} />)

    expect(wrapper.find('Image').length).toEqual(0)
  })

  it('should render Image', () => {
    const wrapper = shallow(<RecipeImagesStep files={recipeStep[0].files} />)

    expect(wrapper.find('Image').length).toEqual(2)
  })
})
