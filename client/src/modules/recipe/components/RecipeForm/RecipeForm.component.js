import React from "react";
import { Form, Button, Row, Col, Divider } from "antd";

import { Input } from "components/Form/Input.component";
import { CheckboxWithImage } from "components/Form/CheckboxWithImage.component";
import { categories } from "constants/categories.constants";

import RecipeIngredientsForm from "../RecipeIngredientsForm";
import { RecipeValidator } from "./RecipeForm.validator";

const RecipeForm = () => {
  const onFinish = (values) => {
    console.log("Success:", values);
  };

  const onFinishFailed = (errorInfo) => {
    console.log("Failed:", errorInfo);
  };

  const onChange = (data) => {
    console.log("checked:", data);
  };

  return (
    <>
      <Form
        layout="vertical"
        name="basic"
        onFinish={onFinish}
        onFinishFailed={onFinishFailed}
      >

        {/* Catégories */}
        <CheckboxWithImage
          label="Catégories"
          name="categories"
          datas={categories}
          onChange={onChange}
        />

        {/* Titre de la recette */}
        <Input
          label="Titre de la recette"
          name="title"
          required={RecipeValidator['title'].required}
          error={RecipeValidator['title'].errorMessage}
          placeholder={RecipeValidator['title'].placeholder}
        />

        <Row gutter="32">
          <Col lg={8} md={8} sm={24} xs={24}>
            {/* Temps de préparation */}
            <Input
              label="Temps de préparation"
              name="preparation_time"
              required={RecipeValidator['preparation_time'].required}
              error={RecipeValidator['preparation_time'].errorMessage}
              placeholder={RecipeValidator['preparation_time'].placeholder}
              addonAfter="min"
            />
          </Col>
          <Col lg={8} md={8} sm={24} xs={24}>
            {/* Temps de cuisson */}
            <Input
              label="Temps de cuisson"
              name="cooking_time"
              required={RecipeValidator['cooking_time'].required}
              error={RecipeValidator['cooking_time'].errorMessage}
              placeholder={RecipeValidator['cooking_time'].placeholder}
              addonAfter="min"
            />
          </Col>
          <Col lg={8} md={8} sm={24} xs={24}>
            {/* Nb portions */}
            <Input
              label="Nombre de portions"
              name="nb_people"
              required={RecipeValidator['nb_people'].required}
              error={RecipeValidator['nb_people'].errorMessage}
              placeholder={RecipeValidator['nb_people'].placeholder}
            />
          </Col>
        </Row>

        <Divider />

        <Row gutter={32}>
          {/* Ingrédients */}
          <Col span={8}>
            <RecipeIngredientsForm />
          </Col>
          {/* Steps */}
          <Col span={16}>
            <h2>Préparation</h2>
          </Col>
        </Row>

        <Form.Item>
          <Button type="primary" htmlType="submit">
            Submit
          </Button>
        </Form.Item>
      </Form>
    </>
  );
};

export default RecipeForm;
