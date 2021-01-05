import React, { useEffect } from 'react'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'
import { Col, Row, Spin } from 'antd'

import RecipeForm from 'modules/recipe/components/RecipeForm'
import { putRecipe, fetchRecipe } from 'modules/recipe/thunks'

const RecipePageEdit = ({ recipes, putRecipe, match, fetchRecipe }) => {
  const slug = match.params.id

  useEffect(() => {
    if (recipes[slug] === undefined) {
      fetchRecipe(slug)
    }
  })

  const recipe = recipes[slug]

  const updateRecipe = (data, file) => {
    console.log('data', data)
    console.log('file', file)
    //putRecipe(data._id, data)
  }

  if (recipe === undefined) {
    return <Spin />
  }

  const stepsWithIdFront = recipe.steps.map((step, index) => ({ ...step, idFront: index }))

  return (
    <Row>
      <Col span={24}>
        <h2>Modifier une recette</h2>
        <RecipeForm sendRecipe={updateRecipe} values={{ ...recipe, steps: stepsWithIdFront }} />
      </Col>
    </Row>
  )
}

const mapDispatchToProps = {
  putRecipe,
  fetchRecipe,
}

const mapStateToProps = ({ recipes: { content, loadingPutRecipes } }) => ({
  recipes: content,
  loadingPutRecipes,
})

RecipePageEdit.propTypes = {
  recipes: PropTypes.object,
  putRecipe: PropTypes.func,
  match: PropTypes.object,
  fetchRecipe: PropTypes.func,
}

export default connect(mapStateToProps, mapDispatchToProps)(RecipePageEdit)
