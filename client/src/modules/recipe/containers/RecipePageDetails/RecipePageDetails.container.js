import { connect } from 'react-redux'
import React, { Component } from 'react'

import { fetchRecipe } from '../../thunks'

class RecipePageDetails extends Component {
    componentDidMount() {
        const {recipes, match, fetchRecipe} = this.props
        const {slug} = match.params

        if(recipes[slug] === undefined) {
          fetchRecipe(slug)
        }
    }

      
  render() {
    console.log('this.props', this.props)

    return (
      <>
        wsh tata
      </>
    )
  }
}

const mapDispatchToProps = {
    fetchRecipe,
}

const mapStateToProps = ({recipes : {content, loadingFetchRecipes}}) => ({recipes: content, loadingFetchRecipes})

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(RecipePageDetails)
