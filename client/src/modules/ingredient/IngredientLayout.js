import React from 'react'
import { Switch, Route } from 'react-router-dom'

import IngredientPageList from './containers/IngredientPageList'

import Routes from './IngredientRoutes'

export const IngredientLayout = () => (
  <Switch>
    <Route path={Routes.ingredient()} exact component={IngredientPageList} />
  </Switch>
)
