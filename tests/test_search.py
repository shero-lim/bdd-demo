from pytest_bdd import given, when, then, parsers, scenario, scenarios
from retry import retry

scenarios("../features/search.feature")


@given(parsers.parse("关键词 {keyword}"), target_fixture="keyword")
def set_keyword(keyword):
    return keyword


@when(parsers.parse("打开{url}页面"))
def go_to_url(browser, url):
    browser.get(url)


@when("输入关键词")
def input_username(browser, keyword):
    browser.baidu.searchbox.send_keys(keyword)


@when("点击搜索按钮")
def click_search(browser):
    browser.baidu.search_button.click()


@then("页面标题中应包含关键词")
@retry(tries=10, max_delay=10e3)
def assert_include_keyword(browser, keyword):
    assert keyword in browser.title


@when("不点击搜索按钮")
def not_click_search():
    pass


@then("页面标题中不包含关键词")
@retry(tries=10, max_delay=10e3)
def assert_exclude_keyword(browser, keyword):
    assert keyword not in browser.title
