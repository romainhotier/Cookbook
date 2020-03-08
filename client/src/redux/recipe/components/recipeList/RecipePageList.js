import { connect } from 'react-redux'
import React, { Component } from 'react'
import { Row, Col } from 'antd'

import { getAllRecipes } from '../../thunks/recipeThunks'
import RecipeSingleElement from '../shared/RecipeSingleElement'

import './_RecipeList.scss'

class RecipePageList extends Component {
  constructor(props) {
    super(props)
    this.state = {
      loading: true,
    }
  }

  componentDidMount() {
    this.props.getAllRecipes()
  }

  render() {
    const { fetchRecipes, recipes } = this.props
    if (fetchRecipes === true || Object.entries(recipes).length === 0) {
      return 'Patientez'
    }
    return (
      <>
        <Row>
          {Object.values(recipes).map((singleRecipe, key) => (
            <Col key={key}>
              <RecipeSingleElement recipe={singleRecipe} whenDisplay="list"/>
            </Col>
          ))}
        </Row>
      </>
    )
  }
}

const mapDispatchToProps = {
  getAllRecipes,
}

const mapStateToProps = ({ recipes: { fetchRecipes, content } }) => {
  return {
    fetchRecipes: fetchRecipes,
    recipes: content,
  }
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(RecipePageList)
