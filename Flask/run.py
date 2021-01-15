""" To launch app """

import sys

from app import backend, utils

if __name__ == "__main__":
    """ check mongo up """
    utils.Mongo().check_mongodb_up()
    """ set backend config """
    options = utils.RunOption().get_options_from_command_line(args=sys.argv)
    backend.config.update(ENV=options["env"], TESTING=options["testing"], DEBUG=options["debug"])
    """ launch server """
    if options["env"] == "development":
        backend.run(host='0.0.0.0', port=5000)
    else:
        from waitress import serve
        serve(backend, host="0.0.0.0", port=5000)
