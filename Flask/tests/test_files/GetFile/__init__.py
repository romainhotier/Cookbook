from tests import rep


class GetFile(object):
    """ Class to test GetFiles.
    """

    def __init__(self):
        self.url = 'files'
        self.param_path = "path"
        self.rep_code_msg_error_400 = rep.code_msg_error_400.replace("xxx", "files")
        self.rep_code_msg_error_404_url = rep.code_msg_error_404.replace("xxx", "cookbook")
        self.rep_code_msg_error_404_url_files = rep.code_msg_error_404.replace("xxx", "files")


api = GetFile()
