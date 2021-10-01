define({ "api": [
  {
    "type": "delete",
    "url": "/files/<path>",
    "title": "DeleteFile",
    "group": "Files",
    "description": "<p>Delete a file</p>",
    "parameter": {
      "fields": {
        "Query param": [
          {
            "group": "Query param",
            "type": "String",
            "optional": false,
            "field": "path",
            "description": "<p>File's path</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "DELETE http://127.0.0.1:5000/files/<path>",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.files.success.ok',\n    'codeStatus': 200,\n    'data': 'recipe/6050c6b3a888196e9746f217/image.png'\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.cookbook.error.bad_request',\n    'codeStatus': 404,\n    'detail': 'The requested URL was not found on the server'\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/files/router.py",
    "groupTitle": "Files",
    "name": "DeleteFilesPath"
  },
  {
    "type": "get",
    "url": "/files/<path>",
    "title": "GetFile",
    "group": "Files",
    "description": "<p>Get a file</p>",
    "parameter": {
      "fields": {
        "Query param": [
          {
            "group": "Query param",
            "type": "String",
            "optional": false,
            "field": "path",
            "description": "<p>File's path</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "GET http://127.0.0.1:5000/files/recipe/<path>",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "Files Streamed",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.cookbook.error.bad_request',\n    'codeStatus': 404,\n    'detail': 'The requested URL was not found on the server'\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/files/router.py",
    "groupTitle": "Files",
    "name": "GetFilesPath"
  },
  {
    "type": "post",
    "url": "files/recipe/<_id>",
    "title": "PostFilesRecipe",
    "group": "Files",
    "description": "<p>Add files to a Recipe</p>",
    "parameter": {
      "fields": {
        "Query param": [
          {
            "group": "Query param",
            "type": "String",
            "optional": false,
            "field": "_id",
            "description": "<p>Recipe's ObjectId</p>"
          }
        ],
        "Multipart/form-data": [
          {
            "group": "Multipart/form-data",
            "optional": false,
            "field": "files",
            "description": "<p>Files</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "POST http://127.0.0.1:5000/files/recipe/<_id>\nfiles = [\n         ('files', ('qa_rhr_filename.txt', open(path1, 'rb'), mimetypes)),\n         ('files', ('qa_rhr_filename2.png', open(path2, 'rb'), mimetypes)),\n         ('files', ('qa_rhr_filename3.jpeg', open(path3, 'rb'), mimetypes))]",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 201\n{\n    'codeMsg': 'cookbook.files.success.created',\n    'codeStatus': 201,\n    'data': ['recipe/5ff5869625fcd58c3ecc5f17/qa_rhr_filename.txt',\n             'recipe/5ff5869625fcd58c3ecc5f17/qa_rhr_filename2.png',\n             'recipe/5ff5869625fcd58c3ecc5f17/qa_rhr_filename3.jpeg']}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.files.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/files/router.py",
    "groupTitle": "Files",
    "name": "PostFilesRecipe_id"
  },
  {
    "type": "post",
    "url": "/files/recipe/<_id_recipe>/step/<_id_step>",
    "title": "PostFilesRecipeStep",
    "group": "Files",
    "description": "<p>Add files to a Step's Recipe</p>",
    "parameter": {
      "fields": {
        "Query param": [
          {
            "group": "Query param",
            "type": "String",
            "optional": false,
            "field": "_id_recipe",
            "description": "<p>Recipe's ObjectId</p>"
          },
          {
            "group": "Query param",
            "type": "String",
            "optional": false,
            "field": "_id_step",
            "description": "<p>Step's ObjectId</p>"
          }
        ],
        "Multipart/form-data": [
          {
            "group": "Multipart/form-data",
            "optional": false,
            "field": "files",
            "description": "<p>Files</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "POST http://127.0.0.1:5000/files/recipe/<_id_recipe>/step/<_id_step>\nfiles = [\n         ('files', ('qa_rhr_filename.txt', open(path1, 'rb'), mimetypes)),\n         ('files', ('qa_rhr_filename2.png', open(path2, 'rb'), mimetypes)),\n         ('files', ('qa_rhr_filename3.jpeg', open(path3, 'rb'), mimetypes))]",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 201\n{\n    'codeMsg': 'cookbook.files.success.created',\n    'codeStatus': 201,\n    'data': ['recipe/5ff5869625fcd58c3ecc5f17/step/5ff5869625fcd58c3ecc5f18/qa_rhr_filename.txt',\n             'recipe/5ff5869625fcd58c3ecc5f17/step/5ff5869625fcd58c3ecc5f18/qa_rhr_filename2.png',\n             'recipe/5ff5869625fcd58c3ecc5f17/step/5ff5869625fcd58c3ecc5f18/qa_rhr_filename3.jpeg']}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.files.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Must be an ObjectId', 'param': '_id_recipe', 'value': 'invalid'}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/files/router.py",
    "groupTitle": "Files",
    "name": "PostFilesRecipe_id_recipeStep_id_step"
  },
  {
    "type": "delete",
    "url": "/ingredient/<_id_ingredient>",
    "title": "DeleteIngredient",
    "group": "Ingredient",
    "description": "<p>Delete an ingredient by it's ObjectId</p>",
    "parameter": {
      "fields": {
        "Query param": [
          {
            "group": "Query param",
            "type": "String",
            "optional": false,
            "field": "_id",
            "description": "<p>Ingredient's ObjectId</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "DELETE http://127.0.0.1:5000/ingredient/<_id_ingredient>",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.ingredient.success.ok',\n    'codeStatus': 200,\n    'data': '5fd770e1a9888551191a8743'\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.ingredient.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/ingredient/router.py",
    "groupTitle": "Ingredient",
    "name": "DeleteIngredient_id_ingredient"
  },
  {
    "type": "get",
    "url": "/ingredient",
    "title": "GetAllIngredient",
    "group": "Ingredient",
    "description": "<p>Get file ingredients</p>",
    "parameter": {
      "fields": {
        "Query param": [
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "categories",
            "description": "<p>ingredient's categories</p>"
          },
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "order",
            "description": "<p>criteria for order in ['asc', 'desc']</p>"
          },
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "orderBy",
            "description": "<p>order direction in ['name', 'slug']</p>"
          },
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "name",
            "description": "<p>ingredient's name</p>"
          },
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "slug",
            "description": "<p>ingredient's slug</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "GET http://127.0.0.1:5000/ingredient",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.ingredient.success.ok',\n    'codeStatus': 200,\n    'data': [{'_id': '5e583de9b0fcef0a922a7bc0', 'categories': [], 'name': 'aqa_rhr',\n              'nutriments': {'calories': '0', 'carbohydrates': '0', 'fats': '0', 'portion': 1, 'proteins': '0'},\n              'slug': 'slug_ex1'},\n             {'_id': '5e583de9b0fcef0a922a7bc2', 'categories': [], 'name': 'bqa_rhr',\n              'nutriments': {'calories': '0', 'carbohydrates': '0', 'fats': '0', 'portion': 1, 'proteins': '0'},\n              'slug': 'slug_ex2'}]\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/ingredient/router.py",
    "groupTitle": "Ingredient",
    "name": "GetIngredient"
  },
  {
    "type": "get",
    "url": "/ingredient/<_id_ingredient>",
    "title": "GetIngredient",
    "group": "Ingredient",
    "description": "<p>Get an ingredient by it's ObjectId</p>",
    "parameter": {
      "fields": {
        "Query param": [
          {
            "group": "Query param",
            "type": "String",
            "optional": false,
            "field": "_id",
            "description": "<p>Ingredient's ObjectId</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "GET http://127.0.0.1:5000/ingredient/<_id_ingredient>",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.ingredient.success.ok',\n    'codeStatus': 200,\n    'data': {'_id': '5e583de9b0fcef0a922a7bc0', 'categories': [], 'name': 'aqa_rhr',\n             'nutriments': {'calories': '0', 'carbohydrates': '0', 'fats': '0', 'portion': 1, 'proteins': '0'},\n             'slug': 'slug_ex'}, 'unit': 'g'}\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.ingredient.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/ingredient/router.py",
    "groupTitle": "Ingredient",
    "name": "GetIngredient_id_ingredient"
  },
  {
    "type": "post",
    "url": "/ingredient",
    "title": "PostIngredient",
    "group": "Ingredient",
    "description": "<p>Create an ingredient</p>",
    "parameter": {
      "fields": {
        "Body param": [
          {
            "group": "Body param",
            "type": "Array",
            "optional": true,
            "field": "categories",
            "defaultValue": "Empty_Array",
            "description": "<p>Ingredient's categories</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Ingredient's name</p>"
          },
          {
            "group": "Body param",
            "type": "Object",
            "optional": true,
            "field": "nutriments",
            "description": "<p>Ingredient's nutriments</p>"
          },
          {
            "group": "Body param",
            "type": "Number",
            "optional": false,
            "field": "nutriments[calories]",
            "defaultValue": "0",
            "description": "<p>Ingredient's calories</p>"
          },
          {
            "group": "Body param",
            "type": "Number",
            "optional": false,
            "field": "nutriments[carbohydrates]",
            "defaultValue": "0",
            "description": "<p>Ingredient's carbohydrates</p>"
          },
          {
            "group": "Body param",
            "type": "Number",
            "optional": false,
            "field": "nutriments[fats]",
            "defaultValue": "0",
            "description": "<p>Ingredient's fats</p>"
          },
          {
            "group": "Body param",
            "type": "Number",
            "optional": false,
            "field": "nutriments[portion]",
            "defaultValue": "1",
            "description": "<p>Ingredient's portion</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": false,
            "field": "slug",
            "description": "<p>Ingredient's slug</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": true,
            "field": "unit",
            "defaultValue": "g",
            "description": "<p>Ingredient's unit</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "POST http://127.0.0.1:5000/ingredient\n{\n    'name': <name>\n    'slug': <slug>\n    'categories': [<category1>, <category2>],\n    'nutriments': {'calories': 10, 'carbohydrates': 20, 'fats': 30, 'portion': 1, 'proteins': 40}\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 201\n{\n    'codeMsg': 'cookbook.ingredient.success.created',\n    'codeStatus': 201,\n    'data': {'_id': '5e583de9b0fcef0a922a7bc0', 'categories': [], 'name': 'aqa_rhr_update',\n             'nutriments': {'calories': '0', 'carbohydrates': '0', 'fats': '0', 'portion': 1, 'proteins': '0'},\n             'slug': 'slug_ex', 'unit': 'g'}\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.ingredient.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Is required', 'param': 'name'}}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/ingredient/router.py",
    "groupTitle": "Ingredient",
    "name": "PostIngredient"
  },
  {
    "type": "put",
    "url": "/ingredient/<_id_ingredient>",
    "title": "PutIngredient",
    "group": "Ingredient",
    "description": "<p>Update an ingredient by it's ObjectId</p>",
    "parameter": {
      "fields": {
        "Query param": [
          {
            "group": "Query param",
            "type": "String",
            "optional": false,
            "field": "_id",
            "description": "<p>Ingredient's ObjectId</p>"
          }
        ],
        "Body param": [
          {
            "group": "Body param",
            "type": "Array",
            "optional": true,
            "field": "categories",
            "description": "<p>Ingredient's categories</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": true,
            "field": "name",
            "description": "<p>Ingredient's name</p>"
          },
          {
            "group": "Body param",
            "type": "Object",
            "optional": true,
            "field": "nutriments",
            "description": "<p>Ingredient's nutriments</p>"
          },
          {
            "group": "Body param",
            "type": "Number",
            "optional": true,
            "field": "nutriments[calories]",
            "description": "<p>Ingredient's calories</p>"
          },
          {
            "group": "Body param",
            "type": "Number",
            "optional": true,
            "field": "nutriments[carbohydrates]",
            "description": "<p>Ingredient's carbohydrates</p>"
          },
          {
            "group": "Body param",
            "type": "Number",
            "optional": true,
            "field": "nutriments[fats]",
            "description": "<p>Ingredient's fats</p>"
          },
          {
            "group": "Body param",
            "type": "Number",
            "optional": true,
            "field": "nutriments[portions]",
            "description": "<p>Ingredient's portion</p>"
          },
          {
            "group": "Body param",
            "type": "Number",
            "optional": true,
            "field": "nutriments[proteins]",
            "description": "<p>Ingredient's proteins</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": true,
            "field": "slug",
            "description": "<p>Ingredient's slug</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": true,
            "field": "unit",
            "defaultValue": "g",
            "description": "<p>Ingredient's unit</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "PUT http://127.0.0.1:5000/ingredient/<_id_ingredient>\n{\n    'name': <name>\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.ingredient.success.ok',\n    'codeStatus': 20O,\n    'data': {'_id': '5e583de9b0fcef0a922a7bc0', 'categories': [], 'name': 'aqa_rhr_update',\n             'nutriments': {'calories': '0', 'carbohydrates': '0', 'fats': '0', 'portion': 1, 'proteins': '0'},\n             'slug': 'slug_ex', 'unit': 'g'}\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.ingredient.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Is required', 'param': 'name'}}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/ingredient/router.py",
    "groupTitle": "Ingredient",
    "name": "PutIngredient_id_ingredient"
  },
  {
    "type": "delete",
    "url": "/recipe/<_id_recipe>",
    "title": "DeleteRecipe",
    "group": "Recipe",
    "description": "<p>Delete an recipe by it's ObjectId</p>",
    "parameter": {
      "fields": {
        "Query param": [
          {
            "group": "Query param",
            "type": "String",
            "optional": false,
            "field": "_id",
            "description": "<p>Recipe's ObjectId</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "DELETE http://127.0.0.1:5000/recipe/<_id_recipe>",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "    HTTPS 200\n{\n    'codeMsg': 'cookbook.recipe.success.ok',\n    'codeStatus': 200,\n    'data': '5fd770e1a9888551191a8743'\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.recipe.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/recipe/router.py",
    "groupTitle": "Recipe",
    "name": "DeleteRecipe_id_recipe"
  },
  {
    "type": "get",
    "url": "/recipe",
    "title": "GetAllRecipe",
    "group": "Recipe",
    "description": "<p>Get all recipes</p>",
    "parameter": {
      "fields": {
        "Query param": [
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "categories",
            "description": "<p>search by categories</p>"
          },
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "cooking_time",
            "description": "<p>search by cooking_time</p>"
          },
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "level",
            "description": "<p>search by level</p>"
          },
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "nb_people",
            "description": "<p>search by nb_people</p>"
          },
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "order",
            "description": "<p>criteria for order in ['asc', 'desc']</p>"
          },
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "orderBy",
            "description": "<p>order direction in ['title', 'slug', 'level', 'cooking_time', 'preparation_time', 'nb_people']</p>"
          },
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "preparation_time",
            "description": "<p>search by preparation_time</p>"
          },
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "slug",
            "description": "<p>search by slug</p>"
          },
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "status",
            "description": "<p>search by status</p>"
          },
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "title",
            "description": "<p>search by title</p>"
          },
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "with_calories",
            "description": "<p>if &quot;true&quot;, add Recipe's calories from ingredients</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "GET http://127.0.0.1:5000/recipe",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.recipe.success.ok',\n    'codeStatus': 200,\n    'data': [{'_id': '5e71eb8f39358991f2ea19f6', 'categories': [], 'cooking_time': 0, 'ingredients': [], 'level': 0,\n              'nb_people': 0, 'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'status': 'in_progress',\n              'steps': [], 'title': 'qa_rhr_1', 'files' : []},\n             {'_id': '5e71eb8f39358991f2ea19f7', 'categories': [], 'cooking_time': 0, 'ingredients': [], 'level': 0,\n              'nb_people': 0, 'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'status': 'in_progress',\n              'steps': [], 'title': 'qa_rhr_2', 'files' : []}]\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/recipe/router.py",
    "groupTitle": "Recipe",
    "name": "GetRecipe"
  },
  {
    "type": "get",
    "url": "/recipe/<slug>",
    "title": "GetRecipe",
    "group": "Recipe",
    "description": "<p>Get a recipe by it's slug</p>",
    "parameter": {
      "fields": {
        "Query param": [
          {
            "group": "Query param",
            "type": "String",
            "optional": false,
            "field": "slug",
            "description": "<p>Recipe's slug</p>"
          },
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "with_calories",
            "description": "<p>if &quot;true&quot;, add Recipe's calories from ingredients</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "GET http://127.0.0.1:5000/recipe/<slug>",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.recipe.success.ok',\n    'codeStatus': 200,\n    'data': {'_id': '5e71eb8f39358991f2ea19f6', 'categories': [], 'cooking_time': 0, 'ingredients': [], 'level': 0,\n              'nb_people': 0, 'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'status': 'in_progress',\n              'steps': [], 'title': 'qa_rhr_1', 'files' : []}\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.recipe.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Must be not empty', 'param': 'slug', 'value': ''}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/recipe/router.py",
    "groupTitle": "Recipe",
    "name": "GetRecipeSlug"
  },
  {
    "type": "post",
    "url": "/recipe",
    "title": "PostRecipe",
    "group": "Recipe",
    "description": "<p>Create a recipe</p>",
    "parameter": {
      "fields": {
        "Body param": [
          {
            "group": "Body param",
            "type": "Array",
            "optional": true,
            "field": "categories",
            "description": "<p>=Empty_Array Recipe's categories</p>"
          },
          {
            "group": "Body param",
            "type": "Integer",
            "optional": true,
            "field": "cooking_time",
            "description": "<p>=0 Recipe's cooking time</p>"
          },
          {
            "group": "Body param",
            "type": "Array",
            "optional": true,
            "field": "ingredients",
            "description": "<p>=Empty_Array Recipe's Ingredients</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": false,
            "field": "ingredients[_id]",
            "description": "<p>Ingredient's ObjectId</p>"
          },
          {
            "group": "Body param",
            "type": "Integer",
            "optional": false,
            "field": "ingredients[quantity]",
            "description": "<p>Ingredient's quantity</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": false,
            "field": "ingredients[unit]",
            "description": "<p>Ingredient's unit</p>"
          },
          {
            "group": "Body param",
            "type": "Integer",
            "optional": true,
            "field": "level",
            "description": "<p>=0 Recipe's level (between 0 and 3)</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": true,
            "field": "nb_people",
            "description": "<p>=0 Recipe's number of people</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": true,
            "field": "note",
            "description": "<p>=&quot;&quot; Recipe's note</p>"
          },
          {
            "group": "Body param",
            "type": "Integer",
            "optional": true,
            "field": "preparation_time",
            "description": "<p>=0 Recipe's preparation time</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": true,
            "field": "resume",
            "description": "<p>=&quot;&quot; Recipe's resume</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": false,
            "field": "slug",
            "description": "<p>Recipe's slug for url</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": true,
            "field": "status",
            "description": "<p>=&quot;in_progress&quot; Recipe's categories (&quot;in_progress&quot; or &quot;finished&quot;)</p>"
          },
          {
            "group": "Body param",
            "type": "Array",
            "optional": true,
            "field": "steps",
            "description": "<p>=Empty_Array Recipe's steps</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": false,
            "field": "steps[description]",
            "description": "<p>Step's description</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": false,
            "field": "title",
            "description": "<p>Recipe's title</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "POST http://127.0.0.1:5000/recipe\n{\n    'title': <title>,\n    'slug': <slug>,\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 201\n{\n    'codeMsg': 'cookbook.recipe.success.created',\n    'codeStatus': 201,\n    'data': {'_id': '5e71eb8f39358991f2ea19f6', 'categories': [], 'cooking_time': 0, 'ingredients': [], 'level': 0,\n              'nb_people': 0, 'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'status': 'in_progress',\n              'steps': [], 'title': 'qa_rhr_1', 'files' : []}\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.recipe.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Must be a string', 'param': 'title', 'value': {}}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/recipe/router.py",
    "groupTitle": "Recipe",
    "name": "PostRecipe"
  },
  {
    "type": "put",
    "url": "/recipe/<_id_recipe>",
    "title": "PutRecipe",
    "group": "Recipe",
    "description": "<p>Update a recipe</p>",
    "parameter": {
      "fields": {
        "Query param": [
          {
            "group": "Query param",
            "type": "String",
            "optional": false,
            "field": "_id",
            "description": "<p>Recipe's ObjectId</p>"
          }
        ],
        "Body param": [
          {
            "group": "Body param",
            "type": "Array",
            "optional": true,
            "field": "categories",
            "description": "<p>=Empty_Array Recipe's categories</p>"
          },
          {
            "group": "Body param",
            "type": "Integer",
            "optional": true,
            "field": "cooking_time",
            "description": "<p>=0 Recipe's cooking time</p>"
          },
          {
            "group": "Body param",
            "type": "Array",
            "optional": true,
            "field": "ingredients",
            "description": "<p>=Empty_Array Recipe's Ingredients</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": false,
            "field": "ingredients[_id]",
            "description": "<p>Ingredient's ObjectId</p>"
          },
          {
            "group": "Body param",
            "type": "Integer",
            "optional": false,
            "field": "ingredients[quantity]",
            "description": "<p>Ingredient's quantity</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": false,
            "field": "ingredients[unit]",
            "defaultValue": "Ingredient's",
            "description": "<p>unit</p>"
          },
          {
            "group": "Body param",
            "type": "Integer",
            "optional": true,
            "field": "level",
            "description": "<p>=0 Recipe's level (between 0 and 3)</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": true,
            "field": "nb_people",
            "description": "<p>=0 Recipe's number of people</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": true,
            "field": "note",
            "description": "<p>=&quot;&quot; Recipe's note</p>"
          },
          {
            "group": "Body param",
            "type": "Integer",
            "optional": true,
            "field": "preparation_time",
            "description": "<p>=0 Recipe's preparation time</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": true,
            "field": "resume",
            "description": "<p>=&quot;&quot; Recipe's resume</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": false,
            "field": "slug",
            "description": "<p>Recipe's slug for url</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": true,
            "field": "status",
            "description": "<p>=&quot;in_progress&quot; Recipe's categories (&quot;in_progress&quot; or &quot;finished&quot;)</p>"
          },
          {
            "group": "Body param",
            "type": "Array",
            "optional": true,
            "field": "steps",
            "description": "<p>=Empty_Array Recipe's steps</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": false,
            "field": "steps[description]",
            "description": "<p>Step's description</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": false,
            "field": "title",
            "description": "<p>Recipe's title</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "PUT http://127.0.0.1:5000/recipe/<_id_recipe>\n{\n    'title': <title>\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.recipe.success.created',\n    'codeStatus': 201,\n    'data': {'_id': '5e71eb8f39358991f2ea19f6', 'categories': [], 'cooking_time': 0, 'ingredients': [], 'level': 0,\n              'nb_people': 0, 'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'status': 'in_progress',\n              'steps': [], 'title': 'qa_rhr_1', 'files' : []}\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.recipe.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Must be a string', 'param': 'title', 'value': {}}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/recipe/router.py",
    "groupTitle": "Recipe",
    "name": "PutRecipe_id_recipe"
  },
  {
    "type": "get",
    "url": "/user/me",
    "title": "GetMyUser",
    "group": "User",
    "description": "<p>Get my user</p>",
    "examples": [
      {
        "title": "Example usage:",
        "content": "GET http://127.0.0.1:5000/user/me",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.user.success.ok',\n    'codeStatus': 200,\n    'data': {'_id': '5f6a0327e9fea33b5861445c', 'display_name': 'qa_rhr_display_name', 'email': 'qa@rhr.com',\n             'status': []}\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 401\n{\n    'codeMsg': 'cookbook.user.error.bad_request',\n    'codeStatus': 401,\n    'detail': {'msg': 'Is required', 'param': 'token'}}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/user/router.py",
    "groupTitle": "User",
    "name": "GetUserMe"
  },
  {
    "type": "post",
    "url": "/user/login",
    "title": "PostUserLogin",
    "group": "User",
    "description": "<p>Log in an user</p>",
    "parameter": {
      "fields": {
        "Body param": [
          {
            "group": "Body param",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>User's email</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>User's password</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "POST http://127.0.0.1:5000/user/login\n{\n    'email': <email>,\n    'password': <password>\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.user.success.created',\n    'codeStatus': 200,\n    'data': {'token': '...'}\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.user.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Is required', 'param': 'email'}}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/user/router.py",
    "groupTitle": "User",
    "name": "PostUserLogin"
  },
  {
    "type": "post",
    "url": "/user/signup",
    "title": "PostUserSignup",
    "group": "User",
    "description": "<p>Create an user</p>",
    "parameter": {
      "fields": {
        "Body param": [
          {
            "group": "Body param",
            "type": "String",
            "optional": false,
            "field": "display_name",
            "description": "<p>User's name in UI</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>User's email to login</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>User's password</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "POST http://127.0.0.1:5000/user/singup\n{\n    'display_name': <display_name>,\n    'email': <email>,\n    'password': <password>\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 201\n{\n    'codeMsg': 'cookbook.user.success.created',\n    'codeStatus': 201,\n    'data': {'_id': '5e5840e63ed55d9119064649', 'display_name': 'display_name_qa_rhr', 'email': 'qa@rhr.com'}\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.user.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Is required', 'param': 'display_name'}}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/user/router.py",
    "groupTitle": "User",
    "name": "PostUserSignup"
  }
] });
