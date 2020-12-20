import React, { useEffect } from 'react'
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

  const updateRecipe = data => {
    putRecipe(data._id, data)
  }

  if (recipe === undefined) {
    return <Spin />
  }

  const stepsWithIdFront = recipe.steps.map((step, index) => ({ ...step, idFront: index }))

  return (
    <Row>
      <Col span={24}>
        <h1>Modifier une recette</h1>
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

export default connect(mapStateToProps, mapDispatchToProps)(RecipePageEdit)
