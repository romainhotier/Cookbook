import React from "react";
import { Button } from 'antd';
import map from 'lodash/map';
import remove from 'lodash/remove';
import findIndex from 'lodash/findIndex';

import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';

import {reorder, getListStyle} from './RecipeStepForm.helpers';
import RecipeStepElement from './RecipeStepElement.component';

import './_RecipeStepForm.scss';

const RecipeStepForm = ({recipeExist, listSteps, setListSteps, disabled}) => {

  const addStep = () => {
    const lastIndex = listSteps.length-1
    const lastId = listSteps[lastIndex].id
    setListSteps([...listSteps, {id: lastId+1, description: ''}])
  }

  const removeStep = (key) => {
    const newListSteps = Array.from(listSteps)
    remove(newListSteps, (elem) => elem.id === key)
    setListSteps(newListSteps)
  }

  const onDragEnd = (result) => {
    if (!result.destination) {
      return;
    }

    const items = reorder(
      listSteps,
      result.source.index,
      result.destination.index,
    );

    setListSteps(items)
  }

  const changeDescription = ({ target: { value } }, id) => {
    const newListSteps = Array.from(listSteps)
    const index = findIndex(newListSteps, (elem) => elem.id === id)
    newListSteps[index].description = value;
    setListSteps(newListSteps)
  };

  return (
    // <div className={recipeExist ? '' : 'blockDisabled'}>
    <div>
      <h2>Préparation</h2>
      <DragDropContext onDragEnd={onDragEnd}>
        <Droppable droppableId="droppable">
          {(droppableProvided, droppableSnapshot) => (
            <div
              ref={droppableProvided.innerRef}
              style={getListStyle(droppableSnapshot.isDraggingOver, listSteps.length)}
            >
              {map(listSteps, ({id, description}, index) => (
                <article className="step_item" key={`${index}-step`}>
                  <Draggable key={id} draggableId={`${id}-step`} index={index}>
                    {(draggableProvided, draggableSnapshot) => (
                    <div
                      ref={draggableProvided.innerRef}
                      {...draggableProvided.draggableProps}
                      {...draggableProvided.dragHandleProps}

                    >
                      <label key={`${index}-label`} className={`${id}-recipeStep`}>Etape {index +1}</label>
                      <RecipeStepElement key={`${id}-recipeStep`} id={id} description={description} removeStep={removeStep} changeDescription={changeDescription} />
                    </div>
                    )}
                  </Draggable>
                </article>
              ))}
              {droppableProvided.placeholder}
            </div>
          )}
        </Droppable>
      </DragDropContext>
      <div className="button_add_step">
        <Button type="primary" onClick={addStep} >Ajouter une étape</Button>
      </div>
    </div>
  )
}

export default RecipeStepForm;
