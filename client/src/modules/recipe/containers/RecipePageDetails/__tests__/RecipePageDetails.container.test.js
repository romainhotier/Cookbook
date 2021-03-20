import React from 'react'
import { List } from 'immutable'
import { shallow } from 'enzyme'

import { RecipePageDetails } from '../RecipePageDetails.container'
import { recipes } from 'modules/recipe/mocks/recipes.mock'
import { ingredientsList } from 'modules/ingredient/mocks/ingredients.mock'

describe('RecipePageDetails.container', () => {
  const match = { params: { slug: 'pancakes-a-la-banane' } }

  it('should if loader is render if loadingFetchIngredient is true', () => {
    const wrapperWithloadingFetchIngredient = shallow(
      <RecipePageDetails
        allIngredients={{}}
        fetchAllIngredients={jest.fn()}
        loadingFetchIngredient={true}
        match={match}
        recipesList={List(recipes.content)}
      />
    )

    expect(wrapperWithloadingFetchIngredient.find('Loader').length).toEqual(1)
  })

  it('should render RecipePageDetailsComponent', () => {
    const wrapper = shallow(
      <RecipePageDetails
        allIngredients={List(ingredientsList)}
        fetchAllIngredients={jest.fn()}
        loadingFetchIngredient={false}
        match={match}
        recipesList={List(recipes.content)}
      />
    )

    expect(wrapper.find('RecipePageDetailsComponent').length).toEqual(1)
  })

  it('should fetchRecipe is called', () => {
    const fetchRecipe = jest.fn()

    shallow(
      <RecipePageDetails
        allIngredients={List(ingredientsList)}
        fetchAllIngredients={jest.fn()}
        fetchRecipe={fetchRecipe}
        loadingFetchIngredient={false}
        match={match}
        recipesList={List([])}
      />
    )

    expect(fetchRecipe).toHaveBeenCalled()
  })

  it('should fetchAllIngredients is called', () => {
    const fetchAllIngredients = jest.fn()

    const wrapper = shallow(
      <RecipePageDetails
        allIngredients={List([])}
        fetchAllIngredients={fetchAllIngredients}
        loadingFetchIngredient={false}
        match={match}
        recipesList={List(recipes.content)}
      />
    )

    expect(fetchAllIngredients).toHaveBeenCalled()
  })

  it('should updatePortionEdited change the state', () => {
    const wrapper = shallow(
      <RecipePageDetails
        allIngredients={List(ingredientsList)}
        fetchAllIngredients={jest.fn()}
        loadingFetchIngredient={false}
        match={match}
        recipesList={List(recipes.content)}
      />
    )

    expect(wrapper.find('RecipePageDetailsComponent').length).toEqual(1)
    expect(wrapper.state()).toMatchObject({
      portionEdited: null,
      modalDeleteRecipeIsVisible: false,
      uploadFilesIsVisible: false,
    })
    wrapper.find('RecipePageDetailsComponent').props().updatePortionEdited(5)
    expect(wrapper.state()).toMatchObject({
      portionEdited: 5,
      modalDeleteRecipeIsVisible: false,
      uploadFilesIsVisible: false,
    })

    wrapper.find('RecipePageDetailsComponent').props().updatePortionEdited('abc')
    expect(wrapper.state()).toMatchObject({
      portionEdited: 0,
      modalDeleteRecipeIsVisible: false,
      uploadFilesIsVisible: false,
    })
  })

  it('should showModal change the state', () => {
    const wrapper = shallow(
      <RecipePageDetails
        allIngredients={List(ingredientsList)}
        fetchAllIngredients={jest.fn()}
        loadingFetchIngredient={false}
        match={match}
        recipesList={List(recipes.content)}
      />
    )

    expect(wrapper.find('RecipePageDetailsComponent').length).toEqual(1)
    expect(wrapper.state()).toMatchObject({
      portionEdited: null,
      modalDeleteRecipeIsVisible: false,
      uploadFilesIsVisible: false,
    })
    wrapper.find('RecipePageDetailsComponent').props().showModal()
    expect(wrapper.state()).toMatchObject({
      portionEdited: null,
      modalDeleteRecipeIsVisible: true,
      uploadFilesIsVisible: false,
    })
  })

  it('should closeModal change the state', () => {
    const wrapper = shallow(
      <RecipePageDetails
        allIngredients={List(ingredientsList)}
        fetchAllIngredients={jest.fn()}
        loadingFetchIngredient={false}
        match={match}
        recipesList={List(recipes.content)}
      />
    )

    expect(wrapper.find('RecipePageDetailsComponent').length).toEqual(1)
    wrapper.find('RecipePageDetailsComponent').props().showModal()
    expect(wrapper.state()).toMatchObject({
      portionEdited: null,
      modalDeleteRecipeIsVisible: true,
      uploadFilesIsVisible: false,
    })
    wrapper.find('RecipePageDetailsComponent').props().closeModal()
    expect(wrapper.state()).toMatchObject({
      portionEdited: null,
      modalDeleteRecipeIsVisible: false,
      uploadFilesIsVisible: false,
    })
  })

  it('should handleUploadFiles change the state', () => {
    const wrapper = shallow(
      <RecipePageDetails
        allIngredients={List(ingredientsList)}
        fetchAllIngredients={jest.fn()}
        loadingFetchIngredient={false}
        match={match}
        recipesList={List(recipes.content)}
      />
    )

    expect(wrapper.find('RecipePageDetailsComponent').length).toEqual(1)
    expect(wrapper.state()).toMatchObject({
      portionEdited: null,
      modalDeleteRecipeIsVisible: false,
      uploadFilesIsVisible: false,
    })
    wrapper.find('RecipePageDetailsComponent').props().handleUploadFiles()
    expect(wrapper.state()).toMatchObject({
      portionEdited: null,
      modalDeleteRecipeIsVisible: false,
      uploadFilesIsVisible: true,
    })
  })
})
