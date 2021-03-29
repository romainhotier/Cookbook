import React from 'react'
import PropTypes from 'prop-types'
import { Col, Row, Dropdown } from 'antd'

import { RecipeInformations } from 'modules/recipe/components/RecipeDetails/RecipeInformations.component'
import { RecipeMenu } from 'modules/recipe/components/RecipeDetails/RecipeMenu.component'
import { BuildListIngredients } from '../../components/RecipeDetails/BuildListIngredients.component'
import { EditPortion } from '../../components/RecipeDetails/EditPortion.component'
import { RecipeImagesStep } from '../../components/RecipeDetails/RecipeImagesStep.component'
import RecipeModalDelete from '../../components/RecipeModalDelete'
import { UploadFilesRecipe, UploadFilesRecipeStep } from '../../components/RecipeUploadFiles'
import Carousel from 'components/Carousel'
import CategoryTag from 'components/CategoryTag'

import './_RecipePageDetails.scss'

export const RecipePageDetailsComponent = ({
  allIngredients,
  closeModal,
  deleteRecipe,
  handleUploadFiles,
  history,
  modalDeleteRecipeIsVisible,
  portionEdited,
  recipe,
  showModal,
  updatePortionEdited,
  uploadFilesIsVisible,
}) => {
  const {
    title,
    steps = [],
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
        <Dropdown.Button overlay={RecipeMenu(slug, showModal, handleUploadFiles)}>
          <i className="fas fa-play-circle icons"></i> Démarrer la recette
        </Dropdown.Button>
      </div>
      <RecipeModalDelete
        deleteRecipe={deleteRecipe}
        id={_id}
        isModalVisible={modalDeleteRecipeIsVisible}
        closeModal={closeModal}
        history={history}
      />

      <Row className="RecipeDetails_header" gutter={16}>
        <Col xs={24} sm={24} md={24} lg={24} xl={12}>
          {uploadFilesIsVisible ? (
            <UploadFilesRecipe _id={_id} />
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
            <>
              {uploadFilesIsVisible ? <UploadFilesRecipeStep id_recipe={_id} id_step={element._id} /> : ''}
              <article className="step" key={`key-${element._id}`}>
                <div className="step_index">{index + 1}</div>
                <div className="step_describe">
                  {uploadFilesIsVisible ? '' : <RecipeImagesStep files={element.files} />}
                  {element.description}
                </div>
              </article>
            </>
          ))}
        </Col>
      </Row>
    </section>
  )
}

RecipePageDetailsComponent.propTypes = {
  allIngredients: PropTypes.object,
  closeModal: PropTypes.func,
  deleteRecipe: PropTypes.func,
  handleUploadFiles: PropTypes.func,
  history: PropTypes.object,
  modalDeleteRecipeIsVisible: PropTypes.bool,
  portionEdited: PropTypes.number,
  recipe: PropTypes.object,
  showModal: PropTypes.func,
  updatePortionEdited: PropTypes.func,
  uploadFilesIsVisible: PropTypes.bool,
}
