import React from 'react'
import PropTypes from 'prop-types'
import { Divider } from 'antd'

import { ReactComponent as CookTimesSVG } from 'ressources/iconsGlobals/cook_times.svg'
import { ReactComponent as CaloriesSVG } from 'ressources/iconsGlobals/calories.svg'
import { ReactComponent as TimesSVG } from 'ressources/iconsGlobals/times.svg'

import './_RecipeDetails.scss'

export const RecipeInformations = ({ preparation_time, cooking_time, caloriesForOnePortion }) => {
  return (
    <div className="RecipeDetails_informations">
      {preparation_time ? (
        <>
          <div className="RecipeDetails_information">
            <TimesSVG className={`RecipeDetails_information_icon`} />
            <br />
            <strong className="RecipeDetails_information_label">Temps de préparation</strong>
            <br />
            <span className="RecipeDetails_information_value">{`${preparation_time} min`}</span>
          </div>
          <Divider type="vertical" />
        </>
      ) : (
        ''
      )}

      {cooking_time ? (
        <>
          <div className="RecipeDetails_information">
            <CookTimesSVG className={`RecipeDetails_information_icon`} />
            <br />
            <strong className="RecipeDetails_information_label">Temps de cuisson</strong>
            <br />
            <span className="RecipeDetails_information_value">{`${cooking_time} min`}</span>
          </div>
          <Divider type="vertical" />
        </>
      ) : (
        ''
      )}

      {caloriesForOnePortion ? (
        <div className="RecipeDetails_information">
          <CaloriesSVG className={`RecipeDetails_information_icon`} />
          <br />
          <strong className="RecipeDetails_information_label">Calories par portions</strong>
          <br />
          <span className="RecipeDetails_information_value">{caloriesForOnePortion}</span>
        </div>
      ) : (
        ''
      )}
    </div>
  )
}

RecipeInformations.propTypes = {
  preparation_time: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
  cooking_time: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
  caloriesForOnePortion: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
}
