import React, { Component } from 'react'

class CategoryElement extends Component {

  render() {
    const { categories, whenDisplay } = this.props

    if (categories === undefined) {
      return 'Patientez'
    }

    const listOfCategories = (whenDisplay === 'list') ? categories.split(',') : categories
    return (
      <span>
        {listOfCategories.map((category, key) => {
          let separator = key === 0 ? '' : ' -'
          if(whenDisplay === 'list') {
            return (
              <strong key={key}>
                {separator} {category}
              </strong>
            )
          } else {
            return (
              <strong key={key}>
                {separator} {category.name}
              </strong>
            )
          }

        })}
      </span>
    )
  }
}

export default CategoryElement
