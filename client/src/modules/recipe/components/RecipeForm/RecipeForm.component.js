import React, { useState } from 'react'
import { Form, Button, Row, Col, Divider, Space } from 'antd'

import { Input } from 'components/Form/Input.component'
import { CheckboxWithImage } from 'components/Form/CheckboxWithImage.component'
import { categories } from 'constants/categories.constants'
import { slugify } from 'constants/functions.constants'

import RecipeIngredientsForm from '../RecipeIngredientsForm'
import RecipeStepForm from '../RecipeStepForm'
import { RecipeValidator } from './RecipeForm.validator'

const RecipeForm = ({ createRecipe }) => {
  const [listSteps, setListSteps] = useState([{ id: 0, description: '' }])
  const [formRecipe] = Form.useForm()

  const validateForm = state => {
    formRecipe.setFieldsValue({ status: state })
    formRecipe.submit()
  }

  const onFinish = values => {
    const slug = slugify(values.title)
    createRecipe({ ...values, slug, steps: listSteps })
  }

  return (
    <>
      <Form layout="vertical" form={formRecipe} onFinish={onFinish} initialValues={{ ingredients: [{}] }}>
        {/* Catégories */}
        <CheckboxWithImage label="Catégories" name="categories" datas={categories} />
        {/* Status */}
        <Input name="status" hidden={true} />
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

        <Divider />

        <Row gutter={32}>
          {/* Ingrédients */}
          <Col lg={12} md={12} sm={24} xs={24}>
            <RecipeIngredientsForm />
          </Col>

          {/* Steps */}
          <Col lg={12} md={12} sm={24} xs={24} style={{ borderLeft: '1px solid rgba(0, 0, 0, 0.06)' }}>
            <RecipeStepForm listSteps={listSteps} setListSteps={setListSteps} />
          </Col>
        </Row>

        <Row style={{ justifyContent: 'center', marginTop: '45px' }}>
          <Space>
            <Button type="default" size="large" htmlType="button" onClick={() => validateForm('in_progress')}>
              Sauvegarder la recette
            </Button>
            <Button type="primary" size="large" htmlType="button" onClick={() => validateForm('finished')}>
              Publier la recette
            </Button>
          </Space>
        </Row>
      </Form>
    </>
  )
}

export default RecipeForm
