import React from 'react'
import { Form, Checkbox, Col, Row } from 'antd'

import * as listIconsCategories from 'ressources/iconsCategories/Icons'

import './_Form.scss'

export const CheckboxWithImage = ({ label, name, required = false, error = '', datas }) => (
  <Form.Item label={label} name={name} rules={[{ required, message: error }]}>
    <Checkbox.Group style={{ width: '100%' }}>
      <Row gutter={16}>
        {datas.map((data, index) => {
          const img = data.icon ? (
            <img src={listIconsCategories[`${data.icon}`]} alt={data.title} width="20" height="20" />
          ) : (
            ''
          )
          return (
            <Col
              xs={{ span: 12 }}
              sm={{ span: 12 }}
              md={{ span: 6 }}
              lg={{ span: 4 }}
              xl={{ span: 4 }}
              key={`colCheckbox-${index}`}
            >
              <Checkbox className="iconCheckbox" key={`checkbox-${index}`} value={data.title}>
                {img} {data.title}
              </Checkbox>
            </Col>
          )
        })}
      </Row>
    </Checkbox.Group>
  </Form.Item>
)
