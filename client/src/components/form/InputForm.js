import React from 'react'
import { Field } from 'formik'
import { Input } from 'antd'

const InputForm = ({
  addonAfter,
  addonBefore,
  className,
  handleChange,
  label,
  name,
  value
}) => {
  return (
    <div className={className}>
      <label className="form_label" htmlFor={name}>
          {label}
      </label>
      <Field
        addonBefore={addonBefore}
        addonAfter={addonAfter}
        className="form_element"
        component={Input}
        defaultValue={value}
        id={name}
        onChange={handleChange}
        placeholder={label}
      />
    </div>
  )
}

export default InputForm
