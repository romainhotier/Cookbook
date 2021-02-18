import React from 'react'
import { Row, Col } from 'antd'

import RecipeRouter from 'modules/recipe/RecipeRouter'
import IngredientRouter from 'modules/ingredient/IngredientRouter'
import { Menu } from 'components/Menu/Menu.component'
import { MobileMenu } from 'components/Menu/MobileMenu.component'

import './_Layout.scss'

const Layout = () => {
  return (
    <Row>
      <Col
        xs={{ span: 24, offset: 0 }}
        sm={{ span: 24, offset: 0 }}
        md={{ span: 24, offset: 0 }}
        lg={{ span: 24, offset: 0 }}
        xl={{ span: 24, offset: 0 }}
      >
        <div className="layout">
          <Menu className={'layout_desktopMenu'} />
          <MobileMenu className={'layout_mobileMenu'} />
          <main className="layout_content">
            {RecipeRouter}
            {IngredientRouter}
          </main>
        </div>
      </Col>
    </Row>
  )
}

export default Layout
