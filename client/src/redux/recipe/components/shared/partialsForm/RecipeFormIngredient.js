import React from 'react'
import { Field, FieldArray } from 'formik'
import { Icon, Button } from 'antd'

const recipeFormIngredient = ({ ingredients, handleChange }) => {
  return (
    <>
      <h4>Liste des ingredients</h4>
      <div className="form_block form_list_ingredients">
        <FieldArray
          name="ingredients"
          render={(arrayHelpers) => (
            <>
              {ingredients.length > 0 ? (
                ingredients.map((attribute, index) => (
                  <div className="form_inline" key={index}>
                    <div className="form_inline_element">
                      <label className="form_label" htmlFor={`ingredients[${index}]name`}>
                        Nom
                      </label>
                      <Field
                        type="text"
                        className="ant-input form_element"
                        value={attribute.name}
                        id={`ingredients[${index}]name`}
                        name={`ingredients[${index}]name`}
                        onChange={handleChange}
                        placeholder="Nom"
                      />
                    </div>
                    <div className="form_inline_element">
                      <label className="form_label" htmlFor={`ingredients[${index}]quantity`}>
                        Quantité
                      </label>
                      <Field
                        type="text"
                        className="ant-input form_element"
                        value={attribute.quantity}
                        id={`ingredients[${index}]quantity`}
                        name={`ingredients[${index}]quantity`}
                        onChange={handleChange}
                        placeholder="Nom"
                      />
                    </div>
                    <div className="form_inline_element">
                      <label className="form_label" htmlFor={`ingredients[${index}]unity`}>
                        Unité
                      </label>
                      <Field
                        type="text"
                        className="ant-input form_element"
                        value={attribute.unity}
                        id={`ingredients[${index}]unity`}
                        name={`ingredients[${index}]unity`}
                        onChange={handleChange}
                        placeholder="Unité"
                      />
                    </div>
                    <div className="form_inline_element">
                      <Button
                        type="danger"
                        className="form_inline_element"
                        onClick={() => arrayHelpers.remove(index)}
                      >
                        <Icon type="delete" />
                      </Button>
                    </div>
                  </div>
                ))
              ) : ''}
              <Button
                className="form_button form_button_addIngredient"
                onClick={() => arrayHelpers.push({ name: '', quantity: '', unity: '' })}
              >
                Ajouter
              </Button>
            </>
          )}
        />
      </div>
    </>
  )
}

export default recipeFormIngredient
