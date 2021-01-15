from tests import rep


class DeleteFile(object):
    """ Class to test DeleteFile.
    """

    def __init__(self):
        self.url = 'files'
        self.param_path = "path"
        self.rep_code_msg_ok = rep.code_msg_ok.replace("xxx", "files")
        self.rep_code_msg_error_400 = rep.code_msg_error_400.replace("xxx", "files")
        self.rep_code_msg_error_404_url = rep.code_msg_error_404.replace("xxx", "cookbook")


api = DeleteFile()
