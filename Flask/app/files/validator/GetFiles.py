import utils
import app.files.factory.GetFiles as Factory

mongo = utils.Mongo()
validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate GetFiles.
    """