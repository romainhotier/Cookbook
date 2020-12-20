import React from 'react'
import { connect } from 'react-redux'
import { Col, Row } from 'antd'

import RecipeForm from 'modules/recipe/components/RecipeForm'
import { postRecipe } from 'modules/recipe/thunks'

const RecipePageAdd = ({ postRecipe }) => {
  const createRecipe = data => {
    postRecipe(data)
  }

  return (
    <Row>
      <Col span={24}>
        <h1>Ajouter une recette</h1>
        <RecipeForm
          sendRecipe={createRecipe}
          values={{ ingredients: [{}], steps: [{ idFront: 0, description: '' }] }}
        />
      </Col>
    </Row>
  )
}

const mapDispatchToProps = {
  postRecipe,
}

const mapStateToProps = ({ recipes: { loadingPostRecipes } }) => ({
  loadingPostRecipes,
})

export default connect(mapStateToProps, mapDispatchToProps)(RecipePageAdd)
