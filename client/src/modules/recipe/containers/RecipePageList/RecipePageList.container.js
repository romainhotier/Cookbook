import React, { Component } from 'react'
import { connect } from 'react-redux'
import PropTypes from 'prop-types'
import { Row, Col } from 'antd'

import { PUBLISH_STATUS } from 'constants/data.constants'
import { fetchAllRecipe } from '../../thunks'
import { getAllRecipes, getloadingFetchRecipe } from '../../reducers'
import RecipeSingleElement from '../../components/RecipeSingleElement'
import Loader from 'components/Loader'

export class RecipePageList extends Component {
  componentDidMount() {
    this.props.fetchAllRecipe()
  }

  render() {
    const { loading, recipesList } = this.props

    if (loading || recipesList.size === 0) {
      return <Loader />
    }

    const recipes = recipesList.toJS()

    return (
      <>
        <Row>
          {Object.values(recipes).map((singleRecipe, key) => {
            if (singleRecipe.status !== PUBLISH_STATUS) {
              return ''
            }

            return (
              <Col key={key} xs={24} sm={12} md={12} lg={8} xl={6}>
                <RecipeSingleElement recipe={singleRecipe} />
              </Col>
            )
          })}
        </Row>
      </>
    )
  }
}

const mapDispatchToProps = {
  fetchAllRecipe,
}

const mapStateToProps = ({ recipes }) => ({
  recipesList: getAllRecipes(recipes),
  loading: getloadingFetchRecipe(recipes),
})

RecipePageList.propTypes = {
  fetchAllRecipe: PropTypes.func,
  recipes: PropTypes.object,
  loadingFetchRecipe: PropTypes.bool,
}

export default connect(mapStateToProps, mapDispatchToProps)(RecipePageList)
