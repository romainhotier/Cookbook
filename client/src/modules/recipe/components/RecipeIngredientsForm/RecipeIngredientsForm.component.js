import { connect } from 'react-redux'
import React, { Component } from 'react'
import { Select, Form, Input, Button, Spin } from 'antd'
import find from 'lodash/find'
import keyBy from 'lodash/keyBy'
import forEach from 'lodash/forEach'

import { fetchAllIngredients } from 'modules/ingredient/thunks'
import { RecipeIngredientsValidator } from './RecipeIngredientsForm.validator'
import IngredientModalAdd from 'modules/ingredient/containers/IngredientModalAdd'

import './_RecipeIngredientsForm.scss'

const { Option } = Select

class RecipeIngredientsForm extends Component {
  constructor(props) {
    super(props)

    this.state = {
      researchIngredients: [],
      selectedIngredients: [],
      initializeComponent: false,
    }
  }

  componentDidMount() {
    this.props.fetchAllIngredients()
  }

  componentDidUpdate(prevProps) {
    const { ingredients, ingredientsRecipe } = this.props
    if (
      (Object.keys(prevProps.ingredients).length === 0 && Object.keys(ingredients).length > 0) ||
      !this.state.initializeComponent
    ) {
      const ingredientsById = keyBy(ingredients, '_id')
      let ingredientsInForm = []
      if (Object.keys(ingredientsRecipe[0]).length > 0) {
        ingredientsInForm = ingredientsRecipe.map(elem => ingredientsById[elem._id])
      }

      this.setState({
        researchIngredients: Object.values(ingredients),
        selectedIngredients: ingredientsInForm,
        initializeComponent: true,
      })
    }
  }

  handleSearch = value => {
    const { ingredients } = this.props
    if (value) {
      const valueLowerCase = value.toLowerCase()
      const filters = Object.values(ingredients).filter(({ name = '' }) => {
        const nameLowercase = name.toLowerCase()
        return nameLowercase.search(valueLowerCase) > -1
      })
      this.setState({ researchIngredients: filters })
    }
  }

  handleChange = value => {
    const { ingredients } = this.props

    const ingSelected = find(ingredients, ing => ing._id === value)
    this.setState({ selectedIngredients: [...this.state.selectedIngredients, ingSelected] })
  }

  createUnitOption = index => {
    const ingredient = this.state.selectedIngredients[index]

    if (!ingredient) {
      return
    }

    if (parseInt(ingredient.nutriments.portion) > 1) {
      return (
        <>
          <Option value={ingredient.unit}>{`${ingredient.unit}`}</Option>
          <Option value="portion">
            {`${ingredient.name} soit (${ingredient.nutriments.portion} ${ingredient.unit})`}
          </Option>
        </>
      )
    }
    return (
      <>
        <Option value={ingredient.unit}>{`${ingredient.unit}`}</Option>
      </>
    )
  }

  render() {
    const { ingredients } = this.props
    const { researchIngredients } = this.state

    if (Object.entries(ingredients).length === 0) {
      return <Spin />
    }

    const options = researchIngredients.map(d => (
      <Option key={`researchIngredientsOption-${d._id}`} value={d._id}>
        {d.name}
      </Option>
    ))

    return (
      <>
        <div className="ingredientForm_head">
          <h2>Ingrédients</h2>
          <IngredientModalAdd
            contentButton={<i className="fas fa-plus"></i>}
            shapeButton="circle"
            sizeButton={'small'}
          />
        </div>

        <Form.List name="ingredients">
          {(fields, { add, remove }) => (
            <>
              {fields.map(field => (
                <div className="IngredientsForm" key={`IngredientsForm-${field.key}`}>
                  <div>
                    <Form.Item
                      {...field}
                      key={`fieldName-${field.key}`}
                      name={[field.name, '_id']}
                      fieldKey={[field.fieldKey, '_id']}
                      rules={[
                        {
                          required: RecipeIngredientsValidator['name'].required,
                          message: RecipeIngredientsValidator['name'].message,
                        },
                      ]}
                      label="Nom"
                    >
                      <Select
                        showSearch
                        placeholder={RecipeIngredientsValidator['name'].placeholder}
                        defaultActiveFirstOption={true}
                        showArrow={false}
                        filterOption={false}
                        onSearch={this.handleSearch}
                        onChange={this.handleChange}
                        notFoundContent={null}
                      >
                        {options}
                      </Select>
                    </Form.Item>
                    <Form.Item
                      {...field}
                      key={`fieldquantity-${field.key}`}
                      name={[field.name, 'quantity']}
                      label="Quantité"
                      fieldKey={[field.fieldKey, 'quantity']}
                      rules={[
                        {
                          required: RecipeIngredientsValidator['quantity'].required,
                          message: RecipeIngredientsValidator['quantity'].message,
                        },
                      ]}
                    >
                      <Input placeholder={RecipeIngredientsValidator['quantity'].placeholder} />
                    </Form.Item>

                    <Form.Item
                      {...field}
                      key={`fieldunit-${field.key}`}
                      name={[field.name, 'unit']}
                      label="Unité"
                      fieldKey={[field.fieldKey, 'unit']}
                      rules={[
                        {
                          required: RecipeIngredientsValidator['unit'].required,
                          message: RecipeIngredientsValidator['unit'].message,
                        },
                      ]}
                    >
                      <Select placeholder={RecipeIngredientsValidator['unit'].placeholder}>
                        {this.createUnitOption(field.name)}
                      </Select>
                    </Form.Item>
                  </div>
                  <Button
                    key={`buttonRemoveIngredientsfield-${field.name}`}
                    htmlType="button"
                    type="text"
                    onClick={() => remove(field.name)}
                    className="button_remove"
                  >
                    <i className="fas fa-trash"></i>
                  </Button>
                </div>
              ))}
              <Form.Item style={{ textAlign: 'right' }}>
                <Button type="default" onClick={() => add()}>
                  Ajouter un ingrédient
                </Button>
              </Form.Item>
            </>
          )}
        </Form.List>
      </>
    )
  }
}

const mapDispatchToProps = {
  fetchAllIngredients,
}

const mapStateToProps = ({ ingredients: { content, loadingFetchIngredients } }) => ({
  ingredients: content,
  loadingFetchIngredients,
})

export default connect(mapStateToProps, mapDispatchToProps)(RecipeIngredientsForm)
