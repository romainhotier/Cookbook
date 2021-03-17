import React from 'react'
import { Table } from 'antd'
import PropTypes from 'prop-types'

import { IngredientsListColumns } from './ingredientsList.columns'

const IngredientsList = ({ data, deleteIngredient, searchIngredients }) => (
  <Table
    columns={IngredientsListColumns(deleteIngredient, searchIngredients)}
    dataSource={data}
    rowKey={record => record._id}
  />
)

IngredientsList.propTypes = {
  data: PropTypes.array,
  deleteIngredient: PropTypes.func,
  searchIngredients: PropTypes.func,
}

export default IngredientsList
