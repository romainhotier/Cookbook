import React from 'react'
import PropTypes from 'prop-types'
import { Form, Checkbox } from 'antd'

import * as listIconsCategories from 'ressources/iconsCategories/Icons'

import './_Form.scss'

export const CheckboxWithImage = ({ label, name, required = false, error = '', datas }) => (
  <Form.Item label={label} name={name} rules={[{ required, message: error }]}>
    <Checkbox.Group className={'checkboxWithImage'} style={{ width: '100%' }}>
      {datas.map((data, index) => {
        const img = data.icon ? (
          <img src={listIconsCategories[`${data.icon}`]} alt={data.title} width="20" height="20" />
        ) : (
          ''
        )
        return (
          <Checkbox className="iconCheckbox" key={`checkbox-${index}`} value={data.title}>
            {data.title}
          </Checkbox>
        )
      })}
    </Checkbox.Group>
  </Form.Item>
)

CheckboxWithImage.propTypes = {
  label: PropTypes.string,
  name: PropTypes.string,
  required: PropTypes.bool,
  error: PropTypes.string,
  datas: PropTypes.array,
}
