from pymongo import MongoClient
from server import mongo_config as mongo_conf
mongo = mongo_conf.MongoConnection()

import app.ingredient.ingredient.model as ingredient
import app.recipe.recipe.model as recipe
import app.link.ingredient_recipe.model as link


""" clean """
client = MongoClient(mongo.ip, mongo.port)
db_recipe = client[mongo.name][mongo.collection_recipe]
db_recipe.delete_many({'title': {'$in': ["ratatouille", "crepe", "gateau au chocolat"]}})
db_ingredient = client[mongo.name][mongo.collection_ingredient]
db_ingredient.delete_many({'name': {'$in': ["oeuf", "carotte", "chocolat"]}})
client.close()


ingredient1 = ingredient.IngredientTest().custom({"name": "oeuf"}).insert()
ingredient2 = ingredient.IngredientTest().custom({"name": "carotte"}).insert()
ingredient3 = ingredient.IngredientTest().custom({"name": "chocolat"}).insert()


recipe1 = recipe.RecipeTest().custom({
                     "title": "ratatouille",
                     "slug": "ratatouille",
                     "level": 1,
                     "resume": "comment faire une bonne ratatouille",
                     "cooking_time": 130,
                     "preparation_time": 10,
                     "nb_people": 3,
                     "note": "super bonne ratatouille pas trop calorique de chez auchan rayon bio",
                     "steps": [],
                     "categories": ["chaud", "legume", "plat"]
                     })
recipe1.add_step(_id_step="111111111111111111111111", step="deviser le pot")
recipe1.add_step(_id_step="122222222222222222222222", step="verser dans la caserolle")
recipe1.insert()

recipe2 = recipe.RecipeTest().custom({
                     "title": "crepe",
                     "slug": "crepe",
                     "level": 2,
                     "resume": "crepe pour faire plaisirs à sa petite cherie",
                     "cooking_time": 2,
                     "preparation_time": 20,
                     "nb_people": 1,
                     "note": "avec amour c'est encore meilleur",
                     "steps": [],
                     "categories": ["chaud", "froid", "gourmand"]
                     })
recipe2.add_step(_id_step="211111111111111111111111", step="verser la farine avec des oeufs")
recipe2.add_step(_id_step="222222222222222222222222", step="rajouter du lait")
recipe2.add_step(_id_step="233333333333333333333333", step="mettre de la cuvé des trolls")
recipe2.insert()

recipe3 = recipe.RecipeTest().custom({
                     "title": "gateau au chocolat",
                     "slug": "gateau_au_chocolat",
                     "level": 2,
                     "resume": "super gateau au chocolat bien goutu",
                     "cooking_time": 40,
                     "preparation_time": 20,
                     "nb_people": 6,
                     "note": "on peut le faire fondant ou bien cuit",
                     "steps": [],
                     "categories": ["chaud", "froid", "gourmand"]
                     })
recipe3.add_step(_id_step="311111111111111111111111", step="fondre le chocolat avec du beurre")
recipe3.add_step(_id_step="322222222222222222222222", step="rajouter la farine et plein d'autre truc")
recipe3.add_step(_id_step="333333333333333333333333", step="au four")
recipe3.add_step(_id_step="344444444444444444444444", step="manger")
recipe3.insert()

link1 = link.LinkIngredientRecipeTest().custom({
    "_id_recipe": recipe1.get_id_objectId(),
    "_id_ingredient": ingredient2.get_id_objectId(),
    "quantity": 10,
    "unit": ""
}).insert()

link2 = link.LinkIngredientRecipeTest().custom({
    "_id_recipe": recipe2.get_id_objectId(),
    "_id_ingredient": ingredient1.get_id_objectId(),
    "quantity": 3,
    "unit": ""
}).insert()

link3 = link.LinkIngredientRecipeTest().custom({
    "_id_recipe": recipe3.get_id_objectId(),
    "_id_ingredient": ingredient1.get_id_objectId(),
    "quantity": 3,
    "unit": ""
}).insert()

link4 = link.LinkIngredientRecipeTest().custom({
    "_id_recipe": recipe3.get_id_objectId(),
    "_id_ingredient": ingredient3.get_id_objectId(),
    "quantity": 1,
    "unit": "plaquette"
}).insert()

