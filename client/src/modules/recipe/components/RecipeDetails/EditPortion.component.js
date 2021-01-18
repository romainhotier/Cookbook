import React from 'react'
import { Input, Button } from 'antd'

import './_RecipeDetails.scss'

export const EditPortion = ({ portion = 0, portionEdited, updatePortionEdited }) => {
  const value = portionEdited ?? portion
  const suffix = value > 1 ? 'portions' : 'portion'

  const addOrRemoveANumber = number => {
    if (portionEdited === null) {
      return updatePortionEdited(portion + number)
    }
    updatePortionEdited(portionEdited + number)
  }

  return (
    <div className="RecipeDetails_editPortion">
      <Button shape="circle" onClick={() => addOrRemoveANumber(-1)}>
        -
      </Button>
      <Input
        value={value}
        placeholder="Entrer le nombre de "
        suffix={suffix}
        onChange={e => updatePortionEdited(parseInt(e.target.value))}
      />
      <Button shape="circle" onClick={() => addOrRemoveANumber(+1)}>
        +
      </Button>
    </div>
  )
}
