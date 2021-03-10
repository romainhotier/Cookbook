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
      loadingFetchIngredients,
      fetchAllIngredients,
    } = this.props

    const recipe = find(recipesList.toJS(), recipe => recipe.slug === slug)

    if (recipe === undefined) {
      fetchRecipe(slug)
    }

    if (recipe !== undefined && Object.keys(allIngredients).length === 0 && !loadingFetchIngredients) {
      fetchAllIngredients()
    }
  }

  componentDidUpdate(prevProps) {
    const { allIngredients, fetchAllIngredients, loadingFetchIngredients } = this.props
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
      recipesList,
      match: {
        params: { slug },
      },
      loadingFetchIngredients,
      loadingFetchRecipe,
      allIngredients,
      deleteRecipe,
      history,
    } = this.props

    const { portionEdited, modalDeleteRecipeIsVisible, uploadFilesIsVisible } = this.state
    const recipe = find(recipesList.toJS(), recipe => recipe.slug === slug)

    if (
      recipe === undefined ||
      loadingFetchIngredients ||
      loadingFetchRecipe ||
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
  recipesList: getAllRecipes(recipes),
  loadingFetchRecipe: getloadingFetchRecipe(recipes),
  allIngredients: ingredients.content,
  loadingFetchIngredients: ingredients.loadingFetchIngredients,
  loadingDeleteRecipe: recipes.loading,
})

export default connect(mapStateToProps, mapDispatchToProps)(RecipePageDetails)

RecipePageDetails.propTypes = {
  recipesList: PropTypes.array,
  history: PropTypes.object,
  match: PropTypes.object,
  allIngredients: PropTypes.array,
  fetchRecipe: PropTypes.func,
  fetchAllIngredients: PropTypes.func,
  loadingFetchIngredients: PropTypes.bool,
}
