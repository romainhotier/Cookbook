import AppRoutes from 'Routes'

export class Routes extends AppRoutes {
  static category(param) {
    return super.build('categories', super.base(), param)
  }

}

export default Routes
