import React from 'react'
import { List } from 'immutable'
import { shallow } from 'enzyme'

import { UploadFilesRecipe } from '../UploadFilesRecipe.container'
import { recipes } from 'modules/recipe/mocks/mock.recipes'

describe('UploadFilesRecipe.component', () => {
  it('should render Upload without files', () => {
    const wrapper = shallow(
      <UploadFilesRecipe
        _id={recipes.content[0]._id}
        postFileRecipe={jest.fn()}
        deleteFileRecipe={jest.fn()}
        recipesList={List(recipes.content)}
      />
    )

    expect(wrapper.find('.RecipeDetails_uploadImages').length).toEqual(1)
    expect(wrapper.find('Upload').length).toEqual(1)
  })

  it('should render Upload with files', () => {
    const wrapper = shallow(
      <UploadFilesRecipe
        _id={recipes.content[1]._id}
        postFileRecipe={jest.fn()}
        deleteFileRecipe={jest.fn()}
        recipesList={List(recipes.content)}
      />
    )

    expect(wrapper.find('.RecipeDetails_uploadImages').length).toEqual(1)
    expect(wrapper.find('Upload').length).toEqual(1)
  })

  it('should postFileRecipe is called', () => {
    const postFileRecipe = jest.fn()
    const wrapper = shallow(
      <UploadFilesRecipe
        _id={recipes.content[1]._id}
        postFileRecipe={postFileRecipe}
        deleteFileRecipe={jest.fn()}
        recipesList={List(recipes.content)}
      />
    )

    expect(wrapper.find('Upload').length).toEqual(1)
    wrapper.find('Upload').props().addFileInRecipe('myFile.jpg')
    expect(postFileRecipe).toHaveBeenCalled()
  })

  it('should deleteFileRecipe is called', () => {
    const deleteFileRecipe = jest.fn()
    const wrapper = shallow(
      <UploadFilesRecipe
        _id={recipes.content[1]._id}
        postFileRecipe={jest.fn()}
        deleteFileRecipe={deleteFileRecipe}
        recipesList={List(recipes.content)}
      />
    )

    expect(wrapper.find('Upload').length).toEqual(1)
    wrapper.find('Upload').props().deleteFileInRecipe({ url: 'recipes/12345/marbre.jpg', name: 'myFile.jpg' })
    expect(deleteFileRecipe).toHaveBeenCalled()

    wrapper.find('Upload').props().deleteFileInRecipe({ name: 'marbre.jpg' })
    expect(deleteFileRecipe).toHaveBeenCalled()
  })
})
