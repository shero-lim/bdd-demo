from page_object.base_page import BasePage


class IndexPage(BasePage):

    # def validate_page(self):
    #     return self.driver.title == "百度"
    def validate_page(self):
        return self.title.find("百度搜索")

    @property
    def search_box(self):
        return self.find_element_by_selector("#kw")

    @property
    def search_button(self):
        return self.find_element_by_selector("#su")

    def search_keyword(self, keyword):
        return self.search_box.send_keys(keyword)

    def click_search(self):
        return self.search_button.click()
