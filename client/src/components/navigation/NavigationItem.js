import React from 'react'
import PropTypes from 'prop-types'

import { NavLink } from 'react-router-dom'

import './_NavigationItem.scss'

const NavigationItem = ({name, url}) => {
  return (
    <div className="navigationItem">
      <NavLink
        to={url}
        className="navigationItem_Link"
        activeClassName="active"
        exact
      >
        {name}
      </NavLink>
    </div>
  )
}

NavigationItem.propTypes = {
  name: PropTypes.string.isRequired,
  url: PropTypes.string.isRequired,
}

export default NavigationItem

