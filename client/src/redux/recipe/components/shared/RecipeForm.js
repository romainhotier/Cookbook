import React from 'react'
//import PropTypes from 'prop-types'
import { withFormik } from 'formik'
import { Icon, Upload, Button, Form, Row, Col } from 'antd'

import { string_to_slug } from 'components/form/SlugMethod'
import { levels } from '../../sources/levels'
import InputForm from 'components/form/InputForm'
import SelectForm from 'components/form/SelectForm'
import RecipeFormStape from './partialsForm/RecipeFormStape'
import RecipeFormIngredient from './partialsForm/RecipeFormIngredient'

import './_RecipeForm.scss'

const onSubmit = (values, { props }) => {
  const { handleSubmit } = props

  let ingredients = []

  values.ingredients.forEach((item) => {
    let nameSlugify = string_to_slug(item.name)
    ingredients.push({
      name: item.name,
      unity: item.unity,
      quantity: item.quantity,
      slug: nameSlugify,
    })
  })
  values['ingredients'] = ingredients
  handleSubmit(values, values.id)
}

class recipeForm extends React.Component {
  constructor(props) {
    super(props)
    let nbStape = 0

    if (props.values.stape4 !== (undefined || '')) {
      nbStape = 4
    } else if (props.values.stape3 !== (undefined || '')) {
      nbStape = 3
    } else if (props.values.stape2 !== (undefined || '')) {
      nbStape = 2
    } else {
      nbStape = 1
    }

    this.state = {
      stape: nbStape,
      selectedFile: null,
      loaded: 0,
    }
  }

  componentDidMount() {
    if (this.props.recipes === undefined || this.props.recipes === null  || this.props.recipes.image === '') {
      return
    }

    this.setState({
      fileList: [
        {
          uid: '-1',
          name: `${this.props.recipes.title}`,
          status: 'done',
          url: `http://localhost:5000/${this.props.recipes.image}`,
          thumbUrl: `http://localhost:5000/${this.props.recipes.image}`,
        },
      ],
    })
  }

  render() {
    const uploads = {
      onRemove: (file) => {
        this.setState((state) => {
          const index = state.fileList.indexOf(file)
          const newFileList = state.fileList.slice()
          newFileList.splice(index, 1)
          return { fileList: newFileList }
        })
      },
      beforeUpload: (file) => {
        this.setState({
          fileList: [file],
        })
        this.props.setFieldValue('image', file)
        return false
      },
    }

    const {
      values,
      handleSubmit,
      isSubmitting,
      handleChange,
      categoriesList,
      setFieldValue,
    } = this.props

    const categoriesOption = categoriesList === undefined ? [] : categoriesList
    return (
      <Form className="form recipeForm" onSubmit={handleSubmit}>
        <Row gutter={32} className="recipeForm_stape ">
          <h2 className="titleStape">Etape 1</h2>
          <Col xs={24} sm={24} md={18} lg={18} xl={18}>
            <h4>Informations importantes</h4>
            {/* TITRE */}
            <InputForm
              className="form_block"
              handleChange={handleChange}
              label="Titre"
              name="title"
              value={values.title}
            />

            {/* CATEGORIES */}
            <SelectForm
              dataOption={categoriesOption}
              defaultValue="Catégorie(s) de la recipe"
              itemField={values.categories}
              label="Catégories"
              mode="multiple"
              name="categories"
              setFieldValue={setFieldValue}
              typeDataOption="object"
            />

            {/* LEVEL */}
            <SelectForm
              dataOption={levels}
              defaultValue="Niveau de difficulé"
              itemField={values.level}
              label="Niveau de difficulé"
              name="level"
              setFieldValue={setFieldValue}
              typeDataOption="object"
            />

            {/* DESCRIPTION */}
            <InputForm
              className="form_block"
              handleChange={handleChange}
              label="Description"
              name="resume"
              value={values.resume}
            />
          </Col>
          <Col xs={24} sm={24} md={6} lg={6} xl={6}>
            <h4>Compléments</h4>
            {/* PREPARE TIME */}
            <InputForm
              addonAfter="minutes"
              className="form_block"
              handleChange={handleChange}
              label="Temps de préparation"
              name="preparationTime"
              value={values.preparationTime}
            />
            {/* COOKING TIME */}
            <InputForm
              addonAfter="minutes"
              className="form_block"
              handleChange={handleChange}
              label="Temps de cuisson"
              name="cookingTime"
              value={values.cookingTime}
            />
            {/* NB PERSONNE */}
            <InputForm
              addonAfter={<Icon type="user" />}
              className="form_block"
              handleChange={handleChange}
              label="Nombre de personne"
              name="nbPeople"
              value={values.nbPeople}
            />
          </Col>
        </Row>

        <Row gutter={32} className="recipeForm_stape prepaAndIngredients">
          <h2 className="titleStape">Etape 2</h2>
          <Col xs={24} sm={24} md={14} lg={14} xl={14}>
            <RecipeFormStape
              state={this.state}
              stape1={values.stape1}
              stape2={values.stape2}
              stape3={values.stape3}
              stape4={values.stape4}
              handleChange={handleChange}
            />
            {this.state.stape < 4 ? (
              <Button
                className="form_button form_button_addStape"
                onClick={() => {
                  this.setState({ stape: this.state.stape + 1 })
                }}
              >
                Ajouter une étape
              </Button>
            ) : (
              ''
            )}
          </Col>
          <Col xs={24} sm={24} md={10} lg={10} xl={10}>
            <RecipeFormIngredient ingredients={values.ingredients} handleChange={handleChange} />
          </Col>
        </Row>

        <Row gutter={32} className="recipeForm_stape prepaAndIngredients">
          <h2 className="titleStape">Etape 3</h2>
          <Col xs={24} sm={24} md={14} lg={14} xl={14}>
            <h4>Infos supplémentaires</h4>
            <InputForm
              className="form_block"
              handleChange={handleChange}
              label="Note"
              name="note"
              value={values.note}
            />
          </Col>
          <Col xs={24} sm={24} md={10} lg={10} xl={10}>
            <h4>Photo de la recette</h4>
            <div className="form_block">
              <label htmlFor="civilLiabilityFile" className="form_label">
                Image
              </label>
              <div className="inputAndFilesUploads">
                <Upload {...uploads} fileList={this.state.fileList} listType="picture">
                  <Button>
                    <Icon type="upload" /> Importer
                  </Button>
                </Upload>
              </div>
            </div>
          </Col>
        </Row>
        <div className="form_block TxtRight">
          <Button type="primary" htmlType="submit" disabled={isSubmitting}>
            Enregistrer
          </Button>
        </div>
      </Form>
    )
  }
}

