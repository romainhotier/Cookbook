class Factory(object):

    def __init__(self):
        self.list_param = ["title", "slug", "level", "resume", "cooking_time", "preparation_time", "nb_people",
                           "note", "steps", "categories"]

    def clean_body(self, data):
        cleaned = self.remove_foreign_key(data)
        filled = self.fill_body_with_missing_key(cleaned)
        return filled

    def remove_foreign_key(self, data):
        clean_data = {}
        for i, j in data.items():
            if i in self.list_param:
                clean_data[i] = j
        return clean_data

    def fill_body_with_missing_key(self, data):
        for key in self.list_param:
            if key not in data.keys():
                if key in ["resume", "note"]:
                    data[key] = ""
                elif key in ["level", "cooking_time", "preparation_time", "nb_people"]:
                    data[key] = 0
                elif key in ["categories", "steps"]:
                    data[key] = []
        return data
