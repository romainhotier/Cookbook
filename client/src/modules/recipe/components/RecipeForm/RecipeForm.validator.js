export const RecipeValidator = {
  title: {
    required: true,
    errorMessage: 'Le titre de la recette est obligatoire.',
    placeholder: 'ex: Tarte aux citrons',
  },
  cooking_time: {
    required: false,
    errorMessage: '',
    placeholder: 'ex: 30',
  },
  preparation_time: {
    required: false,
    errorMessage: '',
    placeholder: 'ex: 45',
  },
  nb_people: {
    required: false,
    errorMessage: '',
    placeholder: 'ex: 26',
  },
}
