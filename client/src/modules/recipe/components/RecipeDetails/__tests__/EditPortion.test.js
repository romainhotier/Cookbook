import React from 'react'
import { shallow } from 'enzyme'

import { EditPortion } from '../EditPortion.component'

describe('EditPortion.component', () => {
  it('should if RecipeDetails_editPortion, input and buttons are render, render portion with s', () => {
    const wrapper = shallow(<EditPortion portionEdited={10} updatePortionEdited={jest.fn()} />)

    expect(wrapper.find('.RecipeDetails_editPortion').length).toEqual(1)
    expect(wrapper.find('Button').length).toEqual(2)
    expect(wrapper.find('Input').props().suffix).toEqual('portions')
  })

  it('should if RecipeDetails_editPortion, input and buttons are render, render portion without s', () => {
    const wrapper = shallow(<EditPortion portion={0} portionEdited={1} updatePortionEdited={jest.fn()} />)

    expect(wrapper.find('.RecipeDetails_editPortion').length).toEqual(1)
    expect(wrapper.find('Button').length).toEqual(2)
    expect(wrapper.find('Input').props().suffix).toEqual('portion')
  })

  it('should if updatePortionEdited is call when i click on button', () => {
    const updatePortionEdited = jest.fn()
    const wrapper = shallow(<EditPortion portion={5} portionEdited={null} updatePortionEdited={updatePortionEdited} />)

    expect(wrapper.find('Button').length).toEqual(2)
    wrapper.find('Button').first().props().onClick()
    expect(updatePortionEdited).toHaveBeenCalled()

    wrapper.find('Button').last().props().onClick()
    expect(updatePortionEdited).toHaveBeenCalled()
  })

  it('should if updatePortionEdited is call when i click on button', () => {
    const updatePortionEdited = jest.fn()
    const wrapper = shallow(<EditPortion portion={5} portionEdited={9} updatePortionEdited={updatePortionEdited} />)

    expect(wrapper.find('Button').length).toEqual(2)
    wrapper.find('Button').last().props().onClick()
    expect(updatePortionEdited).toHaveBeenCalled()
  })

  it('should if updatePortionEdited is call when i change value in input', () => {
    const updatePortionEdited = jest.fn()
    const wrapper = shallow(<EditPortion portion={5} portionEdited={null} updatePortionEdited={updatePortionEdited} />)

    expect(wrapper.find('Input').length).toEqual(1)
    wrapper
      .find('Input')
      .props()
      .onChange({ target: { value: 10 } })
    expect(updatePortionEdited).toHaveBeenCalled()
  })
})
