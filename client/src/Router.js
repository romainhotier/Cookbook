import React from 'react'
import { Route } from 'react-router-dom'

import Layout from './components/layout/Layout'

const Router = () => {
  return <Route path="/" component={Layout} />
}

export default Router
