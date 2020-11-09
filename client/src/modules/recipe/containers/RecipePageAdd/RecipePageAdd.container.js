import React from "react";
import { Col, Row } from "antd";

import RecipeForm from 'modules/recipe/components/RecipeForm'

const RecipePageAdd = () => {

  return (
    <Row>
      <Col span={24}>
        <h1>Ajouter une recette</h1>
        <RecipeForm />
      </Col>
    </Row>
  );
}

export default RecipePageAdd;
