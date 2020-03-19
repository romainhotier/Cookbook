from flask import Blueprint, request

import server.factory as factory
import app.link.ingredient_recipe.model as link_model
import app.link.ingredient_recipe.validator.GetIngredientForRecipe as validator_GetIngredientForRecipe
import app.link.ingredient_recipe.validator.GetRecipeForIngredient as validator_GetRecipeForIngredient
import app.link.ingredient_recipe.factory.PostIngredientRecipe as factory_PostIngredientRecipe
import app.link.ingredient_recipe.validator.PostIngredientRecipe as validator_PostIngredientRecipe
import app.link.ingredient_recipe.factory.PutIngredientRecipe as factory_PutIngredientRecipe
import app.link.ingredient_recipe.validator.PutIngredientRecipe as validator_PutIngredientRecipe
import app.link.ingredient_recipe.validator.DeleteIngredientRecipe as validator_DeleteIngredientRecipe

ingredient_recipe_api = Blueprint('ingredient_recipe_api', __name__)

link = link_model.LinkIngredientRecipe()
get_ingredient_for_recipe_validator = validator_GetIngredientForRecipe.Validator()
get_recipe_for_ingredient_validator = validator_GetRecipeForIngredient.Validator()
post_ingredient_recipe_factory = factory_PostIngredientRecipe.Factory()
post_ingredient_recipe_validator = validator_PostIngredientRecipe.Validator()
put_ingredient_recipe_factory = factory_PutIngredientRecipe.Factory()
put_ingredient_recipe_validator = validator_PutIngredientRecipe.Validator()
delete_ingredient_recipe_validator = validator_DeleteIngredientRecipe.Validator()


@ingredient_recipe_api.route('/link_ingredient_recipe/ingredient/<_id_ingredient>', methods=['GET'])
def get_recipe_for_ingredient(_id_ingredient):
    """
    @api {get} /link_ingredient_recipe/ingredient/<_id_ingredient>  GetRecipeForIngredient
    @apiGroup IngredientRecipe
    @apiDescription Get all recipes for an ingredient by it's ObjectId

    @apiParam (Query param) {String} _id Ingredient's ObjectId
    @apiParam (Query param) {String} [with_title] if "true", add recipe's title

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/link_ingredient_recipe/ingredient/<_id_ingredient>

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.link_ingredient_recipe.success.ok',
        'codeStatus': 200,
        'data': [{'_id': '5e7347c82222535ac818942b', '_id_ingredient': '5e7347c82222535ac8189425',
                  '_id_recipe': '5e7347c82222535ac8189423', 'quantity': 0, 'unit': 'qa_rhr_unit_qa_rhr'},
                {'_id': '5e7347c82222535ac818942f', '_id_ingredient': '5e7347c82222535ac8189427',
                 '_id_recipe': '5e7347c82222535ac8189423', 'quantity': 0, 'unit': 'qa_rhr_unit_qa_rhr'}]
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.link_ingredient_recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    """ check param enrichment """
    with_title = get_recipe_for_ingredient_validator.is_string_boolean(with_title=request.args.get('with_title'))[1]
    """ check param _id """
    get_recipe_for_ingredient_validator.is_object_id_valid(_id=_id_ingredient)
    """ get all """
    data = link.select_all_by_id_ingredient(_id_ingredient=_id_ingredient)
    """ add enrichment if needed """
    if with_title:
        data.add_enrichment_title_for_all()
    """ return response """
    return factory.ServerResponse().return_response(data=data.get_result(), api="link_ingredient_recipe", code=200)


@ingredient_recipe_api.route('/link_ingredient_recipe/recipe/<_id_recipe>', methods=['GET'])
def get_ingredient_for_recipe(_id_recipe):
    """
    @api {get} /link_ingredient_recipe/recipe/<_id_recipe>  GetIngredientForRecipe
    @apiGroup IngredientRecipe
    @apiDescription Get all ingredients for a recipe by it's ObjectId

    @apiParam (Query param) {String} _id Recipe's ObjectId
    @apiParam (Query param) {String} [with_name] if "true", add ingredient's name

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/link_ingredient_recipe/recipe/<_id_recipe>

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.link_ingredient_recipe.success.ok',
        'codeStatus': 200,
        'data': [{'_id': '5e7347c82222535ac818942b', '_id_ingredient': '5e7347c82222535ac8189425',
                  '_id_recipe': '5e7347c82222535ac8189423', 'quantity': 0, 'unit': 'qa_rhr_unit_qa_rhr'},
                {'_id': '5e7347c82222535ac818942f', '_id_ingredient': '5e7347c82222535ac8189427',
                 '_id_recipe': '5e7347c82222535ac8189423', 'quantity': 0, 'unit': 'qa_rhr_unit_qa_rhr'}]
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.link_ingredient_recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    """ check param enrichment """
    with_name = get_ingredient_for_recipe_validator.is_string_boolean(with_name=request.args.get('with_name'))[1]
    """ check param _id """
    get_ingredient_for_recipe_validator.is_object_id_valid(_id=_id_recipe)
    """ get all """
    data = link.select_all_by_id_recipe(_id_recipe=_id_recipe)
    """ add enrichment if needed """
    if with_name:
        data.add_enrichment_name_for_all()
    """ return response """
    return factory.ServerResponse().return_response(data=data.get_result(), api="link_ingredient_recipe", code=200)


