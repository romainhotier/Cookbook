import React from 'react'
import { shallow } from 'enzyme'
import { Upload } from '../Upload.component'

describe('Upload.component', () => {
  it('should if FormItem is present in the page', () => {
    const wrapper = shallow(<Upload label={'my Input'} />)
    expect(wrapper.find('FormItem').length).toEqual(1)
    expect(wrapper.find('Upload').length).toEqual(1)
  })

  it('should addFileInRecipe is called when beforeUpload is called', () => {
    const addFileInRecipe = jest.fn()
    const wrapper = shallow(<Upload label={'my Input'} addFileInRecipe={addFileInRecipe} />)
    expect(wrapper.find('Upload').length).toEqual(1)
    wrapper.find('Upload').props().beforeUpload({})
    expect(addFileInRecipe).toHaveBeenCalled()
  })

  it('should deleteFileInRecipe is called when onRemove is called', () => {
    const deleteFileInRecipe = jest.fn()
    const wrapper = shallow(<Upload label={'my Input'} deleteFileInRecipe={deleteFileInRecipe} />)
    expect(wrapper.find('Upload').length).toEqual(1)
    wrapper.find('Upload').props().onRemove({})
    expect(deleteFileInRecipe).toHaveBeenCalled()
  })

  it('should getValueFromEvent return fileList', () => {
    const wrapper = shallow(<Upload label={'my Input'} />)
    expect(wrapper.find('Upload').length).toEqual(1)
    const fileList = wrapper.find('FormItem').props().getValueFromEvent({ fileList: [] })
    expect(fileList).toMatchObject([])
    const e = wrapper.find('FormItem').props().getValueFromEvent([])
    expect(e).toMatchObject([])
  })
})
