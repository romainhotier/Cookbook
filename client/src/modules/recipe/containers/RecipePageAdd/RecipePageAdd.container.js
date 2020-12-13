import React, { useState, useEffect } from 'react'
import { connect } from 'react-redux'
import { Col, Row } from 'antd'

import RecipeForm from 'modules/recipe/components/RecipeForm'
import { fetchRecipe, postRecipe, putRecipe } from 'modules/recipe/thunks'
import { postIngredientsRecipe } from 'modules/ingredient/thunks'

const RecipePageAdd = ({ recipe, postRecipe, fetchRecipe, putRecipe }) => {
  const [slugRecipe, setSlugRecipe] = useState(undefined)

  useEffect(() => {
    if (recipe.length > 0) {
      fetchRecipe(recipe.slug)
    }
  }, [fetchRecipe, recipe])

  const createRecipe = data => {
    console.log('data', data)
    postRecipe(data)
  }

  const updateRecipe = (recipe, ingredientsRecipe) => {
    console.log('recipe', ingredientsRecipe)
    //putRecipe(data);
  }

  return (
    <Row>
      <Col span={24}>
        <h1>Ajouter une recette</h1>
        <RecipeForm
          createRecipe={createRecipe}
          updateRecipe={updateRecipe}
          recipe={recipe}
          slugRecipe={slugRecipe}
          setSlugRecipe={setSlugRecipe}
        />
      </Col>
    </Row>
  )
}

const mapDispatchToProps = {
  fetchRecipe,
  postRecipe,
  putRecipe,
  postIngredientsRecipe,
}

const mapStateToProps = ({ recipes: { content, loadingFetchRecipes } }) => ({
  recipe: content,
  loadingFetchRecipes,
})

export default connect(mapStateToProps, mapDispatchToProps)(RecipePageAdd)
