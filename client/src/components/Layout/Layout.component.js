import React from 'react'
import {Row, Col} from 'antd'

import RecipeRouter from 'modules/recipe/RecipeRouter'
// import CategoryRouter from 'redux/category/components/CategoryRouter'
// import NavigationItem from '../navigation/NavigationItem'

// import {Routes as RecettesRoute} from 'redux/recipe/components/RecipeRoutes'
// import {Routes as CategoriesRoute} from 'redux/category/components/CategoryRoutes'

import './_Layout.scss'

const Layout = () => {
  return (
    <Row>
      <Col span={16} offset={4}>
        <div className="layout">
          <nav className="layout_menu">
            <div className="layout_logo">
              <h1>Cook</h1>
            </div>
            <div className="layout_menu_items">
              {/* <NavigationItem
                name="Liste des recettes"
                url={RecettesRoute.recipe()}
              />
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
