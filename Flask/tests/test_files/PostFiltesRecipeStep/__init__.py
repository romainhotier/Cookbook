from tests import rep


class PostFilesRecipeStep(object):
    """ Class to test PostFilesRecipe.
    """

    def __init__(self):
        self.url_1 = 'files/recipe'
        self.url_2 = 'step'
        self.param_id_recipe = "_id_recipe"
        self.param_id_step = "_id_step"
        self.rep_code_msg_created = rep.code_msg_created.replace("xxx", "files")
        self.rep_code_msg_error_400 = rep.code_msg_error_400.replace("xxx", "files")
        self.rep_code_msg_error_404_url = rep.code_msg_error_404.replace("xxx", "cookbook")
        self.rep_code_msg_error_405 = rep.code_msg_error_405.replace("xxx", "cookbook")

    @staticmethod
    def data_expected(files):
        """ Format data's response.

        Parameters
        ----------
        files : list
            FileTest

        Returns
        -------
        str
            Data's response.
        """
        return [f.short_path for f in files]


api = PostFilesRecipeStep()
