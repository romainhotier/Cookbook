import React from 'react'
import PropTypes from 'prop-types'

import './_Ingredient.scss'

const articleLiaison = (name) => {
  const firstLetter = name.substr(0, 1)

  return (
    firstLetter === 'a' ||
    firstLetter === 'h' ||
    firstLetter === 'e' ||
    firstLetter === 'y' ||
    firstLetter === 'u' ||
    firstLetter === 'i' ||
    firstLetter === 'o'
  ) ?
    (
      `d'${name}`
    ) :
    (
      `de ${name}`
    )
}

const Ingredient = ({ name, quantity, unity = '' }) => {
  const nameModified = name.toLowerCase()
  const notUnity = unity === ''
  const nameWithArticle = articleLiaison(nameModified)

  return (
    <div className="ingredientLabel">
      {notUnity ?
        <span>{quantity} {nameModified}</span>
        :
        <span>{quantity} {unity} {nameWithArticle} </span>
      }
    </div>
  )
}

Ingredient.propTypes = {
  quantity: PropTypes.number.isRequired,
  name: PropTypes.string.isRequired,
  unity: PropTypes.string,
}

export default Ingredient
