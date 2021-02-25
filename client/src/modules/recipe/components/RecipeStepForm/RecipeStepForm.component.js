import React from 'react'
import { Button, Collapse } from 'antd'
import map from 'lodash/map'
import remove from 'lodash/remove'
import findIndex from 'lodash/findIndex'

import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd'

import { reorder, getListStyle } from './RecipeStepForm.helpers'
import RecipeStepElement from './RecipeStepElement.component'

import './_RecipeStepForm.scss'

const { Panel } = Collapse

const RecipeStepForm = ({ listSteps, setListSteps }) => {
  const addStep = () => {
    const lastIndex = listSteps.length - 1
    const lastIdFront = listSteps > 0 ? listSteps[lastIndex].idFront : 0
    setListSteps([...listSteps, { idFront: lastIdFront + 1, description: '' }])
  }

  const removeStep = key => {
    const newListSteps = Array.from(listSteps)
    remove(newListSteps, elem => elem.idFront === key)
    setListSteps(newListSteps)
  }

  const onDragEnd = result => {
    if (!result.destination) {
      return
    }

    const items = reorder(listSteps, result.source.index, result.destination.index)

    setListSteps(items)
  }

  const changeDescription = ({ target: { value } }, idFront) => {
    const newListSteps = Array.from(listSteps)
    const index = findIndex(newListSteps, elem => elem.idFront === idFront)
    newListSteps[index].description = value
    setListSteps(newListSteps)
  }

  return (
    <Collapse defaultActiveKey={['RecipeStepForm']} expandIconPosition="right" className="FormRecipe_collapse">
      <Panel header={<h3>Préparation</h3>} key="RecipeStepForm" className="FormRecipe_panel">
        <DragDropContext onDragEnd={onDragEnd}>
          <Droppable droppableId="droppable">
            {(droppableProvided, droppableSnapshot) => (
              <div
                ref={droppableProvided.innerRef}
                style={getListStyle(droppableSnapshot.isDraggingOver, listSteps.length)}
              >
                {map(listSteps, ({ idFront, description }, index) => (
                  <article className="step_item" key={`${index}-step`}>
                    <Draggable key={`Draggable-${idFront}`} draggableId={`${idFront}-step`} index={index}>
                      {draggableProvided => (
                        <div
                          ref={draggableProvided.innerRef}
                          {...draggableProvided.draggableProps}
                          {...draggableProvided.dragHandleProps}
                        >
                          <label key={`${index}-label`} className={`${idFront}-recipeStep`}>
                            Etape {index + 1}
                          </label>
                          <RecipeStepElement
                            key={`${idFront}-recipeStep`}
                            id={idFront}
                            description={description}
                            removeStep={removeStep}
                            changeDescription={changeDescription}
                          />
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
          <Button type="default" onClick={addStep}>
            Ajouter une étape
          </Button>
        </div>
      </Panel>
    </Collapse>
  )
}

export default RecipeStepForm
