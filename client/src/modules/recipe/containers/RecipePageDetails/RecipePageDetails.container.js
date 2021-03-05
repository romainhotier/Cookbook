import React, { Component } from 'react'
import { connect } from 'react-redux'

import { fetchRecipe, deleteRecipe } from 'modules/recipe/thunks'
import { fetchAllIngredients } from 'modules/ingredient/thunks'
import { RecipePageDetailsComponent } from './RecipePageDetails.component'
import Loader from 'components/Loader'

class RecipePageDetails extends Component {
  constructor(props) {
    super(props)

    this.state = {
      portionEdited: null,
      modalDeleteRecipeIsVisible: false,
      uploadFilesIsVisible: false,
    }
  }

  componentDidMount() {
    const { recipes, match, fetchRecipe, allIngredients, loadingFetchIngredients, fetchAllIngredients } = this.props
    const { slug } = match.params
    if (recipes[slug] === undefined) {
      fetchRecipe(slug)
    }

    if (recipes[slug] !== undefined && Object.keys(allIngredients).length === 0 && !loadingFetchIngredients) {
      fetchAllIngredients()
    }
  }

  componentDidUpdate() {
    const { allIngredients, fetchAllIngredients, loadingFetchIngredients, recipes } = this.props
    if (Object.keys(allIngredients).length === 0 && !loadingFetchIngredients) {
      fetchAllIngredients()
    }
  }

  updatePortionEdited = newPortion => {
    if (isNaN(newPortion)) {
      return this.setState({
        portionEdited: 0,
      })
    }
    return this.setState({
      portionEdited: newPortion,
    })
  }

  showModal = () => {
    return this.setState({
      modalDeleteRecipeIsVisible: true,
    })
  }

  handleUploadFiles = () => {
    const isVisible = this.state.uploadFilesIsVisible
    return this.setState({
      uploadFilesIsVisible: !isVisible,
    })
  }

  render() {
    const {
      recipes,
      match,
      loadingFetchIngredients,
      loadingFetchRecipes,
      allIngredients,
      deleteRecipe,
      history,
    } = this.props

    const { portionEdited, modalDeleteRecipeIsVisible, uploadFilesIsVisible } = this.state
    const { slug } = match.params
    const recipe = recipes[slug]

    if (
      recipe === undefined ||
      loadingFetchIngredients ||
      loadingFetchRecipes ||
      Object.keys(allIngredients).length === 0
    ) {
      return <Loader />
    }

    return (
      <RecipePageDetailsComponent
        recipe={recipe}
        allIngredients={allIngredients}
        portionEdited={portionEdited}
        updatePortionEdited={this.updatePortionEdited}
        history={history}
        modalDeleteRecipeIsVisible={modalDeleteRecipeIsVisible}
        deleteRecipe={deleteRecipe}
        showModal={this.showModal}
        handleUploadFiles={this.handleUploadFiles}
        uploadFilesIsVisible={uploadFilesIsVisible}
      />
    )
  }
}

const mapDispatchToProps = {
  fetchRecipe,
  fetchAllIngredients,
  deleteRecipe,
}

const mapStateToProps = ({ recipes, ingredients }) => ({
  recipes: recipes.content,
  loadingFetchRecipes: recipes.loadingFetchRecipes,
  allIngredients: ingredients.content,
  loadingFetchIngredients: ingredients.loadingFetchIngredients,
  loadingDeleteRecipe: recipes.loading,
})

export default connect(mapStateToProps, mapDispatchToProps)(RecipePageDetails)
