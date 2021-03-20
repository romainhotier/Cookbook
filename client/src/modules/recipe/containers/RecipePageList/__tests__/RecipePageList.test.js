import React from 'react'
import { List } from 'immutable'
import { shallow } from 'enzyme'

import { RecipePageList } from '../RecipePageList.container'
import { recipes } from 'modules/recipe/mocks/recipes.mock'

describe('RecipePageList.container', () => {
  it('should if loader is render', () => {
    const wrapper = shallow(
      <RecipePageList fetchAllRecipe={jest.fn()} recipesList={List(recipes.content)} loading={true} />
    )

    expect(wrapper.find('Loader').length).toEqual(1)
  })
  it('should if RecipeSingleElement is render', () => {
    const wrapper = shallow(
      <RecipePageList
        fetchAllRecipe={jest.fn()}
        recipesList={List(recipes.content)}
        loading={recipes.loadingFetchRecipe}
      />
    )
    expect(wrapper.find('RecipeSingleElement').length).toEqual(2)
  })
})
