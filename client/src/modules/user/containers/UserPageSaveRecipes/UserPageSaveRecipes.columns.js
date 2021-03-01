import React from 'react'
import { NavLink } from 'react-router-dom'

import Routes from 'modules/recipe/RecipeRoutes'

export const columns = [
  {
    title: 'Titre',
    dataIndex: 'title',
    key: 'title',
    render: (title, { slug }) => (
      <NavLink to={Routes.recipeEdit(slug)} exact>
        {title}
      </NavLink>
    ),
  },
  {
    title: "Nombre d'étapes",
    dataIndex: 'steps',
    key: 'steps',
    align: 'center',
    render: elem => {
      const nb = elem.length
      return nb < 2 ? `${nb} étape` : `${nb} étapes`
    },
  },
  {
    title: "Nombre d'ingrédients",
    dataIndex: 'ingredients',
    key: 'ingredients',
    align: 'center',
    render: elem => {
      const nb = elem.length
      return nb < 2 ? `${nb} ingredient` : `${nb} ingredients`
    },
  },
]
