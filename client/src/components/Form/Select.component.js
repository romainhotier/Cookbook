import React from 'react'
import PropTypes from 'prop-types'
import { Form, Select as SelectAntd } from 'antd'

export const Select = ({
  label,
  name,
  required = false,
  value,
  error = '',
  placeholder = '',
  hidden = false,
  options = [],
  ...props
}) => (
  <Form.Item label={label} name={name} rules={[{ required, message: error }]} hidden={hidden}>
    <SelectAntd {...props}>
      {options.map(({ value, label, disabled }) => (
        <SelectAntd.Option key={value} disabled={disabled} value={value}>
          {label}
        </SelectAntd.Option>
      ))}
    </SelectAntd>
  </Form.Item>
)

Select.propTypes = {
  label: PropTypes.string,
  name: PropTypes.string,
  required: PropTypes.bool,
  value: PropTypes.string,
  error: PropTypes.string,
  placeholder: PropTypes.string,
  hidden: PropTypes.bool,
  options: PropTypes.array,
}
