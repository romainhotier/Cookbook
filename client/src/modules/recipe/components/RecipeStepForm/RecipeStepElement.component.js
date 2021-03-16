import React from 'react'
import PropTypes from 'prop-types'
import { Input, Button } from 'antd'

const RecipeStepElement = ({ id, description, removeStep, changeDescription }) => {
  return (
    <div className="step_item_content">
      <Input.TextArea rows={4} value={description} onChange={e => changeDescription(e, id)} />
      <Button
        key={`${id}-button`}
        htmlType="button"
        type="text"
        className="button_remove"
        onClick={() => removeStep(id)}
      >
        <i className="fas fa-trash"></i>
      </Button>
    </div>
  )
}

RecipeStepElement.propTypes = {
  id: PropTypes.number,
  description: PropTypes.string,
  removeStep: PropTypes.func,
  changeDescription: PropTypes.func,
}

export default RecipeStepElement
