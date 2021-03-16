import React from 'react'
import { shallow } from 'enzyme'

import RecipeStepForm from '../RecipeStepForm.component'
import { recipes } from 'modules/recipe/mocks/mock.recipes'

describe('RecipeStepForm.component', () => {
  it('should render RecipeStepForm', () => {
    const wrapper = shallow(<RecipeStepForm listSteps={recipes.content[0].steps} setListSteps={jest.fn()} />)

    expect(wrapper.find('Collapse').length).toEqual(1)
    expect(wrapper.find('Button').length).toEqual(1)
    expect(wrapper.find('DragDropContext').length).toEqual(1)
  })

  it('should setListSteps is called when add step', () => {
    const setListSteps = jest.fn()
    const wrapper = shallow(<RecipeStepForm listSteps={recipes.content[0].steps} setListSteps={setListSteps} />)

    expect(wrapper.find('Button').length).toEqual(1)
    wrapper.find('Button').props().onClick()
    expect(setListSteps).toHaveBeenCalled()
  })

  it('should setListSteps is called when drag and drop steps', () => {
    const setListSteps = jest.fn()
    const wrapper = shallow(<RecipeStepForm listSteps={recipes.content[0].steps} setListSteps={setListSteps} />)

    expect(wrapper.find('DragDropContext').length).toEqual(1)
    wrapper
      .find('DragDropContext')
      .props()
      .onDragEnd({ destination: { index: 2 }, source: { index: 1 } })
    expect(setListSteps).toHaveBeenCalled()
  })

  it('should setListSteps is not called when drag and drop steps', () => {
    const setListSteps = jest.fn()
    const wrapper = shallow(<RecipeStepForm listSteps={recipes.content[0].steps} setListSteps={setListSteps} />)

    expect(wrapper.find('DragDropContext').length).toEqual(1)
    wrapper.find('DragDropContext').props().onDragEnd({})
    expect(setListSteps).not.toHaveBeenCalled()
  })
})
