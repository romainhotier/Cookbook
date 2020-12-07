import { connect } from "react-redux"
import React, { Component } from "react"
import { Select, Table } from 'antd'
import keyBy from 'lodash/keyBy'
import omitBy from 'lodash/omitBy'

import { fetchAllIngredients } from 'modules/ingredient/thunks'
import { columns } from "./RecipeIngredientsColumn";

import './_RecipeIngredientsForm.scss'

const { Option } = Select

const defaultLineIngredientState = {
  _id_ingredient: null,
  quantity: null,
  unit: null,
  name: null,
}

class RecipeIngredientsForm extends Component {
  constructor(props) {
    super(props)

    this.state = {
      recipeIngredients: [],
      ingredientsById: [],
      researchIngredients: [],
      lineIngredient: {
        _id_recipe: this.props._id_recipe,
        ...defaultLineIngredientState
      }
    }
  }


  componentDidMount() {
    this.props.fetchAllIngredients();
  }

  componentDidUpdate(prevProps, prevState) {
    const {ingredients, setListIngredients} = this.props
    const {recipeIngredients} = this.state

    if(prevProps.ingredients !== ingredients) {
      this.setState({
        ingredientsById: keyBy(ingredients, '_id'),
      })
    }
    if(prevState.recipeIngredients !== recipeIngredients) {
      setListIngredients(recipeIngredients)
    }
  }

  addIngredient = () => {
    const {lineIngredient: {_id_ingredient, quantity}, lineIngredient, recipeIngredients} = this.state
    const {_id_recipe, } = this.props

    if(!!_id_ingredient && !!quantity) {
      this.setState({
        lineIngredient: {
          _id_recipe,
          name: null,
          ...defaultLineIngredientState
        },
        recipeIngredients: [...recipeIngredients, {...lineIngredient, id: recipeIngredients.length}]
      })
    }

  }

  removeIngredient = (id) => {
    const {recipeIngredients} = this.state

    const newRecipeIngredients = omitBy(recipeIngredients, line => line.id === id)

    this.setState({
      recipeIngredients: Object.values(newRecipeIngredients)
    })
  }

  handleChange = (value, elem) => {
    const {lineIngredient, ingredientsById} = this.state
    if(elem === '_id_ingredient' && !!ingredientsById) {
      const infoIng = ingredientsById[value]
      this.setState({lineIngredient: {...lineIngredient, name: infoIng.name, [elem]: value}  })
    } else {
      this.setState({lineIngredient: {...lineIngredient, [elem]: value}  })

    }
  };

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
    const { recipeIngredients, ingredientsById, researchIngredients, lineIngredient } = this.state

    if( Object.entries(ingredients).length === 0 ) {
      return 'loader'
    }

    const options = researchIngredients.map(d => <Option key={d._id}>{d.name}</Option>)

    const listIngredients = recipeIngredients.map((ing) => {
      const infoIng = ingredientsById[ing._id_ingredient]
      return { name: infoIng.name, quantity: ing.quantity, unity: ing.unit, id: ing.id}
    })

    return (
      <div className={recipeExist ? '' : 'blockDisabled'}>
        <h2>Ingrédients</h2>

        <Table
          columns={
            columns(
              disabled,
              this.handleSearch,
              this.handleChange,
              this.addIngredient,
              this.removeIngredient,
              options,
              lineIngredient
            )
          }
          className="ingredients_table"
          dataSource={listIngredients}
          rowKey={record => record.id}
        />
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
