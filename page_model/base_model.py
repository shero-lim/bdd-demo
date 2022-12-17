from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from utils.find_strategy import find_strategy
from typing import Type, TypeVar

T = TypeVar("T")


class BaseModel(WebElement):
    def __init__(self, driver: WebDriver, selector):
        self.driver = driver
        self.s = self.__find_element_by_selector(selector)

    def __find_element_by_selector(self, selector):
        using, value = find_strategy(selector)
        return self.driver.find_element(using, value)

    @classmethod
    def get_element(cls, self, selector):
        return cls(self.driver, selector)

    def get_custom_element(self, cls: Type[T], selector: str) -> T:
        return cls(self.driver, selector)

    def implicitly_wait(self, time_to_wait: float):
        return self.driver.implicitly_wait(time_to_wait)

    @property
    def current_url(self):
        return self.driver.current_url

    @property
    def title(self):
        return self.driver.title

    def get(self, url: str):
        return self.driver.get(url)

    def send_keys(self, *value):
        return self.s.send_keys(value)

    def click(self):
        return self.s.click()
