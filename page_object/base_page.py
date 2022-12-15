from abc import abstractclassmethod

from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver

from utils.find_strategy import find_strategy


class BasePage(object):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @classmethod
    def validate_page(cls):
        return

    def find_element(self, by: str, value):
        self.driver.find_element()
        return self.driver.find_element(by, value)

    def find_element_by_selector(self, selector):
        using, value = find_strategy(selector)
        print(using, value)
        return self.driver.find_element(using, value)

    def get(self, url):
        return self.driver.get(url)

    @property
    def title(self):
        return self.driver.title



