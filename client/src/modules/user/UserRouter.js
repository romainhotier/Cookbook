import React from 'react'
import { Route } from 'react-router-dom'

import { UserLayout } from './UserLayout'
import Routes from './UserRoutes'

const UserRouter = <Route path={Routes.myAccount()} component={UserLayout} />

export default UserRouter
