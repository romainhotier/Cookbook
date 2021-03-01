import AppRoutes from 'Routes'

export class Routes extends AppRoutes {
  static myAccount(param) {
    return super.build('mon-compte', super.base(), param)
  }
  static myAccountSaveRecipes() {
    return super.build('recettes-non-terminees', Routes.myAccount())
  }
  static myAccountFavorites() {
    return super.build('recettes-favoris', Routes.myAccount())
  }
}

export default Routes
