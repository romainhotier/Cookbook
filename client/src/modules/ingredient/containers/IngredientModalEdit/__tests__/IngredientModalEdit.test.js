import React from 'react'
import { List } from 'immutable'
import { shallow } from 'enzyme'

import { IngredientModalEdit } from '../IngredientModalEdit.container'
import { ingredientsList } from 'modules/ingredient/mocks/ingredients.mock'

describe('IngredientModalEdit.container', () => {
  it('should render Button and Modal', () => {
    const wrapper = shallow(
      <IngredientModalEdit fetchAllIngredients={jest.fn()} ingredientsList={List(ingredientsList)} loading={false} />
    )

    expect(wrapper.find('Button').length).toEqual(1)
    expect(wrapper.find('Modal').length).toEqual(1)
  })

  it('should modal is visible when button is clicked', () => {
    const wrapper = shallow(
      <IngredientModalEdit fetchAllIngredients={jest.fn()} ingredientsList={List(ingredientsList)} loading={false} />
    )

    expect(wrapper.find('Button').length).toEqual(1)
    expect(wrapper.find('Modal').length).toEqual(1)

    expect(wrapper.find('Modal').props().visible).toEqual(false)
    wrapper.find('Button').props().onClick()
    expect(wrapper.find('Modal').props().visible).toEqual(true)
  })

  it('should be the modal that closes when we call the onCancel function', () => {
    const wrapper = shallow(
      <IngredientModalEdit fetchAllIngredients={jest.fn()} ingredientsList={List(ingredientsList)} loading={false} />
    )

    expect(wrapper.find('Button').length).toEqual(1)
    expect(wrapper.find('Modal').length).toEqual(1)

    expect(wrapper.find('Modal').props().visible).toEqual(false)
    wrapper.find('Button').props().onClick()
    expect(wrapper.find('Modal').props().visible).toEqual(true)

    wrapper.find('Modal').props().onCancel()
    expect(wrapper.find('Modal').props().visible).toEqual(false)
  })
})
