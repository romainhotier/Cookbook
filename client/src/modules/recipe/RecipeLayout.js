import React from 'react'
import {Switch, Route} from 'react-router-dom'

// import ContentPage from 'components/contentPage/ContentPage'
import RecipePageList from './containers/RecipePageList'
import RecipePageAdd from './containers/RecipePageAdd'
import RecipePageDetails from './containers/RecipePageDetails'
// import RecipePageEdit from './recipeEdit/RecipePageEdit'

import Routes from './RecipeRoutes'

const RecipeLayout = ({children}) => (
    <Switch>
      <Route path={Routes.recipe()} exact component={RecipePageList} />
      <Route path={Routes.recipeAdd()} exact component={RecipePageAdd} />
      <Route path={Routes.recipeDetails()} exact component={RecipePageDetails} />
      {/* <Route path={Routes.recipeEdit()} exact component={RecipePageEdit} /> */}
    </Switch>
)

export default RecipeLayout
