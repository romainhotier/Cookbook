import React from 'react'
import { Route } from 'react-router-dom'

import { IngredientLayout } from './IngredientLayout'
import Routes from './IngredientRoutes'

const IngredientRouter = <Route path={Routes.ingredient()} component={IngredientLayout} />

export default IngredientRouter
