import AppRoutes from 'Routes'

export class Routes extends AppRoutes {
  static ingredient(param) {
    return super.build('ingredients', super.base(), param)
  }

  static ingredientAdd() {
    return super.build('ajouter', Routes.ingredient())
  }

  static ingredientDetails(param) {
    return super.build(':slug', Routes.ingredient(), param)
  }

  static ingredientEdit(param) {
    return super.build('modifier/:id', Routes.ingredient(), param)
  }
}

export default Routes
