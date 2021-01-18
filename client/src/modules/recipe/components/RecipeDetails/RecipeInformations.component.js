import React from 'react'

import * as listIcons from 'ressources/iconsGlobals'

import './_RecipeDetails.scss'

export const RecipeInformations = ({ label, value, icon }) => {
  return (
    <div className="RecipeDetails_information">
      <img
        alt={`${icon}`}
        className={`RecipeDetails_information_icon`}
        src={listIcons[`${icon}`]}
        width="40"
        height="40"
      />
      <br />
      <strong className="RecipeDetails_information_label">{label}</strong>
      <br />
      <span className="RecipeDetails_information_value">{value}</span>
    </div>
  )
}
