import { connect } from 'react-redux'
import React, { Component } from 'react'
import { Spin } from 'antd'

import IngredientsList from '../../components/IngredientsList'
import IngredientModalAdd from '../IngredientModalAdd'
import { fetchAllIngredients, deleteIngredient, searchIngredients } from '../../thunks'

import './_IngredientPageList.scss'

class IngredientPageList extends Component {
  componentDidMount() {
    this.props.fetchAllIngredients()
  }

  render() {
    const { loading, ingredients, deleteIngredient, searchIngredients } = this.props
    if (loading === true) {
      return (
        <div className="page_loader">
          <Spin size="large" />
        </div>
      )
    }

    return (
      <>
        <div className="ingredientsList_header">
          <h1>Liste des ingrédients</h1>
          <IngredientModalAdd />
        </div>
        <IngredientsList
          data={Object.values(ingredients)}
          deleteIngredient={id => deleteIngredient(id)}
          searchIngredients={searchIngredients}
        />
      </>
    )
  }
}

const mapDispatchToProps = {
  fetchAllIngredients,
  deleteIngredient,
  searchIngredients,
}

const mapStateToProps = ({ ingredients: { content, loadingFetchIngredients, loadingDeleteIngredient } }) => ({
  ingredients: content,
  loading: loadingFetchIngredients || loadingDeleteIngredient,
})

export default connect(mapStateToProps, mapDispatchToProps)(IngredientPageList)
