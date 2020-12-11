import React from "react"
import { Input, Button } from 'antd';

const { TextArea } = Input;

const RecipeStepElement = ({id, description, disabled, removeStep, changeDescription}) => {
  return (
    <div className="step_item_content">
      <TextArea
        rows={4}
        value={description}
        disabled={disabled}
        onChange={(e) => changeDescription(e, id)}
      />
      <Button disabled={disabled} key={`${id}-button`} htmlType="button" type="text" className='button_remove' onClick={() => removeStep(id)}>
        <i className="fas fa-trash"></i>
      </Button>
    </div>
  )
}

export default RecipeStepElement;
