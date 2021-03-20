import get from 'lodash/get'
import { codeMsg } from '../codeMsg.constants'
import { slugifyResponse } from '../functions.constants'

describe('codeMsg.constants', () => {
  const firstResponse = {
    codeMsg: 'cookbook.recipe.error.bad_request',
    detail: {
      msg: 'already exist',
    },
  }
  it('should render good message', () => {
    const message = get(codeMsg, `${firstResponse.codeMsg}.${slugifyResponse(firstResponse.detail.msg)}`)
    expect(message('pancakes')).toEqual(`La recette "pancakes" existe déjà.`)
  })

  const secondResponse = {
    codeMsg: 'cookbook.ingredient.error.bad_request',
    detail: {
      msg: 'already exist',
    },
  }
  it('should render good message', () => {
    const message = get(codeMsg, `${secondResponse.codeMsg}.${slugifyResponse(secondResponse.detail.msg)}`)
    expect(message('beurre')).toEqual(`L'ingrédient "beurre" existe déjà.`)
  })
})
