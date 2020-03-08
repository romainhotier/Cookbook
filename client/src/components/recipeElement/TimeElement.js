import React from 'react'
import PropTypes from 'prop-types'

const TimeElement = ({ time }) => {

    if (time === 0) {
      return (
        <span>NC</span>
      )
    } else if (time === 1) {
      return (
        <span>{time} minute</span>
      )
    } else {
      return (
        <span>{time} minutes</span>
      )
    }

}


export default TimeElement

TimeElement.propTypes = {
  time: PropTypes.number.isRequired
}
