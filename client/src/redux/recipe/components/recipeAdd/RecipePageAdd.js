import { connect } from 'react-redux'
import React, { Component } from 'react'

import { getAllCategories } from 'redux/category/thunks/categoryThunks'
import { addRecipe, uploadDocument } from '../../thunks/recipeThunks'
import RecipeFormFormik from '../shared/RecipeForm'
import Routes from '../RecipeRoutes'

class RecipePageAdd extends Component {
  constructor(props) {
    super(props)
    this.state = {
      isSubmitting: false
    }
  }

  componentDidMount() {
    this.props.getAllCategories()
  }

  componentDidUpdate() {
    if(this.state.isSubmitting && this.props.submittingIsSuccess) {
      this.props.history.push(Routes.recipe());
    }
  }

  handleSubmit = (recipeData) => {
    this.setState({isSubmitting: true})
    this.props.addRecipe(recipeData)
  }

  render() {
    const { inProgressRecipe, inProgressCategoriesList, categoriesList } = this.props
    if (inProgressRecipe || inProgressCategoriesList) {
      return 'Patientez'
    }

    return (
      <div className="panel">
        <div className="panel_content">
          <h1 className="title">Ajouter une recette</h1>
          <RecipeFormFormik handleSubmit={this.handleSubmit} categoriesList={categoriesList} />
        </div>
      </div>
    )
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    addRecipe: (data) => {
      dispatch(addRecipe(data))
      dispatch(uploadDocument(data))
    },
    getAllCategories: () => dispatch(getAllCategories()),
  }
}

const mapStateToProps = ({ recipes, categories }) => {
  return {
    inProgressRecipe: recipes.submitRecipe,
    content: recipes.content,
    submittingIsSuccess: recipes.submittingIsSuccess,
    inProgressCategoriesList: categories.isFetching,
    categoriesList: categories.content
  }
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(RecipePageAdd)


/* recipePageAdd.propTypes = {
    title: PropTypes.string.isRequired,
    ingredients: PropTypes.array.isRequired,
    level: PropTypes.string.isRequired,
}
 */
