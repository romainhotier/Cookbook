import React, { useState } from 'react'
import { Button, Form, Row, Col } from 'antd'
import PropTypes from 'prop-types'

import { slugify } from 'constants/functions.constants'
import { Input } from 'components/Form/Input.component'
import { Select } from 'components/Form/Select.component'
import { IngredientValidator } from './IngredientForm.validator'

const IngredientForm = ({ createIngredient, loading, updateIngredient, values = { unit: 'g' } }) => {
  const [form] = Form.useForm()
  const [unitPortion, setUnitPortion] = useState(values.unit)

  const onReset = () => {
    form.resetFields()
  }

  const handleChange = changedFields => {
    if (changedFields.length === 0) {
      return
    }
    const { name, value } = changedFields[0]
    if (name[0] === 'unit') {
      setUnitPortion(value)
    }
  }

  const onFinish = values => {
    const nutriments = values.calories
      ? {
          nutriments: {
            calories: values.calories,
            proteins: values.proteins,
            carbohydrates: values.carbohydrates,
            fats: values.fats,
            portion: values.portion ? values.portion : 0,
          },
        }
      : {}

    const ingredient = {
      name: values.name,
      slug: slugify(values.name),
      categories: values.categories && values.categories.length > 0 ? values.categories.toString().split(',') : [''],
      unit: values.unit,
      ...nutriments,
    }

    onReset()

    if (values._id) {
      return updateIngredient({ id: values._id, data: { _id: values._id, ...ingredient } })
    }

    createIngredient(ingredient)
  }

  return (
    <Form
      name="IngredientPageAdd"
      form={form}
      layout="vertical"
      onFinish={onFinish}
      initialValues={values}
      onFieldsChange={handleChange}
    >
      <Input hidden={true} name="_id" style={{ hidden: 0, display: 'none' }} />
      <Row gutter={32}>
        <Col span={12}>
          <Input
            label="Nom de l'ingrédient"
            name="name"
            required={IngredientValidator['name'].required}
            error={IngredientValidator['name'].errorMessage}
            placeholder={IngredientValidator['name'].placeholder}
          />
        </Col>
        <Col span={12}>
          <Input
            label="Groupe alimentaire"
            name="categories"
            required={IngredientValidator['categories'].required}
            error={IngredientValidator['categories'].errorMessage}
            placeholder={IngredientValidator['categories'].placeholder}
          />
        </Col>
      </Row>

      <Row gutter={32}>
        <Col span={12}>
          <Select
            label="Unité"
            name="unit"
            required={IngredientValidator['unit'].required}
            error={IngredientValidator['unit'].errorMessage}
            placeholder={IngredientValidator['unit'].placeholder}
            options={[
              { value: 'g', label: 'Pour 100 grammes' },
              { value: 'ml', label: 'Pour 100 millilitres' },
            ]}
          />
        </Col>
        <Col span={12}>
          <Input
            label="Portion"
            name="portion"
            required={IngredientValidator['portion'].required}
            error={IngredientValidator['portion'].errorMessage}
            placeholder={IngredientValidator['portion'].placeholder}
            suffix={unitPortion}
          />
        </Col>
      </Row>

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
            label="Protéines"
            name="proteins"
            required={IngredientValidator['proteins'].required}
            error={IngredientValidator['proteins'].errorMessage}
            placeholder={IngredientValidator['proteins'].placeholder}
            suffix={'g'}
          />
        </Col>
        <Col span={6}>
          <Input
            label="Glucides"
            name="carbohydrates"
            required={IngredientValidator['carbohydrates'].required}
            error={IngredientValidator['carbohydrates'].errorMessage}
            placeholder={IngredientValidator['carbohydrates'].placeholder}
            suffix={'g'}
          />
        </Col>
        <Col span={6}>
          <Input
            label="Lipides"
            name="fats"
            required={IngredientValidator['fats'].required}
            error={IngredientValidator['fats'].errorMessage}
            placeholder={IngredientValidator['fats'].placeholder}
            suffix={'g'}
          />
        </Col>
      </Row>
      <Form.Item style={{ textAlign: 'right' }}>
        <Button type="primary" htmlType="submit" loading={loading} disabled={loading}>
          {values._id ? 'Modifier' : 'Créer'}
        </Button>
      </Form.Item>
    </Form>
  )
}

IngredientForm.propTypes = {
  values: PropTypes.object,
  loading: PropTypes.bool,
  createIngredient: PropTypes.func,
  updateIngredient: PropTypes.func,
}

export default IngredientForm
