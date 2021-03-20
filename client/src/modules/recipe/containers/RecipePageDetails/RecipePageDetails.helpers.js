import keyBy from 'lodash/keyBy'

export const useAllIngredients = (allIngredients, ingredients) => {
  const allIngredientsById = keyBy(allIngredients, '_id')
  return ingredients.map(ingredient => ({ ...allIngredientsById[ingredient._id], ...ingredient }))
}
