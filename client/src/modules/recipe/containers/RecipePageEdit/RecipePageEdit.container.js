import React, { useEffect } from 'react'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'
import { Col, Row } from 'antd'
import omit from 'lodash/omit'

import RecipeForm from 'modules/recipe/components/RecipeForm'
import { putRecipe, fetchRecipe, postFileRecipe, deleteFileRecipe } from 'modules/recipe/thunks'
import Loader from 'components/Loader'

const RecipePageEdit = ({ recipes, putRecipe, match, fetchRecipe, postFileRecipe, deleteFileRecipe }) => {
  const slug = match.params.id

  useEffect(() => {
    if (recipes[slug] === undefined) {
      fetchRecipe(slug)
    }
  })

  const recipe = recipes[slug]

  const addFileInRecipe = file => {
    const formData = new FormData()
    formData.append('files', file)
    postFileRecipe(recipe._id, formData)
  }

  const deleteFileInRecipe = file => {
    deleteFileRecipe(file.url)
  }

  const updateRecipe = data => {
    const recipeWithoutFiles = omit(data, 'filesRecipe')
    putRecipe(data._id, recipeWithoutFiles)
  }

  if (recipe === undefined) {
    return <Loader />
  }

  const stepsWithIdFront = recipe.steps.map((step, index) => ({ ...step, idFront: index }))

  return (
    <Row>
      <Col span={24}>
        <h2>Modifier une recette</h2>
        <RecipeForm
          sendRecipe={updateRecipe}
          values={{ ...recipe, steps: stepsWithIdFront }}
          addFileInRecipe={addFileInRecipe}
          deleteFileInRecipe={deleteFileInRecipe}
          action={'update'}
        />
      </Col>
    </Row>
  )
}

const mapDispatchToProps = {
  putRecipe,
  fetchRecipe,
  postFileRecipe,
  deleteFileRecipe,
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
  postFileRecipe: PropTypes.func,
  deleteFileRecipe: PropTypes.func,
}

export default connect(mapStateToProps, mapDispatchToProps)(RecipePageEdit)
