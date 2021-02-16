import React from 'react'
import PropTypes from 'prop-types'

import './_CategoryTag.scss'

const CategoryTag = ({ category, className = '' }) => (
  <div className={`${className} categoryTag`} key={category}>
    {category}
  </div>
)

CategoryTag.propTypes = {
  category: PropTypes.string,
  className: PropTypes.string,
}

export default CategoryTag
