import React from 'react'
import keyBy from 'lodash/keyBy'
import { worldConnector, searchInListIcons } from 'constants/functions.constants'

const useAllIngredients = (allIngredients, ingredients) => {
  const allIngredientsById = keyBy(allIngredients, '_id')
  return ingredients.map(ingredient => ({ ...allIngredientsById[ingredient._id], ...ingredient }))
}

export const BuildListIngredients = (allIngredients, ingredients) => {
  const listIngredients = useAllIngredients(allIngredients, ingredients)
  if (listIngredients.length === 0) {
    return
  }

  return listIngredients.map(({ quantity, slug, unit, name }) => {
    const nameModified = name.toLowerCase()
    const noUnit = unit === 'portion'
    const nameWithArticle = worldConnector(nameModified)

    return noUnit ? (
      <li key={slug}>
        <img src={searchInListIcons(slug)} alt={name} width="30" height="30" />
        {`${quantity} ${nameModified}${quantity > 1 ? '(s)' : ''}`}
      </li>
    ) : (
      <li key={slug}>
        <img src={searchInListIcons(slug)} alt={name} width="30" height="30" />
        <span className="listIngredients_quantity">
          {quantity} {unit}
        </span>{' '}
        {nameWithArticle}
      </li>
    )
  })
}
