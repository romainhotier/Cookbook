import React from 'react'
import PropTypes from 'prop-types'
import { Upload as UploadAntd, Button, Form } from 'antd'

import './_Form.scss'

const normFile = e => {
  if (Array.isArray(e)) {
    return e
  }
  return e && e.fileList
}

export const Upload = ({ label, name, filesUpladed = [], setFilesUpladed, addFileInRecipe, deleteFileInRecipe }) => {
  const uploads = {
    onRemove: file => {
      deleteFileInRecipe(file)
      const index = filesUpladed.indexOf(file)
      const newFileList = filesUpladed.slice()
      newFileList.splice(index, 1)
      return newFileList
    },
    beforeUpload: file => {
      addFileInRecipe(file)
      setFilesUpladed([...filesUpladed, file])
      return false
    },
  }

  return (
    <>
      <Form.Item name={name} label={label} valuePropName="fileList" getValueFromEvent={normFile}>
        <UploadAntd {...uploads} listType="picture" defaultFileList={[...filesUpladed]} className="upload-list-inline">
          <Button>Importer une photo</Button>
        </UploadAntd>
      </Form.Item>
    </>
  )
}

Upload.propTypes = {
  label: PropTypes.string,
  name: PropTypes.string,
  addFileInRecipe: PropTypes.func,
  action: PropTypes.string,
  filesUpladed: PropTypes.array,
  setFilesUpladed: PropTypes.func,
  deleteFileInRecipe: PropTypes.func,
}
