import React from 'react'
import { shallow } from 'enzyme'

import RecipeStepElement from '../RecipeStepElement.component'

describe('RecipeStepElement.component', () => {
  it('should render Button and Textarea', () => {
    const wrapper = shallow(
      <RecipeStepElement id={1} description={'step 1'} removeStep={jest.fn()} changeDescription={jest.fn()} />
    )

    expect(wrapper.find('TextArea').length).toEqual(1)
    expect(wrapper.find('Button').length).toEqual(1)
  })

  it('should removeStep is called', () => {
    const removeStep = jest.fn()
    const wrapper = shallow(
      <RecipeStepElement id={1} description={'step 1'} removeStep={removeStep} changeDescription={jest.fn()} />
    )

    expect(wrapper.find('Button').length).toEqual(1)
    wrapper.find('Button').props().onClick()
    expect(removeStep).toHaveBeenCalled()
  })

  it('should changeDescription is called', () => {
    const changeDescription = jest.fn()
    const wrapper = shallow(
      <RecipeStepElement id={1} description={'step 1'} removeStep={jest.fn()} changeDescription={changeDescription} />
    )

    expect(wrapper.find('TextArea').length).toEqual(1)
    wrapper.find('TextArea').props().onChange()
    expect(changeDescription).toHaveBeenCalled()
  })
})
