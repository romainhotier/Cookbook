import React from 'react'
import { Form, Checkbox, Col, Row } from 'antd'

import './_Form.scss'

export const CheckboxWithImage = ({ label, name, required = false, error = '', datas }) => (
  <Form.Item label={label} name={name} rules={[{ required, message: error }]}>
    <Checkbox.Group style={{ width: '100%' }}>
      <Row gutter={16}>
        {datas.map((data, index) => (
          <Col span={4} key={index}>
            <Checkbox className="iconCheckbox" key={index} value={data.title}>
              <i className={data.icon}></i> {data.title}
            </Checkbox>
          </Col>
        ))}
      </Row>
    </Checkbox.Group>
  </Form.Item>
)
