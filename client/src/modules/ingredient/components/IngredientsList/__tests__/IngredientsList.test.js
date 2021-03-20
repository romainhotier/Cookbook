import React from 'react'
import { shallow } from 'enzyme'
import { Table } from 'antd'

import IngredientsList from '../IngredientsList.component'

describe('IngredientsList.component', () => {
  it('should if Table is present in IngredientsList', () => {
    const wrapper = shallow(<IngredientsList data={[]} />)

    expect(wrapper.find(Table).length).toEqual(1)
    expect(wrapper.find(Table).props().rowKey({ _id: '123', name: 'Banane' })).toEqual('123')
  })
})
