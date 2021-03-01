import React from 'react'
import PropTypes from 'prop-types'
import { NavLink } from 'react-router-dom'

import { Nav } from './Nav.component'
import { Routes as UserRoutes } from 'modules/user/UserRoutes'
import SearchBar from 'components/SearchBar'
import SwitchTheme from 'components/SwitchTheme'

import './_Menu.scss'

export const Menu = ({ className = '' }) => {
  return (
    <div className={`${className}`}>
      <div className="layout_header">
        <div className="layout_logo">
          <h1>
            The <br />
            CookBook
          </h1>
        </div>
        <div className="layout_search">
          <SearchBar />
        </div>
        <div className="layout_user">
          <NavLink to={UserRoutes.myAccount()} exact>
            <i className="fas fa-user"></i> Mon compte
          </NavLink>
        </div>
      </div>
      <nav className="layout_menu">
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
