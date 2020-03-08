import React from 'react'
import { Field } from 'formik'
import { Input } from 'antd'

const { TextArea } = Input

const recipeFormStape = ({ state, stape1, stape2, stape3, stape4, handleChange }) => {

  return (
    <>
      <h4>Préparation</h4>
      <div className="form_block">
        <label className="form_label" htmlFor="stape1">
          Etape 1
        </label>
        <Field
          autosize={{ minRows: 2, maxRows: 6 }}
          className="form_element"
          component={TextArea}
          defaultValue={stape1}
          id="stape1"
          onChange={handleChange}
          placeholder="Etape 1"
        />
      </div>
      {state.stape > 1 || stape2 !== (undefined || "") ? (
        <div className="form_block">
          <label className="form_label" htmlFor="stape1">
            Etape 2
          </label>
          <Field
            autosize={{ minRows: 2, maxRows: 6 }}
            className="form_element"
            component={TextArea}
            defaultValue={stape2}
            id="stape2"
            onChange={handleChange}
            placeholder="Etape 2"
          />
        </div>
      ) : (
        ''
      )}
      {state.stape > 2 || stape3 !== (undefined || "") ? (
        <div className="form_block">
          <label className="form_label" htmlFor="stape1">
            Etape 3
          </label>
          <Field
            autosize={{ minRows: 2, maxRows: 6 }}
            placeholder="Etape 3"
            className="form_element"
            component={TextArea}
            id="stape3"
            defaultValue={stape3}
            onChange={handleChange}
          />
        </div>
      ) : (
        ''
      )}
      {state.stape > 3 || stape4 !== (undefined || "") ? (
        <div className="form_block">
          <label className="form_label" htmlFor="stape1">
            Etape 4
          </label>
          <Field
            autosize={{ minRows: 2, maxRows: 6 }}
            placeholder="Etape 4"
            className="form_element"
            component={TextArea}
            id="stape4"
            defaultValue={stape4}
            onChange={handleChange}
          />
        </div>
      ) : (
        ''
      )}

    </>
  )
}

export default recipeFormStape
