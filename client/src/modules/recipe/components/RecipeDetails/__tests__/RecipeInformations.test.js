import React from 'react'
import { shallow } from 'enzyme'

import { RecipeInformations } from '../RecipeInformations.component'

describe('RecipeInformations.component', () => {
  it("should if props are empties, don't render label and value", () => {
    const wrapper = shallow(<RecipeInformations />)

    expect(wrapper.find('.RecipeDetails_informations').length).toEqual(1)
    expect(wrapper.find('.RecipeDetails_information_label').length).toEqual(0)
  })

  it('should if props exist, render label and value', () => {
    const wrapper = shallow(
      <RecipeInformations preparation_time={'20'} cooking_time={'20'} caloriesForOnePortion={300} />
    )

    expect(wrapper.find('.RecipeDetails_informations').length).toEqual(1)
    expect(wrapper.find('.RecipeDetails_information_label').length).toEqual(3)
    expect(wrapper.find('.RecipeDetails_information_value').length).toEqual(3)
  })
})
