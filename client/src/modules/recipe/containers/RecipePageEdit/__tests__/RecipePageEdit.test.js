import React from 'react'
import { List } from 'immutable'
import { shallow } from 'enzyme'

import { RecipePageEdit } from '../RecipePageEdit.container'
import { recipes } from 'modules/recipe/mocks/recipes.mock'

describe('RecipePageEdit.container', () => {
  const match = { params: { id: 'pancakes-a-la-banane' } }

  it('should render h2 and RecipeForm', () => {
    const wrapper = shallow(
      <RecipePageEdit
        recipesList={List([])}
        putRecipe={jest.fn()}
        match={match}
        fetchRecipe={jest.fn()}
        postFileRecipe={jest.fn()}
        deleteFileRecipe={jest.fn()}
      />
    )

    expect(wrapper.find('Loader').length).toEqual(1)
  })

  it('should render h2 and RecipeForm', () => {
    const wrapper = shallow(
      <RecipePageEdit
        recipesList={List(recipes.content)}
        putRecipe={jest.fn()}
        match={match}
        fetchRecipe={jest.fn()}
        postFileRecipe={jest.fn()}
        deleteFileRecipe={jest.fn()}
      />
    )
    expect(wrapper.find('h2').length).toEqual(1)
    expect(wrapper.find('RecipeForm').length).toEqual(1)
  })

  it('should updateRecipe call putRecipe', () => {
    const putRecipe = jest.fn()

    const wrapper = shallow(
      <RecipePageEdit
        recipesList={List(recipes.content)}
        putRecipe={putRecipe}
        match={match}
        fetchRecipe={jest.fn()}
        postFileRecipe={jest.fn()}
        deleteFileRecipe={jest.fn()}
      />
    )
    expect(wrapper.find('h2').length).toEqual(1)
    expect(wrapper.find('RecipeForm').length).toEqual(1)
    wrapper.find('RecipeForm').props().sendRecipe({ _id: '123', file: 'photo.jpg' })
    expect(putRecipe).toHaveBeenCalled()
  })
})
