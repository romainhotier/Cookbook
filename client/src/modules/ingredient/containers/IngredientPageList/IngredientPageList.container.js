import { connect } from 'react-redux'
import React, { Component } from 'react'
import { Spin } from 'antd'

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
    if (loadingFetchIngredients === true) {
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
          <IngredientPageAdd />
        </div>
        <IngredientsList
          data={Object.values(ingredients)}
          deleteIngredient={() => console.log('delete')}
          editIngredient={data => console.log('edit', data)}
        />
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
