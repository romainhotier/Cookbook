import utils

server = utils.Server()


class PutFileIsMain(object):

    def __init__(self):
        self.url = 'file/is_main'
        self.param_id = "_id"
        self.rep_code_msg_ok = server.rep_code_msg_ok.replace("xxx", "file")
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "file")
        self.rep_code_msg_error_404_url = server.rep_code_msg_error_404.replace("xxx", "cookbook")

    @staticmethod
    def create_detail(param, msg, **kwargs):
        detail = {"param": param, "msg": msg}
        if "value" in kwargs:
            detail["value"] = kwargs["value"]
        return detail

    @staticmethod
    def check_not_present(value, rep):
        if value in rep.keys():
            return False
        else:
            return True

    @staticmethod
    def data_expected(_id_file, _id_parent):
        return "{0} is now set as main file for {1}".format(str(_id_file), str(_id_parent))
