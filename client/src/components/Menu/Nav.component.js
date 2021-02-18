import React from 'react'
// import PropTypes from 'prop-types'
import { NavLink } from 'react-router-dom'

import { Routes as RecipeRoutes } from 'modules/recipe/RecipeRoutes'
import { Routes as IngredientRoutes } from 'modules/ingredient/IngredientRoutes'

export const Nav = () => {
  return (
    <>
      <NavLink to={RecipeRoutes.recipe()} exact>
        Liste des recettes
      </NavLink>
      <NavLink to={RecipeRoutes.recipeAdd()} exact>
        Ajouter une recette
      </NavLink>
      <NavLink to={IngredientRoutes.ingredient()} exact>
        Liste des ingrédients
      </NavLink>
    </>
  )
}

Nav.propTypes = {}
