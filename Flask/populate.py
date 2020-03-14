import app.ingredient.ingredient.model as ingredient
import app.recipe.recipe.model as recipe

ingredient1 = ingredient.IngredientTest().custom({"name": "oeuf"}).insert()
ingredient2 = ingredient.IngredientTest().custom({"name": "carotte"}).insert()
ingredient3 = ingredient.IngredientTest().custom({"name": "chocolat"}).insert()


recipe1 = recipe.RecipeTest().custom({
                     "title": "ratatouille",
                     "level": "1",
                     "resume": "comment faire une bonne ratatouille",
                     "cooking_time": "1h30",
                     "preparation_time": "1h",
                     "nb_people": "3",
                     "note": "super bonne ratatouille pas trop calorique de chez auchan rayon bio",
                     "steps": []
                     })
recipe1.add_step(_id_step="111111111111111111111111", step="deviser le pot")
recipe1.add_step(_id_step="122222222222222222222222", step="verser dans la caserolle")
recipe1.insert()

recipe2 = recipe.RecipeTest().custom({
                     "title": "crepe",
                     "level": "2",
                     "resume": "crepe pour faire plaisirs à sa petite cherie",
                     "cooking_time": "2min",
                     "preparation_time": "20min",
                     "nb_people": "1",
                     "note": "avec amour c'est encore meilleur",
                     "steps": []
                     })
recipe2.add_step(_id_step="211111111111111111111111", step="verser la farine avec des oeufs")
recipe2.add_step(_id_step="222222222222222222222222", step="rajouter du lait")
recipe2.add_step(_id_step="233333333333333333333333", step="mettre de la cuvé des trolls")
recipe2.insert()

recipe3 = recipe.RecipeTest().custom({
                     "title": "gateau au chocolat",
                     "level": "2",
                     "resume": "super gateau au chocolat bien goutu",
                     "cooking_time": "40min",
                     "preparation_time": "20min",
                     "nb_people": "6",
                     "note": "on peut le faire fondant ou bien cuit",
                     "steps": []
                     })
recipe3.add_step(_id_step="311111111111111111111111", step="fondre le chocolat avec du beurre")
recipe3.add_step(_id_step="322222222222222222222222", step="rajouter la farine et plein d'autre truc")
recipe3.add_step(_id_step="333333333333333333333333", step="au four")
recipe3.add_step(_id_step="344444444444444444444444", step="manger")
recipe3.insert()

