import { connect } from 'react-redux'
import React, { Component } from 'react'
/* import PropTypes from 'prop-types' */
import { Row, Col, Icon } from 'antd'
import { NavLink } from 'react-router-dom'

import { getRecipe, getAllIngredientsOfRecipe } from '../../thunks/recipeThunks'
import Routes from '../RecipeRoutes'

import Ingredient from 'components/ingredient/Ingredient'
import CategoryElement from 'components/recipeElement/CategoryElement'
import TimeElement from 'components/recipeElement/TimeElement'
import PeopleElement from 'components/recipeElement/PeopleElement'

import './_RecipePageDetails.scss'

class RecipePageDetails extends Component {
  constructor(props) {
    super(props)
    this.state = {
      loading: true,
    }
  }

  componentDidMount() {
    const id = this.props.match.params.id

    this.props.getRecipe(id)
    this.props.getAllIngredientsOfRecipe(id)

  }


  render() {
    const { fetchRecipes, fetchIngredients, recipes } = this.props
    const id = this.props.match.params.id
    if (
      fetchIngredients ||
      fetchRecipes ||
      Object.entries(recipes).length === 0 ||
      recipes[id] === undefined
    ) {
      return 'Patientez'
    }
    const recipe = recipes[id]

    return (
      <>
        <Row gutter={16} className="contentRecipe">
          <Col span={18}>
            <div className="contentRecipe_stepOfMake">
              <h2 className="title">{recipe.title}</h2>
              <NavLink
                to={Routes.recipeEdit(recipe.id)}
                className="edit-link"
                activeClassName="active"
                exact
              >
                <Icon type="edit" />
              </NavLink>

              <div className="metadata">
                <span>
                  <Icon type="tag" /> Catégories:{' '}
                  <CategoryElement categories={recipe.categories} whenDisplay="list" />
                </span>
                <span>
                  <Icon type="clock-circle" /> Préparation:{' '}
                  <TimeElement time={recipe.preparationTime} />
                </span>
                <span>
                  <Icon type="clock-circle" /> Cuisson: <TimeElement time={recipe.cookingTime} />
                </span>
                <span>
                  <Icon type="team" /> <PeopleElement people={recipe.nbPeople} />
                </span>
              </div>
              <h4>Etape 1</h4>
              <p>{recipe.stape1}</p>
              {recipe.stape2 !== '' ? (
                <>
                  <h4>Etape 2</h4>
                  <p>{recipe.stape2}</p>
                </>
              ) : (
                ''
              )}
              {recipe.stape3 !== '' ? (
                <>
                  <h4>Etape 3</h4>
                  <p>{recipe.stape3}</p>
                </>
              ) : (
                ''
              )}
              {recipe.stape4 !== '' ? (
                <>
                  <h4>Etape 4</h4>
                  <p>{recipe.stape4}</p>
                </>
              ) : (
                ''
              )}
            </div>
            {recipe.note !== '' && recipe.note !== undefined && recipe.note !== 'undefined' ? (
              <div className="contentRecipe_note">
                <h5>Note</h5>
                <p>{recipe.note}</p>
              </div>
            ) : (
              ''
            )}
          </Col>
          <Col span={6}>
            <div className="contentRecipe_ingredientList">
              <h3>Liste des ingredients</h3>
              {recipe.ingredients !== undefined
                ? Object.values(recipe.ingredients).map((ingredient, i) => (
                    <Ingredient
                      key={i}
                      name={ingredient.name}
                      quantity={ingredient.quantity}
                      unity={ingredient.unity}
                    />
                  ))
                : ''}
            </div>

            {(recipe.image === undefined || recipe.image === '') ? (
              '111'
            ) : (
              <div className="pictureOfRecipe">
                222
                <img
                  alt={recipe.title}
                  src={`${process.env.REACT_APP_SERVER_URL + '/' + recipe.image}`}
                />
              </div>
            )}
          </Col>
        </Row>
      </>
    )
  }
}

const mapDispatchToProps = {
  getRecipe,
  getAllIngredientsOfRecipe,
}

const mapStateToProps = ({ recipes }) => {
  return {
    fetchRecipes: recipes.fetchRecipes,
    fetchIngredients: recipes.fetchIngredients,
    recipes: recipes.content,
  }
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(RecipePageDetails)
