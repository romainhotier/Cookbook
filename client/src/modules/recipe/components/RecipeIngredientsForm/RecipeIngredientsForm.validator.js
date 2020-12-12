export const RecipeIngredientsValidator = {
  name: {
    required: true,
    errorMessage: 'Le nom est obligatoire',
    placeholder: 'ex: Chocolat',
  },
  quantity: {
    required: true,
    errorMessage: 'La quantité est obligatoire',
    placeholder: 'ex: 200',
  },
  unity: {
    required: false,
    errorMessage: '',
    placeholder: 'gr',
  },
}
