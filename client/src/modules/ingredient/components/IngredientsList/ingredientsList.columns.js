import React from 'react'
import PropTypes from 'prop-types'
import { Button, Popover, Tag, Space } from 'antd'

import TableTitleWithSearch from 'components/TableTitleWithSearch'
import IngredientModalEdit from 'modules/ingredient/containers/IngredientModalEdit'
import { searchInListIcons } from 'constants/functions.constants'

const contentPopover = (deleteIngredient, id) => (
  <div style={{ textAlign: 'center' }}>
    Êtes-vous sur de vouloir supprimer cet ingrédient ?
    <br />
    <Space style={{ marginTop: '20px' }}>
      <Button onClick={() => deleteIngredient(id)} htmlType="button">
        Oui !
      </Button>
    </Space>
  </div>
)

contentPopover.propTypes = {
  deleteIngredient: PropTypes.func,
  id: PropTypes.string,
}

export const IngredientsListColumns = (deleteIngredient, searchIngredients) => [
  {
    title: '',
    dataIndex: 'icon',
    key: 'icon',
    align: 'left',
    render: (_text, { slug, name }) => <img src={searchInListIcons(slug)} alt={name} width="40" height="40" />,
  },
  {
    title: TableTitleWithSearch({
      title: 'Ingrédients',
      placeholder: 'Rechercher un ingrédient..',
      filterName: 'name',
      onChange: (filter, value) => (value.length === 0 ? searchIngredients() : searchIngredients({ [filter]: value })),
    }),
    dataIndex: 'name',
    key: 'name',
    align: 'left',
    width: 270,
    sorter: (a, b) => a.name.localeCompare(b.name),
  },
  {
    title: 'Groupe alternatif',
    dataIndex: 'categories',
    key: 'categories',
    align: 'center',
    responsive: ['lg'],
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
        responsive: ['lg'],
        render: unit => `Pour 100 ${unit ?? 'g'} :`,
      },
      {
        title: 'Calories',
        dataIndex: 'calories',
        key: 'calories',
        align: 'center',
        sorter: (a, b) => parseInt(a.nutriments.calories) - parseInt(b.nutriments.calories),
        render: (_text, { nutriments }) => (nutriments.calories ? `${nutriments.calories} cal` : '-'),
      },
      {
        title: 'Protéines',
        dataIndex: 'proteins',
        key: 'proteins',
        align: 'center',
        sorter: (a, b) => parseInt(a.nutriments.proteins) - parseInt(b.nutriments.proteins),
        render: (_text, { nutriments }) => (nutriments.proteins ? `${nutriments.proteins} g` : '-'),
      },
      {
        title: 'Glucides',
        dataIndex: 'carbohydrates',
        key: 'carbohydrates',
        align: 'center',
        sorter: (a, b) => parseInt(a.nutriments.carbohydrates) - parseInt(b.nutriments.carbohydrates),
        render: (_text, { nutriments }) => (nutriments.carbohydrates ? `${nutriments.carbohydrates} g` : '-'),
      },
      {
        title: 'Lipides',
        dataIndex: 'fats',
        key: 'fats',
        align: 'center',
        sorter: (a, b) => parseInt(a.nutriments.fats) - parseInt(b.nutriments.fats),
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

IngredientsListColumns.propTypes = {
  deleteIngredient: PropTypes.func,
  searchIngredients: PropTypes.func,
}
