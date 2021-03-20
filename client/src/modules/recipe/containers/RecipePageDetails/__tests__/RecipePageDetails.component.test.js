import React from 'react'
import { shallow } from 'enzyme'

import { RecipePageDetailsComponent } from '../RecipePageDetails.component'
import { recipes } from 'modules/recipe/mocks/recipes.mock'

describe('RecipePageDetailsComponent', () => {
  it('should render RecipeDetails without props', () => {
    const wrapper = shallow(
      <RecipePageDetailsComponent
        deleteRecipe={jest.fn()}
        history={{}}
        modalDeleteRecipeIsVisible={false}
        allIngredients={{}}
        portionEdited={null}
        updatePortionEdited={jest.fn()}
        showModal={jest.fn()}
        recipe={{}}
        handleUploadFiles={jest.fn()}
        uploadFilesIsVisible={false}
      />
    )

    expect(wrapper.find('.RecipeDetails').length).toEqual(1)
    expect(wrapper.find('.RecipeDetails_actions').length).toEqual(1)
    expect(wrapper.find('.RecipeDetails_header').length).toEqual(1)
    expect(wrapper.find('Carousel').length).toEqual(1)
    expect(wrapper.find('UploadFilesRecipe').length).toEqual(0)
    expect(wrapper.find('.RecipeDetails_categories').length).toEqual(0)
  })

  it('should render UploadFilesRecipe', () => {
    const wrapper = shallow(
      <RecipePageDetailsComponent
        deleteRecipe={jest.fn()}
        history={{}}
        modalDeleteRecipeIsVisible={false}
        allIngredients={{}}
        portionEdited={null}
        updatePortionEdited={jest.fn()}
        showModal={jest.fn()}
        recipe={{}}
        handleUploadFiles={jest.fn()}
        uploadFilesIsVisible={true}
      />
    )

    expect(wrapper.find('.RecipeDetails').length).toEqual(1)
    expect(wrapper.find('Carousel').length).toEqual(0)
    expect(wrapper.find('Connect(UploadFilesRecipe)').length).toEqual(1)
  })

  it('should closeModal is called', () => {
    const closeModal = jest.fn()
    const wrapper = shallow(
      <RecipePageDetailsComponent
        allIngredients={{}}
        closeModal={closeModal}
        deleteRecipe={jest.fn()}
        handleUploadFiles={jest.fn()}
        history={{}}
        modalDeleteRecipeIsVisible={false}
        portionEdited={null}
        recipe={{}}
        showModal={jest.fn()}
        updatePortionEdited={jest.fn()}
        uploadFilesIsVisible={true}
      />
    )

    expect(wrapper.find('.RecipeDetails').length).toEqual(1)
    wrapper.find('RecipeModalDelete').props().closeModal()
    expect(closeModal).toHaveBeenCalled()
  })

  it('should render RecipeDetails with recipe props', () => {
    const wrapper = shallow(
      <RecipePageDetailsComponent
        deleteRecipe={jest.fn()}
        history={{}}
        modalDeleteRecipeIsVisible={false}
        allIngredients={{}}
        portionEdited={null}
        updatePortionEdited={jest.fn()}
        showModal={jest.fn()}
        recipe={recipes.content[0]}
        handleUploadFiles={jest.fn()}
        uploadFilesIsVisible={true}
      />
    )

    expect(wrapper.find('.RecipeDetails').length).toEqual(1)
    expect(wrapper.find('.RecipeDetails_categories').length).toEqual(1)
  })
})
