from app.ingredient.validator import DeleteIngredient, DeleteIngredientRecipe, GetAllIngredient, GetIngredient, \
    GetRecipeForIngredient, PostIngredient, PostIngredientRecipe, PutIngredient, PutIngredientRecipe

ValidatorDeleteIngredient = DeleteIngredient.Validator()
ValidatorDeleteIngredientRecipe = DeleteIngredientRecipe.Validator()
ValidatorGetAllIngredient = GetAllIngredient.Validator()
ValidatorGetIngredient = GetIngredient.Validator()
ValidatorGetRecipeForIngredient = GetRecipeForIngredient.Validator()
ValidatorPostIngredient = PostIngredient.Validator()
ValidatorPostIngredientRecipe = PostIngredientRecipe.Validator()
ValidatorPutIngredient = PutIngredient.Validator()
ValidatorPutIngredientRecipe = PutIngredientRecipe.Validator()
