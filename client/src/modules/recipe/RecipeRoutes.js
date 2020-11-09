import AppRoutes from 'Routes'

export class Routes extends AppRoutes {
  static recipe(param) {
    return super.build('recettes', super.base(), param)
  }

  static recipeAdd() {
    return super.build('ajouter', Routes.recipe())
  }

  static recipeDetails(param) {
    return super.build(':slug', Routes.recipe(), param)
  }

  static recipeEdit(param) {
    return super.build('modifier/:id', Routes.recipe(), param)
  }
}

export default Routes
