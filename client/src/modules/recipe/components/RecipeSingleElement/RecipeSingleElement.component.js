import React from 'react'
import PropTypes from 'prop-types'
import { NavLink } from 'react-router-dom'

import Routes from '../../RecipeRoutes.js'
import CategoryTag from 'components/CategoryTag'
import { no_image } from 'ressources/iconsGlobals'

import './_RecipeSingleElement.scss'

const convertMinutes = value => {
  const hourExiste = Math.round(value / 60, 10)

  if (hourExiste > 1) {
    const minutes = value % 60
    return `${hourExiste} h ${minutes} min`
  }
  return `${value} minutes`
}

const RecipeSingleElement = ({ recipe }) => {
  const { title, categories, preparation_time, cooking_time, nb_people, calories, slug, files = [] } = recipe
  const imagePath = files[0] ? `${process.env.REACT_APP_IMAGES_SERVER}/${files[0]}` : no_image

  return (
    <article className="recipeSingleElement">
      <div className="recipeSingleElement_image" style={{ backgroundImage: `url(${imagePath})` }}>
        <div className="recipeSingleElement_mainCategorie">
          <a href="/">{categories[0]}</a>
        </div>
      </div>
      <h3>
        <NavLink to={Routes.recipeDetails(slug)} exact>
          {title}
        </NavLink>
      </h3>
      <div className="recipeSingleElement_details">
        <span>
          <i className="far fa-clock"></i> {convertMinutes(parseInt(preparation_time) + parseInt(cooking_time))}
        </span>{' '}
        |
        <span>
          <i className="far fa-list-alt"></i> {Math.round(calories / nb_people, 0)} cal
        </span>
      </div>

      <div className="RecipeDetails_categories recipeSingleElement_categories">
        {categories.map(category => (
          <CategoryTag key={`key-${category}`} category={category} />
        ))}
      </div>
    </article>
  )
}

RecipeSingleElement.propTypes = {
  recipe: PropTypes.object,
}

export default RecipeSingleElement
