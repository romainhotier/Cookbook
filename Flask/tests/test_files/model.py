import shutil

import utils


class FilesTest(object):

    @staticmethod
    def clean():
        """ Clean FilesTest repository.
        """
        shutil.rmtree(path=utils.Server().path_file_storage+"/", ignore_errors=True)
        return
