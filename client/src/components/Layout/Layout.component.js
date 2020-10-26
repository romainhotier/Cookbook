import React from 'react'
import {Row, Col} from 'antd'
import { NavLink } from 'react-router-dom'

import RecipeRouter from 'modules/recipe/RecipeRouter'
// import CategoryRouter from 'redux/category/components/CategoryRouter'
// import NavigationItem from '../navigation/NavigationItem'
import {Routes as RecipeRoutes} from 'modules/recipe/RecipeRoutes'
// import {Routes as CategoriesRoute} from 'redux/category/components/CategoryRoutes'

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
              {/* 
              <NavigationItem
                name="Ajouter une recette"
                url={RecettesRoute.recipeAdd()}
              />
              <NavigationItem
                name="Liste des catégories"
                url={CategoriesRoute.category()}
              /> */}
            </div>
          </nav>
          <main className='layout_content'>
            { RecipeRouter }
            {/* { CategoryRouter } */}
          </main>
        </div>
      </Col>
    </Row>
  )
}

export default Layout
