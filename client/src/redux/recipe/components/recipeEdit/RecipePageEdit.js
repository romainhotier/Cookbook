import { connect } from 'react-redux'
import React, { Component } from 'react'
/*import PropTypes from 'prop-types' */

import { getRecipe, getAllIngredientsOfRecipe, uploadDocument, editRecipe } from '../../thunks/recipeThunks'
import { getAllCategories } from 'redux/category/thunks/categoryThunks'

import RecipeFormFormik from '../shared/RecipeForm'

class RecipePageEdit extends Component {
  constructor(props) {
    super(props)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  componentDidMount() {
    const recipeID = this.props.match.params.id

    this.props.getRecipe(recipeID)
    this.props.getAllIngredientsOfRecipe(recipeID)
    this.props.getAllCategories()
  }

  handleSubmit(recipeData, id) {
    this.props.editRecipe(id, recipeData)

    if (typeof recipeData.image === 'object') {
      this.props.uploadDocument(recipeData)
    }
    this.props.history.push(`/recipes/${recipeData.id}`)
  }

  render() {
    const {
      inProgressRecipe,
      inProgressCategory,
      categoriesList,
      inProgresscategoriesList,
      inProgressIngredient,
      recipes,
    } = this.props

    if (
      inProgressIngredient === true ||
      inProgressRecipe === true ||
      inProgressCategory === true ||
      inProgresscategoriesList === true ||
      Object.keys(recipes).length === 0 ||
      Object.keys(categoriesList).length === 0
    ) {
      return 'Patientez'
    }
    const recipe = recipes[this.props.match.params.id]

    return (
      <div className="panel">
        <div className="panel_content">
          <h2 className="title">Modifier la recipe</h2>
          <RecipeFormFormik
            handleSubmit={this.handleSubmit}
            recipe={recipe}
            categoriesList={categoriesList}
          />
        </div>
      </div>
    )
  }
}

const mapDispatchToProps = {
  getRecipe,
  getAllIngredientsOfRecipe,
  editRecipe,
  uploadDocument,
  getAllCategories,
}

const mapStateToProps = ({ recipes, categories }) => {
  return {
    categoriesList: categories.content,
    inProgresscategoriesList: categories.inProgress,
    inProgressIngredient: recipes.fetchIngredients,
    inProgressRecipe: recipes.fetchRecipes,
    recipes: recipes.content,
  }
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(RecipePageEdit)

/* recipePageEdit.propTypes = {
    title: PropTypes.string.isRequired,
    ingredients: PropTypes.array.isRequired,
    level: PropTypes.string.isRequired,
}
 */
