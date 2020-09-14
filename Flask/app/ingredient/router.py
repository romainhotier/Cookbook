from flask import Blueprint, request

import utils
import app.ingredient.factory as factory
import app.ingredient.validator as validator
import app.ingredient as ingredient_model
import app.file as file_model

api = Blueprint('ingredient', __name__, url_prefix='/ingredient')
#auth = utils.Auth

ingredient = ingredient_model.IngredientModel
ingredient_recipe = ingredient_model.IngredientRecipeModel
file = file_model.FileModel

#@api.before_request
#@auth.login_required
#def protect():
#    pass

# print(get_jwt_identity())
# headers={"Authorization": "Bearer " + token}


@api.route('/<_id>', methods=['DELETE'])
def delete_ingredient(_id):
    """
    @api {delete} /ingredient/<_id_ingredient>  DeleteIngredient
    @apiGroup Ingredient
    @apiDescription Delete an ingredient by it's ObjectId

    @apiParam (Query param) {String} _id Ingredient's ObjectId

    @apiExample {json} Example usage:
    DELETE http://127.0.0.1:5000/ingredient/<_id_ingredient>

    @apiSuccessExample {json} Success response:
    HTTPS 204

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    """ check param _id """
    validator.ValidatorDeleteIngredient.is_object_id_valid(_id=_id)
    """ clean files and link """
    file.clean_file_by_id_parent(_id_parent=_id)
    ingredient_recipe.clean_link_by_id_ingredient(_id_ingredient=_id)
    """ delete ingredient """
    ingredient.delete(_id=_id)
    return utils.Server.return_response(data=None, api=api.name, code=204)


@api.route('/recipe/<_id>', methods=['DELETE'])
def delete_ingredient_recipe(_id):
    """
    @api {delete} /ingredient/recipe/<_id_ingredient_recipe>  DeleteIngredientRecipe
    @apiGroup Ingredient
    @apiDescription Delete an association ingredient-recipe

    @apiParam (Query param) {String} _id Link's ObjectId

    @apiExample {json} Example usage:
    DELETE http://127.0.0.1:5000/ingredient/recipe/<_id_ingredient_recipe>

    @apiSuccessExample {json} Success response:
    HTTPS 204

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    """ check id """
    validator.ValidatorDeleteIngredientRecipe.is_object_id_valid(_id=_id)
    """ delete link """
    ingredient_recipe.delete(_id=_id)
    """ return response """
    return utils.Server.return_response(data=None, api=api.name, code=204)


@api.route('', methods=['GET'])
def get_all_ingredient():
    """
    @api {get} /ingredient  GetAllIngredient
    @apiGroup Ingredient
    @apiDescription Get file ingredients

    @apiParam (Query param) {String} [with_files] if "true", add ingredient's files

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/ingredient

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.ingredient.success.ok',
        'codeStatus': 200,
        'data': [{'_id': '5e583de9b0fcef0a922a7bc0', 'name': 'aqa_rhr'},
                 {'_id': '5e583de9b0fcef0a922a7bc2', 'name': 'bqa_rhr'}]
    }
    """
    """ check param enrichment """
    with_files = validator.ValidatorGetAllIngredient.is_string_boolean(with_files=request.args.get('with_files'))[1]
    """ get all ingredient """
    data = ingredient.select_all()
    """ add enrichment if needed """
    if with_files:
        data.add_enrichment_file_for_all()
    """ return response """
    return utils.Server.return_response(data=data.result, api=api.name, code=200)


