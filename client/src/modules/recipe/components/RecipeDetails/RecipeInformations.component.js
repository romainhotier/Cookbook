import React from 'react'

import './_RecipeDetails.scss'

export const RecipeInformations = ({ label, value, icon }) => {
  return (
    <div className="RecipeDetails_information">
      <i className={`RecipeDetails_information_icon ${icon}`}></i>
      <br />
      <strong className="RecipeDetails_information_label">{label}</strong>
      <br />
      <span className="RecipeDetails_information_value">{value}</span>
    </div>
  )
}
