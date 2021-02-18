import React from 'react'
import PropTypes from 'prop-types'

import { Nav } from './Nav.component'
import SwitchTheme from 'components/SwitchTheme'

import './_Menu.scss'

export const Menu = ({ className }) => {
  return (
    <div className={`${className}`}>
      <nav className="layout_menu">
        <div className="layout_logo">
          <h1>Cook</h1>
        </div>
        <div className="layout_menu_items">
          <Nav />
        </div>
        <div className="layout_darkmode">
          <SwitchTheme />
        </div>
      </nav>
    </div>
  )
}

Menu.propTypes = {
  className: PropTypes.string,
}
