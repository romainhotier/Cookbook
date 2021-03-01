import React from 'react'
import { Row, Col } from 'antd'

import RecipeRouter from 'modules/recipe/RecipeRouter'
import IngredientRouter from 'modules/ingredient/IngredientRouter'
import UserRouter from 'modules/user/UserRouter'
import { Menu } from 'components/Menu/Menu.component'
import { MobileMenu } from 'components/Menu/MobileMenu.component'

import './_Layout.scss'

const Layout = () => {
  const responsive = {
    xs: { span: 24, offset: 0 },
    sm: { span: 24, offset: 0 },
    md: { span: 24, offset: 0 },
    lg: { span: 20, offset: 2 },
    xl: { span: 18, offset: 3 },
  }

  return (
    <Row>
      <Col {...responsive}>
        <div className="layout">
          <Menu className={'layout_desktopMenu'} />
          <MobileMenu className={'layout_mobileMenu'} />
          <main className="layout_content">
            {RecipeRouter}
            {IngredientRouter}
            {UserRouter}
          </main>
        </div>
      </Col>
    </Row>
  )
}

export default Layout
