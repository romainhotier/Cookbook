import React from 'react'
import { shallow } from 'enzyme'
import { List } from 'immutable'

import { RecipeIngredientsForm } from '../RecipeIngredientsForm.container'
import { recipes } from 'modules/recipe/mocks/recipes.mock'
import { ingredientsList } from 'modules/ingredient/mocks/ingredients.mock'

describe('RecipeIngredientsForm.container', () => {
  it('should render Spin', () => {
    const wrapper = shallow(
      <RecipeIngredientsForm ingredientsList={List([])} ingredientsRecipe={[]} fetchAllIngredients={jest.fn()} />
    )

    expect(wrapper.find('Spin').length).toEqual(1)
  })

  it('should render RecipeIngredientsFormComponent', () => {
    const wrapper = shallow(
      <RecipeIngredientsForm
        ingredientsList={List(ingredientsList)}
        ingredientsRecipe={[]}
        fetchAllIngredients={jest.fn()}
      />
    )

    expect(wrapper.find('RecipeIngredientsFormComponent').length).toEqual(1)
  })

  it('should handleSearch change researchIngredients state', () => {
    const wrapper = shallow(
      <RecipeIngredientsForm
        ingredientsList={List(ingredientsList)}
        ingredientsRecipe={recipes.content[0].ingredients}
        fetchAllIngredients={jest.fn()}
      />
    )

    expect(wrapper.find('RecipeIngredientsFormComponent').length).toEqual(1)
    expect(wrapper.state().researchIngredients).toMatchObject([])

    wrapper.find('RecipeIngredientsFormComponent').props().handleSearch('ban')

    expect(wrapper.state().researchIngredients).toMatchObject([
      {
        _id: '5fdb8dbdc0749c35c039b43f',
        name: 'Banane',
        nutriments: {
          calories: '89',
          carbohydrates: '23',
          fats: '0.3',
          portion: '120',
          proteins: '1.1',
        },
        slug: 'banane',
        unit: 'g',
      },
      {
        _id: '6gtr48dc0749c35c039b43f',
        name: 'Farine',
        nutriments: {
          calories: '89',
          carbohydrates: '23',
          fats: '0.3',
          portion: '120',
          proteins: '1.1',
        },
        slug: 'farine',
        unit: 'g',
      },
    ])
  })

  it('should handleChange change selectedIngredients state', () => {
    const wrapper = shallow(
      <RecipeIngredientsForm
        ingredientsList={List(ingredientsList)}
        ingredientsRecipe={recipes.content[0].ingredients}
        fetchAllIngredients={jest.fn()}
      />
    )

    expect(wrapper.find('RecipeIngredientsFormComponent').length).toEqual(1)
    expect(wrapper.state().selectedIngredients).toMatchObject([])

    wrapper.find('RecipeIngredientsFormComponent').props().handleChange('5fdb8dbdc0749c35c039b43f')

    expect(wrapper.state().selectedIngredients).toMatchObject([
      {
        _id: '5fdb8dbdc0749c35c039b43f',
        name: 'Banane',
        nutriments: {
          calories: '89',
          carbohydrates: '23',
          fats: '0.3',
          portion: '120',
          proteins: '1.1',
        },
        slug: 'banane',
        unit: 'g',
      },
      {
        _id: '6gtr48dc0749c35c039b43f',
        name: 'Farine',
        nutriments: {
          calories: '89',
          carbohydrates: '23',
          fats: '0.3',
          portion: '120',
          proteins: '1.1',
        },
        slug: 'farine',
        unit: 'g',
      },
    ])
  })

  it('should createUnitOption return undefined', () => {
    const wrapper = shallow(
      <RecipeIngredientsForm
        ingredientsList={List(ingredientsList)}
        ingredientsRecipe={[{}]}
        fetchAllIngredients={jest.fn()}
      />
    )

    expect(wrapper.find('RecipeIngredientsFormComponent').length).toEqual(1)
    expect(wrapper.state().selectedIngredients).toMatchObject([])

    wrapper.find('RecipeIngredientsFormComponent').props().handleChange('5fdb8dbdc0749c35c039b43f')

    const unitOption = wrapper.find('RecipeIngredientsFormComponent').props().createUnitOption(0)
    expect(unitOption).toBeUndefined()
  })

  it('should createUnitOption return select', () => {
    const wrapper = shallow(
      <RecipeIngredientsForm
        ingredientsList={List(ingredientsList)}
        ingredientsRecipe={recipes.content[0].ingredients}
        fetchAllIngredients={jest.fn()}
      />
    )

    expect(wrapper.find('RecipeIngredientsFormComponent').length).toEqual(1)
    expect(wrapper.state().selectedIngredients).toMatchObject([])

    wrapper.find('RecipeIngredientsFormComponent').props().handleChange('5fdb8dbdc0749c35c039b43f')

    const unitOption = wrapper.find('RecipeIngredientsFormComponent').props().createUnitOption(0)
    expect(unitOption).toBeDefined()
    const unitOption2 = wrapper.find('RecipeIngredientsFormComponent').props().createUnitOption(1)
    expect(unitOption2).toBeDefined()
  })
})
