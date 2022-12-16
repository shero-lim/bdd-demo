from typing import Type, List

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from page_model.base_model import T
from utils.browser_options import get_option


class WebdriverManager(object):

    def __init__(self):
        self.drivers: List[WebDriver] = []

    def __get_webdriver(self, browser_name, selenium_server: str):
        options = get_option(browser_name)
        driver = webdriver.Remote(selenium_server, options=options)
        driver.set_page_load_timeout(120e3)
        self.drivers.append(driver)
        return driver

    def get_browser_page_model(self, ctor: Type[T], browser_name, selenium_server: str) -> T:
        driver = self.__get_webdriver(browser_name, selenium_server)
        return ctor(driver, "html")

    def teardown(self):
        for driver in self.drivers:
            driver.quit()
