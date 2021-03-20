import React from 'react'
import { List } from 'immutable'
import { shallow } from 'enzyme'

import { IngredientPageList } from '../IngredientPageList.container'
import { ingredientsList } from 'modules/ingredient/mocks/ingredients.mock'

describe('IngredientPageList.container', () => {
  it('should if h1 is render', () => {
    const wrapper = shallow(
      <IngredientPageList fetchAllIngredients={jest.fn()} ingredientsList={List(ingredientsList)} loading={true} />
    )

    expect(wrapper.find('.page_loader').length).toEqual(1)
  })

  it('should if h1 and IngredientsList are render', () => {
    const wrapper = shallow(
      <IngredientPageList fetchAllIngredients={jest.fn()} ingredientsList={List(ingredientsList)} loading={false} />
    )

    expect(wrapper.find('h1').length).toEqual(1)
    expect(wrapper.find('IngredientsList').length).toEqual(1)
  })

  it('should if deleteIngredient is called', () => {
    const deleteIngredient = jest.fn()
    const wrapper = shallow(
      <IngredientPageList
        deleteIngredient={deleteIngredient}
        fetchAllIngredients={jest.fn()}
        ingredientsList={List(ingredientsList)}
        loading={false}
      />
    )
    expect(wrapper.find('IngredientsList').length).toEqual(1)
    wrapper.find('IngredientsList').props().deleteIngredient('123')
    expect(deleteIngredient).toHaveBeenCalled()
  })
})
