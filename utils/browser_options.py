import json

from selenium import webdriver
from selenium.webdriver.common.options import ArgOptions

from configs.browser import browserConfigurations
from configs.config import config


def get_option(browser_name: str):
    capability = None
    if browserConfigurations.get(browser_name) is None:
        return

    capability = browserConfigurations[browser_name]
    options = None
    key = ""
    if "chrome" in browser_name or "electron" in browser_name:
        options = webdriver.ChromeOptions()
        key = "goog:chromeOptions"
    elif "firefox" in browser_name:
        options = webdriver.FirefoxOptions()
        key = "moz:firefoxOptions"
    elif "msedge" in browser_name:
        options = webdriver.EdgeOptions()
        key = "ms:edgeOptions"
    elif "safari" in browser_name:
        options = ArgOptions()
    else:
        return

    if key and capability.get(key) is not None:
        for k, v in capability[key].items():
            if k == "args":
                for arg in capability[key]["args"]:
                    options.add_argument(arg)
            elif k == "extensions":
                for extension in capability[key]["extension"]:
                    options.add_extension(extension)
            elif k == "prefs" and browser_name == "firefox":
                for pk, pv in capability[key][k].items():
                    options.set_preference(pk, pv)
            else:
                options.add_experimental_option(k, capability[key][k])

    for k, v in capability.items():
        if k == key:
            continue
        else:
            options.set_capability(k, v)

    return options
