import React from 'react'
import { Card } from 'antd'
import { NavLink } from 'react-router-dom'

import CategoryElement from 'components/recipeElement/CategoryElement'
import TimeElement from 'components/recipeElement/TimeElement'
import Routes from '../RecipeRoutes'

import './_RecipeSingleElement.scss'

const RecipeSingleElement = ({ recipe, whenDisplay }) => {

  const { id, title, level, resume, cookingTime, preparationTime, categories, image } = recipe

  return (
    <div className="recipeSingleElement">
      {(image === undefined || image === '') ? (
        ''
      ) : (
        <div
          className="card_image"
          style={{ backgroundImage: `url(${process.env.REACT_APP_SERVER_URL + '/' + image})` }}
        />
      )}
      <Card
        className="card"
        title={
          <NavLink to={Routes.recipeDetails(id)} exact>
            {title}
          </NavLink>
        }
        extra={<div className={`level level-${level}`} />}
        bordered={false}
      >
        <div className="card_body">{resume}</div>
        <div className="card_footer">
          <div className="card_categories">
            <CategoryElement categories={categories} whenDisplay={whenDisplay}/>
          </div>
          <div className="card_time">
            <TimeElement time={cookingTime + preparationTime} />
          </div>
        </div>
      </Card>
    </div>
  )
}

export default RecipeSingleElement
