class RunOption(object):

    @staticmethod
    def get_options_from_command_line(args):
        """ Catch command line options.

        Parameters
        ----------
        args: list
            All arguments in the command line.
            1st can be ["test", "dev", "prod"].

        Returns
        -------
        dict
            Set env / debug / testing to update server config.
        """
        try:
            mode = args[1]
            if mode == "test":
                return {"env": "development", "debug": True, "testing": True}
            elif mode == "dev":
                return {"env": "development", "debug": True, "testing": False}
            elif mode == "prod":
                return {"env": "production", "debug": False, "testing": False}
            else:
                return {"env": "production", "debug": False, "testing": False}
        except IndexError:
            return {"env": "production", "debug": False, "testing": False}
