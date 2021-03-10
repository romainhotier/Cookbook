import React, { useState, useEffect } from 'react'
import PropTypes from 'prop-types'
import { Form } from 'antd'
import { connect } from 'react-redux'
import find from 'lodash/find'

import { getAllRecipes } from 'modules/recipe/reducers'
import { Upload } from 'components/Form/Upload.component'
import { displayFile } from 'components/Form/Upload.helpers'
import { postFileRecipe, deleteFileRecipe } from 'modules/recipe/thunks'

import './_RecipeUploadFiles.scss'

const UploadFilesRecipe = ({ _id, postFileRecipe, deleteFileRecipe, recipesList }) => {
  const recipe = find(recipesList.toJS(), recipe => recipe._id === _id)
  const filesFormated = recipe.files !== undefined ? recipe.files.map((file, index) => displayFile(file, index)) : []
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
    postFileRecipe(_id, formData)
  }

  const deleteFileInRecipe = ({ url, name }) => {
    if (url === undefined) {
      const fileState = find(filesUpladed, file => file.name === name)
      return deleteFileRecipe(fileState.url)
    }

    deleteFileRecipe(url)
  }

  return (
    <div className="RecipeDetails_uploadImages">
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
  postFileRecipe,
  deleteFileRecipe,
}

UploadFilesRecipe.propTypes = {
  _id: PropTypes.string,
  files: PropTypes.array,
  postFileRecipe: PropTypes.func,
  deleteFileRecipe: PropTypes.func,
}

export default connect(mapStateToProps, mapDispatchToProps)(UploadFilesRecipe)
