Feature: 搜索

  Scenario Outline: 搜索关键词
    Given 关键词 behave
    When 打开<url>页面
    And  输入关键词
    And  点击搜索按钮
    Then 页面标题中应包含关键词

    Examples: 搜索页面
      | url                   |
      | https://www.baidu.com |