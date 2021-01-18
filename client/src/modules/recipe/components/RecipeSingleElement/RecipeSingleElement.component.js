import React from 'react'
import { NavLink } from 'react-router-dom'
import Routes from '../../RecipeRoutes.js'

import './_RecipeSingleElement.scss'

const convertMinutes = value => {
  const hourExiste = Math.round(value / 60, 0)
  if (hourExiste > 1) {
    const minutes = value % 60
    return `${hourExiste} h ${minutes} min`
  }
  return `${value} minutes`
}

const RecipeSingleElement = ({ recipe }) => {
  const { title, categories, preparation_time, cooking_time, nb_people, slug, files = [] } = recipe

  return (
    <article className="recipeSingleElement">
      <div
        className="recipeSingleElement_image"
        style={{ backgroundImage: `url(${process.env.REACT_APP_IMAGES_SERVER}/${files[0]})` }}
      >
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
          <i className="far fa-clock"></i> {convertMinutes(preparation_time + cooking_time)}
        </span>{' '}
        |
        <span>
          <i className="far fa-user"></i> {nb_people}
        </span>
      </div>
    </article>
  )
}

export default RecipeSingleElement
