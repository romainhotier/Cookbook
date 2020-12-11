import React, {useState, useEffect} from "react";
import { connect } from "react-redux";
import { Col, Row } from "antd";
import head from "lodash/head";

import RecipeForm from 'modules/recipe/components/RecipeForm'
import { fetchRecipe, postRecipe } from "modules/recipe/thunks";

const RecipePageAdd = ({recipe, postRecipe, fetchRecipe}) => {
  const [slugRecipe, setSlugRecipe] = useState(undefined);

  useEffect(() => {
    if(recipe.length > 0) {
      fetchRecipe(recipe.slug)
    }
  }, [recipe])

  const createRecipe = (data) => {
    console.log('data', data)
    postRecipe(data);
  }

  console.log("----Container")
  console.log("recipe", recipe)
  console.log("----")

  return (
    <Row>
      <Col span={24}>
        <h1>Ajouter une recette</h1>
        <RecipeForm createRecipe={createRecipe} recipe={recipe} slugRecipe={slugRecipe} setSlugRecipe={setSlugRecipe} />
      </Col>
    </Row>
  );
}

const mapDispatchToProps = {
  fetchRecipe,
  postRecipe,
};

const mapStateToProps = ({ recipes: { content, loadingFetchRecipes } }) => ({
  recipe: content,
  loadingFetchRecipes,
});

export default connect(mapStateToProps, mapDispatchToProps)(RecipePageAdd);
