import React from 'react'
import { Col, Row, Dropdown, Button } from 'antd'

import { RecipeInformations } from 'modules/recipe/components/RecipeDetails/RecipeInformations.component'
import { menuActions } from 'modules/recipe/components/RecipeDetails/RecipeMenu.component'
import { BuildListIngredients } from '../../components/RecipeDetails/BuildListIngredients.component'
import { EditPortion } from '../../components/RecipeDetails/EditPortion.component'
import RecipeModalDelete from '../../components/RecipeModalDelete'
import { UploadFilesRecipe } from '../../components/RecipeUploadFiles'
import Carousel from 'components/Carousel'
import CategoryTag from 'components/CategoryTag'

import './_RecipePageDetails.scss'

export const RecipePageDetailsComponent = ({
  deleteRecipe,
  history,
  modalDeleteRecipeIsVisible,
  allIngredients,
  portionEdited,
  updatePortionEdited,
  showModal,
  recipe,
  handleUploadFiles,
  uploadFilesIsVisible,
}) => {
  const {
    title,
    steps,
    preparation_time,
    cooking_time,
    nb_people,
    categories,
    ingredients,
    files,
    _id,
    calories,
    slug,
  } = recipe

  const caloriesForOnePortion = Math.round(calories / nb_people, 2)

  return (
    <section className="RecipeDetails">
      <div className="RecipeDetails_actions">
        <Dropdown.Button overlay={menuActions(slug, showModal)}>
          <i className="fas fa-play-circle icons"></i> Démarrer la recette
        </Dropdown.Button>
        <Button type="default" onClick={handleUploadFiles}>
          Ajouter/Supprimer des images
        </Button>
      </div>
      <RecipeModalDelete
        deleteRecipe={deleteRecipe}
        id={_id}
        isModalVisible={modalDeleteRecipeIsVisible}
        closeModal={() => this.setState({ modalDeleteRecipeIsVisible: false })}
        history={history}
      />

      <Row className="RecipeDetails_header" gutter={16}>
        <Col xs={24} sm={24} md={24} lg={24} xl={12}>
          {uploadFilesIsVisible ? (
            <UploadFilesRecipe _id={_id} files={files} />
          ) : (
            <Carousel files={files} className={'RecipeDetails_carousel'} height={'400px'} />
          )}
        </Col>
        <Col xs={24} sm={24} md={24} lg={24} xl={12}>
          <h2>{title}</h2>
          <em>Créé par XXXX XXXX</em>

          <RecipeInformations
            preparation_time={preparation_time}
            cooking_time={cooking_time}
            caloriesForOnePortion={caloriesForOnePortion}
          />

          {categories && (
            <div className="RecipeDetails_categories">
              {categories.map(category => (
                <CategoryTag key={`key-${category}`} category={category} />
              ))}
            </div>
          )}
        </Col>
      </Row>

      <Row>
        {/* INGREDIENTS  */}

        <Col xs={12} sm={12} md={12} lg={8} xl={8} className="listIngredients">
          <h3>Ingrédients</h3>
          {!ingredients ? (
            'Aucun ingrédient'
          ) : (
            <>
              <EditPortion
                portion={parseInt(nb_people)}
                portionEdited={portionEdited}
                updatePortionEdited={updatePortionEdited}
              />

              <ul>
                <BuildListIngredients
                  allIngredients={allIngredients}
                  ingredients={ingredients}
                  portion={parseInt(nb_people)}
                  portionEdited={portionEdited}
                />
              </ul>
            </>
          )}
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
