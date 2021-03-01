import React from 'react'
import { Switch, Route } from 'react-router-dom'
import { Row, Col } from 'antd'

import UserPageAccount from './containers/UserPageAccount'
import UserPageSaveRecipes from './containers/UserPageSaveRecipes'
import UserMenu from './components/UserMenu'

import Routes from './UserRoutes'

export const UserLayout = () => (
  <Row gutter={16}>
    <Col xs={4} sm={4} md={4} lg={4} xl={4} className={'UserMenu'}>
      <UserMenu />
    </Col>
    <Col xs={20} sm={20} md={20} lg={20} xl={20}>
      <Switch>
        <Route path={Routes.myAccount()} exact component={UserPageAccount} />
        <Route path={Routes.myAccountSaveRecipes()} exact component={UserPageSaveRecipes} />
        <Route path={Routes.myAccountFavorites()} exact component={UserPageAccount} />
      </Switch>
    </Col>
  </Row>
)
