import { connect } from 'react-redux'
import React, { Component } from 'react'
import { Col, Row, Spin, Dropdown, Carousel, Divider } from 'antd'

import { fetchRecipe } from 'modules/recipe/thunks'
import { fetchAllIngredients } from 'modules/ingredient/thunks'
import { RecipeInformations } from 'modules/recipe/components/RecipeDetails/RecipeInformations.component'
import { menuActions } from 'modules/recipe/components/RecipeDetails/RecipeMenu.component'
import { BuildListIngredients } from '../../components/RecipeDetails/BuildListIngredients.component'
import { EditPortion } from '../../components/RecipeDetails/EditPortion.component'

import './_RecipePageDetails.scss'

class RecipePageDetails extends Component {
  constructor(props) {
    super(props)

    this.state = {
      portionEdited: null,
    }
  }

  componentDidMount() {
    const { recipes, match, fetchRecipe, allIngredients, loadingFetchIngredients, fetchAllIngredients } = this.props
    const { slug } = match.params
    if (recipes[slug] === undefined) {
      fetchRecipe(slug)
    }

    if (recipes[slug] !== undefined && Object.keys(allIngredients).length === 0 && !loadingFetchIngredients) {
      fetchAllIngredients()
    }
  }

  componentDidUpdate() {
    const { allIngredients, fetchAllIngredients, loadingFetchIngredients } = this.props
    if (Object.keys(allIngredients).length === 0 && !loadingFetchIngredients) {
      fetchAllIngredients()
    }
  }

  updatePortionEdited = newPortion => {
    if (isNaN(newPortion)) {
      return this.setState({
        portionEdited: 0,
      })
    }
    this.setState({
      portionEdited: newPortion,
    })
  }

  render() {
    const { recipes, match, loadingFetchIngredients, loadingFetchRecipes, allIngredients } = this.props
    const { portionEdited } = this.state
    const { slug } = match.params
    const recipe = recipes[slug]

    if (
      recipe === undefined ||
      loadingFetchIngredients ||
      loadingFetchRecipes ||
      Object.keys(allIngredients).length === 0
    ) {
      return <Spin />
    }

    const { title, steps, preparation_time, cooking_time, nb_people, categories, ingredients, files } = recipe
    console.log('files', files)
    return (
      <section className="RecipeDetails">
        <div className="RecipeDetails_actions">
          <Dropdown.Button overlay={menuActions(slug)}>
            <i className="fas fa-play-circle icons"></i> Démarrer la recette
          </Dropdown.Button>
        </div>
        <Row className="RecipeDetails_header" gutter={16}>
          <Col xs={24} sm={24} md={24} lg={24} xl={12}>
            <Carousel className="RecipeDetails_carousel">
              {files &&
                files.map((image, index) => (
                  <div>
                    <div
                      className="RecipeDetails_carousel_img"
                      style={{ backgroundImage: `url(${process.env.REACT_APP_IMAGES_SERVER}/${image})` }}
                      key={`img-${index}`}
                    />
                  </div>
                ))}
            </Carousel>
          </Col>
          <Col xs={24} sm={24} md={24} lg={24} xl={12}>
            <h2>{title}</h2>
            <em>Créé par XXXX XXXX</em>
            <div className="RecipeDetails_informations">
              {preparation_time ? (
                <>
                  <RecipeInformations label="Temps de préparation" value={`${preparation_time} min`} icon="times" />
                  <Divider type="vertical" />
                </>
              ) : (
                ''
              )}

              {cooking_time ? (
                <>
                  <RecipeInformations label="Temps de cuisson" value={`${cooking_time} min`} icon="cook_times" />
                  <Divider type="vertical" />
                </>
              ) : (
                ''
              )}

              {nb_people ? <RecipeInformations label="Nombre de part" value={`${nb_people}`} icon="portion" /> : ''}
            </div>
            {categories && (
              <div className="RecipeDetails_categories">
                {categories.map(category => (
                  <div key={category}>{category}</div>
                ))}
              </div>
            )}
          </Col>
        </Row>

        <Row>
          {/* INGREDIENTS  */}
          <Col xs={12} sm={12} md={12} lg={8} xl={8} className="listIngredients">
            <h3>Ingrédients</h3>
            <EditPortion
              portion={parseInt(nb_people)}
              portionEdited={portionEdited}
              updatePortionEdited={this.updatePortionEdited}
            />
            <ul>
              <BuildListIngredients
                allIngredients={allIngredients}
                ingredients={ingredients}
                portion={parseInt(nb_people)}
                portionEdited={portionEdited}
              />
            </ul>
          </Col>

          {/* ETAPES  */}
          <Col xs={12} sm={12} md={12} lg={16} xl={16}>
            <h3>Instructions</h3>
            {steps.map((element, index) => (
              <article className="step" key={index}>
                <div className="step_index">{index + 1}</div>
                <div className="step_describe">{element.description}</div>
              </article>
            ))}
          </Col>
        </Row>
      </section>
    )
  }
}

const mapDispatchToProps = {
  fetchRecipe,
  fetchAllIngredients,
}

const mapStateToProps = ({ recipes, ingredients }) => ({
  recipes: recipes.content,
  loadingFetchRecipes: recipes.loadingFetchRecipes,
  allIngredients: ingredients.content,
  loadingFetchIngredients: ingredients.loadingFetchIngredients,
})

export default connect(mapStateToProps, mapDispatchToProps)(RecipePageDetails)
