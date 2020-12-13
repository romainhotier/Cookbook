import { connect } from 'react-redux'
import React, { Component } from 'react'
import { Spin } from 'antd'

import IngredientsList from '../../components/IngredientsList'
import IngredientModalAdd from '../IngredientModalAdd'
import { fetchAllIngredients, deleteIngredient } from '../../thunks'

import './_IngredientPageList.scss'

class IngredientPageList extends Component {
  componentDidMount() {
    this.props.fetchAllIngredients()
  }

  render() {
    const { loading, ingredients, deleteIngredient } = this.props
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
          editIngredient={data => console.log('edit', data)}
        />
      </>
    )
  }
}

const mapDispatchToProps = {
  fetchAllIngredients,
  deleteIngredient,
}

const mapStateToProps = ({ ingredients: { content, loadingFetchIngredients, loadingDeleteIngredient } }) => ({
  ingredients: content,
  loading: loadingFetchIngredients || loadingDeleteIngredient,
})

export default connect(mapStateToProps, mapDispatchToProps)(IngredientPageList)
