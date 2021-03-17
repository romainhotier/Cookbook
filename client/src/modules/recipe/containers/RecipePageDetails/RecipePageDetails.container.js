import React, { Component } from 'react'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'
import find from 'lodash/find'

import { fetchRecipe, deleteRecipe } from 'modules/recipe/thunks'
import { fetchAllIngredients } from 'modules/ingredient/thunks'
import { RecipePageDetailsComponent } from './RecipePageDetails.component'
import { getAllRecipes, getloadingFetchRecipe } from 'modules/recipe/reducers'
import Loader from 'components/Loader'

export class RecipePageDetails extends Component {
  constructor(props) {
    super(props)

    this.state = {
      portionEdited: null,
      modalDeleteRecipeIsVisible: false,
      uploadFilesIsVisible: false,
    }
  }

  componentDidMount() {
    const {
      recipesList,
      match: {
        params: { slug },
      },
      fetchRecipe,
      allIngredients,
      loadingFetchIngredient,
      fetchAllIngredients,
    } = this.props

    const recipe = find(recipesList.toJS(), recipe => recipe.slug === slug)

    if (recipe === undefined) {
      fetchRecipe(slug)
    }

    if (recipe !== undefined && Object.keys(allIngredients).length === 0 && !loadingFetchIngredient) {
      fetchAllIngredients()
    }
  }

  componentDidUpdate(prevProps) {
    const { allIngredients, fetchAllIngredients, loadingFetchIngredient } = this.props
    if (Object.keys(allIngredients).length === 0 && !loadingFetchIngredient) {
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

  closeModal = () => {
    return this.setState({
      modalDeleteRecipeIsVisible: false,
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
      recipesList,
      match: {
        params: { slug },
      },
      loadingFetchIngredient,
      loadingFetchRecipe,
      allIngredients,
      deleteRecipe,
      history,
    } = this.props

    const { portionEdited, modalDeleteRecipeIsVisible, uploadFilesIsVisible } = this.state
    const recipe = find(recipesList.toJS(), recipe => recipe.slug === slug)

    if (
      recipe === undefined ||
      loadingFetchIngredient ||
      loadingFetchRecipe ||
      Object.keys(allIngredients).length === 0
    ) {
      return <Loader />
    }

    return (
      <RecipePageDetailsComponent
        allIngredients={allIngredients}
        closeModal={this.closeModal}
        deleteRecipe={deleteRecipe}
        handleUploadFiles={this.handleUploadFiles}
        history={history}
        modalDeleteRecipeIsVisible={modalDeleteRecipeIsVisible}
        portionEdited={portionEdited}
        recipe={recipe}
        showModal={this.showModal}
        updatePortionEdited={this.updatePortionEdited}
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
  recipesList: getAllRecipes(recipes),
  loadingFetchRecipe: getloadingFetchRecipe(recipes),
  allIngredients: ingredients.content,
  loadingFetchIngredient: ingredients.loadingFetchIngredient,
  loadingDeleteRecipe: recipes.loading,
})

export default connect(mapStateToProps, mapDispatchToProps)(RecipePageDetails)

RecipePageDetails.propTypes = {
  recipesList: PropTypes.object,
  history: PropTypes.object,
  match: PropTypes.object,
  allIngredients: PropTypes.object,
  fetchRecipe: PropTypes.func,
  fetchAllIngredients: PropTypes.func,
  loadingFetchIngredient: PropTypes.bool,
}
