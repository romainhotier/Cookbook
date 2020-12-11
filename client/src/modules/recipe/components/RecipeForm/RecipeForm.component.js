import React, {useState} from "react";
import { Form, Button, Row, Col, Divider } from "antd";
import omit from "lodash/omit";

import { Input } from "components/Form/Input.component";
import { CheckboxWithImage } from "components/Form/CheckboxWithImage.component";
import { categories } from "constants/categories.constants";
import { slugify } from "constants/functions.constants";

import RecipeIngredientsForm from "../RecipeIngredientsForm";
import RecipeStepForm from "../RecipeStepForm";
import { RecipeValidator } from "./RecipeForm.validator";

const RecipeForm = ({recipe = {}, createRecipe, slugRecipe, setSlugRecipe}) => {
  const [recipeState, setRecipeState] = useState({});
  const [listSteps, setListSteps] = useState([{id: 0, description: ''}]);

  const recipeExist = !!slugRecipe && Object.keys(recipe).length > 0 && !!recipe[slugRecipe]._id;

  console.log("!!slugRecipe", !!slugRecipe)
  console.log("Object.keys(recipe).length", Object.keys(recipe).length)

  if(recipeExist && Object.keys(recipeState).length === 0) {
    console.log('if set recipe state')
    console.log(recipe[slugRecipe])
    setRecipeState(recipe[slugRecipe])
  }

  console.log("recipeExist", recipeExist)
  console.log("Object.keys(recipeState)", Object.keys(recipeState))
  console.log("Object.keys(recipeState)", Object.keys(recipeState).length)
  console.log("recipeState", recipeState)

  const onFinish = (values) => {
    console.log("Success:", values);

    if(Object.keys(recipeState).length === 0) {
      const slug = slugify(values.title);
      setSlugRecipe(slug);
      createRecipe({...values, slug});
      return;
    }

    const ingredientsList = omit(values, 'ingredients')
    console.log("ingredientsList:", ingredientsList);
    console.log("values:", values);
    console.log("listSteps:", listSteps);


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
          {/* Temps de préparation */}
          <Col lg={8} md={8} sm={24} xs={24}>
            <Input
              label="Temps de préparation"
              name="preparation_time"
              required={RecipeValidator['preparation_time'].required}
              error={RecipeValidator['preparation_time'].errorMessage}
              placeholder={RecipeValidator['preparation_time'].placeholder}
              addonAfter="min"
            />
          </Col>
          {/* Temps de cuisson */}
          <Col lg={8} md={8} sm={24} xs={24}>
            <Input
              label="Temps de cuisson"
              name="cooking_time"
              required={RecipeValidator['cooking_time'].required}
              error={RecipeValidator['cooking_time'].errorMessage}
              placeholder={RecipeValidator['cooking_time'].placeholder}
              addonAfter="min"
            />
          </Col>
          {/* Nb portions */}
          <Col lg={8} md={8} sm={24} xs={24}>

            <Input
              label="Nombre de portions"
              name="nb_people"
              required={RecipeValidator['nb_people'].required}
              error={RecipeValidator['nb_people'].errorMessage}
              placeholder={RecipeValidator['nb_people'].placeholder}
            />
          </Col>
        </Row>

        {
          recipeExist
          ? ''
          : <Divider><Button type="primary" htmlType="submit">Continuer <i style={{ paddingLeft: '10px' }} className="fas fa-angle-down"></i></Button></Divider>
        }

        <Row gutter={32}>
          {/* Ingrédients */}
          <Col lg={10} md={12} sm={24} xs={24}>
            <RecipeIngredientsForm
              //disabled={!recipeExist}
              _id_recipe={recipe._id}/>
          </Col>
          {/* Steps */}
          <Col lg={14} md={12} sm={24} xs={24}>
            <RecipeStepForm disabled={!recipeExist} _id_recipe={recipe._id} listSteps={listSteps} setListSteps={setListSteps}/>
          </Col>
        </Row>

        <Row style={{ justifyContent: 'flex-end' }}>
          <Button
            type="primary"
            htmlType="submit"
            // disabled={!recipeExist}
          >
            Ajoutée la recette
          </Button>
        </Row>
      </Form>
    </>
  );
};

export default RecipeForm;
