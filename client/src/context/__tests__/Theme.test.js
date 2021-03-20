import React from 'react'
import { shallow } from 'enzyme'

import { ThemeProvider } from '../Theme.context'

describe('ThemeProvider', () => {
  it('should render children', () => {
    const wrapper = shallow(
      <ThemeProvider>
        <h1>Hello</h1>
      </ThemeProvider>
    )

    expect(wrapper.find('ContextProvider').length).toEqual(1)
    expect(wrapper.find('h1').length).toEqual(1)
  })

  it('should change theme if call setTheme', () => {
    const wrapper = shallow(
      <ThemeProvider>
        <h1>Hello</h1>
      </ThemeProvider>
    )

    expect(wrapper.find('ContextProvider').length).toEqual(1)
    expect(wrapper.find('ContextProvider').props().value.theme).toBeUndefined()

    wrapper.find('ContextProvider').props().value.setTheme()
    expect(wrapper.find('ContextProvider').props().value.theme).toEqual('light')

    wrapper.find('ContextProvider').props().value.setTheme()
    expect(wrapper.find('ContextProvider').props().value.theme).toEqual('dark')
  })
})
