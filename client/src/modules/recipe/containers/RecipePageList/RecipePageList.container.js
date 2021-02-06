import React, { Component } from 'react'

import { connect } from 'react-redux'
import PropTypes from 'prop-types'
import { Row, Col } from 'antd'

import { fetchAllRecipe } from '../../thunks'
import RecipeSingleElement from '../../components/RecipeSingleElement'

import './_RecipePageList.scss'

class RecipePageList extends Component {
  componentDidMount() {
    this.props.fetchAllRecipe()
  }

  render() {
    const { loadingFetchRecipes, recipes } = this.props
    if (loadingFetchRecipes === true || Object.entries(recipes).length === 0) {
      return 'Patientez'
    }

    return (
      <>
        <Row>
          {Object.values(recipes).map((singleRecipe, key) => (
            <Col key={key} xs={24} sm={12} md={12} lg={6} xl={6}>
              <RecipeSingleElement recipe={singleRecipe} />
            </Col>
          ))}
        </Row>
      </>
    )
  }
}

const mapDispatchToProps = {
  fetchAllRecipe,
}

const mapStateToProps = ({ recipes: { content, loadingFetchRecipes } }) => ({ recipes: content, loadingFetchRecipes })

RecipePageList.propTypes = {
  fetchAllRecipe: PropTypes.func,
  recipes: PropTypes.array,
  loadingFetchRecipes: PropTypes.bool,
}

export default connect(mapStateToProps, mapDispatchToProps)(RecipePageList)
