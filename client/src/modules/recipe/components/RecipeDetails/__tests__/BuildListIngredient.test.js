import React from 'react'
import { shallow } from 'enzyme'
import { List } from 'immutable'

import { BuildListIngredients } from '../BuildListIngredients.component'
import { recipes } from 'modules/recipe/mocks/recipes.mock'
import { ingredientsList } from 'modules/ingredient/mocks/ingredients.mock'

describe('BuildListIngredients.component', () => {
  it('should render nothing', () => {
    const wrapper = shallow(
      <BuildListIngredients allIngredients={List([])} ingredients={recipes.content[0].ingredients} />
    )

    expect(wrapper.find('.listIngredients_quantity').length).toEqual(0)
    expect(wrapper.find('img').length).toEqual(0)
    expect(wrapper.find('li').length).toEqual(0)
  })

  it('should render li', () => {
    const wrapper = shallow(
      <BuildListIngredients allIngredients={List(ingredientsList)} ingredients={recipes.content[0].ingredients} />
    )

    expect(wrapper.find('.listIngredients_quantity').length).toEqual(1)
    expect(wrapper.find('img').length).toEqual(2)
    expect(wrapper.find('li').length).toEqual(2)
  })

  it('should render li with portionEdited', () => {
    const wrapper = shallow(
      <BuildListIngredients
        portionEdited={10}
        allIngredients={List(ingredientsList)}
        ingredients={recipes.content[0].ingredients}
      />
    )

    expect(wrapper.find('.listIngredients_quantity').length).toEqual(1)
    expect(wrapper.find('img').length).toEqual(2)
    expect(wrapper.find('li').length).toEqual(2)
  })
})
