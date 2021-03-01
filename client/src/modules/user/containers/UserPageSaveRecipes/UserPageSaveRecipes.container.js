import React, { Component } from 'react'
import { Table } from 'antd'
import { connect } from 'react-redux'
import PropTypes from 'prop-types'

import { DRAFT_STATUS } from 'constants/data.constants'
import { fetchAllRecipe } from 'modules/recipe/thunks'
import UserContent from '../../components/UserContent'
import { columns } from './UserPageSaveRecipes.columns'
import Loader from 'components/Loader'

import './_UserPageSaveRecipes.scss'

class UserPageSaveRecipes extends Component {
  componentDidMount() {
    this.props.fetchAllRecipe()
  }

  render() {
    const { loadingFetchRecipes, recipes } = this.props
    if (loadingFetchRecipes || Object.entries(recipes).length === 0) {
      return <Loader />
    }

    const data = Object.values(recipes).filter(recipe => recipe.status === DRAFT_STATUS)

    return (
      <UserContent title="Recettes non terminées">
        <Table className="save_recipes" columns={columns} dataSource={data} />
      </UserContent>
    )
  }
}

const mapDispatchToProps = {
  fetchAllRecipe,
}

const mapStateToProps = ({ recipes: { content, loadingFetchRecipes } }) => ({ recipes: content, loadingFetchRecipes })

UserPageSaveRecipes.propTypes = {
  fetchAllRecipe: PropTypes.func,
  recipes: PropTypes.object,
  loadingFetchRecipes: PropTypes.bool,
}

export default connect(mapStateToProps, mapDispatchToProps)(UserPageSaveRecipes)
