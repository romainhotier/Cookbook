import React from 'react'
import { List } from 'immutable'
import { shallow } from 'enzyme'

import { RecipePageDetails } from '../RecipePageDetails.container'
import { recipes } from 'modules/recipe/mocks/mock.recipes'

describe('RecipePageDetails.container', () => {
  const match = { params: { slug: 'pancakes-a-la-banane' } }
  it('should if loader is render if loadingFetchIngredient is true', () => {
    const wrapperWithloadingFetchIngredient = shallow(
      <RecipePageDetails
        match={match}
        recipesList={List(recipes.content)}
        loadingFetchIngredient={true}
        allIngredients={{}}
        fetchAllIngredients={jest.fn()}
      />
    )

    expect(wrapperWithloadingFetchIngredient.find('Loader').length).toEqual(1)
  })

  it('should if loader is render if loadingFetchRecipe is true', () => {
    const wrapperWithLoadingFetchRecipe = shallow(
      <RecipePageDetails
        match={match}
        fetchAllIngredients={jest.fn()}
        recipesList={List(recipes.content)}
        loadingFetchRecipe={true}
        allIngredients={{}}
      />
    )

    expect(wrapperWithLoadingFetchRecipe.find('Loader').length).toEqual(1)
  })

  it('should if loader is render if allIngredients is empry', () => {
    const wrapperWithLoadingFetchRecipe = shallow(
      <RecipePageDetails
        match={match}
        fetchAllIngredients={jest.fn()}
        recipesList={List(recipes.content)}
        allIngredients={{}}
      />
    )

    expect(wrapperWithLoadingFetchRecipe.find('Loader').length).toEqual(1)
  })

  // it('should if RecipePageDetailsComponent is render', () => {
  //   const wrapperWithLoadingFetchRecipe = shallow(
  //     <RecipePageDetails
  //       match={match}
  //       fetchAllIngredients={jest.fn()}
  //       recipesList={List(recipes.content)}
  //       allIngredients={{}}
  //     />
  //   )

  //   expect(wrapperWithLoadingFetchRecipe.find('Loader').length).toEqual(1)
  // })
})
