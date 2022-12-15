from time import localtime, time
import datetime

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from page_model.webdriver_manager import WebdriverManager
import logging
import asyncio

def before_all(context):
    # concurrency = config["concurrency"]
    # print(concurrency)
    # context.semaphore = asyncio.Semaphore(concurrency)
    pass


def before_scenario(context, scenario):
    # context.semaphore.locked()
    context.wm = WebdriverManager()

def before_step(context, step):
    now = datetime.datetime.now().__str__()

def after_scenario(context, scenario):
    context.wm.teardown()
    # context.semaphore.release()
