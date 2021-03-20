import AppRoutes from 'Routes'

export class Routes extends AppRoutes {
  static ingredient(param) {
    return super.build('ingredients', super.base(), param)
  }
}

export default Routes
