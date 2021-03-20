import { connect } from 'react-redux'
import React, { Component } from 'react'
import { Select, Spin } from 'antd'
import find from 'lodash/find'
import keyBy from 'lodash/keyBy'

import { fetchAllIngredients } from 'modules/ingredient/thunks'
import { getAllIngredients, getloadingFetchIngredient } from 'modules/ingredient/reducers'
import { RecipeIngredientsFormComponent } from './RecipeIngredientsForm.component'

import './_RecipeIngredientsForm.scss'

export class RecipeIngredientsForm extends Component {
  constructor(props) {
    super(props)

    this.state = {
      researchIngredients: [],
      selectedIngredients: [],
      initializeComponent: false,
    }
  }

  componentDidMount() {
    this.props.fetchAllIngredients()
  }

  componentDidUpdate(prevProps) {
    const { ingredientsList, ingredientsRecipe } = this.props

    if ((prevProps.ingredientsList.size === 0 && ingredientsList.size > 0) || !this.state.initializeComponent) {
      const ingredients = ingredientsList.toJS()

      const ingredientsById = keyBy(ingredients, '_id')
      let ingredientsInForm = []
      if (Object.keys(ingredientsRecipe[0]).length > 0) {
        ingredientsInForm = ingredientsRecipe.map(elem => ingredientsById[elem._id])
      }

      this.setState({
        researchIngredients: ingredients,
        selectedIngredients: ingredientsInForm,
        initializeComponent: true,
      })
    }
  }

  handleSearch = value => {
    const { ingredientsList } = this.props
    const ingredients = ingredientsList.toJS()

    if (value) {
      const valueLowerCase = value.toLowerCase()
      const filters = ingredients.filter(({ name = '' }) => {
        const nameLowercase = name.toLowerCase()
        return nameLowercase.search(valueLowerCase) > -1
      })
      this.setState({ researchIngredients: filters })
    }
  }

  handleChange = value => {
    const { ingredientsList } = this.props
    const ingredients = ingredientsList.toJS()

    const ingSelected = find(ingredients, ing => ing._id === value)
    this.setState({ selectedIngredients: [...this.state.selectedIngredients, ingSelected] })
  }

  createUnitOption = index => {
    const ingredient = this.state.selectedIngredients[index]

    if (!ingredient) {
      return
    }

    if (parseInt(ingredient.nutriments.portion) > 1) {
      return (
        <>
          <Select.Option value={ingredient.unit}>{`${ingredient.unit}`}</Select.Option>
          <Select.Option value="portion">
            {`${ingredient.name} soit (${ingredient.nutriments.portion} ${ingredient.unit})`}
          </Select.Option>
        </>
      )
    }
    return (
      <>
        <Select.Option value={ingredient.unit}>{`${ingredient.unit}`}</Select.Option>
      </>
    )
  }

  render() {
    const { ingredientsList } = this.props
    const { researchIngredients } = this.state

    if (ingredientsList.size === 0) {
      return <Spin />
    }

    const options = researchIngredients.map(d => (
      <Select.Option key={`researchIngredientsOption-${d._id}`} value={d._id}>
        {d.name}
      </Select.Option>
    ))

    return (
      <RecipeIngredientsFormComponent
        handleSearch={this.handleSearch}
        handleChange={this.handleChange}
        createUnitOption={this.createUnitOption}
        options={options}
      />
    )
  }
}

const mapDispatchToProps = {
  fetchAllIngredients,
}

const mapStateToProps = ({ ingredients }) => ({
  ingredientsList: getAllIngredients(ingredients),
  loading: getloadingFetchIngredient(ingredients),
})

export default connect(mapStateToProps, mapDispatchToProps)(RecipeIngredientsForm)
