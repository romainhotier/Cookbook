import { connect } from 'react-redux'
import React, { Component } from 'react'
import { Select, Form, Input, Button, Spin, Collapse } from 'antd'
import find from 'lodash/find'
import keyBy from 'lodash/keyBy'

import { fetchAllIngredients } from 'modules/ingredient/thunks'
import { RecipeIngredientsValidator } from './RecipeIngredientsForm.validator'
import IngredientModalAdd from 'modules/ingredient/containers/IngredientModalAdd'

import './_RecipeIngredientsForm.scss'

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
          <Select.Option value={ingredient.unit}>{`${ingredient.unit}`}</Select.Option>
          <Select.Option value="portion">
            {`${ingredient.name} soit (${ingredient.nutriments.portion} ${ingredient.unit})`}
          </Select.Option>
        </>
      )
    }
    return (
      <>
        <Select.Option value={ingredient.unit}>{`${ingredient.unit}`}</Select.Option>
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
      <Select.Option key={`researchIngredientsOption-${d._id}`} value={d._id}>
        {d.name}
      </Select.Option>
    ))

    return (
      <Collapse defaultActiveKey={['ingredientForm']} expandIconPosition="right" className="FormRecipe_collapse">
        <Collapse.Panel
          header={
            <div className="ingredientForm_head">
              <h3>Ingrédients</h3>
            </div>
          }
          key="ingredientForm"
          className="FormRecipe_panel"
        >
          <div className="ingredientsForm_buttonModalContainer">
            <IngredientModalAdd
              className="ingredientsForm_buttonModal"
              type="link"
              contentButton={'Vous ne trouvez pas un ingrédient ? Créez le ici !'}
            />
          </div>
          <Form.List name="ingredients">
            {(fields, { add, remove }) => (
              <>
                {fields.map((field, index) => (
                  <div
                    className={`ingredientsForm ingredientsForm-${index % 2 ? 'odd' : 'even'}`}
                    key={`ingredientsForm-${field.key}`}
                  >
                    <div className={'ingredientsForm_row'}>
                      {/* Name */}
                      <Form.Item
                        {...field}
                        key={`fieldName-${field.key}`}
                        name={[field.name, '_id']}
                        fieldKey={[field.fieldKey, '_id']}
                        rules={[
                          {
                            required: RecipeIngredientsValidator['name'].required,
                            message: RecipeIngredientsValidator['name'].errorMessage,
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
                      {/* Quantity */}
                      <Form.Item
                        {...field}
                        className="quantity-form"
                        key={`fieldQuantity-${field.key}`}
                        name={[field.name, 'quantity']}
                        label="Quantité"
                        fieldKey={[field.fieldKey, 'quantity']}
                        rules={[
                          {
                            required: RecipeIngredientsValidator['quantity'].required,
                            message: RecipeIngredientsValidator['quantity'].errorMessage,
                          },
                        ]}
                      >
                        <Input placeholder={RecipeIngredientsValidator['quantity'].placeholder} />
                      </Form.Item>

                      {/* Unity */}
                      <Form.Item
                        {...field}
                        key={`fieldUnit-${field.key}`}
                        name={[field.name, 'unit']}
                        label="Unité"
                        fieldKey={[field.fieldKey, 'unit']}
                        rules={[
                          {
                            required: RecipeIngredientsValidator['unit'].required,
                            message: RecipeIngredientsValidator['unit'].errorMessage,
                          },
                        ]}
                      >
                        <Select placeholder={RecipeIngredientsValidator['unit'].placeholder}>
                          {this.createUnitOption(field.name)}
                        </Select>
                      </Form.Item>

                      {/* Button */}
                      <Button
                        key={`buttonRemoveIngredientsfield-${field.name}`}
                        htmlType="button"
                        type="text"
                        onClick={() => remove(field.name)}
                        className="ingredientsForm_buttonRemove desktopButton"
                      >
                        <i className="fas fa-trash"></i>
                      </Button>
                    </div>
                    <Button
                      key={`buttonRemoveIngredientsfield-${field.name}`}
                      htmlType="button"
                      type="text"
                      size={'large'}
                      onClick={() => remove(field.name)}
                      className="ingredientsForm_buttonRemove mobileButton"
                    >
                      <i className="fas fa-trash"></i>
                    </Button>
                  </div>
                ))}
                <Form.Item style={{ textAlign: 'right' }}>
                  <Button className="ingredientsForm button_add" type="default" onClick={() => add()}>
                    Ajouter un ingrédient à la recette
                  </Button>
                </Form.Item>
              </>
            )}
          </Form.List>
        </Collapse.Panel>
      </Collapse>
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
