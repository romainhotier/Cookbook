from flask import Blueprint, request

import utils
import app.recipe.factory as factory
import app.recipe.validator as validator
import app.recipe as recipe_model
import app.ingredient as ingredient_model
import app.file as file_model

api = Blueprint('recipe', __name__, url_prefix='/recipe')

recipe = recipe_model.RecipeModel
step = recipe_model.StepModel
ingredient_recipe = ingredient_model.IngredientRecipeModel
file = file_model.FileModel


@api.route('/<_id>', methods=['DELETE'])
def delete_recipe(_id):
    """
    @api {delete} /recipe/<_id_recipe>  DeleteRecipe
    @apiGroup Recipe
    @apiDescription Delete an recipe by it's ObjectId

    @apiParam (Query param) {String} _id Recipe's ObjectId

    @apiExample {json} Example usage:
    DELETE http://127.0.0.1:5000/recipe/<_id_recipe>

    @apiSuccessExample {json} Success response:
    HTTPS 204

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    """ check param _id """
    validator.ValidatorDeleteRecipe.is_object_id_valid(_id=_id)
    """ clean files recipe """
    file.clean_file_by_id_parent(_id_parent=_id)
    """ clean files steps and link """
    for _id_step in recipe.get_all_step_id(_id=_id):
        file.clean_file_by_id_parent(_id_parent=_id_step)
    ingredient_recipe.clean_link_by_id_recipe(_id_recipe=_id)
    """ delete recipe """
    recipe.delete(_id=_id)
    """ return response """
    return utils.Server.return_response(data=None, api=api.name, code=204)


@api.route('/<_id_recipe>/step/<_id_step>', methods=['DELETE'])
def delete_recipe_step(_id_recipe, _id_step):
    """
    @api {delete} /recipe/<_id_recipe>/step/<_id_step>  DeleteRecipeStep
    @apiGroup Recipe
    @apiDescription Delete a recipe's step

    @apiParam (Query param) {String} _id_recipe Recipe's ObjectId
    @apiParam (Query param) {String} _id_step Step's ObjectId
    @apiParam (Query param) {String} [with_files] if "true", add recipe's files

    @apiExample {json} Example usage:
    DELETE http://127.0.0.1:5000/recipe/<_id_recipe>/step/<_id_step>

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.recipe.success.ok',
        'codeStatus': 200,
        'data': {'_id': '5e68acb9e067528c70c75f3c', 'cooking_time': 0, 'level': 0, 'nb_people': 0, 'note': '',
                 'preparation_time': 0, 'resume': '', title': 'qa_rhr', 'slug': '', 'categories': [],
                 'steps': [{'_id': '5e68acb97b0ead079be3cef7', 'step': 'another_previous_step'}]}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an integer', 'param': 'position', 'value': 'invalid'}
    }
    """
    """ check param enrichment """
    with_files = validator.ValidatorDeleteRecipeStep.is_string_boolean(with_files=request.args.get('with_files'))[1]
    """ check param _id """
    validator.ValidatorDeleteRecipeStep.is_object_id_valid_recipe(_id=_id_recipe)
    validator.ValidatorDeleteRecipeStep.is_object_id_valid_steps(_id_recipe=_id_recipe, _id_step=_id_step)
    """ delete step """
    data = step.delete(_id_recipe=_id_recipe, _id_step=_id_step)
    """ clean files """
    file.clean_file_by_id_parent(_id_parent=_id_step)
    """ add enrichment if needed """
    if with_files:
        data.add_enrichment_file_for_one()
    """ return response """
    return utils.Server.return_response(data=data.json, api=api.name, code=200)


@api.route('', methods=['GET'])
def get_all_recipe():
    """
    @api {get} /recipe  GetAllRecipe
    @apiGroup Recipe
    @apiDescription Get file recipes

    @apiParam (Query param) {String} [with_files] if "true", add recipe's files

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/recipe

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.recipe.success.ok',
        'codeStatus': 200,
        'data': [{'_id': '5e71eb8f39358991f2ea19f6', 'categories': [], 'cooking_time': 0, 'level': 0, 'nb_people': 0,
                  'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'steps': [], 'title': 'qa_rhr_1'},
                 {'_id': '5e71eb8f39358991f2ea19f7', 'categories': [], 'cooking_time': 0, 'level': 0, 'nb_people': 0,
                  'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'steps': [], 'title': 'aqa_rhr_2'}]
    }
    """
    """ check param enrichment """
    with_files = validator.ValidatorGetAllRecipe.is_string_boolean(with_files=request.args.get('with_files'))[1]
    """ get all recipe """
    data = recipe.select_all()
    """ add enrichment if needed """
    if with_files:
        data.add_enrichment_file_for_all()
    """ return response """
    return utils.Server.return_response(data=data.json, api=api.name, code=200)


@api.route('/<_id_recipe>/ingredient', methods=['GET'])
def get_ingredient_for_recipe(_id_recipe):
    """
    @api {get} /recipe/<_id_recipe>/ingredient  GetIngredientForRecipe
    @apiGroup Recipe
    @apiDescription Get all ingredients for a recipe by it's ObjectId

    @apiParam (Query param) {String} _id Recipe's ObjectId
    @apiParam (Query param) {String} [with_name] if "true", add ingredient's name

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/recipe/<_id_recipe>/ingredient

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.recipe.success.ok',
        'codeStatus': 200,
        'data': [{'_id': '5e7347c82222535ac818942b', '_id_ingredient': '5e7347c82222535ac8189425',
                  '_id_recipe': '5e7347c82222535ac8189423', 'quantity': 0, 'unit': 'qa_rhr_unit_qa_rhr'},
                {'_id': '5e7347c82222535ac818942f', '_id_ingredient': '5e7347c82222535ac8189427',
                 '_id_recipe': '5e7347c82222535ac8189423', 'quantity': 0, 'unit': 'qa_rhr_unit_qa_rhr'}]
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    """ check param enrichment """
    with_name = validator.ValidatorGetIngredientForRecipe.is_string_boolean(with_name=request.args.get('with_name'))[1]
    """ check param _id """
    validator.ValidatorGetIngredientForRecipe.is_object_id_valid(_id=_id_recipe)
    """ get all """
    data = ingredient_recipe.select_all_by_id_recipe(_id_recipe=_id_recipe)
    """ add enrichment if needed """
    if with_name:
        data.add_enrichment_name_for_all()
    """ return response """
    return utils.Server.return_response(data=data.json, api=api.name, code=200)


@api.route('/<_id>', methods=['GET'])
def get_recipe(_id):
    """
    @api {get} /recipe/<_id_recipe>  GetRecipe
    @apiGroup Recipe
    @apiDescription Get a recipe by it's ObjectId

    @apiParam (Query param) {String} _id Recipe's ObjectId
    @apiParam (Query param) {String} [with_files] if "true", add recipe's files

    @apiExample {json} Example usage:
    GET http://127.0.0.1:5000/recipe/<_id_recipe>

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.recipe.success.ok',
        'codeStatus': 200,
        'data': {'_id': '5e71eb8f39358991f2ea19f6', 'categories': [], 'cooking_time': 0, 'level': 0, 'nb_people': 0,
                 'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'steps': [], 'title': 'aqa_rhr'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an ObjectId', 'param': '_id', 'value': 'invalid'}
    }
    """
    """ check param enrichment """
    with_files = validator.ValidatorGetRecipe.is_string_boolean(with_files=request.args.get('with_files'))[1]
    """ check param _id """
    validator.ValidatorGetRecipe.is_object_id_valid(_id=_id)
    """ get recipe """
    data = recipe.select_one(_id=_id)
    """ add enrichment if needed """
    if with_files:
        data.add_enrichment_file_for_one()
    """ return response """
    return utils.Server.return_response(data=data.json, api=api.name, code=200)


@api.route('', methods=['POST'])
def post_recipe():
    """
    @api {post} /recipe  PostRecipe
    @apiGroup Recipe
    @apiDescription Create a recipe

    @apiParam (Body param) {String} title Recipe's title
    @apiParam (Body param) {String} slug Recipe's slug for url
    @apiParam (Body param) {Integer} [level] Recipe's level (between 0 and 3)
    @apiParam (Body param) {String} [resume] Recipe's resume
    @apiParam (Body param) {Integer} [cooking_time] Recipe's cooking time
    @apiParam (Body param) {Integer} [preparation_time] Recipe's preparation time
    @apiParam (Body param) {String} [nb_people] Recipe's number of people
    @apiParam (Body param) {String} [note] Recipe's note
    @apiParam (Body param) {Array} [steps] Recipe's steps
    @apiParam (Body param) {Array} [categories] Recipe's categories

    @apiExample {json} Example usage:
    POST http://127.0.0.1:5000/recipe
    {
        'title': <title>
    }

    @apiSuccessExample {json} Success response:
    HTTPS 201
    {
        'codeMsg': 'cookbook.recipe.success.created',
        'codeStatus': 201,
        'data': {'_id': '5e71eb8f39358991f2ea19f6', 'categories': [], 'cooking_time': 0, 'level': 0, 'nb_people': 0,
                 'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'steps': [], 'title': 'aqa_rhr'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be a string', 'param': 'title', 'value': {}}
    }
    """
    """ check body """
    body = factory.FactoryPostRecipe.clean_body(data=request.json)
    validator.ValidatorPostRecipe.is_body_valid(data=body)
    """ insert recipe """
    data = recipe.insert(data=body)
    """ return result """
    return utils.Server.return_response(data=data.json, api=api.name, code=201)


@api.route('/<_id>/step', methods=['POST'])
def post_recipe_step(_id):
    """
    @api {post} /recipe/<_id_recipe>/step PostRecipeStep
    @apiGroup Recipe
    @apiDescription Create a recipe's step. Can specify where to add the step

    @apiParam (Query param) {String} _id Recipe's ObjectId
    @apiParam (Query param) {String} [with_files] if "true", add recipe's files
    @apiParam (Body param) {String} step Step's value to add
    @apiParam (Body param) {Integer} [position] Position in recipe's steps array.
                                                If not specified, add at the end of the array

    @apiExample {json} Example usage:
    POST http://127.0.0.1:5000/recipe/<_id_recipe>/step
    {
        'step': <step>,
        'position': <position>
    }

    @apiSuccessExample {json} Success response:
    HTTPS 201
    {
        'codeMsg': 'cookbook.recipe.success.created',
        'codeStatus': 201,
        'data': {'_id': '5e68acb9e067528c70c75f3c', 'cooking_time': 0, 'level': 0, 'nb_people': 0, 'note': '',
                 'preparation_time': 0, 'resume': '', title': 'qa_rhr', 'slug': '', 'categories': [],
                 'steps': [{'_id': '5e68acb97b0ead079be3cef7', 'step': 'new_step'}]}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an integer', 'param': 'position', 'value': 'invalid'}
    }
    """
    """ check param enrichment """
    with_files = validator.ValidatorPostRecipeStep.is_string_boolean(with_files=request.args.get('with_files'))[1]
    """ check param _id """
    validator.ValidatorPostRecipeStep.is_object_id_valid(_id=_id)
    """ check body """
    body = factory.FactoryPostRecipeStep.clean_body(data=request.json)
    validator.ValidatorPostRecipeStep.is_body_valid(_id=_id, data=body)
    """ insert step """
    data = step.insert(_id=_id, data=body)
    """ add enrichment if needed """
    if with_files:
        data.add_enrichment_file_for_one()
    """ return response """
    return utils.Server.return_response(data=data.json, api=api.name, code=201)


@api.route('/step', methods=['POST'])
def post_step():
    """
    @api {post} /recipe/step PostStep
    @apiGroup Recipe
    @apiDescription Return en step to add in param 'steps' for PostRecipe

    @apiParam (Body param) {String} step Step's value

    @apiExample {json} Example usage:
    POST http://127.0.0.1:5000/recipe/step
    {
        'step': <step>,
    }

    @apiSuccessExample {json} Success response:
    HTTPS 201
    {
        'codeMsg': 'cookbook.recipe.success.created',
        'codeStatus': 201,
        'data': {'_id': '5e68acb9e067528c70c75f3c', 'step': ''}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be not empty', 'param': 'step', 'value': ''}
    }
    """
    """ check body """
    body = factory.FactoryPostStep.clean_body(data=request.json)
    validator.ValidatorPostStep.is_body_valid(data=body)
    """ insert step """
    data = factory.FactoryPostStep.create_step(data=body)
    """ return response """
    return utils.Server.return_response(data=data, api=api.name, code=201)


@api.route('/<_id>', methods=['PUT'])
def put_recipe(_id):
    """
    @api {put} /recipe/<_id_recipe>  PutRecipe
    @apiGroup Recipe
    @apiDescription Update a recipe

    @apiParam (Query param) {String} _id Recipe's ObjectId
    @apiParam (Query param) {String} [with_files] if "true", add recipe's files
    @apiParam (Body param) {String} [title] Recipe's title
    @apiParam (Body param) {String} [slug] Recipe's slug for url
    @apiParam (Body param) {String} [level] Recipe's level
    @apiParam (Body param) {String} [resume] Recipe's resume
    @apiParam (Body param) {String} [cooking_time] Recipe's cooking time
    @apiParam (Body param) {String} [preparation_time] Recipe's preparation time
    @apiParam (Body param) {String} [nb_people] Recipe's number of people
    @apiParam (Body param) {String} [note] Recipe's note
    @apiParam (Body param) {Array} [categories] Recipe's categories

    @apiExample {json} Example usage:
    PUT http://127.0.0.1:5000/recipe/<_id_recipe>
    {
        'title': <title>
    }

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.recipe.success.created',
        'codeStatus': 201,
        'data': {'_id': '5e71eb8f39358991f2ea19f6', 'categories': [], 'cooking_time': 0, 'level': 0, 'nb_people': 0,
                 'note': '', 'preparation_time': 0, 'resume': '', 'slug': '', 'steps': [], 'title': 'aqa_rhr'}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be a string', 'param': 'title', 'value': {}}
    }
    """
    """ check param enrichment """
    with_files = validator.ValidatorPutRecipe.is_string_boolean(with_files=request.args.get('with_files'))[1]
    """ check param _id """
    validator.ValidatorPutRecipe.is_object_id_valid(_id=_id)
    """ check body """
    body = factory.FactoryPutRecipe.clean_body(data=request.json)
    validator.ValidatorPutRecipe.is_body_valid(data=body)
    """ update recipe """
    data = recipe.update(_id=_id, data=body)
    """ add enrichment if needed """
    if with_files:
        data.add_enrichment_file_for_one()
    """ return response """
    return utils.Server.return_response(data=data.json, api=api.name, code=200)


@api.route('/<_id_recipe>/step/<_id_step>', methods=['PUT'])
def put_recipe_step(_id_recipe, _id_step):
    """
    @api {put} /recipe/<_id_recipe>/step/<_id_step>  PutRecipeStep
    @apiGroup Recipe
    @apiDescription Update a recipe's step

    @apiParam (Query param) {String} _id_recipe Recipe's ObjectId
    @apiParam (Query param) {String} _id_step Step's ObjectId
    @apiParam (Query param) {String} [with_files] if "true", add recipe's files
    @apiParam (Body param) {String} step Step's value to add

    @apiExample {json} Example usage:
    PUT http://127.0.0.1:5000/recipe/<_id_recipe>/step/<_id_step>
    {
        'step': <step>
    }

    @apiSuccessExample {json} Success response:
    HTTPS 200
    {
        'codeMsg': 'cookbook.recipe.success.ok',
        'codeStatus': 200,
        'data': {'_id': '5e68acb9e067528c70c75f3c', 'cooking_time': 0, 'level': 0, 'nb_people': 0, 'note': '',
                 'preparation_time': 0, 'resume': '', title': 'qa_rhr', 'slug': '', 'categories': [],
                 'steps': [{'_id': '5e68acb97b0ead079be3cef7', 'step': 'updated_step'}]}
    }

    @apiErrorExample {json} Error response:
    HTTPS 400
    {
        'codeMsg': 'cookbook.recipe.error.bad_request',
        'codeStatus': 400,
        'detail': {'msg': 'Must be an integer', 'param': 'position', 'value': 'invalid'}
    }
    """
    """ check param enrichment """
    with_files = validator.ValidatorPutRecipeStep.is_string_boolean(with_files=request.args.get('with_files'))[1]
    """ check param _id """
    validator.ValidatorPutRecipeStep.is_object_id_valid_recipe(_id=_id_recipe)
    validator.ValidatorPutRecipeStep.is_object_id_valid_steps(_id_recipe=_id_recipe, _id_step=_id_step)
    """ check body """
    body = factory.FactoryPutRecipeStep.clean_body(data=request.json)
    validator.ValidatorPutRecipeStep.is_body_valid(data=body)
    """ update step """
    data = step.update(_id_recipe=_id_recipe, _id_step=_id_step, data=body)
    """ add enrichment if needed """
    if with_files:
        data.add_enrichment_file_for_one()
    """ return response """
    return utils.Server.return_response(data=data.json, api=api.name, code=200)


@api.errorhandler(400)
def validator_failed(error):
    """" abort 400 """
    return utils.Server.return_response(data=error.description, api=api.name, code=400)


@api.errorhandler(404)
def not_found(error):
    """" abort 404 """
    return utils.Server.return_response(data=error.description, api=api.name, code=404)