@ingredient_recipe_api.route('/link_ingredient_recipe', methods=['POST'])
def post_ingredient_recipe():
    """
    @api {post} /link_ingredient_recipe  PostIngredientRecipe
    @apiGroup IngredientRecipe
    @apiDescription Associate an ingredient to a recipe

    @apiParam (Body param) {String} _id_ingredient Ingredient's ObjectId to link
    @apiParam (Body param) {String} _id_recipe Recipe's ObjectId to link
    @apiParam (Body param) {Integer} quantity Ingredient's quantity for the recipe
    @apiParam (Body param) {String} unit Ingredient's unit for the recipe

    @apiExample {json} Example usage:
    POST http://127.0.0.1:5000/link_ingredient_recipe
    {
        '_id_ingredient': <_id_ingredient>,
        '_id_recipe': <_id_recipe>,
        'quantity': <quantity>,
        'unit': <unit>,
    }

    @apiSuccessExample {json} Success response:
    HTTPS 201
    {
        'codeMsg': 'cookbook.ingredient_recipe.success.created',
        'codeStatus': 201,
        'data': {'_id': '5e722e87f94648b72c7d8f03', '_id_ingredient': '5e722e875754d5e780a8f1e5',
                 '_id_recipe': '5e722e875754d5e780a8f1e3', 'quantity': 5, 'unit': 'qa_rhr_unit'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient_recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id_ingredient', 'value': 'invalid'}
    }
    """
    """ check body """
    body = post_ingredient_recipe_factory.clean_body(data=request.json)
    post_ingredient_recipe_validator.is_body_valid(data=body)
    """ check if link already exist """
    post_ingredient_recipe_validator.is_link_already_exist(_id_ingredient=body["_id_ingredient"],
                                                           _id_recipe=body["_id_recipe"])
    """ add link """
    data = link.insert(data=body)
    """ return response """
    return factory.ServerResponse().return_response(data=data.get_result(), api="link_ingredient_recipe", code=201)


@ingredient_recipe_api.route('/link_ingredient_recipe/<_id>', methods=['PUT'])
def put_ingredient_recipe(_id):
    """
    @api {put} /link_ingredient_recipe/<_id>  PutIngredientRecipe
    @apiGroup IngredientRecipe
    @apiDescription Update quantity and unit of an association ingredient-recipe

    @apiParam (Query param) {String} _id Link's ObjectId
    @apiParam (Body param) {Integer} [quantity] Ingredient's quantity for the recipe
    @apiParam (Body param) {String} [unit] Ingredient's unit for the recipe

    @apiExample {json} Example usage:
    PUT http://127.0.0.1:5000/link_ingredient_recipe/<_id>
    {
        'quantity': <quantity>,
        'unit': <unit>,
    }

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.ingredient_recipe.success.created',
        'codeStatus': 201,
        'data': {'_id': '5e722e87f94648b72c7d8f03', '_id_ingredient': '5e722e875754d5e780a8f1e5',
                 '_id_recipe': '5e722e875754d5e780a8f1e3', 'quantity': 10, 'unit': 'qa_rhr_unit_update'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient_recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    """ check id """
    put_ingredient_recipe_validator.is_object_id_valid(_id=_id)
    """ check body """
    body = put_ingredient_recipe_factory.clean_body(data=request.json)
    put_ingredient_recipe_validator.is_body_valid(data=body)
    """ update link """
    data = link.update(_id=_id, data=body)
    """ return response """
    return factory.ServerResponse().return_response(data=data.get_result(), api="link_ingredient_recipe", code=200)


@ingredient_recipe_api.route('/link_ingredient_recipe/<_id>', methods=['DELETE'])
def delete_ingredient_recipe(_id):
    """
    @api {delete} /link_ingredient_recipe/<_id>  DeleteIngredientRecipe
    @apiGroup IngredientRecipe
    @apiDescription Delete an association ingredient-recipe

    @apiParam (Query param) {String} _id Link's ObjectId

    @apiExample {json} Example usage:
    DELETE http://127.0.0.1:5000/link_ingredient_recipe/<_id>

    @apiSuccessExample {json} Success response:
    HTTPS 204

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.ingredient_recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    """ check id """
    delete_ingredient_recipe_validator.is_object_id_valid(_id=_id)
    """ delete link """
    link.delete(_id=_id)
    """ return response """
    return factory.ServerResponse().return_response(data=None, api="link_ingredient_recipe", code=204)


@ingredient_recipe_api.errorhandler(400)
def validator_failed(error):
    """" abort 400 """
    return factory.ServerResponse().return_response(data=error.description, api="link_ingredient_recipe", code=400)


@ingredient_recipe_api.errorhandler(404)
def not_found(error):
    """" abort 404 """
    return factory.ServerResponse().return_response(data=error.description, api="ingredient_recipe", code=404)
