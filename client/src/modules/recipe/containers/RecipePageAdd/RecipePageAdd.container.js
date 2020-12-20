import React from 'react'
import { connect } from 'react-redux'
import { Col, Row } from 'antd'

import RecipeForm from 'modules/recipe/components/RecipeForm'
import { postRecipe } from 'modules/recipe/thunks'

const RecipePageAdd = ({ recipe, postRecipe }) => {
  const createRecipe = data => {
    console.log('createRecipe data', data)
    postRecipe(data)
  }

  return (
    <Row>
      <Col span={24}>
        <h1>Ajouter une recette</h1>
        <RecipeForm createRecipe={createRecipe} />
      </Col>
    </Row>
  )
}

const mapDispatchToProps = {
  postRecipe,
}

const mapStateToProps = ({ recipes: { content, loadingPostRecipes } }) => ({
  recipe: content,
  loadingPostRecipes,
})

export default connect(mapStateToProps, mapDispatchToProps)(RecipePageAdd)
