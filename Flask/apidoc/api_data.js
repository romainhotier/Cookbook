define({ "api": [
  {
    "type": "get",
    "url": "/ingredient",
    "title": "Get all ingredient",
    "name": "GetAllIngredient",
    "group": "Ingredient",
    "version": "0.0.0",
    "filename": "Flask/app/ingredient/ingredient/router.py",
    "groupTitle": "Ingredient"
  },
  {
    "type": "get",
    "url": "/ingredient/<_id>",
    "title": "Get one ingredient",
    "name": "GetIngredient",
    "group": "Ingredient",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "ObjectId",
            "optional": false,
            "field": "_id",
            "description": "<p>Ingredient ObjectId</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "Flask/app/ingredient/ingredient/router.py",
    "groupTitle": "Ingredient"
  },
  {
    "type": "get",
    "url": "/ingredient",
    "title": "Post an ingredient",
    "name": "PostIngredient",
    "group": "Ingredient",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Ingredient's name</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "Flask/app/ingredient/ingredient/router.py",
    "groupTitle": "Ingredient"
  },
  {
    "type": "get",
    "url": "/recipe",
    "title": "Get all recipe",
    "name": "GetAllRecipe",
    "group": "Recipe",
    "version": "0.0.0",
    "filename": "Flask/app/recipe/recipe/router.py",
    "groupTitle": "Recipe"
  }
] });
