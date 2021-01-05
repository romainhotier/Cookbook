import React, { useState } from 'react'
import PropTypes from 'prop-types'
import { Upload as UploadAntd, Button, Form } from 'antd'

import './_Form.scss'

const normFile = e => {
  if (Array.isArray(e)) {
    return e
  }
  return e && e.fileList
}

export const Upload = ({ label, name, files = [] }) => {
  const [filesUpladed, setFilesUpladed] = useState([])

  const uploads = {
    onRemove: file => {
      const index = filesUpladed.indexOf(file)
      const newFileList = filesUpladed.slice()
      newFileList.splice(index, 1)
      return setFilesUpladed(newFileList)
    },
    beforeUpload: file => {
      console.log('beforeUpload file', file)
      setFilesUpladed([...filesUpladed, file])

      return false
    },
  }

  console.log('filesUpladed', filesUpladed)
  return (
    <>
      <Form.Item name={name} label={label} valuePropName="fileList" getValueFromEvent={normFile}>
        <UploadAntd {...uploads} listType="picture" file={filesUpladed} className="upload-list-inline">
          <Button>Upload</Button>
        </UploadAntd>
      </Form.Item>
    </>
  )
}

Upload.propTypes = {
  label: PropTypes.string,
  name: PropTypes.string,
  // required: PropTypes.bool,
  // error: PropTypes.string,
  files: PropTypes.array,
}
