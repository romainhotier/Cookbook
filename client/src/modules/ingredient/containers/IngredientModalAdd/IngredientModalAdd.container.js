import { connect } from 'react-redux'
import React, { useState, useEffect } from 'react'
import { Modal, Button } from 'antd'

import { postIngredient } from '../../thunks'
import IngredientForm from '../../components/ingredientForm'

const IngredientModalAdd = ({ loadingPostIngredients, ingredients, postIngredient, contentButton }) => {
  const [modalVisible, setModalVisible] = useState(false)

  useEffect(() => {
    setModalVisible(false)
  }, [ingredients])

  return (
    <>
      <Button type="primary" onClick={() => setModalVisible(true)}>
        {contentButton ?? 'Ajouter un nouvel ingrédient'}
      </Button>
      <Modal
        title="Ajouter un nouvel ingrédient"
        visible={modalVisible}
        footer={null}
        onCancel={() => setModalVisible(false)}
        width={'80%'}
      >
        <IngredientForm createIngredient={postIngredient} loading={loadingPostIngredients} />
      </Modal>
    </>
  )
}

const mapDispatchToProps = {
  postIngredient,
}

const mapStateToProps = ({ ingredients: { content, loadingPostIngredients } }) => ({
  ingredients: content,
  loadingPostIngredients,
})

export default connect(mapStateToProps, mapDispatchToProps)(IngredientModalAdd)