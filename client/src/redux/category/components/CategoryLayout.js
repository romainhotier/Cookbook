import React from 'react'
import {Switch, Route} from 'react-router-dom'

import ContentPage from '../../../components/contentPage/ContentPage'
import CategoryPageList from './categoryList/CategoryPageList'

const CategoryLayout = ({children}) => (
  <ContentPage
    children={children}
  >
    <Switch>
      <Route path="/categories" exact component={CategoryPageList} />
    </Switch>
  </ContentPage>
)

export default CategoryLayout
