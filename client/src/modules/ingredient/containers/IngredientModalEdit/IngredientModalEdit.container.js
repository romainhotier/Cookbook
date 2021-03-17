import React, { useState, useEffect } from 'react'
import { connect } from 'react-redux'
import PropTypes from 'prop-types'
import { Modal, Button } from 'antd'

import { putIngredient } from '../../thunks'
import { getAllIngredients, getloadingPutIngredient } from '../../reducers'
import IngredientForm from '../../components/ingredientForm'

export const IngredientModalEdit = ({ loading, ingredientsList, putIngredient, contentButton, values }) => {
  const [modalVisible, setModalVisible] = useState(false)

  useEffect(() => {
    setModalVisible(false)
  }, [ingredientsList])

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
        <IngredientForm updateIngredient={putIngredient} loading={loading} values={values} />
      </Modal>
    </>
  )
}

const mapDispatchToProps = {
  putIngredient,
}

const mapStateToProps = ({ ingredients }) => ({
  ingredientsList: getAllIngredients(ingredients),
  loading: getloadingPutIngredient(ingredients),
})

export default connect(mapStateToProps, mapDispatchToProps)(IngredientModalEdit)

IngredientModalEdit.propTypes = {
  putIngredient: PropTypes.func,
  ingredientsList: PropTypes.object,
  loading: PropTypes.bool,
  contentButton: PropTypes.oneOfType([PropTypes.string, PropTypes.node]),
  values: PropTypes.object,
}
