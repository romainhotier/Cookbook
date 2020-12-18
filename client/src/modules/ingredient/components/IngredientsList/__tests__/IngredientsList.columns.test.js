import React from 'react'
import { Tag } from 'antd'

import { IngredientsListColumns } from '../ingredientsList.columns'
import { ingredient, ingredientEmpty } from 'modules/ingredient/__mocks__/ingredients.mock'

describe('IngredientsListColumns', () => {
  it('should columns are goods', () => {
    const buildColumns = IngredientsListColumns()

    expect(buildColumns[0].dataIndex).toEqual('icon')

    expect(buildColumns[1].dataIndex).toEqual('name')

    expect(buildColumns[2].dataIndex).toEqual('categories')
    expect(buildColumns[2].render(['Farines'])).toEqual([<Tag key={'Farines'}>{'Farines'}</Tag>])

    expect(buildColumns[3].title).toEqual('Nutriments')

    const childrenColumn = buildColumns[3].children

    expect(childrenColumn[0].dataIndex).toEqual('unit')
    expect(childrenColumn[0].render('ml')).toEqual('Pour 100 ml :')
    expect(childrenColumn[0].render()).toEqual('Pour 100 g :')

    expect(childrenColumn[1].dataIndex).toEqual('calories')
    expect(childrenColumn[1].render('', ingredient)).toEqual('89 cal')
    expect(childrenColumn[1].render('', ingredientEmpty)).toEqual('-')

    expect(childrenColumn[2].dataIndex).toEqual('proteins')
    expect(childrenColumn[2].render('', ingredient)).toEqual('1.1 g')
    expect(childrenColumn[2].render('', ingredientEmpty)).toEqual('-')

    expect(childrenColumn[3].dataIndex).toEqual('carbohydrates')
    expect(childrenColumn[3].render('', ingredient)).toEqual('23 g')
    expect(childrenColumn[3].render('', ingredientEmpty)).toEqual('-')

    expect(childrenColumn[4].dataIndex).toEqual('fats')
    expect(childrenColumn[4].render('', ingredient)).toEqual('0.3 g')
    expect(childrenColumn[4].render('', ingredientEmpty)).toEqual('-')

    expect(childrenColumn[5].dataIndex).toEqual('portion')
    expect(childrenColumn[5].render('', ingredient)).toEqual('120 g')
    expect(childrenColumn[5].render('', ingredientEmpty)).toEqual('-')

    expect(buildColumns[4].dataIndex).toEqual('action')

    const ActionColumn = buildColumns[4].render('', ingredient)

    expect(ActionColumn).toBeDefined()
  })
})
