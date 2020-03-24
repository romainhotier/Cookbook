import server.server as server

server = server.Server()


class DeleteIngredientRecipe(object):

    def __init__(self):
        self.url = 'link_ingredient_recipe'
        self.param_id = "_id"
        self.rep_code_status = 'codeStatus'
        self.rep_code_msg = 'codeMsg'
        self.rep_data = 'data'
        self.rep_detail = 'detail'
        self.rep_code_msg_ok = server.rep_code_msg_ok.replace("xxx", "link_ingredient_recipe")
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "link_ingredient_recipe")
        self.rep_code_msg_error_404 = server.rep_code_msg_error_404.replace("xxx", "link_ingredient_recipe")
        self.rep_code_msg_error_404_url = server.rep_code_msg_error_404.replace("xxx", "cookbook")
        self.detail_param = "param"
        self.detail_msg = "msg"
        self.detail_value = "value"

    def create_detail(self, param, msg, value):
        detail = {self.detail_param: param, self.detail_msg: msg}
        if value != "missing":
            detail[self.detail_value] = value
        return detail