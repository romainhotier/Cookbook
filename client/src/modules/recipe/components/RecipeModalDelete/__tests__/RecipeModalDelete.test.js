import React from 'react'
import { shallow } from 'enzyme'

import RecipeModalDelete from '../RecipeModalDelete.component'

describe('RecipeModalDelete.component', () => {
  it('should render Modal', () => {
    const wrapper = shallow(
      <RecipeModalDelete closeModal={jest.fn()} deleteRecipe={jest.fn()} isModalVisible={true} history={{}} id={'1'} />
    )

    expect(wrapper.find('Modal').length).toEqual(1)
  })
})
