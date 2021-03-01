import React from 'react'
import { Menu } from 'antd'
import { NavLink } from 'react-router-dom'

import Routes from '../../UserRoutes'

import './_UserMenu.scss'

const UserMenu = () => {
  return (
    <Menu defaultSelectedKeys={['1']} mode="inline">
      <Menu.Item key="1">
        <NavLink to={Routes.myAccount()} exact>
          Votre profil
        </NavLink>
      </Menu.Item>
      <Menu.Item key="2">
        <NavLink to={Routes.myAccountSaveRecipes()} exact>
          Recettes non terminées
        </NavLink>
      </Menu.Item>
      <Menu.Item key="3">
        <NavLink to={Routes.myAccountFavorites()} exact>
          Favoris
        </NavLink>
      </Menu.Item>
    </Menu>
  )
}

export default UserMenu
