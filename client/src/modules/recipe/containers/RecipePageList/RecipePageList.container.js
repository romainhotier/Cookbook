import { connect } from 'react-redux'
import React, { Component } from 'react'
import { Row, Col } from 'antd'

import { fetchAllRecipe } from '../../thunks'
import RecipeSingleElement from '../../components/RecipeSingleElement'

import './_RecipePageList.scss'

class RecipePageList extends Component {
  componentDidMount() {
    this.props.fetchAllRecipe()
  }

  render() {
    const { loadingFetchRecipes, recipes } = this.props
    if (loadingFetchRecipes === true || Object.entries(recipes).length === 0) {
      return 'Patientez'
    }

    return (
      <>
        <Row>
          {Object.values(recipes).map((singleRecipe, key) => (
            <Col
              key={key}
              xs={{ span: 24 }}
              sm={{ span: 12 }}
              md={{ span: 12}}
              lg={{ span: 6}}
              xl={{ span: 4}}
            >
              <RecipeSingleElement recipe={singleRecipe} />
            </Col>
          ))}
        </Row>
      </>
    )
  }
}

const mapDispatchToProps = {
  fetchAllRecipe,
}

const mapStateToProps = ({recipes : {content, loadingFetchRecipes}}) => ({recipes: content, loadingFetchRecipes})

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(RecipePageList)
