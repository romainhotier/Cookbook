import React from 'react'
import { Route } from 'react-router-dom'

import RecipeLayout from './RecipeLayout'
import Routes from './RecipeRoutes'

const RecipeRouter = (
  <Route path={Routes.recipe()} component={RecipeLayout} />
)

export default RecipeRouter
