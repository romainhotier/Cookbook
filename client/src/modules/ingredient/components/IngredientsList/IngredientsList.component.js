import React from 'react'
import { Table, Button } from 'antd'
import PropTypes from 'prop-types'

const columns = (editIngredient, deleteIngredient) => [
  {
    title: 'Ingrédients',
    dataIndex: 'name',
    key: 'name',
    align: 'center',
  },
  {
    title: 'Groupe alimentaire',
    dataIndex: 'categories',
    key: 'categories',
    align: 'center',
  },
  {
    title: 'Calories (100gr)',
    dataIndex: 'calories',
    key: 'calories',
    align: 'center',
    render: (_text, { nutriments }) => nutriments.calories,
  },
  {
    title: 'Protéines (gr)',
    dataIndex: 'proteins',
    key: 'proteins',
    align: 'center',
    render: (_text, { nutriments }) => nutriments.proteins,
  },
  {
    title: 'Glucides (gr)',
    dataIndex: 'carbohydrates',
    key: 'carbohydrates',
    align: 'center',
    render: (_text, { nutriments }) => nutriments.carbohydrates,
  },
  {
    title: 'Lipides (gr)',
    dataIndex: 'fats',
    key: 'fats',
    align: 'center',
    render: (_text, { nutriments }) => nutriments.fats,
  },
  {
    title: '',
    dataIndex: 'action',
    key: 'action',
    width: '12%',
    render(action, { _id }) {
      return (
        <div style={{ display: 'flex', justifyContent: 'space-around', width: '100%' }}>
          <Button onClick={() => editIngredient(_id)} htmlType="button">
            <i className="fas fa-pen"></i>
          </Button>
          <Button onClick={() => deleteIngredient(_id)} htmlType="button">
            <i className="fas fa-trash-alt"></i>
          </Button>
        </div>
      )
    },
  },
]

const IngredientsList = ({ data, editIngredient, deleteIngredient }) => {
  return <Table columns={columns(editIngredient, deleteIngredient)} dataSource={data} rowKey={record => record._id} />
}

IngredientsList.propTypes = {
  data: PropTypes.array,
  editIngredient: PropTypes.func,
  deleteIngredient: PropTypes.func,
}

export default IngredientsList
