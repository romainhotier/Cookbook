import React from 'react'
import PropTypes from 'prop-types'
import { Carousel as CarouselAntd } from 'antd'

import './_Carousel.scss'

const Carousel = ({ files, className = '', heightImage = '400px' }) => {
  return (
    <CarouselAntd className={className} dots={{ className: 'carousel_dots' }}>
      {files &&
        files.map((image, index) => (
          <div key={`containerImg-${index}`}>
            <div
              key={`img-${index}`}
              className="carousel_img"
              style={{ backgroundImage: `url(${process.env.REACT_APP_IMAGES_SERVER}/${image})`, height: heightImage }}
            ></div>
          </div>
        ))}
    </CarouselAntd>
  )
}

Carousel.propTypes = {
  files: PropTypes.array,
  className: PropTypes.string,
  heightImage: PropTypes.string,
}

export default Carousel