@api.route('/<_id>', methods=['GET'])
def get_ingredient(_id):
    """
    @api {get} /ingredient/<_id_ingredient>  GetIngredient
    @apiGroup Ingredient
    @apiDescription Get an ingredient by it's ObjectId

    @apiParam (Query param) {String} _id Ingredient's ObjectId
    @apiParam (Query param) {String} [with_files] if "true", add ingredient's files

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/ingredient/<_id_ingredient>

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.ingredient.success.ok',
        'codeStatus': 200,
        'data': {'_id': '5e583de9b0fcef0a922a7bc0', 'name': 'aqa_rhr'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    """ check param enrichment """
    with_files = validator.ValidatorGetIngredient.is_string_boolean(with_files=request.args.get('with_files'))[1]
    """ check param _id """
    validator.ValidatorGetIngredient.is_object_id_valid(_id=_id)
    """ get ingredient """
    data = ingredient.select_one(_id=_id)
    """ add enrichment if needed """
    if with_files:
        data.add_enrichment_file_for_one()
    """ return response """
    return utils.Server.return_response(data=data.result, api=api.name, code=200)


@api.route('/search', methods=['GET'])
def search_ingredient():
    """
    @api {get} /ingredient/search SearchIngredient
    @apiGroup Ingredient
    @apiDescription Search an ingredient by key/value

    @apiParam (Query param) {String} name ingredient's name
    @apiParam (Query param) {String} [with_files] if "true", add ingredient's files

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/ingredient/search?name=<ingredient_name>

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.ingredient.success.ok',
        'codeStatus': 200,
        'data': [{'_id': '5e583de9b0fcef0a922a7bc0', 'name': 'aqa_rhr'}]
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be a string', 'param': 'name', 'value': ''}
    }
    """
    """ check param enrichment """
    with_files = validator.ValidatorSearchIngredient.is_string_boolean(with_files=request.args.get('with_files'))[1]
    """ check param name """
    validator.ValidatorSearchIngredient.is_name_valid(name=request.args.get('name'))
    """ search ingredient """
    data = ingredient.search(key=request.args.get('name'))
    """ add enrichment if needed """
    if with_files:
        data.add_enrichment_file_for_all()
    """ return response """
    return utils.Server.return_response(data=data.result, api=api.name, code=200)


@api.route('/<_id>/recipe', methods=['GET'])
def get_recipe_for_ingredient(_id):
    """
    @api {get} /ingredient/<_id_ingredient>/recipe  GetRecipeForIngredient
    @apiGroup Ingredient
    @apiDescription Get all recipes for an ingredient by it's ObjectId

    @apiParam (Query param) {String} _id Ingredient's ObjectId
    @apiParam (Query param) {String} [with_title] if "true", add recipe's title

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/ingredient/<_id_ingredient>/recipe

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.ingredient.success.ok',
        'codeStatus': 200,
        'data': [{'_id': '5e7347c82222535ac818942b', '_id_ingredient': '5e7347c82222535ac8189425',
                  '_id_recipe': '5e7347c82222535ac8189423', 'quantity': 0, 'unit': 'qa_rhr_unit_qa_rhr'},
                {'_id': '5e7347c82222535ac818942f', '_id_ingredient': '5e7347c82222535ac8189427',
                 '_id_recipe': '5e7347c82222535ac8189423', 'quantity': 0, 'unit': 'qa_rhr_unit_qa_rhr'}]
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    """ check param enrichment """
    with_title = validator.ValidatorGetRecipeForIngredient.is_string_boolean(with_title=request.args.get('with_title'))[
        1]
    """ check param _id """
    validator.ValidatorGetRecipeForIngredient.is_object_id_valid(_id=_id)
    """ get all """
    data = ingredient_recipe.select_all_by_id_ingredient(_id_ingredient=_id)
    """ add enrichment if needed """
    if with_title:
        data.add_enrichment_title_for_all()
    """ return response """
    return utils.Server.return_response(data=data.result, api=api.name, code=200)


@api.route('', methods=['POST'])
def post_ingredient():
    """
    @api {post} /ingredient  PostIngredient
    @apiGroup Ingredient
    @apiDescription Create an ingredient

    @apiParam (Body param) {String} name Ingredient's name

    @apiExample {json} Example usage:
    POST http://127.0.0.1:5000/ingredient
    {
        'name': <name>
    }

    @apiSuccessExample {json} Success response:
    HTTPS 201
    {
        'codeMsg': 'cookbook.ingredient.success.created',
        'codeStatus': 201,
        'data': {'_id': '5e5840e63ed55d9119064649', 'name': 'qa_rhr_name'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Is required', 'param': 'name'}}
    }
    """
    """ check body """
    body = factory.FactoryPostIngredient.clean_body(data=request.json)
    validator.ValidatorPostIngredient.is_body_valid(data=body)
    """ add ingredient """
    data = ingredient.insert(data=body)
    """ return response """
    return utils.Server.return_response(data=data.result, api=api.name, code=201)


