import json
import re

DIRECT_SELECTOR_REGEXP = '^(id|css selector|xpath|link text|partial link text|name|tag name|class name|-android uiautomator|-android datamatcher|-android viewmatcher|-android viewtag|-ios uiautomation|-ios predicate string|-ios class chain|accessibility id):(.+)'
XPATH_SELECTORS_START = [
    '/', '(', '../', './', '*/'
]
IMAGEPATH_MOBILE_SELECTORS_ENDSWITH = [
    '.jpg', '.jpeg', '.gif', '.png', '.bmp', '.svg'
]
DEEP_SELECTOR = '>>>'
ARIA_SELECTOR = 'aria/'
NAME_MOBILE_SELECTORS_START = [
    'uia', 'xcuielementtype', 'android.widget', 'cyi', 'android.view'
]
XPATH_SELECTOR_REGEXP = [
    # HTML tag
    '^([a-z0-9|-]*)',
    # optional . or # + class or id
    '(?:(\.|#)(-?[_a-zA-Z]+[_a-zA-Z0-9-]*))?',
    # optional [attribute-name="attribute-selector"]
    '(?:\[(-?[_a-zA-Z]+[_a-zA-Z0-9-]*)(?:=(?:"|\')([a-zA-z0-9\-_. ]+)(?:"|\'))?\])?',
    # *=query or =query
    '(\*)?=(.+)$',
]


def define_strategy(selector: str):
    if re.match(DIRECT_SELECTOR_REGEXP, selector):
        return 'directly'

    if check_img(IMAGEPATH_MOBILE_SELECTORS_ENDSWITH, selector):
        return '-image'

    if check_xpath(XPATH_SELECTORS_START, selector):
        return 'xpath'

    if selector.startswith('='):
        return 'link text'

    if selector.startswith('*='):
        return 'partial link text'

    if selector.startswith('id='):
        return 'id'

    if selector.startswith(DEEP_SELECTOR):
        return 'shadow'

    if selector.startswith(ARIA_SELECTOR):
        return 'aria'

    if selector.startswith('android='):
        return '-android uiautomator'

    if selector.startswith('ios='):
        return '-ios uiautomation'

    if selector.startswith('~'):
        return 'accessibility id'

    if check_class_name(NAME_MOBILE_SELECTORS_START, selector):
        return 'class name'

    if re.search('<[0-9a-zA-Z-]+(\/)*>', selector) != None:
        return 'tag name'

    if re.search("^\[name=(\"|')([a-zA-z0-9\-_.@=[\] ']+)(\"|')]$", selector) != None:
        return 'name'

    if (selector == '..') | (selector == '.'):
        return 'xpath'

    # if (selector.match(new RegExp(XPATH_SELECTOR_REGEXP.map(rx = > rx.source).join(''))))
    #     return 'xpath extended'

    # if re.match('\[role=[A-Za-z]+]$', selector) != None:
    #     return 'role'


DEFAULT_STRATEGY = 'css selector'


def find_strategy(selector: str, is_mobile=False, is_w3c=True):
    using: str = DEFAULT_STRATEGY
    value = selector
    strategy = define_strategy(selector)
    if strategy == "directly":
        match = re.match(DIRECT_SELECTOR_REGEXP, selector)
        if match == None:
            raise Exception("InvalidSelectorStrategy")
        using = match[1]
        value = match[2]
    elif strategy == "xpath":
        using = 'xpath'
    elif strategy == "id":
        using = 'id'
        value = selector[3:]
    elif strategy == "link text":
        using = 'link text'
        value = selector[1:]
    elif strategy == "partial link tex":
        using = 'partial link text'
        value = selector[2:]
    elif strategy == 'shadow':
        using = 'shadow'
        value = selector[len(DEEP_SELECTOR):]
    elif strategy == "aria":
        label = selector[len(ARIA_SELECTOR):]
        conditions = [
            './/*[@aria-labelledby=(//*[normalize-space()="' + label + '"]/@id)]',
            './/*[@aria-describedby=(//*[normalize-space() = "' + label + '"]/@id)]',
            './/*[@aria-label = "' + label + '"]',
            './/input[@id = (//label[normalize-space() = "' + label + '"]/@for)]',
            './/input[@placeholder="' + label + '"',
            './/input[@aria-placeholder="' + label + '"]',
            './/*[@title="' + label + '"]',
            './/img[@alt="' + label + '"]',
            './/*[normalize-space() = "' + label + '"]'
        ]
        using = 'xpath'
        value = '(' + "|".join(conditions) + ')[1]'
    elif strategy == "-android uiautomator":
        using = '-android uiautomator'
        value = selector[8:]
    elif strategy == "-android datamatcher":
        using = '-android datamatcher'
        value = json.dumps(value)
    elif strategy == "-android viewmatcher":
        using = '-android viewmatcher'
        value = json.dumps(value)
    elif strategy == '-ios uiautomation':
        using = '-ios uiautomation'
        value = selector[4:]
    elif strategy == 'accessibility id':
        using = 'accessibility id'
        value = selector[1:]
    elif strategy == 'class name':
        using = 'class name'
    elif strategy == 'tag name':
        using = 'tag name'
        value = re.sub('<|>|\/|\s', '', selector)
    elif strategy == 'name':
        match = None
        if is_mobile or is_w3c == False:
            match = re.match(selector, "^\[name=(\"|')([a-zA-z0-9\-_.@=[\] ']+)(\"|')]$")
            if match == None:
                raise Exception("InvalidSelectorMatch.Strategy 'name' has failed to match " + selector)
        using = 'name'
        value = match[2]
    elif strategy == '-image':
        using = '-image'
        value = open(selector, encoding='base64').read()
    return using, value


def check_img(img_list, selector: str):
    s = selector.lower()
    for i in img_list:
        if s.endswith(i) & (selector != i):
            return True
    return False


def check_xpath(xpath_list, selector: str):
    for i in xpath_list:
        if selector.startswith(i):
            return True
    return False


def check_class_name(class_name_list, selector: str):
    s = selector.lower()
    for i in class_name_list:
        if s.startswith(i):
            return True
    return False
