class Factory(object):

    def __init__(self):
        self.list_param = ["step"]

    def clean_body(self, data):
        cleaned = self.remove_foreign_key(data)
        return cleaned

    def remove_foreign_key(self, data):
        clean_data = {}
        for i, j in data.items():
            if i in self.list_param:
                clean_data[i] = j
        return clean_data
