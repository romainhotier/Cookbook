import React, {useState, useEffect} from "react";
import { connect } from "react-redux";
import { Col, Row } from "antd";

import RecipeForm from 'modules/recipe/components/RecipeForm'
import { fetchRecipe, postRecipe } from "modules/recipe/thunks";

const RecipePageAdd = ({recipe, postRecipe, fetchRecipe}) => {
  // const [slugRecipe, setSlugRecipe] = useState('');

  useEffect(() => {
    console.log("recipe", recipe)
    if(recipe.length > 0) {
      fetchRecipe(recipe.slug)
    }
  }, [recipe])

  const createRecipe = (data) => {
    console.log('data', data)
    postRecipe(data);
  }

  return (
    <Row>
      <Col span={24}>
        <h1>Ajouter une recette</h1>
        <RecipeForm createRecipe={createRecipe} recipe={recipe}/>
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
