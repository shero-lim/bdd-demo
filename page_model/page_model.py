from page_model.base_model import BaseModel


class PageModel(BaseModel):
    @property
    def baidu(self):
        return self.get_custom_element(BaiDu, "html")


class BaiDu(BaseModel):
    @property
    def searchbox(self):
        return self.get_element(self, "#kw")

    @property
    def search_button(self):
        return self.get_element(self, "#su")
