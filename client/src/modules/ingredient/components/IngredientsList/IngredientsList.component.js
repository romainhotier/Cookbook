import React from 'react'
import { Table, Button } from 'antd'

const columns = [
  {
    title: 'Ingrédients',
    dataIndex: 'name',
    key: 'name',
  },
  {
    title: 'Groupe alimentaire',
    dataIndex: 'categories',
    key: 'categories',
  },
  {
    title: 'Calories (100gr)',
    dataIndex: 'calories',
    key: 'calories',
  },
  {
    title: 'Protéines (gr)',
    dataIndex: 'prot',
    key: 'prot',
  },
  {
    title: 'Glucides (gr)',
    dataIndex: 'glucide',
    key: 'glucide',
  },
  {
    title: 'Lipides (gr)',
    dataIndex: 'lipide',
    key: 'lipide',
  },
  {
    title: '',
    dataIndex: 'action',
    key: 'action',
    width: '12%',
    render(action, record) {
      return (
        <div style={{ display: 'flex', justifyContent: 'space-around', width: '100%' }}>
          <Button>
            <i className="fas fa-pen"></i>
          </Button>
          <Button>
            <i className="fas fa-trash-alt"></i>
          </Button>
        </div>
      )
    },
  },
]

const IngredientsList = ({ data }) => {
  return <Table columns={columns} dataSource={data} rowKey={record => record._id} />
}

export default IngredientsList
