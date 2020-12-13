import { connect } from 'react-redux'
import React, { Component } from 'react'

import IngredientsList from '../../components/IngredientsList'
import IngredientPageAdd from '../IngredientPageAdd'
import { fetchAllIngredients } from '../../thunks'

import './_IngredientPageList.scss'

class IngredientPageList extends Component {
  componentDidMount() {
    this.props.fetchAllIngredients()
  }

  render() {
    const { loadingFetchIngredients, ingredients } = this.props
    if (loadingFetchIngredients === true || Object.entries(ingredients).length === 0) {
      return 'Patientez'
    }

    return (
      <>
        <div className="ingredientsList_header">
          <h1>Liste des ingrédients</h1>
          <IngredientPageAdd />
        </div>
        <IngredientsList data={Object.values(ingredients)} />
      </>
    )
  }
}

const mapDispatchToProps = {
  fetchAllIngredients,
}

const mapStateToProps = ({ ingredients: { content, loadingFetchIngredients } }) => ({
  ingredients: content,
  loadingFetchIngredients,
})

export default connect(mapStateToProps, mapDispatchToProps)(IngredientPageList)