const recipeFormFormik = withFormik({
  mapPropsToValues: (props) => ({
    id: props.recipe && props.recipe.id ? props.recipe.id : 0,
    title: props.recipe && props.recipe.title ? props.recipe.title : '',
    level: props.recipe && props.recipe.level ? props.recipe.level : '',
    resume: props.recipe && props.recipe.resume ? props.recipe.resume : '',
    categories: props.recipe && props.recipe.categories ? categoriesPropsToValue(props.recipe.categories, props.categoriesList) : [],
    cookingTime: props.recipe && props.recipe.cookingTime ? props.recipe.cookingTime : 0,
    preparationTime:
      props.recipe && props.recipe.preparationTime ? props.recipe.preparationTime : 0,
    nbPeople: props.recipe && props.recipe.nbPeople ? props.recipe.nbPeople : 0,
    stape1: props.recipe && props.recipe.stape1 ? props.recipe.stape1 : '',
    stape2: props.recipe && props.recipe.stape2 ? props.recipe.stape2 : '',
    stape3: props.recipe && props.recipe.stape3 ? props.recipe.stape3 : '',
    stape4: props.recipe && props.recipe.stape4 ? props.recipe.stape4 : '',
    ingredients: props.recipe && props.recipe.ingredients ? ingredientPropsToValue(props.recipe.ingredients) : [{ name: '', quantity: '', unity: '' }],
    note: props.recipe && props.recipe.note ? props.recipe.note : '',
    image: props.recipe && props.recipe.image ? props.recipe.image : '',
  }),
  handleSubmit: onSubmit,
})(recipeForm)

const ingredientPropsToValue = (props) => {
  let ingredients = []

  Object.keys(props).forEach((item) => {
    ingredients.push({
      name: props[item].name,
      quantity: props[item].quantity,
      unity: props[item].unity ? props[item].unity : '',
    })
  })
  return ingredients
}

const categoriesPropsToValue = (props, allCategories) => {
  let categories = props.split(',')
  let categoriesID = []
  for (const category of Object.values(allCategories)) {
    for(const categoryName of categories) {
      if(category.name === categoryName) {
        categoriesID.push(category.id)
      }
    }
  }

  return categoriesID
}

export default recipeFormFormik

/* recipeFormFormik.propTypes = {
    title: PropTypes.string.isRequired,
    ingredients: PropTypes.array.isRequired,
    level: PropTypes.string.isRequired,
} */
