import React from 'react'
import { Button, Form, Row, Col } from 'antd'

import { slugify } from 'constants/functions.constants'
import { Input } from 'components/Form/Input.component'
import { IngredientValidator } from './IngredientForm.validator'

const IngredientForm = ({ createIngredient, loading, updateIngredient, values = {} }) => {
  const [form] = Form.useForm()

  const onReset = () => {
    form.resetFields()
  }

  const onFinish = values => {
    const nutriments = values.calories
      ? {
          nutriments: {
            calories: values.calories,
            proteins: values.proteins,
            carbohydrates: values.carbohydrates,
            fats: values.fats,
          },
        }
      : {}

    const ingredient = {
      name: values.name,
      slug: slugify(values.name),
      categories: [values.categories],
      ...nutriments,
    }

    onReset()

    if (!!values._id) {
      return updateIngredient({ _id: values._id, ...ingredient })
    }

    createIngredient(ingredient)
  }

  return (
    <Form name="IngredientPageAdd" form={form} layout="vertical" onFinish={onFinish} initialValues={values}>
      <Input hidden={true} name="_id" style={{ hidden: 0, display: 'none' }} />
      <Input
        label="Nom de l'ingrédient"
        name="name"
        required={IngredientValidator['name'].required}
        error={IngredientValidator['name'].errorMessage}
        placeholder={IngredientValidator['name'].placeholder}
      />
      <Input
        label="Groupe alimentaire"
        name="categories"
        required={IngredientValidator['categories'].required}
        error={IngredientValidator['categories'].errorMessage}
        placeholder={IngredientValidator['categories'].placeholder}
      />

      <Row gutter={32}>
        <Col span={6}>
          <Input
            label="Nombre de calories"
            name="calories"
            required={IngredientValidator['calories'].required}
            error={IngredientValidator['calories'].errorMessage}
            placeholder={IngredientValidator['calories'].placeholder}
          />
        </Col>
        <Col span={6}>
          <Input
            label="Protéine"
            name="proteins"
            required={IngredientValidator['proteins'].required}
            error={IngredientValidator['proteins'].errorMessage}
            placeholder={IngredientValidator['proteins'].placeholder}
          />
        </Col>
        <Col span={6}>
          <Input
            label="Glucide"
            name="carbohydrates"
            required={IngredientValidator['carbohydrates'].required}
            error={IngredientValidator['carbohydrates'].errorMessage}
            placeholder={IngredientValidator['carbohydrates'].placeholder}
          />
        </Col>
        <Col span={6}>
          <Input
            label="Lipide"
            name="fats"
            required={IngredientValidator['fats'].required}
            error={IngredientValidator['fats'].errorMessage}
            placeholder={IngredientValidator['fats'].placeholder}
          />
        </Col>
      </Row>
      <Form.Item style={{ textAlign: 'right' }}>
        <Button type="primary" htmlType="submit" loading={loading} disabled={loading}>
          Créer
        </Button>
      </Form.Item>
    </Form>
  )
}

export default IngredientForm
