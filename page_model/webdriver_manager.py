from typing import Type, List

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from page_model.base_model import T


class WebdriverManager(object):

    def __init__(self):
        self.drivers: List[WebDriver] = []

    def __get_webdriver(self, browser, seleniumServer: str):
        driver = webdriver.Remote(seleniumServer, desired_capabilities={"browserName": "chrome"})
        driver.set_page_load_timeout(120e3)
        self.drivers.append(driver)
        return driver

    def get_browser_page_model(self, ctor: Type[T], browser, seleniumServer: str) -> T:
        driver = self.__get_webdriver(browser, seleniumServer)
        return ctor(driver, "html")

    def teardown(self):
        for driver in self.drivers:
            driver.quit()
