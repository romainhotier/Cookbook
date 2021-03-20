import React from 'react'
import { shallow } from 'enzyme'

import { RecipeIngredientsFormComponent } from '../RecipeIngredientsForm.component'

describe('RecipeIngredientsFormComponent', () => {
  it('should render Collapse and FormList', () => {
    const wrapper = shallow(
      <RecipeIngredientsFormComponent
        options={[]}
        handleSearch={jest.fn()}
        handleChange={jest.fn()}
        createUnitOption={jest.fn()}
      />
    )

    expect(wrapper.find('Collapse').length).toEqual(1)
    expect(wrapper.find('FormList').length).toEqual(1)
  })

  it('should render fields', () => {
    const fieds = [
      {
        key: '123',
        fieldKey: 'name',
        name: 'name',
      },
      {
        key: '124',
        fieldKey: 'quantity',
        name: 'quantity',
      },
    ]

    const wrapper = shallow(
      <RecipeIngredientsFormComponent
        options={[]}
        handleSearch={jest.fn()}
        handleChange={jest.fn()}
        createUnitOption={jest.fn()}
      />
    )

    const fieldsMap = wrapper.find('FormList').props().children(fieds, { add: jest.fn(), remove: jest.fn() })
    expect(fieldsMap.props.children[0][0].key).toEqual('ingredientsForm-123')
  })
})
