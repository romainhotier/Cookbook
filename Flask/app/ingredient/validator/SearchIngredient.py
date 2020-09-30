import utils


class Validator(object):

    @staticmethod
    def is_string_boolean(with_files):
        if with_files is None:
            return True, False
        else:
            utils.Validator.is_string(param="with_files", value=with_files)
            utils.Validator.is_in(param="with_files", value=with_files, values=["true", "false"])
            if with_files == "true":
                return True, True
            elif with_files == "false":
                return True, False

    @staticmethod
    def is_search_valid(data):
        for i, j in data.items():
            if i in ["name", "slug", "categories"]:
                utils.Validator.is_string_non_empty(param=i, value=j)
        return True
