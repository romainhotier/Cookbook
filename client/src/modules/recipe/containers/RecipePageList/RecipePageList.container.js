import { connect } from 'react-redux'
import React, { Component } from 'react'
import { Row, Col } from 'antd'

import { fetchAllRecipe } from '../../thunks'

// import './_RecipeList.scss'

class RecipePageList extends Component {
  constructor(props) {
    super(props)
    this.state = {
      loading: true,
    }
  }

  componentDidMount() {
    this.props.fetchAllRecipe()
  }

  render() {
    const { loadingFetchRecipes, recipes } = this.props
    // if (fetchRecipes === true || Object.entries(recipes).length === 0) {
    //   return 'Patientez'
    // }
    console.log(recipes)
    return (
      <>
      coucou
        {/* <Row>
          {Object.values(recipes).map((singleRecipe, key) => (
            <Col key={key}>
              <RecipeSingleElement recipe={singleRecipe} whenDisplay="list"/>
            </Col>
          ))}
        </Row> */}
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
