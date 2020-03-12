import app.recipe.steps.model as steps_model

list_param_step = steps_model.Steps().list_param


class Factory(object):

    def clean_body(self, data):
        cleaned = self.remove_foreign_key(data)
        return cleaned

    @staticmethod
    def remove_foreign_key(data):
        clean_data = {}
        for i, j in data.items():
            if i in list_param_step:
                clean_data[i] = j
        return clean_data
