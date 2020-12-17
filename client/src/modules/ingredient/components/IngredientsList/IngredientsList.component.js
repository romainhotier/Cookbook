import React from 'react'
import { Table, Button, Popover, Space, Tag } from 'antd'
import PropTypes from 'prop-types'

import IngredientModalEdit from 'modules/ingredient/containers/IngredientModalEdit'

const contentPopover = (deleteIngredient, _id) => (
  <div style={{ textAlign: 'center' }}>
    Êtes-vous sur de vouloir supprimer cet ingrédient ?
    <br />
    <Space style={{ marginTop: '20px' }}>
      <Button onClick={() => deleteIngredient(_id)} htmlType="button">
        Oui !
      </Button>
    </Space>
  </div>
)
const columns = deleteIngredient => [
  {
    title: '',
    dataIndex: 'icon',
    key: 'icon',
    align: 'left',
  },
  {
    title: 'Ingrédients',
    dataIndex: 'name',
    key: 'name',
    align: 'left',
  },
  {
    title: 'Groupe alternatif',
    dataIndex: 'categories',
    key: 'categories',
    align: 'center',
    render: categories => categories.map(elem => <Tag key={elem}>{elem}</Tag>),
  },
  {
    title: 'Nutriments',
    children: [
      {
        title: '',
        dataIndex: 'unit',
        key: 'unit',
        align: 'right',
        render: unit => `Pour 100 ${unit ?? 'g'} :`,
      },
      {
        title: 'Calories',
        dataIndex: 'calories',
        key: 'calories',
        align: 'center',
        render: (_text, { nutriments }) => (nutriments.calories ? `${nutriments.calories} cal` : '-'),
      },
      {
        title: 'Protéines',
        dataIndex: 'proteins',
        key: 'proteins',
        align: 'center',
        render: (_text, { nutriments }) => (nutriments.proteins ? `${nutriments.proteins} g` : '-'),
      },
      {
        title: 'Glucides',
        dataIndex: 'carbohydrates',
        key: 'carbohydrates',
        align: 'center',
        render: (_text, { nutriments }) => (nutriments.carbohydrates ? `${nutriments.carbohydrates} g` : '-'),
      },
      {
        title: 'Lipides',
        dataIndex: 'fats',
        key: 'fats',
        align: 'center',
        render: (_text, { nutriments }) => (nutriments.fats ? `${nutriments.fats} g` : '-'),
      },
      {
        title: '1 portion',
        dataIndex: 'portion',
        key: 'portion',
        align: 'center',
        render: (_text, { nutriments }) =>
          nutriments.portion && nutriments.portion !== '0' ? `${nutriments.portion} g` : '-',
      },
    ],
  },
  {
    title: '',
    dataIndex: 'action',
    key: 'action',
    width: '12%',
    render(action, record) {
      const { nutriments } = record
      const editableValues = { ...record, ...nutriments }
      return (
        <div style={{ display: 'flex', justifyContent: 'space-around', width: '100%' }}>
          <IngredientModalEdit values={editableValues} contentButton={<i className="fas fa-pen"></i>} />
          <Popover placement="top" content={contentPopover(deleteIngredient, record._id)} trigger="click">
            <Button>
              <i className="fas fa-trash-alt"></i>
            </Button>
          </Popover>
        </div>
      )
    },
  },
]

const IngredientsList = ({ data, deleteIngredient }) => {
  return <Table columns={columns(deleteIngredient)} dataSource={data} rowKey={record => record._id} />
}

IngredientsList.propTypes = {
  data: PropTypes.array,
  editIngredient: PropTypes.func,
  deleteIngredient: PropTypes.func,
}

export default IngredientsList
