define({ "api": [
  {
    "type": "delete",
    "url": "/file/<_id_file>",
    "title": "DeleteFile",
    "group": "File",
    "description": "<p>Delete a file by it's ObjectId</p>",
    "parameter": {
      "fields": {
        "Query param": [
          {
            "group": "Query param",
            "type": "String",
            "optional": false,
            "field": "_id",
            "description": "<p>File's ObjectId</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "DELETE http://127.0.0.1:5000/file/<_id_file>",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 204",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.file.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/file/router.py",
    "groupTitle": "File",
    "name": "DeleteFile_id_file"
  },
  {
    "type": "get",
    "url": "/file/<_id_file>",
    "title": "DownloadFile",
    "group": "File",
    "description": "<p>Get a file by it's ObjectId</p>",
    "parameter": {
      "fields": {
        "Query param": [
          {
            "group": "Query param",
            "type": "String",
            "optional": false,
            "field": "_id",
            "description": "<p>File's ObjectId</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "GET http://127.0.0.1:5000/file/<_id_file>",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 200\n�PNG\n\u001anp������Q*D�l1<��j3",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.file.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/file/router.py",
    "groupTitle": "File",
    "name": "GetFile_id_file"
  },
  {
    "type": "post",
    "url": "/file/ingredient/<_id_ingredient>",
    "title": "PostIngredientFile",
    "group": "File",
    "description": "<p>Add a file to an ingredient</p>",
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
        "Body Param": [
          {
            "group": "Body Param",
            "type": "String",
            "optional": false,
            "field": "path",
            "description": "<p>File's path</p>"
          },
          {
            "group": "Body Param",
            "type": "String",
            "optional": false,
            "field": "filename",
            "description": "<p>File's filename</p>"
          },
          {
            "group": "Body Param",
            "type": "Boolean",
            "optional": true,
            "field": "is_main",
            "description": "<p>If True, file will be the main file. False by default</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "POST http://127.0.0.1:5000/file/ingredient/<_id_ingredient>\n{\n    'path': <path>,\n    'filename': <filename>,\n    'is_main': <is_main>\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 201\n{\n    'codeMsg': 'cookbook.file.success.created',\n    'codeStatus': 201,\n    'data': {'_id': '5e622b52c49ed1e0df987e55',\n            'name': 'qa_rhr',\n            'files': [{'_id': '5e622b537aa097121df95d93', 'is_main': False}]},\n    'detail': 'added file ObjectId: 5e622b537aa097121df95d93'\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.file.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/file/router.py",
    "groupTitle": "File",
    "name": "PostFileIngredient_id_ingredient"
  },
  {
    "type": "post",
    "url": "/file/recipe/<_id_recipe>",
    "title": "PostRecipeFile",
    "group": "File",
    "description": "<p>Add a file to a recipe</p>",
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
        "Body Param": [
          {
            "group": "Body Param",
            "type": "String",
            "optional": false,
            "field": "path",
            "description": "<p>File's path</p>"
          },
          {
            "group": "Body Param",
            "type": "String",
            "optional": false,
            "field": "filename",
            "description": "<p>File's filename</p>"
          },
          {
            "group": "Body Param",
            "type": "Boolean",
            "optional": true,
            "field": "is_main",
            "description": "<p>If True, file will be the main file. False by default</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "POST http://127.0.0.1:5000/file/recipe/<_id_recipe>\n{\n    'path': <path>,\n    'filename': <filename>,\n    'is_main': <is_main>\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 201\n{\n    'codeMsg': 'cookbook.file.success.created',\n    'codeStatus': 201,\n    'data': {'_id': '5e67a99745378d7c10124235', 'cooking_time': 0,\n             'files': [{'_id': '5e67a997ed11fd9361b2e374', 'is_main': False}], 'level': 0, 'nb_people': 0,\n             'note': '', 'preparation_time': 0, 'resume': '', 'steps': [], 'title': 'qa_rhr', 'slug': 'x',\n             'categories': []},\n    'detail': 'added file ObjectId: 5e67a997ed11fd9361b2e374'\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.file.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/file/router.py",
    "groupTitle": "File",
    "name": "PostFileRecipe_id_recipe"
  },
  {
    "type": "post",
    "url": "/file/recipe/<_id_recipe>/step/<_id_step>",
    "title": "PostStepFile",
    "group": "File",
    "description": "<p>Add a file to a step</p>",
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
            "description": "<p>Steps's ObjectId</p>"
          }
        ],
        "Body Param": [
          {
            "group": "Body Param",
            "type": "String",
            "optional": false,
            "field": "path",
            "description": "<p>File's path</p>"
          },
          {
            "group": "Body Param",
            "type": "String",
            "optional": false,
            "field": "filename",
            "description": "<p>File's filename</p>"
          },
          {
            "group": "Body Param",
            "type": "Boolean",
            "optional": true,
            "field": "is_main",
            "description": "<p>If True, file will be the main file. False by default</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "POST http://127.0.0.1:5000/file/recipe/<_id_recipe>/step/<_id_step>\n{\n    'path': <path>,\n    'filename': <filename>,\n    'is_main': <is_main>\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 201\n{\n    'codeMsg': 'cookbook.file.success.created',\n    'codeStatus': 201,\n    'data': {'_id': '5e6a4223e664b60da7cd8626', 'cooking_time': 0, 'files': [], 'level': 0, 'nb_people': 0,\n             'note': '', 'preparation_time': 0, 'resume': '',\n             'steps': [{'_id': '111111111111111111111111', 'files': [{'_id': '5e6a42237e59e8439a883d99',\n             'is_main': False}], 'description': 'a'}, {'_id': '222222222222222222222222', 'files': [],\n             'description': 'b'}], 'title': 'qa_rhr', 'slug': 'x', 'categories': []},\n    'detail': 'added file ObjectId: 5e6a42237e59e8439a883d99'\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.file.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/file/router.py",
    "groupTitle": "File",
    "name": "PostFileRecipe_id_recipeStep_id_step"
  },
  {
    "type": "put",
    "url": "/file/<_id_file>",
    "title": "PutFileIsMain",
    "group": "File",
    "description": "<p>Update a file and set is_main to True by it's ObjectId</p>",
    "parameter": {
      "fields": {
        "Query param": [
          {
            "group": "Query param",
            "type": "String",
            "optional": false,
            "field": "_id",
            "description": "<p>File's ObjectId</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "PUT http://127.0.0.1:5000/file/is_main/<_id_file>",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.file.success.ok',\n    'codeStatus': 200,\n    'data': '5e71f5c94acb9085a19f10b4 is now set as main file for 111111111111111111111111'}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.file.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/file/router.py",
    "groupTitle": "File",
    "name": "PutFile_id_file"
  },
  {
    "type": "delete",
    "url": "/ingredient/recipe/<_id_ingredient_recipe>",
    "title": "DeleteIngredientRecipe",
    "group": "Ingredient",
    "description": "<p>Delete an association ingredient-recipe</p>",
    "parameter": {
      "fields": {
        "Query param": [
          {
            "group": "Query param",
            "type": "String",
            "optional": false,
            "field": "_id",
            "description": "<p>Link's ObjectId</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "DELETE http://127.0.0.1:5000/ingredient/recipe/<_id_ingredient_recipe>",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 204",
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
    "name": "DeleteIngredientRecipe_id_ingredient_recipe"
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
          "content": "HTTPS 204",
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
            "field": "with_files",
            "description": "<p>if &quot;true&quot;, add ingredient's files</p>"
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
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.ingredient.success.ok',\n    'codeStatus': 200,\n    'data': [{'_id': '5e583de9b0fcef0a922a7bc0', 'name': 'aqa_rhr', 'categories': [],\n              'nutriments': {'calories': '0', 'carbohydrates': '0', 'fats': '0', 'proteins': '0',\n                             'info': 'per 100g'}},\n             {'_id': '5e583de9b0fcef0a922a7bc2', 'name': 'bqa_rhr', 'categories': [],\n              'nutriments': {'calories': '0', 'carbohydrates': '0', 'fats': '0', 'proteins': '0',\n                             'info': 'per 100g'}}]\n}",
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
    "url": "/ingredient/search",
    "title": "SearchIngredient",
    "group": "Ingredient",
    "description": "<p>Search an ingredient by key/value</p>",
    "parameter": {
      "fields": {
        "Query param": [
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
          },
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
            "field": "with_files",
            "description": "<p>if &quot;true&quot;, add ingredient's files</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "GET http://127.0.0.1:5000/ingredient/search?name=<ingredient_name>",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.ingredient.success.ok',\n    'codeStatus': 200,\n    'data': [{'_id': '5e583de9b0fcef0a922a7bc0', 'name': 'aqa_rhr'}]\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.ingredient.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Must be a string', 'param': 'name', 'value': ''}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/ingredient/router.py",
    "groupTitle": "Ingredient",
    "name": "GetIngredientSearch"
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
          },
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "with_files",
            "description": "<p>if &quot;true&quot;, add ingredient's files</p>"
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
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.ingredient.success.ok',\n    'codeStatus': 200,\n    'data': {'_id': '5e583de9b0fcef0a922a7bc0', 'name': 'aqa_rhr', 'categories': [],\n             'nutriments': {'calories': '0', 'carbohydrates': '0', 'fats': '0', 'proteins': '0',\n                            'info': 'per 100g'}}\n}",
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
    "type": "get",
    "url": "/ingredient/<_id_ingredient>/recipe",
    "title": "GetRecipeForIngredient",
    "group": "Ingredient",
    "description": "<p>Get all recipes for an ingredient by it's ObjectId</p>",
    "parameter": {
      "fields": {
        "Query param": [
          {
            "group": "Query param",
            "type": "String",
            "optional": false,
            "field": "_id",
            "description": "<p>Ingredient's ObjectId</p>"
          },
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "with_titles",
            "description": "<p>if &quot;true&quot;, add recipe's title</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "GET http://127.0.0.1:5000/ingredient/<_id_ingredient>/recipe",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.ingredient.success.ok',\n    'codeStatus': 200,\n    'data': [{'_id': '5e7347c82222535ac818942b', '_id_ingredient': '5e7347c82222535ac8189425',\n              '_id_recipe': '5e7347c82222535ac8189423', 'quantity': 0, 'unit': 'qa_rhr_unit_qa_rhr'},\n            {'_id': '5e7347c82222535ac818942f', '_id_ingredient': '5e7347c82222535ac8189427',\n             '_id_recipe': '5e7347c82222535ac8189423', 'quantity': 0, 'unit': 'qa_rhr_unit_qa_rhr'}]\n}",
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
    "name": "GetIngredient_id_ingredientRecipe"
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
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Ingredient's name</p>"
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
<<<<<<< Updated upstream
            "type": "String[]",
=======
            "type": "Array",
>>>>>>> Stashed changes
            "optional": true,
            "field": "categories",
            "defaultValue": "Empty_Array",
            "description": "<p>Ingredient's categories</p>"
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
            "type": "String",
            "optional": true,
            "field": "nutriments[info]",
            "defaultValue": "per 100g",
            "description": "<p>Ingredient's info</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "POST http://127.0.0.1:5000/ingredient\n{\n    'name': <name>\n    'slug': <slug>\n    'categories': [<category1>, <category2>],\n    'nutriments': {'calories': 10, 'carbohydrates': 20, 'fats': 30, 'proteins': 40, 'info': 'peer 100g'}\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 201\n{\n    'codeMsg': 'cookbook.ingredient.success.created',\n    'codeStatus': 201,\n    'data': {'_id': '5e5840e63ed55d9119064649', 'name': 'qa_rhr_name', 'slug': 'qa_rhr_slug',\n             'categories': ['qa_rhr_category'],\n             'nutriments': {'calories': '10', 'carbohydrates': '20', 'fats': '30', 'proteins': '40',\n                            'info': 'per 100g'}}\n}",
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
    "type": "post",
    "url": "/ingredient/recipe",
    "title": "PostIngredientRecipe",
    "group": "Ingredient",
    "description": "<p>Associate an ingredient to a recipe</p>",
    "parameter": {
      "fields": {
        "Body param": [
          {
            "group": "Body param",
            "type": "String",
            "optional": false,
            "field": "_id_ingredient",
            "description": "<p>Ingredient's ObjectId to link</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": false,
            "field": "_id_recipe",
            "description": "<p>Recipe's ObjectId to link</p>"
          },
          {
            "group": "Body param",
            "type": "Integer",
            "optional": false,
            "field": "quantity",
            "description": "<p>Ingredient's quantity for the recipe</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": false,
            "field": "unit",
            "description": "<p>Ingredient's unit for the recipe</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "POST http://127.0.0.1:5000/ingredient/recipe\n{\n    '_id_ingredient': <_id_ingredient>,\n    '_id_recipe': <_id_recipe>,\n    'quantity': <quantity>,\n    'unit': <unit>,\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 201\n{\n    'codeMsg': 'cookbook.ingredient.success.created',\n    'codeStatus': 201,\n    'data': {'_id': '5e722e87f94648b72c7d8f03', '_id_ingredient': '5e722e875754d5e780a8f1e5',\n             '_id_recipe': '5e722e875754d5e780a8f1e3', 'quantity': 5, 'unit': 'qa_rhr_unit'}\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.ingredient.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Must be an ObjectId', 'param': '_id_ingredient', 'value': 'invalid'}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/ingredient/router.py",
    "groupTitle": "Ingredient",
    "name": "PostIngredientRecipe"
  },
  {
    "type": "put",
    "url": "/ingredient/recipe/<_id_ingredient_recipe>",
    "title": "PutIngredientRecipe",
    "group": "Ingredient",
    "description": "<p>Update quantity and unit of an association ingredient-recipe</p>",
    "parameter": {
      "fields": {
        "Query param": [
          {
            "group": "Query param",
            "type": "String",
            "optional": false,
            "field": "_id",
            "description": "<p>Link's ObjectId</p>"
          }
        ],
        "Body param": [
          {
            "group": "Body param",
            "type": "Integer",
            "optional": true,
            "field": "quantity",
            "description": "<p>Ingredient's quantity for the recipe</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": true,
            "field": "unit",
            "description": "<p>Ingredient's unit for the recipe</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "PUT http://127.0.0.1:5000/ingredient/recipe/<_id_ingredient_recipe>\n{\n    'quantity': <quantity>,\n    'unit': <unit>,\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.ingredient.success.created',\n    'codeStatus': 201,\n    'data': {'_id': '5e722e87f94648b72c7d8f03', '_id_ingredient': '5e722e875754d5e780a8f1e5',\n             '_id_recipe': '5e722e875754d5e780a8f1e3', 'quantity': 10, 'unit': 'qa_rhr_unit_update'}\n}",
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
    "name": "PutIngredientRecipe_id_ingredient_recipe"
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
          },
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "with_files",
            "description": "<p>if &quot;true&quot;, add ingredient's files</p>"
          }
        ],
        "Body param": [
          {
            "group": "Body param",
            "type": "String",
            "optional": true,
            "field": "name",
            "description": "<p>Ingredient's name</p>"
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
<<<<<<< Updated upstream
            "type": "String[]",
=======
            "type": "Array",
>>>>>>> Stashed changes
            "optional": true,
            "field": "categories",
            "description": "<p>Ingredient's categories</p>"
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
            "field": "nutriments[proteins]",
            "description": "<p>Ingredient's proteins</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": true,
            "field": "nutriments[info]",
            "description": "<p>Ingredient's info</p>"
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
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.ingredient.success.ok',\n    'codeStatus': 20O,\n    'data': {'_id': '5e5840e63ed55d9119064649', 'name': 'qa_rhr_name_update'}\n}",
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
          "content": "HTTPS 204",
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
    "type": "delete",
    "url": "/recipe/<_id_recipe>/step/<_id_step>",
    "title": "DeleteRecipeStep",
    "group": "Recipe",
    "description": "<p>Delete a recipe's step</p>",
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
          },
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "with_files",
            "description": "<p>if &quot;true&quot;, add recipe's files</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "DELETE http://127.0.0.1:5000/recipe/<_id_recipe>/step/<_id_step>",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.recipe.success.ok',\n    'codeStatus': 200,\n    'data': {'_id': '5e68acb9e067528c70c75f3c', 'cooking_time': 0, 'level': 0, 'nb_people': 0, 'note': '',\n             'preparation_time': 0, 'resume': '', title': 'qa_rhr', 'slug': '', 'categories': [],\n             'steps': [{'_id': '5e68acb97b0ead079be3cef7', 'description': 'another_previous_step'}]}\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.recipe.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Must be an integer', 'param': 'position', 'value': 'invalid'}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/recipe/router.py",
    "groupTitle": "Recipe",
    "name": "DeleteRecipe_id_recipeStep_id_step"
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
            "field": "with_files",
            "description": "<p>if &quot;true&quot;, add recipe's files</p>"
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
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.recipe.success.ok',\n    'codeStatus': 200,\n    'data': [{'_id': '5e71eb8f39358991f2ea19f6', 'categories': [], 'cooking_time': 0, 'level': 0, 'nb_people': 0,\n              'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'steps': [], 'title': 'qa_rhr_1',\n              'status': 'in_progress'},\n             {'_id': '5e71eb8f39358991f2ea19f7', 'categories': [], 'cooking_time': 0, 'level': 0, 'nb_people': 0,\n              'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'steps': [], 'title': 'aqa_rhr_2',\n              'status': 'in_progress'}]\n}",
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
    "url": "/recipe/search",
    "title": "SearchRecipe",
    "group": "Recipe",
    "description": "<p>Search an recipe by unique or multiple key/value ($and in query)</p>",
    "parameter": {
      "fields": {
        "Query param": [
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
            "field": "slug",
            "description": "<p>search by slug</p>"
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
            "field": "cooking_time",
            "description": "<p>search by cooking_time</p>"
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
            "field": "nb_people",
            "description": "<p>search by nb_people</p>"
          },
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
            "field": "with_files",
            "description": "<p>if &quot;true&quot;, add recipe's files</p>"
<<<<<<< Updated upstream
=======
          },
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "status",
            "description": "<p>search by status</p>"
>>>>>>> Stashed changes
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "GET http://127.0.0.1:5000/recipe/search?title=<recipe_title>",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
<<<<<<< Updated upstream
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.recipe.success.ok',\n    'codeStatus': 200,\n    'data': [{'_id': '5e71eb8f39358991f2ea19f6', 'categories': [], 'cooking_time': 0, 'level': 0, 'nb_people': 0,\n              'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'steps': [], 'title': 'qa_rhr_1'},\n             {'_id': '5e71eb8f39358991f2ea19f7', 'categories': [], 'cooking_time': 0, 'level': 0, 'nb_people': 0,\n              'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'steps': [], 'title': 'aqa_rhr_2'}]\n}",
=======
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.recipe.success.ok',\n    'codeStatus': 200,\n    'data': [{'_id': '5e71eb8f39358991f2ea19f6', 'categories': [], 'cooking_time': 0, 'level': 0, 'nb_people': 0,\n              'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'steps': [], 'title': 'qa_rhr_1',\n              'status': 'in_progress'},\n             {'_id': '5e71eb8f39358991f2ea19f7', 'categories': [], 'cooking_time': 0, 'level': 0, 'nb_people': 0,\n              'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'steps': [], 'title': 'aqa_rhr_2',\n              'status': 'in_progress'}]\n}",
>>>>>>> Stashed changes
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.recipe.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Must be not empty', 'param': 'title', 'value': ''}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/recipe/router.py",
    "groupTitle": "Recipe",
    "name": "GetRecipeSearch"
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
            "field": "with_files",
            "description": "<p>if &quot;true&quot;, add recipe's files</p>"
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
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.recipe.success.ok',\n    'codeStatus': 200,\n    'data': {'_id': '5e71eb8f39358991f2ea19f6', 'categories': [], 'cooking_time': 0, 'level': 0, 'nb_people': 0,\n             'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'steps': [], 'title': 'aqa_rhr',\n             'status': 'in_progress'}\n}",
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
    "type": "get",
    "url": "/recipe/<_id_recipe>/ingredient",
    "title": "GetIngredientForRecipe",
    "group": "Recipe",
    "description": "<p>Get all ingredients for a recipe by it's ObjectId</p>",
    "parameter": {
      "fields": {
        "Query param": [
          {
            "group": "Query param",
            "type": "String",
            "optional": false,
            "field": "_id",
            "description": "<p>Recipe's ObjectId</p>"
          },
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "with_names",
            "description": "<p>if &quot;true&quot;, add ingredient's name</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "GET http://127.0.0.1:5000/recipe/<_id_recipe>/ingredient",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.recipe.success.ok',\n    'codeStatus': 200,\n    'data': [{'_id': '5e7347c82222535ac818942b', '_id_ingredient': '5e7347c82222535ac8189425',\n              '_id_recipe': '5e7347c82222535ac8189423', 'quantity': 0, 'unit': 'qa_rhr_unit_qa_rhr'},\n            {'_id': '5e7347c82222535ac818942f', '_id_ingredient': '5e7347c82222535ac8189427',\n             '_id_recipe': '5e7347c82222535ac8189423', 'quantity': 0, 'unit': 'qa_rhr_unit_qa_rhr'}]\n}",
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
    "name": "GetRecipe_id_recipeIngredient"
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
            "type": "String",
            "optional": false,
            "field": "title",
            "description": "<p>Recipe's title</p>"
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
            "type": "Integer",
            "optional": true,
            "field": "level",
            "description": "<p>=0 Recipe's level (between 0 and 3)</p>"
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
            "type": "Integer",
            "optional": true,
            "field": "cooking_time",
            "description": "<p>=0 Recipe's cooking time</p>"
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
            "type": "Array",
            "optional": true,
            "field": "categories",
<<<<<<< Updated upstream
            "description": "<p>Recipe's categories</p>"
=======
            "description": "<p>=Empty_Array Recipe's categories</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": true,
            "field": "status",
            "description": "<p>=&quot;in_progress&quot; Recipe's categories (&quot;in_progress&quot; or &quot;finished&quot;)</p>"
>>>>>>> Stashed changes
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "POST http://127.0.0.1:5000/recipe\n{\n    'title': <title>\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 201\n{\n    'codeMsg': 'cookbook.recipe.success.created',\n    'codeStatus': 201,\n    'data': {'_id': '5e71eb8f39358991f2ea19f6', 'categories': [], 'cooking_time': 0, 'level': 0, 'nb_people': 0,\n             'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'steps': [], 'title': 'aqa_rhr',\n             'status': 'in_progress'}\n}",
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
    "type": "post",
    "url": "/recipe/step/<_id_recipe>",
    "title": "PostRecipeStep",
    "group": "Recipe",
    "description": "<p>Create a recipe's step. Can specify where to add the step</p>",
    "parameter": {
      "fields": {
        "Query param": [
          {
            "group": "Query param",
            "type": "String",
            "optional": false,
            "field": "_id",
            "description": "<p>Recipe's ObjectId</p>"
          },
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "with_files",
            "description": "<p>if &quot;true&quot;, add recipe's files</p>"
          }
        ],
        "Body param": [
          {
            "group": "Body param",
            "type": "String",
            "optional": false,
            "field": "description",
            "description": "<p>Step's description to add</p>"
          },
          {
            "group": "Body param",
            "type": "Integer",
            "optional": true,
            "field": "position",
            "description": "<p>Position in recipe's steps array. If not specified, add at the end of the array</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "POST http://127.0.0.1:5000/recipe/step/<_id_recipe>\n{\n    'description': <description>,\n    'position': <position>\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 201\n{\n    'codeMsg': 'cookbook.recipe.success.created',\n    'codeStatus': 201,\n    'data': {'_id': '5e68acb9e067528c70c75f3c', 'cooking_time': 0, 'level': 0, 'nb_people': 0, 'note': '',\n             'preparation_time': 0, 'resume': '', title': 'qa_rhr', 'slug': '', 'categories': [],\n             'steps': [{'_id': '5e68acb97b0ead079be3cef7', 'description': 'new_step'}]}\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.recipe.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Must be an integer', 'param': 'position', 'value': 'invalid'}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/recipe/router.py",
    "groupTitle": "Recipe",
    "name": "PostRecipeStep_id_recipe"
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
          },
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "with_files",
            "description": "<p>if &quot;true&quot;, add recipe's files</p>"
          }
        ],
        "Body param": [
          {
            "group": "Body param",
            "type": "String",
            "optional": true,
            "field": "title",
            "description": "<p>Recipe's title</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": true,
            "field": "slug",
            "description": "<p>Recipe's slug for url</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": true,
            "field": "level",
            "description": "<p>Recipe's level</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": true,
            "field": "resume",
            "description": "<p>Recipe's resume</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": true,
            "field": "cooking_time",
            "description": "<p>Recipe's cooking time</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": true,
            "field": "preparation_time",
            "description": "<p>Recipe's preparation time</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": true,
            "field": "nb_people",
            "description": "<p>Recipe's number of people</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": true,
            "field": "note",
            "description": "<p>Recipe's note</p>"
          },
          {
            "group": "Body param",
            "type": "Array",
            "optional": true,
            "field": "categories",
            "description": "<p>Recipe's categories</p>"
          },
          {
            "group": "Body param",
            "type": "String",
            "optional": true,
            "field": "status",
            "description": "<p>=&quot;in_progress&quot; Recipe's categories (&quot;in_progress&quot; or &quot;finished&quot;)</p>"
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
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.recipe.success.created',\n    'codeStatus': 201,\n    'data': {'_id': '5e71eb8f39358991f2ea19f6', 'categories': [], 'cooking_time': 0, 'level': 0, 'nb_people': 0,\n             'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'steps': [], 'title': 'aqa_rhr',\n             'status': 'in_progress'}\n}",
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
    "type": "put",
    "url": "/recipe/<_id_recipe>/step/<_id_step>",
    "title": "PutRecipeStep",
    "group": "Recipe",
    "description": "<p>Update a recipe's step</p>",
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
          },
          {
            "group": "Query param",
            "type": "String",
            "optional": true,
            "field": "with_files",
            "description": "<p>if &quot;true&quot;, add recipe's files</p>"
          }
        ],
        "Body param": [
          {
            "group": "Body param",
            "type": "String",
            "optional": false,
            "field": "description",
            "description": "<p>Step's description to add</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "PUT http://127.0.0.1:5000/recipe/<_id_recipe>/step/<_id_step>\n{\n    'description': <description>\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.recipe.success.ok',\n    'codeStatus': 200,\n    'data': {'_id': '5e68acb9e067528c70c75f3c', 'cooking_time': 0, 'level': 0, 'nb_people': 0, 'note': '',\n             'preparation_time': 0, 'resume': '', title': 'qa_rhr', 'slug': '', 'categories': [],\n             'steps': [{'_id': '5e68acb97b0ead079be3cef7', 'description': 'updated_step'}]}\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.recipe.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Must be an integer', 'param': 'position', 'value': 'invalid'}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/recipe/router.py",
    "groupTitle": "Recipe",
    "name": "PutRecipe_id_recipeStep_id_step"
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
