import React from 'react'
import PropTypes from 'prop-types'
import { worldConnector, searchInListIcons } from 'constants/functions.constants'
import { useAllIngredients } from 'modules/recipe/containers/RecipePageDetails/RecipePageDetails.helpers'

const crossProduct = (base, comparative, newBase) => {
  const calcul = (newBase * comparative) / base
  return Math.round(calcul * 100) / 100
}

export const BuildListIngredients = ({ allIngredients, ingredients = [], portionEdited, portion }) => {
  const listIngredients = useAllIngredients(allIngredients, ingredients)
  if (listIngredients.length === 0) {
    return ''
  }

  return listIngredients.map(({ quantity, slug, unit, name }) => {
    const nameModified = name.toLowerCase()
    const noUnit = unit === 'portion'
    const nameWithArticle = worldConnector(nameModified)
    let quantityUpdated = quantity

    if (portionEdited !== null) {
      quantityUpdated = crossProduct(portion, parseInt(quantity), portionEdited)
    }

    return noUnit ? (
      <li key={slug}>
        <img src={searchInListIcons(slug)} alt={name} width="30" height="30" />
        {`${quantityUpdated} ${nameModified}${quantity > 1 ? '(s)' : ''}`}
      </li>
    ) : (
      <li key={slug}>
        <img src={searchInListIcons(slug)} alt={name} width="30" height="30" />
        <span className="listIngredients_quantity">
          {quantityUpdated} {unit}
        </span>{' '}
        {nameWithArticle}
      </li>
    )
  })
}

BuildListIngredients.propTypes = {
  allIngredients: PropTypes.object,
  ingredients: PropTypes.array,
  portionEdited: PropTypes.number,
  portion: PropTypes.number,
}
