import { connect } from "react-redux";
import React, { Component } from "react";

import { fetchAllIngredients } from 'modules/ingredient/thunks'

class RecipeIngredientsForm extends Component {
  componentDidMount() {
    this.props.fetchAllIngredients();
  }

  render() {
    const { ingredients } = this.props
    console.log(ingredients)

    if( Object.entries(ingredients).length === 0 ) {
      return 'loader'
    }
    console.log(ingredients)
    const dataIngredients = Object.values(ingredients).map(ing => ({value: ing.name, salut: ing._id, label: ing.name}))

    return (
      <>
        <h2>Ingrédients</h2>
        {/* Ingrédients */}

        {/* <Input
          label="Ingrédient"
          name="ingredient"
          required={RecipeValidator["title"].required}
          error={RecipeValidator["title"].errorMessage}
          placeholder={RecipeValidator["title"].placeholder}
        /> */}
      </>
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
