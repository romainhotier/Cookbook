import React from 'react'
import PropTypes from 'prop-types'

const ContentPage = ({ title, children }) => (
  <div className="contentPage">
    <div className="contentPage_heading">
      <h1 className="title">{title}</h1>
    </div>
    <div className="contentPage_children">{children}</div>
  </div>
)

ContentPage.propTypes = {
  title: PropTypes.object,
  children: PropTypes.object.isRequired,
}

export default ContentPage
