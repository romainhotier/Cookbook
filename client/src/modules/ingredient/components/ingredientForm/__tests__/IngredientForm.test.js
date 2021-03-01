import React from 'react'
import { shallow } from 'enzyme'
import { Form } from 'antd'

import IngredientForm from '../IngredientForm.component'

const defaultProps = {
  createIngredient: jest.fn(),
  loading: false,
  updateIngredient: jest.fn(),
}

const ingredient = {
  name: 'Banane',
  calories: '89',
  carbohydrates: '23',
  fats: '0.3',
  portion: '120',
  proteins: '1.1',
  slug: 'banane',
  unit: 'g',
}

const ingredientWithoutNutriment = {
  name: 'Banane',
  slug: 'banane',
  unit: 'g',
  categories: ['Farines'],
}

describe('IngredientForm.component', () => {
  it('should be Form in IngredientForm', () => {
    const wrapper = shallow(<IngredientForm {...defaultProps} />)
    expect(wrapper.find(Form).length).toEqual(1)
  })

  it('should change modify the suffix of the input portion', () => {
    const wrapper = shallow(<IngredientForm {...defaultProps} />)

    expect(wrapper.find("Input[name='portion']").props().suffix).toEqual('g')

    // Have change
    wrapper
      .find(Form)
      .props()
      .onFieldsChange([{ name: ['unit'], value: 'ml' }])

    expect(wrapper.find("Input[name='portion']").props().suffix).toEqual('ml')

    // Don't have change
    wrapper.find(Form).props().onFieldsChange([])
    wrapper
      .find(Form)
      .props()
      .onFieldsChange([{ name: ['calories'], value: '90' }])

    expect(wrapper.find("Input[name='portion']").props().suffix).toEqual('ml')
  })

  it('should be a call to the createIngredient function with complete ingredient', () => {
    const wrapper = shallow(<IngredientForm {...defaultProps} />)

    wrapper.find(Form).props().onFinish(ingredient)

    expect(defaultProps.createIngredient).toHaveBeenCalled()
  })

  it('should be a call to the createIngredient function without nutriment', () => {
    const wrapper = shallow(<IngredientForm {...defaultProps} />)

    wrapper.find(Form).props().onFinish(ingredientWithoutNutriment)

    expect(defaultProps.createIngredient).toHaveBeenCalled()
  })

  it('should be a call to the updateIngredient function', () => {
    const wrapper = shallow(<IngredientForm {...defaultProps} />)

    wrapper
      .find(Form)
      .props()
      .onFinish({ ...ingredient, _id: '123' })

    expect(defaultProps.updateIngredient).toHaveBeenCalled()
  })
})
