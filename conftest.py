import pytest

from configs.config import config
from page_model.page_model import PageModel
from page_model.webdriver_manager import WebdriverManager
from selenium import webdriver


def pytest_bdd_before_scenario(request, feature, scenario):
    print(request, feature, scenario)


def pytest_bdd_after_scenario(request, feature, scenario):
    pass


@pytest.fixture()
def browser(request):
    pm = WebdriverManager().get_browser_page_model(PageModel, config["default_browser"], config["selenium_server"])
    # driver = webdriver.Remote(config["selenium_server"], desired_capabilities={"browserName": "chrome"})
    return pm
