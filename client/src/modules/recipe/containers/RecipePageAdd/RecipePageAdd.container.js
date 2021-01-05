import React from 'react'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'
import { Col, Row } from 'antd'

import RecipeForm from 'modules/recipe/components/RecipeForm'
import { postRecipe } from 'modules/recipe/thunks'

const RecipePageAdd = ({ postRecipe }) => {
  const createRecipe = (data, file) => {
    console.log('data', data)
    console.log('file', file)
    //postRecipe(data)
  }

  return (
    <Row>
      <Col span={24}>
        <h2>Ajouter une recette</h2>
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

RecipePageAdd.propTypes = {
  postRecipe: PropTypes.func,
}

export default connect(mapStateToProps, mapDispatchToProps)(RecipePageAdd)
