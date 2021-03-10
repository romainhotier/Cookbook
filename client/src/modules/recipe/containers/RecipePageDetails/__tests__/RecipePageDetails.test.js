import React from 'react'
import { List } from 'immutable'
import { shallow } from 'enzyme'

import { RecipePageDetails } from '../RecipePageDetails.container'
import { recipes } from 'modules/recipe/mocks/mock.recipes'

describe('RecipePageDetails.container', () => {
  const match = { params: { slug: 'pancakes-a-la-banane' } }

  it('should if loader is render', () => {
    const wrapper = shallow(
      <RecipePageDetails
        match={match}
        recipesList={List(recipes.content)}
        loadingFetchIngredients={true}
        allIngredients={{}}
      />
    )

    expect(wrapper.find('Loader').length).toEqual(1)
  })
})
