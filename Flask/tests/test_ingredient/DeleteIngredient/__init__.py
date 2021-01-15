from tests import rep


class DeleteIngredient(object):
    """ Class to test DeleteIngredient.
    """

    def __init__(self):
        self.url = 'ingredient'
        self.param_id = "_id"
        self.rep_code_msg_ok = rep.code_msg_ok.replace("xxx", "ingredient")
        self.rep_code_msg_error_400 = rep.code_msg_error_400.replace("xxx", "ingredient")
        self.rep_code_msg_error_404_url = rep.code_msg_error_404.replace("xxx", "cookbook")


api = DeleteIngredient()
