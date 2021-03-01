import React from 'react'
import PropTypes from 'prop-types'

import './_UserContent.scss'

const UserContent = ({ title = '', children }) => {
  return (
    <div className="userContent">
      <h2>{title}</h2>
      {children}
    </div>
  )
}

UserContent.propTypes = {
  title: PropTypes.string,
  children: PropTypes.node,
}

export default UserContent
