import React, { Component } from 'react'
import { connect } from 'react-redux'
import PropTypes from 'prop-types'
import { Spin } from 'antd'

import IngredientsList from '../../components/IngredientsList'
import IngredientModalAdd from '../IngredientModalAdd'
import { getAllIngredients, getloadingFetchIngredient } from '../../reducers'
import { fetchAllIngredients, deleteIngredient, searchIngredients } from '../../thunks'

import './_IngredientPageList.scss'

export class IngredientPageList extends Component {
  componentDidMount() {
    this.props.fetchAllIngredients()
  }

  render() {
    const { loading, ingredientsList, deleteIngredient, searchIngredients } = this.props
    if (loading === true) {
      return (
        <div className="page_loader">
          <Spin size="large" />
        </div>
      )
    }

    const ingredients = ingredientsList.toJS()

    return (
      <>
        <div className="ingredientsList_header">
          <h1>Liste des ingrédients</h1>
          <IngredientModalAdd />
        </div>
        <IngredientsList
          data={ingredients}
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

const mapStateToProps = ({ ingredients }) => ({
  ingredientsList: getAllIngredients(ingredients),
  loading: getloadingFetchIngredient(ingredients),
})

export default connect(mapStateToProps, mapDispatchToProps)(IngredientPageList)

IngredientPageList.propTypes = {
  fetchAllIngredients: PropTypes.func,
  deleteIngredient: PropTypes.func,
  searchIngredients: PropTypes.func,
  ingredientsList: PropTypes.object,
  loading: PropTypes.bool,
}
