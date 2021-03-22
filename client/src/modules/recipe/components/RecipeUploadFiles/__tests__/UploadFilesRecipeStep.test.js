import React from 'react'
import { List } from 'immutable'
import { shallow } from 'enzyme'

import { UploadFilesRecipeStep } from '../UploadFilesRecipeStep.container'
import { recipes, recipeStep } from 'modules/recipe/mocks/recipes.mock'

describe('UploadFilesRecipeStep.component', () => {
  it('should render Upload without files', () => {
    const wrapper = shallow(
      <UploadFilesRecipeStep
        id_recipe={recipes.content[0]._id}
        id_step={recipeStep[1]._id}
        postFileRecipeStep={jest.fn()}
        deleteFileRecipeStep={jest.fn()}
        recipesList={List(recipes.content)}
      />
    )

    expect(wrapper.find('.RecipeDetails_uploadImages').length).toEqual(1)
    expect(wrapper.find('Upload').length).toEqual(1)
  })

  it('should render Upload with files', () => {
    const wrapper = shallow(
      <UploadFilesRecipeStep
        id_recipe={recipes.content[0]._id}
        id_step={recipeStep[0]._id}
        postFileRecipeStep={jest.fn()}
        deleteFileRecipeStep={jest.fn()}
        recipesList={List(recipes.content)}
      />
    )

    expect(wrapper.find('.RecipeDetails_uploadImages').length).toEqual(1)
    expect(wrapper.find('Upload').length).toEqual(1)
  })

  it('should postFileRecipeStep is called', () => {
    const postFileRecipeStep = jest.fn()
    const wrapper = shallow(
      <UploadFilesRecipeStep
        id_recipe={recipes.content[0]._id}
        id_step={recipeStep[0]._id}
        postFileRecipeStep={postFileRecipeStep}
        deleteFileRecipeStep={jest.fn()}
        recipesList={List(recipes.content)}
      />
    )

    expect(wrapper.find('Upload').length).toEqual(1)
    wrapper.find('Upload').props().addFileInRecipe('myFile.jpg')
    expect(postFileRecipeStep).toHaveBeenCalled()
  })

  it('should deleteFileRecipeStep is called', () => {
    const deleteFileRecipeStep = jest.fn()
    const wrapper = shallow(
      <UploadFilesRecipeStep
        id_recipe={recipes.content[0]._id}
        id_step={recipeStep[0]._id}
        postFileRecipeStep={jest.fn()}
        deleteFileRecipeStep={deleteFileRecipeStep}
        recipesList={List(recipes.content)}
      />
    )

    expect(wrapper.find('Upload').length).toEqual(1)
    wrapper.find('Upload').props().deleteFileInRecipe({ url: '123.jpg', name: '123.jpg' })
    expect(deleteFileRecipeStep).toHaveBeenCalled()

    wrapper.find('Upload').props().deleteFileInRecipe({ name: '123.jpg' })
    expect(deleteFileRecipeStep).toHaveBeenCalled()
  })
})
