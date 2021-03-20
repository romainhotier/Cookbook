import React from 'react'
import { shallow } from 'enzyme'

import RecipeForm from '../RecipeForm.component'

const values = {
  ingredients: [{}],
  steps: [{ idFront: 0, description: '' }],
}
describe('RecipeForm.component', () => {
  it('should render Buttons and Collapse', () => {
    const wrapper = shallow(<RecipeForm values={values} sendRecipe={jest.fn()} />)

    expect(wrapper.find('Collapse').length).toEqual(1)
    expect(wrapper.find('Button').length).toEqual(2)
    wrapper.find('Button').first().props().onClick()
    wrapper.find('Button').last().props().onClick()
  })

  it('should if sendRecipe is called', () => {
    const sendRecipe = jest.fn()
    const wrapper = shallow(<RecipeForm values={values} sendRecipe={sendRecipe} />)

    expect(wrapper.find('ForwardRef(InternalForm)').length).toEqual(1)
    expect(wrapper.find('Button').length).toEqual(2)
    wrapper.find('ForwardRef(InternalForm)').props().onFinish({ title: 'pancakes' })
    expect(sendRecipe).toHaveBeenCalled()
  })
})
