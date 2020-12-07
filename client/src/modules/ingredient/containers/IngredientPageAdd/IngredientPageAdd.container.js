import { connect } from "react-redux";
import React, { useState, useEffect } from "react";
import { Modal, Button, Form, Row, Col } from "antd";

import { slugify } from "constants/functions.constants";
import { Input } from "components/Form/Input.component";
import { postIngredient } from "../../thunks";
import { IngredientValidator } from "./IngredientPageAdd.validator";

const IngredientPageAdd = ({ loadingPostIngredients, ingredients, postIngredient }) => {
  const [modalVisible, setModalVisible] = useState(false);

  useEffect(() => {
    setModalVisible(false)
  }, [ingredients])

  const onFinish = (values) => {
    const slug = slugify(values.name)
    postIngredient({ ...values, slug})
  };

  return (
    <>
      <Button type="primary" onClick={() => setModalVisible(true)}>
        Ajouter un nouvel ingrédient
      </Button>
      <Modal
        title="Ajouter un nouvel ingrédient"
        visible={modalVisible}
        footer={null}
        onCancel={() => setModalVisible(false)}
        width={'80%'}
      >
        <Form
          name="IngredientPageAdd"
          layout="vertical"
          onFinish={onFinish}
        >
          <Input
            label="Nom de l'ingrédient"
            name="name"
            required={IngredientValidator['name'].required}
            error={IngredientValidator['name'].errorMessage}
            placeholder={IngredientValidator['name'].placeholder}
          />
          <Input
            label="Groupe alimentaire"
            name="categories"
            required={IngredientValidator['categories'].required}
            error={IngredientValidator['categories'].errorMessage}
            placeholder={IngredientValidator['categories'].placeholder}
          />

          <Row gutter={32}>
            <Col span={6}>
              <Input
                label="Nombre de calories"
                name="calories"
                required={IngredientValidator['calories'].required}
                error={IngredientValidator['calories'].errorMessage}
                placeholder={IngredientValidator['calories'].placeholder}
              />
            </Col>
            <Col span={6}>
              <Input
                label="Protéine"
                name="proteine"
                required={IngredientValidator['proteine'].required}
                error={IngredientValidator['proteine'].errorMessage}
                placeholder={IngredientValidator['proteine'].placeholder}
              />
            </Col>
            <Col span={6}>
              <Input
                label="Glucide"
                name="glucide"
                required={IngredientValidator['glucide'].required}
                error={IngredientValidator['glucide'].errorMessage}
                placeholder={IngredientValidator['glucide'].placeholder}
              />
            </Col>
            <Col span={6}>
              <Input
                label="Lipide"
                name="lipide"
                required={IngredientValidator['lipide'].required}
                error={IngredientValidator['lipide'].errorMessage}
                placeholder={IngredientValidator['lipide'].placeholder}
              />
            </Col>
          </Row>
          <Form.Item style={{ textAlign: 'right' }}>
            <Button type="primary" htmlType="submit" loading={loadingPostIngredients} disabled={loadingPostIngredients}>
              Créer
            </Button>
          </Form.Item>
        </Form>
      </Modal>
    </>
  );
};

const mapDispatchToProps = {
  postIngredient,
};

const mapStateToProps = ({
  ingredients: { content, loadingPostIngredients },
}) => ({ ingredients: content, loadingPostIngredients });

export default connect(mapStateToProps, mapDispatchToProps)(IngredientPageAdd);
