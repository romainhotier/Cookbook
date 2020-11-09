import React from "react";
import { Form, Input as InputAntd } from "antd";

export const Input = ({label, name, required = false, error = ''}) => (
  <Form.Item
    label={label}
    name={name}
    rules={[{ required, message: error }]}
  >
    <InputAntd />
  </Form.Item>
);

