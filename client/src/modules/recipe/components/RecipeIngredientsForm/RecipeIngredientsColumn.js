import React from "react"
import { Select, Button, Input } from 'antd'

import { RecipeIngredientsValidator } from "./RecipeIngredientsForm.validator";

export const columns = (
  disabled,
  handleSearch,
  handleChange,
  addIngredient,
  removeIngredient,
  optionsNameIngredients,
  lineIngredient
) => {
  const {quantity, unit, name} = lineIngredient

  return [
    {
      title: (
        <>
          <label>Nom</label>
          <Select
            showSearch
            placeholder={"Ajouter un ingrédient"}
            style={{ minWidth: '220px' }}
            defaultActiveFirstOption={false}
            showArrow={false}
            filterOption={false}
            onSearch={handleSearch}
            notFoundContent={null}
            onSelect={(value) => handleChange(value, '_id_ingredient')}
            value={name}
            disabled={disabled}
          >
            {optionsNameIngredients}
          </Select>
        </>
      ),
      dataIndex: 'name',
      key: 'name',
    },
    {
      title: (
        <>
          <label>Quantité</label>
          <Input
            name="quantity"
            placeholder={RecipeIngredientsValidator['quantity'].placeholder}
            onChange={(e) => handleChange(e.target.value, 'quantity')}
            value={quantity}
            disabled={disabled}
          />
        </>
      ),
      dataIndex: 'quantity',
      key: 'quantity',
    },
    {
      title: (
        <>
          <label>Unité</label>
          <Input
            label="Unité"
            name="unity"
            placeholder={RecipeIngredientsValidator['unity'].placeholder}
            onChange={(e) => handleChange(e.target.value, 'unit')}
            value={unit}
            disabled={disabled}
          />
        </>
      ),
      dataIndex: 'unity',
      key: 'unity',
    },
    {
      title: (
        <div style={{ marginTop: '22px'}}>
          <Button disabled={disabled} type="primary" htmlType="button" onClick={addIngredient}>
            <i className="fas fa-plus"></i>
          </Button>
        </div>
      ),
      key: 'id',
      dataIndex: 'id',
      render: id => (
        <Button key={id} htmlType="button" ghost onClick={() => removeIngredient(id)} className='button_remove'>
          <i className="fas fa-trash"></i>
        </Button>
      )
    },
  ]
};
