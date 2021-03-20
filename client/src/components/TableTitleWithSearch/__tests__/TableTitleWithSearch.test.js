import React from 'react'
import { shallow } from 'enzyme'

import TableTitleWithSearch from '../TableTitleWithSearch.component'

describe('TableTitleWithSearch.component', () => {
  it('should if TableTitleWithSearch is present in the page', () => {
    const wrapper = shallow(
      <TableTitleWithSearch title={'name'} filterName={'name'} placeholder={'name'} onChange={jest.fn()} />
    )
    expect(wrapper.find('.tableTitleWithSearch').length).toEqual(1)
  })

  it('should onChange is called when onChange on input is trigger', () => {
    const onChange = jest.fn()
    const wrapper = shallow(
      <TableTitleWithSearch title={'name'} filterName={'name'} placeholder={'name'} onChange={onChange} />
    )
    expect(wrapper.find('.tableTitleWithSearch').length).toEqual(1)
    expect(wrapper.find('Input').length).toEqual(1)
    wrapper
      .find('Input')
      .props()
      .onChange({ target: { value: 'hi' } })
    expect(onChange).toHaveBeenCalled()
  })

  it('should onChange is not called when onClick on input is trigger', () => {
    const onChange = jest.fn()
    const wrapper = shallow(
      <TableTitleWithSearch title={'name'} filterName={'name'} placeholder={'name'} onChange={onChange} />
    )
    expect(wrapper.find('.tableTitleWithSearch').length).toEqual(1)
    expect(wrapper.find('Input').length).toEqual(1)
    wrapper.find('Input').props().onClick({ stopPropagation: jest.fn() })
    expect(onChange).not.toHaveBeenCalled()
  })
})
