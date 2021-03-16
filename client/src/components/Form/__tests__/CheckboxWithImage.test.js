import React from 'react'
import { shallow } from 'enzyme'
import { CheckboxWithImage } from '../CheckboxWithImage.component'

const datas = [
  {
    icon: 'recette_salee',
    title: 'Salée',
  },
  {
    icon: 'recette_sucree',
    title: 'Sucrée',
  },
  {
    icon: '',
    title: 'Apéritifs',
  },
]

describe('CheckboxWithImage.component', () => {
  it('should if FormItem is present in the page', () => {
    const wrapper = shallow(<CheckboxWithImage datas={datas} />)
    expect(wrapper.find('FormItem').length).toEqual(1)
    expect(wrapper.find('Checkbox').length).toEqual(datas.length)
  })
})
