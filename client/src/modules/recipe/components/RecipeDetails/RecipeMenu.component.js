import React from 'react'
import { Menu } from 'antd'
import { NavLink } from 'react-router-dom'

import Routes from '../../RecipeRoutes'

export const menuActions = slug => (
  <Menu>
    <Menu.Item key="edit">
      <NavLink to={Routes.recipeEdit(slug)} exact>
        <i className="fas fa-edit icons"></i> Modifier la recette
      </NavLink>
    </Menu.Item>
    <Menu.Item key="delete">
      <i className="fas fa-trash-alt icons"></i> Supprimer
    </Menu.Item>
  </Menu>
)
