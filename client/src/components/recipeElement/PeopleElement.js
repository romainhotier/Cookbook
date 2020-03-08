import React from 'react'
import PropTypes from 'prop-types'

const PeopleElement = ({ people }) => {

    if (people === 0) {
      return (
        <span>NC</span>
      )
    } else if (people === 1) {
      return (
        <span>{people} personne</span>
      )
    } else {
      return (
        <span>{people} personnes</span>
      )
    }

}


export default PeopleElement

PeopleElement.propTypes = {
  people: PropTypes.number.isRequired
}
