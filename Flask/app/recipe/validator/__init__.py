from app.recipe.validator import DeleteRecipe, DeleteRecipeStep, GetAllRecipe, GetRecipe, GetIngredientForRecipe, \
    PostRecipe, PostRecipeStep, PostStep, PutRecipe, PutRecipeStep

ValidatorDeleteRecipe = DeleteRecipe.Validator()
ValidatorDeleteRecipeStep = DeleteRecipeStep.Validator()
ValidatorGetAllRecipe = GetAllRecipe.Validator()
ValidatorGetIngredientForRecipe = GetIngredientForRecipe.Validator()
ValidatorGetRecipe = GetRecipe.Validator()
ValidatorPostRecipe = PostRecipe.Validator()
ValidatorPostRecipeStep = PostRecipeStep.Validator()
ValidatorPostStep = PostStep.Validator()
ValidatorPutRecipe = PutRecipe.Validator()
ValidatorPutRecipeStep = PutRecipeStep.Validator()
