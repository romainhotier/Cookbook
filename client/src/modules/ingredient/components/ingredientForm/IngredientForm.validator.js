export const IngredientValidator = {
  name: {
    required: true,
    errorMessage: "Le nom de l'ingrédient est obligatoire.",
    placeholder: 'ex: Banane',
  },
  categories: {
    required: false,
    errorMessage: '',
    placeholder: 'ex: Purée oléagineux',
  },
  unit: {
    required: true,
    errorMessage: '',
    placeholder: 'grammes',
  },
  portion: {
    required: false,
    errorMessage: '',
    placeholder: 'ex: 120',
  },
  calories: {
    required: false,
    errorMessage: '',
    placeholder: 'ex: 300',
  },
  proteins: {
    required: false,
    errorMessage: '',
    placeholder: 'ex: 30',
  },
  carbohydrates: {
    required: false,
    errorMessage: '',
    placeholder: 'ex: 45',
  },
  fats: {
    required: false,
    errorMessage: '',
    placeholder: 'ex: 30',
  },
}
