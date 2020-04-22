class Factory(object):

    @staticmethod
    def data_information(_id_file, _id_parent):
        return "{0} is now set as main file for {1}".format(str(_id_file), str(_id_parent))
