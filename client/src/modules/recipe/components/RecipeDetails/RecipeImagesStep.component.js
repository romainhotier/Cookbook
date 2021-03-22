import React from 'react'
import PropTypes from 'prop-types'
import { Row, Col, Image } from 'antd'

import './_RecipeDetails.scss'

export const RecipeImagesStep = ({ files }) => {
  if (files === undefined) {
    return ''
  }

  return (
    <div className="RecipeDetails_images_step">
      <Row>
        {files.map((file, index) => (
          <Col span={8} key={`file-${index}`}>
            <Image key={`${file}`} src={`${process.env.REACT_APP_IMAGES_SERVER}/${file}`} />
          </Col>
        ))}
      </Row>
    </div>
  )
}

RecipeImagesStep.propTypes = {
  files: PropTypes.array,
}
