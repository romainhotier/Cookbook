import validator as validator

validator = validator.Validator()


class Validator(object):

    @staticmethod
    def is_object_id(_id):
        validator.is_object_id(_id)
        return True

    @staticmethod
    def is_result_empty(result_mongo):
        validator.is_result_mongo_empty(result_mongo)
        return False
