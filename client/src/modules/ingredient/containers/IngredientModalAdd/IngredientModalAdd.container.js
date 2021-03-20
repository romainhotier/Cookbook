import React, { useState, useEffect } from 'react'
import { connect } from 'react-redux'
import PropTypes from 'prop-types'
import { Modal, Button } from 'antd'

import { postIngredient } from '../../thunks'
import { getAllIngredients, getloadingPostIngredient } from '../../reducers'
import IngredientForm from '../../components/ingredientForm'

export const IngredientModalAdd = ({
  loading,
  ingredientsList,
  postIngredient,
  contentButton,
  shapeButton,
  className = '',
  type = 'primary',
  sizeButton = 'default',
}) => {
  const [modalVisible, setModalVisible] = useState(false)

  useEffect(() => {
    setModalVisible(false)
  }, [ingredientsList])

  return (
    <>
      <Button
        className={className}
        type={type}
        onClick={() => setModalVisible(true)}
        shape={shapeButton}
        size={sizeButton}
      >
        {contentButton ?? 'Créer un nouvel ingrédient'}
      </Button>
      <Modal
        title="Ajouter un nouvel ingrédient"
        visible={modalVisible}
        footer={null}
        onCancel={() => setModalVisible(false)}
        width={'80%'}
      >
        <IngredientForm createIngredient={postIngredient} loading={loading} />
      </Modal>
    </>
  )
}

const mapDispatchToProps = {
  postIngredient,
}

const mapStateToProps = ({ ingredients }) => ({
  ingredientsList: getAllIngredients(ingredients),
  loading: getloadingPostIngredient(ingredients),
})

export default connect(mapStateToProps, mapDispatchToProps)(IngredientModalAdd)

IngredientModalAdd.propTypes = {
  postIngredient: PropTypes.func,
  ingredientsList: PropTypes.object,
  loading: PropTypes.bool,
  contentButton: PropTypes.oneOfType([PropTypes.string, PropTypes.node]),
  shapeButton: PropTypes.string,
  className: PropTypes.string,
  type: PropTypes.string,
  sizeButton: PropTypes.string,
}
