import React from 'react'
import PropTypes from 'prop-types'
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

Input.propTypes = {
  label: PropTypes.string,
  name: PropTypes.string,
  required: PropTypes.bool,
  error: PropTypes.string,
  placeholder: PropTypes.string,
  hidden: PropTypes.bool,
}
