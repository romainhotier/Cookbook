import React from 'react'
import {Row, Col} from 'antd'
import { NavLink } from 'react-router-dom'

import RecipeRouter from 'modules/recipe/RecipeRouter'
import {Routes as RecipeRoutes} from 'modules/recipe/RecipeRoutes'
import IngredientRouter from 'modules/ingredient/IngredientRouter'
import {Routes as IngredientRoutes} from 'modules/ingredient/IngredientRoutes'

import './_Layout.scss'

const Layout = () => {
  return (
    <Row>
      <Col
        xs={{ span: 24, offset: 0 }}
        sm={{ span: 24, offset: 0 }}
        md={{ span: 20, offset: 2 }}
        lg={{ span: 20, offset: 2 }}
        xl={{ span: 20, offset: 2 }}
      >
        <div className="layout">
          <nav className="layout_menu">
            <div className="layout_logo">
              <h1>Cook</h1>
            </div>
            <div className="layout_menu_items">
              <NavLink to={RecipeRoutes.recipe()} exact>
                Liste des recettes
              </NavLink>
              <NavLink to={RecipeRoutes.recipeAdd()} exact>
                Ajouter une recette
              </NavLink>
              <NavLink to={IngredientRoutes.ingredient()} exact>
                Liste des ingrédients
              </NavLink>
            </div>
          </nav>
          <main className='layout_content'>
            { RecipeRouter }
            { IngredientRouter }
          </main>
        </div>
      </Col>
    </Row>
  )
}

export default Layout
