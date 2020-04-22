class Factory(object):

    def __init__(self):
        self.list_param = ["name"]

    def clean_body(self, data):
        clean_body = {}
        for i, j in data.items():
            if i in self.list_param:
                clean_body[i] = j
        return clean_body
