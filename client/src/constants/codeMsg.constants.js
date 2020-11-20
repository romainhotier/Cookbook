export const codeMsg = {
  cookbook: {
    ingredient: {
      success: {
        created: `L'ingrédient vient d'être ajouté à la liste !`
      },
      error: {
        bad_request: {
          'already_exist': (value) => `L'ingrédient ${value} existe déjà.`
        }
      }
    }
  }
}
