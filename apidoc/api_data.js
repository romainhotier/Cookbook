define({ "api": [
  {
    "type": "delete",
    "url": "/file/<_id>",
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
            "description": "<p>Ingredient's ObjectId</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "DELETE http://127.0.0.1:5000/file/<_id>",
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
    "filename": "../Flask/app/file/file/router.py",
    "groupTitle": "File",
    "name": "DeleteFile_id"
  },
  {
    "type": "get",
    "url": "/file/<_id>",
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
        "content": "GET http://127.0.0.1:5000/file/<_id>",
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
    "filename": "../Flask/app/file/file/router.py",
    "groupTitle": "File",
    "name": "GetFile_id"
  },
  {
    "type": "post",
    "url": "/file/ingredient/<_id>",
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
        "content": "GET http://127.0.0.1:5000/file/ingredient/<_id>",
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
    "filename": "../Flask/app/file/file/router.py",
    "groupTitle": "File",
    "name": "PostFileIngredient_id"
  },
  {
    "type": "post",
    "url": "/file/recipe/<_id>",
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
        "content": "GET http://127.0.0.1:5000/file/recipe/<_id>",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 201\n{\n}",
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
    "filename": "../Flask/app/file/file/router.py",
    "groupTitle": "File",
    "name": "PostFileRecipe_id"
  },
  {
    "type": "delete",
    "url": "/ingredient/<_id>",
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
        "content": "DELETE http://127.0.0.1:5000/ingredient/<_id>",
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
    "filename": "../Flask/app/ingredient/ingredient/router.py",
    "groupTitle": "Ingredient",
    "name": "DeleteIngredient_id"
  },
  {
    "type": "get",
    "url": "/ingredient",
    "title": "GetAllIngredient",
    "group": "Ingredient",
    "description": "<p>Get file ingredients</p>",
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
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.ingredient.success.ok',\n    'codeStatus': 200,\n    'data': [{'_id': '5e583de9b0fcef0a922a7bc0', 'name': 'aqa_rhr'},\n             {'_id': '5e583de9b0fcef0a922a7bc2', 'name': 'bqa_rhr'}]\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/ingredient/ingredient/router.py",
    "groupTitle": "Ingredient",
    "name": "GetIngredient"
  },
  {
    "type": "get",
    "url": "/ingredient/<_id>",
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
        "content": "GET http://127.0.0.1:5000/ingredient/<_id>",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.ingredient.success.ok',\n    'codeStatus': 200,\n    'data': {'_id': '5e583de9b0fcef0a922a7bc0', 'name': 'aqa_rhr'}\n}",
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
    "filename": "../Flask/app/ingredient/ingredient/router.py",
    "groupTitle": "Ingredient",
    "name": "GetIngredient_id"
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
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "POST http://127.0.0.1:5000/ingredient\n{\n    'name': <name>\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 201\n{\n    'codeMsg': 'cookbook.ingredient.success.created',\n    'codeStatus': 201,\n    'data': {'_id': '5e5840e63ed55d9119064649', 'name': 'qa_rhr_name'}\n}",
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
    "filename": "../Flask/app/ingredient/ingredient/router.py",
    "groupTitle": "Ingredient",
    "name": "PostIngredient"
  },
  {
    "type": "put",
    "url": "/ingredient/<_id>",
    "title": "UpdateIngredient",
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
        "Body Param": [
          {
            "group": "Body Param",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Ingredient's name</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "PUT http://127.0.0.1:5000/ingredient/<_id>\n{\n    'name': <name>\n}",
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
    "filename": "../Flask/app/ingredient/ingredient/router.py",
    "groupTitle": "Ingredient",
    "name": "PutIngredient_id"
  },
  {
    "type": "delete",
    "url": "/recipe/<_id>",
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
        "content": "DELETE http://127.0.0.1:5000/recipe/<_id>",
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
    "filename": "../Flask/app/recipe/recipe/router.py",
    "groupTitle": "Recipe",
    "name": "DeleteRecipe_id"
  },
  {
    "type": "get",
    "url": "/recipe",
    "title": "GetAllRecipe",
    "group": "Recipe",
    "description": "<p>Get file recipes</p>",
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
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.recipe.success.ok',\n    'codeStatus': 200,\n    'data': [{'_id': '5e58484037c99f3231407fbe', 'cooking_time': '', 'level': '', 'nb_people': '', 'note': '',\n              'preparation_time': '', 'resume': '', 'steps': [], 'title': 'aqa_rhr'},\n             {'_id': '5e58484037c99f3231407fc0', 'cooking_time': '', 'level': '', 'nb_people': '', 'note': '',\n              'preparation_time': '', 'resume': '', 'steps': [], 'title': 'bqa_rhr'}]\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/recipe/recipe/router.py",
    "groupTitle": "Recipe",
    "name": "GetRecipe"
  },
  {
    "type": "get",
    "url": "/recipe/<_id>",
    "title": "GetRecipe",
    "group": "Recipe",
    "description": "<p>Get a recipe by it's ObjectId</p>",
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
        "content": "GET http://127.0.0.1:5000/recipe/<_id>",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.recipe.success.ok',\n    'codeStatus': 200,\n    'data': {'_id': '5e58484037c99f3231407fbe', 'cooking_time': '', 'level': '', 'nb_people': '', 'note': '',\n             'preparation_time': '', 'resume': '', 'steps': [], 'title': 'aqa_rhr'}\n}",
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
    "filename": "../Flask/app/recipe/recipe/router.py",
    "groupTitle": "Recipe",
    "name": "GetRecipe_id"
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
            "field": "steps",
            "description": "<p>Recipe's steps</p>"
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
          "content": "HTTPS 201\n{\n    'codeMsg': 'cookbook.recipe.success.created',\n    'codeStatus': 201,\n    'data': {'_id': '5e584a621e2e0101d1d937e3', 'cooking_time': '', 'level': '', 'nb_people': '',\n             'note': '', 'preparation_time': '', 'resume': '', 'steps': [], 'title': 'qa_rhr_title'}\n}",
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
    "filename": "../Flask/app/recipe/recipe/router.py",
    "groupTitle": "Recipe",
    "name": "PostRecipe"
  },
  {
    "type": "put",
    "url": "/recipe/<_id>",
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
            "type": "String",
            "optional": false,
            "field": "title",
            "description": "<p>Recipe's title</p>"
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
            "field": "steps",
            "description": "<p>Recipe's steps</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "PUT http://127.0.0.1:5000/recipe/<_id>\n{\n    'title': <title>\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.recipe.success.created',\n    'codeStatus': 201,\n    'data': {'_id': '5e584a621e2e0101d1d937e3', 'cooking_time': '', 'level': '', 'nb_people': '', 'note': '',\n             'preparation_time': '', 'resume': '', 'steps': [], 'title': 'qa_rhr_title_update'}\n}",
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
    "filename": "../Flask/app/recipe/recipe/router.py",
    "groupTitle": "Recipe",
    "name": "PutRecipe_id"
  },
  {
    "type": "delete",
    "url": "/recipe/<_id>/step/<_position>",
    "title": "DeleteRecipeStep",
    "group": "RecipeSteps",
    "description": "<p>Delete a recipe's step by it's position in the array</p>",
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
            "optional": false,
            "field": "position",
            "description": "<p>Position in recipe's steps array</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "DELETE http://127.0.0.1:5000/recipe/<_id>/step/<position>",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 200\n{\n    'codeMsg': 'cookbook.recipe_steps.success.ok',\n    'codeStatus': 200,\n    'data': {'_id': '5e584ffd0e7d15c4c1022389', 'cooking_time': '', 'ingredients': {}, 'level': '', 'nb_people': '',\n             'note': '', 'preparation_time': '', 'resume': '', 'steps': ['a'], 'title': 'qa_rhr'}}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.recipe_steps.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Must be an integer', 'param': 'position', 'value': 'invalid'}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/recipe/steps/router.py",
    "groupTitle": "RecipeSteps",
    "name": "DeleteRecipe_idStep_position"
  },
  {
    "type": "post",
    "url": "/recipe/<_id>/step",
    "title": "PostRecipeStep",
    "group": "RecipeSteps",
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
          }
        ],
        "Body param": [
          {
            "group": "Body param",
            "type": "String",
            "optional": false,
            "field": "step",
            "description": "<p>Step's value to add</p>"
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
        "content": "POST http://127.0.0.1:5000/recipe/<_id>/step\n{\n    'step': <step>,\n    'position': <position>\n}",
        "type": "json"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Success response:",
          "content": "HTTPS 201\n{\n    'codeMsg': 'cookbook.recipe_steps.success.created',\n    'codeStatus': 201,\n    'data': {'_id': '5e584e658269f301022369ff', 'cooking_time': '', 'ingredients': {}, 'level': '', 'nb_people': '',\n             'note': '', 'preparation_time': '', 'resume': '', 'steps': ['a', 'new_step', 'b'], 'title': 'qa_rhr'}}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error response:",
          "content": "HTTPS 400\n{\n    'codeMsg': 'cookbook.recipe_steps.error.bad_request',\n    'codeStatus': 400,\n    'detail': {'msg': 'Must be an integer', 'param': 'position', 'value': 'invalid'}\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "../Flask/app/recipe/steps/router.py",
    "groupTitle": "RecipeSteps",
    "name": "PostRecipe_idStep"
  }
] });
