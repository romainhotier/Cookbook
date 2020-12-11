import { connect } from "react-redux"
import React, { Component } from "react"
import { Select, Form, Space, Input, Button, Spin } from 'antd'

import { fetchAllIngredients } from 'modules/ingredient/thunks'
import { RecipeIngredientsValidator } from "./RecipeIngredientsForm.validator";

import './_RecipeIngredientsForm.scss'

const { Option } = Select

class RecipeIngredientsForm extends Component {
  constructor(props) {
    super(props)

    this.state = {
      researchIngredients: [],
    }
  }

  componentDidMount() {
    this.props.fetchAllIngredients();
  }

  handleSearch = value => {
    const { ingredients } = this.props
    if (value) {
      const valueLowerCase = value.toLowerCase();
      const filters = Object.values(ingredients).filter(({name = ''}) => {
        const nameLowercase = name.toLowerCase();
        return nameLowercase.search(valueLowerCase) > -1;
      })
      this.setState({researchIngredients: filters})
    }
  };

  render() {
    const { ingredients, recipeExist, disabled } = this.props
    const { researchIngredients } = this.state

    if( Object.entries(ingredients).length === 0 ) {
      return <Spin />
    }

    const options = researchIngredients.map(d => <Option key={d._id}>{d.name}</Option>)

    return (
      <div className={recipeExist ? '' : 'blockDisabled'}>
        <h2>Ingrédients</h2>
          <Form.List name="ingredients">
          {(fields, { add, remove }) => (
            <>
              {fields.map(field => (
                <Space key={field.key} style={{ display: 'flex', marginBottom: 0, alignItems: 'center' }} align="baseline">

                  <Form.Item
                    {...field}
                    name={[field.name, '_id_ingredient']}
                    fieldKey={[field.fieldKey, '_id_ingredient']}
                    rules={[{ required: RecipeIngredientsValidator['name'].required, message: RecipeIngredientsValidator['name'].message }]}
                    label="Nom"
                  >
                    <Select
                      showSearch
                      placeholder={RecipeIngredientsValidator['name'].placeholder}
                      style={{ minWidth: '220px' }}
                      defaultActiveFirstOption={false}
                      showArrow={false}
                      filterOption={false}
                      onSearch={this.handleSearch}
                      notFoundContent={null}
                      value={field.name}
                      disabled={disabled}
                    >
                      {options}
                    </Select>
                  </Form.Item>

                  <Form.Item
                    {...field}
                    name={[field.name, 'quantity']}
                    label="Quantité"
                    fieldKey={[field.fieldKey, 'quantity']}
                    rules={[{ required: RecipeIngredientsValidator['quantity'].required, message: RecipeIngredientsValidator['quantity'].message }]}
                  >
                    <Input placeholder={RecipeIngredientsValidator['quantity'].placeholder} />
                  </Form.Item>

                  <Form.Item
                    {...field}
                    name={[field.name, 'unity']}
                    label="Unité"
                    fieldKey={[field.fieldKey, 'unity']}
                    rules={[{ required: RecipeIngredientsValidator['unity'].required, message: RecipeIngredientsValidator['unity'].message }]}
                  >
                    <Input placeholder={RecipeIngredientsValidator['unity'].placeholder} />
                  </Form.Item>
                  <Button key={field.name} htmlType="button" type="text" onClick={() => remove(field.name)} className='button_remove'>
                    <i className="fas fa-trash"></i>
                  </Button>
                </Space>
              ))}
              <Form.Item>
                <Button type="dashed" onClick={() => add()} block >
                  Ajouter un ingrédient
                </Button>
              </Form.Item>
            </>
          )}
        </Form.List>
      </div>
    );
  }
}

const mapDispatchToProps = {
  fetchAllIngredients,
};

const mapStateToProps = ({ ingredients: { content, loadingFetchIngredients } }) => ({
  ingredients: content,
  loadingFetchIngredients,
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(RecipeIngredientsForm);
