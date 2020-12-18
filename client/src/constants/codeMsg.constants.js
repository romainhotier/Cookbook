export const codeMsg = {
  cookbook: {
    recipe: {
      success: {
        created: `La recette vient d'être ajoutée !`,
      },
      error: {
        bad_request: {
          already_exist: value => `La recette "${value}" existe déjà.`,
        },
      },
    },
    ingredient: {
      success: {
        created: `L'ingrédient vient d'être ajouté à la liste !`,
        ok: `Bien enregisté en base ;)`,
      },
      error: {
        bad_request: {
          already_exist: value => `L'ingrédient ${value} existe déjà.`,
        },
      },
    },
  },
}
