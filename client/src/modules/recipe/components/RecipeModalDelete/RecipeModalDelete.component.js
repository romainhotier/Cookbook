import React from 'react'
import PropTypes from 'prop-types'
import { Modal, Button } from 'antd'

import Routes from '../../RecipeRoutes'

const RecipeModalDelete = ({ deleteRecipe, id, isModalVisible, closeModal, history }) => {
  const handleOK = () => {
    deleteRecipe(id)
    history.push(Routes.recipe())
  }

  const footerButtons = (
    <>
      <Button type="default" onClick={closeModal}>
        Non, non, non !
      </Button>
      <Button type="primary" onClick={handleOK}>
        Supprimer
      </Button>
    </>
  )

  return (
    <Modal title="Supprimer la recette" visible={isModalVisible} footer={footerButtons} onCancel={closeModal}>
      <p>Êtes-vous sûr de vouloir supprimer cette recette ?</p>
    </Modal>
  )
}

RecipeModalDelete.propTypes = {
  deleteRecipe: PropTypes.func,
  id: PropTypes.string,
  isModalVisible: PropTypes.bool,
  closeModal: PropTypes.func,
  history: PropTypes.object,
}

export default RecipeModalDelete
