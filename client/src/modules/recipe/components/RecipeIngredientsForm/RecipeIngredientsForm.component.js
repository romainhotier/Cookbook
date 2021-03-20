import React from 'react'
import PropTypes from 'prop-types'
import { Select, Form, Input, Button, Collapse } from 'antd'

import { RecipeIngredientsValidator } from './RecipeIngredientsForm.validator'
import IngredientModalAdd from 'modules/ingredient/containers/IngredientModalAdd'

import './_RecipeIngredientsForm.scss'

export const RecipeIngredientsFormComponent = ({ options, handleSearch, handleChange, createUnitOption }) => (
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
        <IngredientModalAdd className="ingredientsForm_buttonModal" type="link" contentButton={'Créer un ingrédient'} />
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
                      onSearch={handleSearch}
                      onChange={handleChange}
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
                      {createUnitOption(field.name)}
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

RecipeIngredientsFormComponent.propTypes = {
  options: PropTypes.array,
  handleSearch: PropTypes.func,
  handleChange: PropTypes.func,
  createUnitOption: PropTypes.func,
}
