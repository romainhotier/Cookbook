import React, {useState} from "react";
import { Input, Button } from 'antd';
import map from 'lodash/map'
import remove from 'lodash/remove'
import last from 'lodash/last'

import RecipeStepElement from './RecipeStepElement.component';

const RecipeStepForm = ({recipeExist, listSteps, setListSteps, disabled}) => {

  const addStep = () => {
    setListSteps([...listSteps, {position: listSteps.length, description: ''}])
  }

  return (
    // <div className={recipeExist ? '' : 'blockDisabled'}>
    <div>
      <h2>Préparation</h2>
      {map(listSteps, ({position, description}) => <RecipeStepElement key={position} position={position} description={description} />)}
      <div style={{ textAlign: 'right', marginTop: '20px'}}>
        <Button type="primary" onClick={addStep} >Ajouter une étape</Button>
      </div>
    </div>
  )
}

export default RecipeStepForm;
