export const IngredientValidator = {
  name: {
    required: true,
    errorMessage: "Le nom de l'ingrédient est obligatoire.",
    placeholder: 'ex: Beurre de cacahuètes',
  },
  categories: {
    required: false,
    errorMessage: '',
    placeholder: 'ex: Purée oléagineux',
  },
  calories: {
    required: false,
    errorMessage: '',
    placeholder: 'ex: 300',
  },
  proteine: {
    required: false,
    errorMessage: '',
    placeholder: 'ex: 30',
  },
  glucide: {
    required: false,
    errorMessage: '',
    placeholder: 'ex: 45',
  },
  lipide: {
    required: false,
    errorMessage: '',
    placeholder: 'ex: 30',
  },
}
