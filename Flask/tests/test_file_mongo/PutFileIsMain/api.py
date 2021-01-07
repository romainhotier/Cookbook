import utils

server = utils.Server()


class PutFileIsMain(object):
    """ Class to test PutFileIsMain.
    """

    def __init__(self):
        self.url = 'file_mongo/is_main'
        self.param_id = "_id"
        self.rep_code_msg_ok = server.rep_code_msg_ok.replace("xxx", "file_mongo")
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "file_mongo")
        self.rep_code_msg_error_404_url = server.rep_code_msg_error_404.replace("xxx", "cookbook")

    @staticmethod
    def create_detail(param, msg, **kwargs):
        """ Format Server's detail response.

        Parameters
        ----------
        param : str
            Tested parameter.
        msg : str
            Server's message.
        kwargs : str
            Value if one existed.

        Returns
        -------
        dict
            Server's detail response.
        """
        detail = {"param": param, "msg": msg}
        if "value" in kwargs:
            detail["value"] = kwargs["value"]
        return detail

    @staticmethod
    def check_not_present(value, rep):
        """ Check if data/detail is not present in Server's response.

        Parameters
        ----------
        value : str
            Tested value.
        rep : dict
            Server's response.

        Returns
        -------
        bool
        """
        if value in rep.keys():
            return False
        else:
            return True

    @staticmethod
    def data_expected(_id_file, _id_parent):
        """ Format detail's response.

        Parameters
        ----------
        _id_file : str
            File's ObjectId.
        _id_parent : str
            Parent's ObjectId.

        Returns
        -------
        str
            Detail's response.
        """
        return "{0} is now set as main file for {1}".format(str(_id_file), str(_id_parent))
