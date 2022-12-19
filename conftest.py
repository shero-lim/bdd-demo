import pytest

from configs.config import config
from page_model.page_model import PageModel
from page_model.webdriver_manager import WebdriverManager
from selenium import webdriver


def pytest_bdd_before_scenario(request, feature, scenario):
    pass


def pytest_bdd_after_scenario(request, feature, scenario):
    pass


@pytest.fixture(scope="function")
def browser(request):
    wm = WebdriverManager()
    pm = wm.get_browser_page_model(PageModel, config["default_browser"], config["selenium_server"])

    def fn():
        print("当用例执行完之后：teardown driver!")
        wm.teardown()

    request.addfinalizer(fn)
    return pm
