import React from 'react'
import { shallow } from 'enzyme'
import { Menu } from '../Menu.component'
import { MobileMenu } from '../MobileMenu.component'

describe('Menu.component', () => {
  it('should if Menu is present', () => {
    const wrapper = shallow(<Menu className="the-menu" />)

    expect(wrapper.find('.the-menu').length).toEqual(1)
    expect(wrapper.find('.layout_header').length).toEqual(1)
    expect(wrapper.find('.layout_menu').length).toEqual(1)
    expect(wrapper.find('Drawer').length).toEqual(0)
  })
})

describe('MobileMenu.component', () => {
  it('should if DrawerWrapper is present', () => {
    const wrapper = shallow(<MobileMenu className="the-menu" />)

    expect(wrapper.find('.the-menu').length).toEqual(1)
    expect(wrapper.find('.layout_header').length).toEqual(1)
    expect(wrapper.find('.layout_menu').length).toEqual(1)
    expect(wrapper.find('DrawerWrapper').length).toEqual(1)
  })
})
