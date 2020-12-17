import React from 'react'
import { Form, Select as SelectAntd } from 'antd'

const { Option } = SelectAntd

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
        <Option key={value} disabled={disabled} value={value}>
          {label}
        </Option>
      ))}
    </SelectAntd>
  </Form.Item>
)
