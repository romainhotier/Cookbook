import React, { Component } from 'react'
import { connect } from 'react-redux'
import PropTypes from 'prop-types'
import { Row, Col } from 'antd'

import { PUBLISH_STATUS } from 'constants/data.constants'
import { fetchAllRecipe } from '../../thunks'
import RecipeSingleElement from '../../components/RecipeSingleElement'
import Loader from 'components/Loader'

import './_RecipePageList.scss'

class RecipePageList extends Component {
  componentDidMount() {
    this.props.fetchAllRecipe()
  }

  render() {
    const { loadingFetchRecipes, recipes } = this.props
    if (loadingFetchRecipes || Object.entries(recipes).length === 0) {
      return <Loader />
    }

    return (
      <>
        <Row>
          {Object.values(recipes).map((singleRecipe, key) => {
            if (singleRecipe.status !== PUBLISH_STATUS) {
              return ''
            }

            return (
              <Col key={key} xs={24} sm={12} md={12} lg={6} xl={6}>
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

const mapStateToProps = ({ recipes: { content, loadingFetchRecipes } }) => ({ recipes: content, loadingFetchRecipes })

RecipePageList.propTypes = {
  fetchAllRecipe: PropTypes.func,
  recipes: PropTypes.object,
  loadingFetchRecipes: PropTypes.bool,
}

export default connect(mapStateToProps, mapDispatchToProps)(RecipePageList)