@api.route('/recipe', methods=['POST'])
def post_ingredient_recipe():
    """
    @api {post} /ingredient/recipe  PostIngredientRecipe
    @apiGroup Ingredient
    @apiDescription Associate an ingredient to a recipe

    @apiParam (Body param) {String} _id_ingredient Ingredient's ObjectId to link
    @apiParam (Body param) {String} _id_recipe Recipe's ObjectId to link
    @apiParam (Body param) {Integer} quantity Ingredient's quantity for the recipe
    @apiParam (Body param) {String} unit Ingredient's unit for the recipe

    @apiExample {json} Example usage:
    POST http://127.0.0.1:5000/ingredient/recipe
    {
        '_id_ingredient': <_id_ingredient>,
        '_id_recipe': <_id_recipe>,
        'quantity': <quantity>,
        'unit': <unit>,
    }

    @apiSuccessExample {json} Success response:
    HTTPS 201
    {
        'codeMsg': 'cookbook.ingredient.success.created',
        'codeStatus': 201,
        'data': {'_id': '5e722e87f94648b72c7d8f03', '_id_ingredient': '5e722e875754d5e780a8f1e5',
                 '_id_recipe': '5e722e875754d5e780a8f1e3', 'quantity': 5, 'unit': 'qa_rhr_unit'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id_ingredient', 'value': 'invalid'}
    }
    """
    """ check body """
    body = factory.FactoryPostIngredientRecipe.clean_body(data=request.json)
    validator.ValidatorPostIngredientRecipe.is_body_valid(data=body)
    """ add link """
    data = ingredient_recipe.insert(data=body)
    """ return response """
    return utils.Server.return_response(data=data.result, api=api.name, code=201)


@api.route('/<_id>', methods=['PUT'])
def put_ingredient(_id):
    """
    @api {put} /ingredient/<_id_ingredient>  UpdateIngredient
    @apiGroup Ingredient
    @apiDescription Update an ingredient by it's ObjectId

    @apiParam (Query param) {String} _id Ingredient's ObjectId
    @apiParam (Query param) {String} [with_files] if "true", add ingredient's files
    @apiParam (Body Param) {String} name Ingredient's name

    @apiExample {json} Example usage:
    PUT http://127.0.0.1:5000/ingredient/<_id_ingredient>
    {
        'name': <name>
    }

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.ingredient.success.ok',
        'codeStatus': 20O,
        'data': {'_id': '5e5840e63ed55d9119064649', 'name': 'qa_rhr_name_update'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Is required', 'param': 'name'}}
    }
    """
    """ check param enrichment """
    with_files = validator.ValidatorPutIngredient.is_string_boolean(with_files=request.args.get('with_files'))[1]
    """ check param _id """
    validator.ValidatorPutIngredient.is_object_id_valid(_id=_id)
    """ check body """
    body = factory.FactoryPutIngredient.clean_body(data=request.json)
    validator.ValidatorPutIngredient.is_body_valid(data=body)
    """ update ingredient """
    data = ingredient.update(_id=_id, data=body)
    """ add enrichment if needed """
    if with_files:
        data.add_enrichment_file_for_one()
    """ return response """
    return utils.Server.return_response(data=data.result, api=api.name, code=200)


@api.route('/recipe/<_id>', methods=['PUT'])
def put_ingredient_recipe(_id):
    """
    @api {put} /ingredient/recipe/<_id_ingredient_recipe>  PutIngredientRecipe
    @apiGroup Ingredient
    @apiDescription Update quantity and unit of an association ingredient-recipe

    @apiParam (Query param) {String} _id Link's ObjectId
    @apiParam (Body param) {Integer} [quantity] Ingredient's quantity for the recipe
    @apiParam (Body param) {String} [unit] Ingredient's unit for the recipe

    @apiExample {json} Example usage:
    PUT http://127.0.0.1:5000/ingredient/recipe/<_id_ingredient_recipe>
    {
        'quantity': <quantity>,
        'unit': <unit>,
    }

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.ingredient.success.created',
        'codeStatus': 201,
        'data': {'_id': '5e722e87f94648b72c7d8f03', '_id_ingredient': '5e722e875754d5e780a8f1e5',
                 '_id_recipe': '5e722e875754d5e780a8f1e3', 'quantity': 10, 'unit': 'qa_rhr_unit_update'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    """ check id """
    validator.ValidatorPutIngredientRecipe.is_object_id_valid(_id=_id)
    """ check body """
    body = factory.FactoryPutIngredientRecipe.clean_body(data=request.json)
    validator.ValidatorPutIngredientRecipe.is_body_valid(data=body)
    """ update link """
    data = ingredient_recipe.update(_id=_id, data=body)
    """ return response """
    return utils.Server.return_response(data=data.result, api=api.name, code=200)


@api.errorhandler(400)
def validator_failed(error):
    """" abort 400 """
    return utils.Server.return_response(data=error.description, api=api.name, code=400)


# @api.errorhandler(404)
# def not_found(error):
#     """" abort 404 """
#     print("router ingredient")
#     return utils.Server.return_response(data=error.description, api=api.name, code=404)
