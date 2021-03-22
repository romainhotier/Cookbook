import React, { useState, useEffect } from 'react'
import PropTypes from 'prop-types'
import { Form } from 'antd'
import { connect } from 'react-redux'
import find from 'lodash/find'

import { getAllRecipes } from 'modules/recipe/reducers'
import { Upload } from 'components/Form/Upload.component'
import { displayFile } from 'components/Form/Upload.helpers'
import { postFileRecipeStep, deleteFileRecipeStep } from 'modules/recipe/thunks'

import './_RecipeUploadFiles.scss'

export const UploadFilesRecipeStep = ({
  id_recipe,
  id_step,
  postFileRecipeStep,
  deleteFileRecipeStep,
  recipesList,
}) => {
  const recipe = find(recipesList.toJS(), recipe => recipe._id === id_recipe)
  const step = recipe && find(recipe.steps, step => step._id === id_step)

  let files = step.files ? step.files : []

  const filesFormated = files.map((file, index) => displayFile(file, index))
  const [filesUpladed, setFilesUpladed] = useState(filesFormated)

  useEffect(
    filesFormated => {
      setFilesUpladed(filesFormated)
    },
    [recipesList]
  )

  const addFileInRecipe = file => {
    const formData = new FormData()
    formData.append('files', file)
    postFileRecipeStep({ id_recipe, id_step, data: formData })
  }

  const deleteFileInRecipe = ({ url, name }) => {
    if (url === undefined) {
      const fileState = find(filesUpladed, file => file.name === name)
      return deleteFileRecipeStep(fileState.url)
    }

    deleteFileRecipeStep(url)
  }

  return (
    <div className="RecipeDetails_uploadImages RecipeDetails_uploadStepImages">
      <Form>
        <Upload
          label=""
          name="filesRecipe"
          filesUpladed={filesUpladed}
          setFilesUpladed={setFilesUpladed}
          addFileInRecipe={addFileInRecipe}
          deleteFileInRecipe={deleteFileInRecipe}
        />
      </Form>
    </div>
  )
}

const mapStateToProps = ({ recipes }) => ({
  recipesList: getAllRecipes(recipes),
})

const mapDispatchToProps = {
  postFileRecipeStep,
  deleteFileRecipeStep,
}

UploadFilesRecipeStep.propTypes = {
  id_recipe: PropTypes.string,
  id_step: PropTypes.string,
  recipesList: PropTypes.object,
  postFileRecipeStep: PropTypes.func,
  deleteFileRecipeStep: PropTypes.func,
}

export default connect(mapStateToProps, mapDispatchToProps)(UploadFilesRecipeStep)
