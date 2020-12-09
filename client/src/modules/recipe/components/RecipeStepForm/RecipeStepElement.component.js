import React from "react"
import { Input } from 'antd';

const { TextArea } = Input;

const RecipeStepElement = ({position, description, disabled, editStep}) => {

  return (
    <div>
      <label>Etape {position+1}</label>
      <TextArea
        rows={4}
        value={description}
        disabled={disabled}
        onBlur={({})}
      />
    </div>
  )
}

export default RecipeStepElement;
