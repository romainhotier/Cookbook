import { connect } from 'react-redux'
import React, { Component } from 'react'
import { Col, Row } from 'antd'

import { fetchRecipe } from '../../thunks'

import './_RecipePageDetails.scss'

class RecipePageDetails extends Component {
  componentDidMount() {
    const { recipes, match, fetchRecipe } = this.props
    const { slug } = match.params
    console.log('recipes[slug]', recipes[slug])
    if (recipes[slug] === undefined) {
      fetchRecipe(slug)
    }
  }

  render() {
    const { recipes, match } = this.props
    const { slug } = match.params
    const recipe = recipes[slug]

    if (recipe === undefined) {
      return 'loader'
    }

    return (
      <>
        <Row>
          <Col xs={24} sm={24} md={18} lg={20} xl={20}>
            <h1>{recipe.title}</h1>
            <Row>
              <Col xs={4} sm={4} md={6} lg={6} xl={6}>
                <h3>Ingrédients</h3>
              </Col>
              <Col xs={16} sm={16} md={14} lg={14} xl={14}>
                <h3>Instructions</h3>
                {recipe.steps.map((element, index) => (
                  <div className="step" key={index}>
                    <div className="step_index">{index + 1}</div>
                    {element.step}
                  </div>
                ))}
              </Col>
            </Row>
          </Col>
          <Col xs={0} sm={0} md={6} lg={4} xl={4}>
            <ul>
              <li>az</li>
              <li>az</li>
              <li>az</li>
              <li>az</li>
              <li>az</li>
              <li>az</li>
            </ul>
          </Col>
        </Row>
      </>
    )
  }
}

const mapDispatchToProps = {
  fetchRecipe,
}

const mapStateToProps = ({ recipes: { content, loadingFetchRecipes } }) => ({
  recipes: content,
  loadingFetchRecipes,
})

export default connect(mapStateToProps, mapDispatchToProps)(RecipePageDetails)
