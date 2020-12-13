import React from 'react'
import { Form, Input as InputAntd } from 'antd'

export const Input = ({
  label,
  name,
  required = false,
  value,
  error = '',
  placeholder = '',
  hidden = false,
  ...props
}) => (
  <Form.Item label={label} name={name} rules={[{ required, message: error }]} hidden={hidden}>
    <InputAntd placeholder={placeholder} value={value} {...props} />
  </Form.Item>
)
