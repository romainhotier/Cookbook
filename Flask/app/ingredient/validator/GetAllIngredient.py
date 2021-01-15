from app import utils
import app.ingredient.factory.GetAllIngredient as Factory

validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate GetAllIngredient.
    """
