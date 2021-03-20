import React, { useState } from 'react'
import PropTypes from 'prop-types'
import { Form, Button, Row, Col, Divider, Space, Collapse } from 'antd'

import { Input } from 'components/Form/Input.component'

import { CheckboxWithImage } from 'components/Form/CheckboxWithImage.component'
import { categories } from 'constants/categories.constants'
import { slugify } from 'constants/functions.constants'

import RecipeIngredientsForm from '../RecipeIngredientsForm'
import RecipeStepForm from '../RecipeStepForm'
import { RecipeValidator } from './RecipeForm.validator'

import './_RecipeForm.scss'

const RecipeForm = ({ sendRecipe, values }) => {
  const [listSteps, setListSteps] = useState(values.steps)
  const [formRecipe] = Form.useForm()

  const validateForm = state => {
    formRecipe.setFieldsValue({ status: state })
    formRecipe.submit()
  }

  const onFinish = values => {
    const slug = slugify(values.title)
    sendRecipe({ ...values, slug, steps: listSteps })
  }

  return (
    <>
      <Form layout="vertical" form={formRecipe} onFinish={onFinish} initialValues={values}>
        <Collapse defaultActiveKey={['Informations']} expandIconPosition="right" className="FormRecipe_collapse">
          <Collapse.Panel
            header={
              <>
                <h3>Informations</h3>
              </>
            }
            key="Informations"
            className="FormRecipe_panel"
          >
            {/* _id */}
            <Input name="_id" hidden={true} />
            {/* Titre de la recette */}
            <Input
              label="Titre de la recette"
              name="title"
              required={RecipeValidator['title'].required}
              error={RecipeValidator['title'].errorMessage}
              placeholder={RecipeValidator['title'].placeholder}
            />
            {/* Status */}
            <Input name="status" hidden={true} />

            {/* Temps préparation / temps cuisson / portions */}
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
                  addonAfter="portion(s)"
                />
              </Col>
            </Row>

            {/* Catégories + images */}
            <Row gutter="32">
              <Col lg={24} md={24} sm={24} xs={24}>
                {/* Catégories */}
                <CheckboxWithImage label="Catégories" name="categories" datas={categories} />
              </Col>
            </Row>
          </Collapse.Panel>
        </Collapse>
        <Divider />

        <Row gutter={24}>
          {/* Ingrédients */}
          <Col lg={12} md={12} sm={24} xs={24} className="RecipeIngredientsForm">
            <RecipeIngredientsForm ingredientsRecipe={values.ingredients} />
          </Col>

          {/* Steps */}
          <Col lg={12} md={12} sm={24} xs={24} style={{ borderLeft: '1px solid var(--grey-border)' }}>
            <RecipeStepForm listSteps={listSteps} setListSteps={setListSteps} />
          </Col>
        </Row>

        <Row style={{ justifyContent: 'center', marginTop: '45px' }}>
          <Space>
            <Button type="default" size="large" htmlType="button" onClick={() => validateForm('in_progress')}>
              Sauvegarder la recette
            </Button>
            <Button type="primary" size="large" htmlType="button" onClick={() => validateForm('finished')}>
              Publier la recette sur le site
            </Button>
          </Space>
        </Row>
      </Form>
    </>
  )
}

RecipeForm.propTypes = {
  sendRecipe: PropTypes.func,
  values: PropTypes.object,
}

export default RecipeForm
