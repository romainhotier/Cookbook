import React from 'react'
import { Menu, Button } from 'antd'
import { NavLink } from 'react-router-dom'

import Routes from '../../RecipeRoutes'

export const menuActions = (slug, showModal) => (
  <Menu className={'RecipeDetails_menu'}>
    <Menu.Item key="edit">
      <NavLink to={Routes.recipeEdit(slug)} exact>
        <i className="fas fa-edit icons"></i> Modifier la recette
      </NavLink>
    </Menu.Item>
    <Menu.Item key="delete">
      <Button onClick={showModal} type="text" className="RecipeDetails_menu_button">
        <i className="fas fa-trash-alt icons"></i> Supprimer
      </Button>
    </Menu.Item>
  </Menu>
)
