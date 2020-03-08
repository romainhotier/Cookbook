import React from 'react'
import { Select } from 'antd'
import { Field } from 'formik'

const { Option } = Select

const buildOptions = (options = [], type, defaultValue) => {
  let dataOptions = []

  dataOptions.push(
    <Option key="-1" disabled value="">
      {defaultValue}
    </Option>
  )
  if (type === 'object') {
    if(Object.keys(options).length !== 0) {
      Object.values(options).forEach((value) =>
        dataOptions.push(
          <Option key={value.id} value={value.id}>
            {value.name}
          </Option>
        )
      )
    }
  } else if (type === 'array') {
    dataOptions = options.map((value, index) => (
      <Option key={index} value={value}>
        {value}
      </Option>
    ))
  }

  return dataOptions
}

const SelectForm = ({
  dataOption,
  defaultValue,
  itemField,
  label,
  mode,
  name,
  setFieldValue,
  typeDataOption
}) => {
  return (
    <div className="form_block">
      <label className="form_label" htmlFor={name}>
        {label}
      </label>
      <Field
        placeholder={label}
        className="form_element"
        component={Select}
        id={name}
        defaultValue={itemField}
        mode={mode}
        onChange={(value) => setFieldValue(name, value)}
        required
      >
        {buildOptions(dataOption, typeDataOption, defaultValue)}
      </Field>
    </div>

  )
}

export default SelectForm
