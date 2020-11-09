import React from "react";
import { Form, Button } from "antd";

import { Input } from "components/Form/Input.component";
import { CheckboxWithImage } from "components/Form/CheckboxWithImage.component";
import { categories } from "constants/categories.constants";

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

        {/* */}
        <CheckboxWithImage label="Catégories" name="categories" datas={categories} onChange={onChange} />

        {/* Titre de la recette */}
        <Input label="Titre de la recette" name="title" required={RecipeValidator['title'].required} error={RecipeValidator['title'].errorMessage} />

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
