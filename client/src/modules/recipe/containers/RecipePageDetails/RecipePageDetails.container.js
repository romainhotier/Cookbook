import { connect } from 'react-redux'
import React, { Component } from 'react'
import { Row, Col } from 'antd'

import { fetchAllRecipe } from '../../thunks'

class RecipePageDetails extends Component {
  render() {
    return (
      <>
        wsh
      </>
    )
  }
}

const mapDispatchToProps = {
  fetchAllRecipe,
}

const mapStateToProps = ({recipes : {content, loadingFetchRecipes}}) => ({recipes: content, loadingFetchRecipes})

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(RecipePageDetails)
