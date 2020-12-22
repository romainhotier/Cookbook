import { connect } from 'react-redux'
import React, { Component } from 'react'
import { Col, Row, Spin, Menu, Dropdown, Carousel, Divider } from 'antd'
import { NavLink } from 'react-router-dom'

import Routes from '../../RecipeRoutes'
import { fetchRecipe } from '../../thunks'
import { RecipeInformations } from '../../components/RecipeDetails/RecipeInformations.component'

import './_RecipePageDetails.scss'

class RecipePageDetails extends Component {
  componentDidMount() {
    const { recipes, match, fetchRecipe } = this.props
    const { slug } = match.params

    if (recipes[slug] === undefined) {
      fetchRecipe(slug)
    }
  }

  render() {
    const { recipes, match } = this.props
    const { slug } = match.params
    const recipe = recipes[slug]

    if (recipe === undefined) {
      return <Spin />
    }

    const menuActions = (
      <Menu>
        <Menu.Item key="edit">
          <NavLink to={Routes.recipeEdit(slug)} exact>
            <i className="fas fa-edit icons"></i> Modifier la recette
          </NavLink>
        </Menu.Item>
        <Menu.Item key="delete">
          <i className="fas fa-trash-alt icons"></i> Supprimer
        </Menu.Item>
      </Menu>
    )

    const { title, steps, preparation_time, cooking_time, nb_people, categories } = recipe
    console.log(recipe)
    return (
      <section className="RecipeDetails">
        <div className="RecipeDetails_actions">
          <Dropdown.Button overlay={menuActions}>
            <i className="fas fa-play-circle icons"></i> Démarer la recette
          </Dropdown.Button>
        </div>
        <Row className="RecipeDetails_header" gutter={16}>
          <Col xs={24} sm={24} md={24} lg={24} xl={12}>
            <Carousel>
              <div>
                <h6 className="carrousel">1</h6>
              </div>
              <div>
                <h6 className="carrousel">2</h6>
              </div>
              <div>
                <h6 className="carrousel">3</h6>
              </div>
            </Carousel>
          </Col>
          <Col xs={24} sm={24} md={24} lg={24} xl={12}>
            <h2>{title}</h2>
            <em>Créé par XXXX XXXX</em>
            <div className="RecipeDetails_informations">
              {preparation_time ? (
                <>
                  <RecipeInformations
                    label="Temps de préparation"
                    value={`${preparation_time} min`}
                    icon="far fa-clock"
                  />
                  <Divider type="vertical" />
                </>
              ) : (
                ''
              )}

              {cooking_time ? (
                <>
                  <RecipeInformations label="Temps de cuisson" value={`${cooking_time} min`} icon="far fa-clock" />
                  <Divider type="vertical" />
                </>
              ) : (
                ''
              )}

              {nb_people ? (
                <RecipeInformations label="Nombre de part" value={`${nb_people}`} icon="fas fa-cookie" />
              ) : (
                ''
              )}
            </div>
            {categories && (
              <div className="RecipeDetails_categories">
                {categories.map(category => (
                  <div>{category}</div>
                ))}
              </div>
            )}
          </Col>
        </Row>
        <Row>
          <Col xs={12} sm={12} md={12} lg={12} xl={12}>
            <h3>Ingrédients</h3>
          </Col>
          <Col xs={12} sm={12} md={12} lg={12} xl={12}>
            <h3>Instructions</h3>
            {steps.map((element, index) => (
              <div className="step" key={index}>
                <div className="step_index">{index + 1}</div>
                {element.step}
              </div>
            ))}
          </Col>
        </Row>
      </section>
    )
  }
}

const mapDispatchToProps = {
  fetchRecipe,
}

const mapStateToProps = ({ recipes: { content, loadingFetchRecipes } }) => ({
  recipes: content,
  loadingFetchRecipes,
})

export default connect(mapStateToProps, mapDispatchToProps)(RecipePageDetails)
