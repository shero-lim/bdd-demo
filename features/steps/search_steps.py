from behave import given, when, then
from time import sleep

from retry import retry
from configs.config import config
from page_model.page_model import PageModel


@given("关键词 {keyword}")
def step_impl(context, keyword):
    context.keyword = keyword


@when("打开{url}页面")
def step_impl(context, url):
    context.pm = context.wm.get_browser_page_model(PageModel, "", config["seleniumServer"])
    context.pm.get(url)


@when("输入关键词")
def step_impl(context):
    context.pm.baidu.searchbox.send_keys(context.keyword)


@when("点击搜索按钮")
def step_impl(context):
    context.pm.baidu.search_button.click()


@then("页面标题中应包含关键词")
@retry(tries=10, max_delay=10e3)
def step_impl(context):
    print(context.keyword + " " + context.pm.title)
    assert context.keyword in context.pm.title


@when("不点击搜索按钮")
def step_impl(context):
    pass


@then("页面标题中不包含关键词")
@retry(tries=10, max_delay=10e3)
def step_impl(context):
    assert context.keyword not in context.pm.title
