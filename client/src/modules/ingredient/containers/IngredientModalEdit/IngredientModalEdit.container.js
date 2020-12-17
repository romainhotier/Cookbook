import { connect } from 'react-redux'
import React, { useState, useEffect } from 'react'
import { Modal, Button } from 'antd'

import { putIngredient } from '../../thunks'
import IngredientForm from '../../components/ingredientForm'

const IngredientModalEdit = ({ loadingPutIngredients, ingredients, putIngredient, contentButton, values }) => {
  const [modalVisible, setModalVisible] = useState(false)

  useEffect(() => {
    setModalVisible(false)
  }, [ingredients])

  return (
    <>
      <Button type="primary" onClick={() => setModalVisible(true)}>
        {contentButton ?? 'Editer un ingrédient'}
      </Button>
      <Modal
        title="Editer un ingrédient"
        visible={modalVisible}
        footer={null}
        onCancel={() => setModalVisible(false)}
        width={'80%'}
      >
        <IngredientForm updateIngredient={putIngredient} loading={loadingPutIngredients} values={values} />
      </Modal>
    </>
  )
}

const mapDispatchToProps = {
  putIngredient,
}

const mapStateToProps = ({ ingredients: { content, loadingPutIngredients } }) => ({
  ingredients: content,
  loadingPutIngredients,
})

export default connect(mapStateToProps, mapDispatchToProps)(IngredientModalEdit)
