import React, { useState, useEffect } from 'react'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'

import { Upload } from 'components/Form/Upload.component'
import { displayFile } from 'components/Form/Upload.helpers'
import { postFileRecipe, deleteFileRecipe } from 'modules/recipe/thunks'

import './_RecipeUploadFiles.scss'

const UploadFilesRecipe = ({ _id, postFileRecipe, deleteFileRecipe, recipes, slug }) => {
  const recipe = recipes[slug]
  console.log('UploadFilesRecipe files', recipe.files)
  const filesFormated = recipe.files !== undefined ? recipe.files.map((file, index) => displayFile(file, index)) : []

  const [filesUpladed, setFilesUpladed] = useState(filesFormated)

  const addFileInRecipe = file => {
    const formData = new FormData()
    formData.append('files', file)
    postFileRecipe(_id, formData)
  }

  const deleteFileInRecipe = file => {
    deleteFileRecipe(file.url)
  }

  console.log('filesUpladed', filesUpladed)
  return (
    <div className="RecipeDetails_uploadImages">
      <Upload
        label=""
        name="filesRecipe"
        filesUpladed={filesUpladed}
        setFilesUpladed={setFilesUpladed}
        addFileInRecipe={addFileInRecipe}
        deleteFileInRecipe={deleteFileInRecipe}
      />
    </div>
  )
}

const mapDispatchToProps = {
  postFileRecipe,
  deleteFileRecipe,
}

const mapStateToProps = ({ recipes }) => ({
  recipes: recipes.content,
})

UploadFilesRecipe.propTypes = {
  _id: PropTypes.string,
  files: PropTypes.array,
  postFileRecipe: PropTypes.func,
  deleteFileRecipe: PropTypes.func,
}

export default connect(mapStateToProps, mapDispatchToProps)(UploadFilesRecipe)
