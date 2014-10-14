# -*- coding: utf-8 -*-
from behave import *

from CustomOperators import *

from Page import *

from World import World as world
from Logger import Logger as log

import re
import time
import datetime


"""
For create combination steps
"""

@step ("user execute following javascript")
def step_impl(context):
    world.driver.execute_script(context.text)


@step ("{execution}, accept fail")
def step_impl(context, execution):
    try:
        context.execute_steps(u"""When %s""" % execution)
    except: pass


@step ("{condition}, {execution}")
def step_impl(context, condition, execution):
    try:
        result = False
        context.execute_steps(u"""When %s""" % condition)
        result = True
    except: pass

    if result == True:
        context.execute_steps(u"""Then %s""" % execution)


"""
Given step definitions
"""

@step ("user repeat following steps '{times}' times")
def step_impl(context, times):
    for index in range(int(times)):
        context.execute_steps(u"""%s""" % context.text)


@step ("user has [{page_name}/{path_name}] page opened") ##->given
def step_impl(context, page_name, path_name):
    page = world.find_page(page_name)
    page.go(path_name)
    page.wait_for_loading()


@step ("user has [{page_name}] page opened") ##->given
@step ("user has [{page_name}] page open")
@step ("user has [{page_name}] open")
def step_impl(context, page_name):
    page = world.find_page(page_name)
    page.go()
    page.wait_for_loading()


@step ("user browse to url '{url}'") ##->given
def step_impl(context, url):
    page = Page()
    page.url = url
    page.driver = world.driver
    page.go()
    page.wait_for_loading()


"""
When step definitions
"""

@step ("user enters '{value}' to the [{element_name}]") ##->when
@step ("user enters '{value}' to [{element_name}]")
def step_impl(context, element_name, value):
    element = world.find_element(element_name)
    if not element.send_keys(value):
        log.failed("Fail to enters value '%s' to '%s'" % (value, element.name))


@step ("user enters following lines to the [{element_name}]")
def step_impl(context, element_name):
    element = world.find_element(element_name)
    element.send_keys(context.text)


@step ("user enters date '{value}' to the [{element_name}]") ##->when
@step ("user enters date '{value}' to [{element_name}]")
def step_impl(context, value, element_name):
    inputdate = value
    today = datetime.date.today()

    if value.lower() == 'today':
        inputdate = "%s 00:00:00" % today
    elif value.lower() == 'tomorrow':
        tomorrow = today + datetime.timedelta(days=1)
        inputdate = "%s 00:00:00" % tomorrow

    element = world.find_element(element_name)
    element.send_keys_by_script(inputdate)


@step ("user enters date next '{value}' days to the [{element_name}]") ##->when
def step_impl(context, value, element_name):
    today = datetime.date.today()

    next_n_days = today + datetime.timedelta(days=int(value))
    inputdate = "%s 00:00:00" % next_n_days

    element = world.find_element(element_name)
    element.send_keys_by_script(inputdate)


@step ("user clears value on the [{element_name}]") ##->when
@step ("user clears input [{element_name}]")
def step_impl(context, element_name):
    element = world.find_element(element_name)
    element.send_keys_by_script("")


@step ("user clicks the [{element_name}] by script") ##->when
def step_impl(context, element_name):
    element = world.find_element(element_name)
    if not element.click_by_script():
        log.failed("Fail to clicks element '%s' by script" % element.name)


@step ("user selects the [{element_name}]") ##->when
@step ("user clicks the [{element_name}]") ##->when
@step ("user clicks [{element_name}] link")
@step ("user clicks [{element_name}] button")
def step_impl(context, element_name):
    element = world.find_element(element_name)
    if not element.click():
        log.failed("Fail to clicks element '%s'" % element.name)


@step ("user selects '{value}' on the [{element_name}]") ##->when
@step ("user selects '{value}' in [{element_name}]")
def step_impl(context, value, element_name):
    element = world.find_element(element_name)
    if not element.select(value):
        log.failed("Fail to selects value '%s' on '%s'" % (value, element.name))


@step ("user checks the [{element_name}]") ##->when
def step_impl(context, element_name):
    element = world.find_element(element_name)
    element.check()


@step ("user unchecks the [{element_name}]") ##->when
def step_impl(context, element_name):
    element = world.find_element(element_name)
    element.uncheck()


@step ("user moves mouse over the [{element_name}]") ##->when
@step ("user moves mouse over [{element_name}]")
def step_impl(context, element_name):
    element = world.find_element(element_name)
    element.move_mouse_over()


@step ("user uploads file '{file_path}' to the [{element_name}]") ##->when
@step ("user uploads file '{file_path}' to [{element_name}]")
def step_impl(context, file_path, element_name):
    element = world.find_element(element_name)
    element.send_keys_by_script(file_path)


@step ("user enters '{value}' to the popup")
def step_impl(context, value):
    alert = world.get_alert()
    alert.send_keys(value)


@step ("user accept the popup")
@step ('user clicks "OK" on the popup')
def step_impl(context):
    alert = world.get_alert_when_exist()

    if alert is not None:
        alert.accept()
    else:
        log.failed("Fail to accept popup alert")


@step ("user cancel the popup")
@step ('user clicks "Cancel" on the popup')
def step_impl(context):
    alert = world.get_alert_when_exist()

    if alert is not None:
        alert.dismiss()
    else:
        log.failed("Fail to cancel popup alert")


@step ("user waits for '{timeout}' seconds")
def step_impl(context, timeout):
    time.sleep(float(timeout))


@step ("user waits [{element_name}] appear for '{timeout}' seconds")
def step_impl(context, element_name, timeout):
    element = world.find_element(element_name)
    element.wait_timeout = int(timeout)

    if not element.wait_for_attribute('visible', True):
        log.failed("Element '%s' not appear in %s seconds" % (element_name, timeout))


@step ("user waits [{element_name}] disappear for '{timeout}' seconds")
def step_impl(context, element_name, timeout):
    element = world.find_element(element_name)
    element.wait_timeout = int(timeout)

    if not element.wait_for_attribute('visible', False):
        log.failed("Element '%s' not disappear in %s seconds" % (element_name, timeout))


"""
Then step definitions
"""

@step ("the browser shows [{page_name}/{path_name}] page") ##->then
def step_impl(context, page_name, path_name):
    page = world.find_page(page_name)
    page.wait_for_loading(path_name)


@step ("the browser shows [{page_name}] page") ##->then
@step ("the system displays [{page_name}]")
def step_impl(context, page_name):
    page = world.find_page(page_name)
    page.wait_for_loading()


@step ("the page url is '{url}'") ##->then
@step ("the system url is '{url}'")
@step ("the system displays '{url}'")
def step_impl(context, url):
    page = Page(url=url)
    page.driver = world.driver
    page.wait_for_loading()

    if url == world.driver.current_url:
        return True
    else:
        log.failed("Verify url is?", world.driver.current_url, url)


@step ("the page url contains '{url}'") ##->then
@step ("the system url contains '{url}'")
def step_impl(context, url):
    page = Page(url=url)
    page.driver = world.driver
    page.wait_for_loading()

    if url in world.driver.current_url:
        return True
    else:
        log.failed("Verify url contains?", world.driver.current_url, url)


@step ("the [{element_name}] value is '{value}'") ##->then
@step ("the [{element_name}] shows '{value}'")
def step_impl(context, element_name, value):
    element = world.find_element(element_name)

    if element.value == value:
        return True
    else:
        log.failed("Verify value is?", element.value, value)


@step ("the [{element_name}] value is") ##->then
def step_impl(context, element_name):
    element = world.find_element(element_name)

    if element.value == context.text:
        return True
    else:
        log.failed("Verify value is? (multi-line)", element.value, context.text)


@step ("the [{element_name}] value is not '{value}'") ##->then
def step_impl(context, element_name, value):
    element = world.find_element(element_name)

    if element.value != value:
        return True
    else:
        log.failed("Verify value is not?", element.value, value)


@step ("the [{element_name}] value contains '{value}'") ##->then
@step ("the [{element_name}] contains '{value}'")
def step_impl(context, element_name, value):
    element = world.find_element(element_name)

    if value in element.value:
        return True
    else:
        log.failed("Verify value contains?", element.value, value)


@step ("the [{element_name}] value contains") ##->then
def step_impl(context, element_name):
    element = world.find_element(element_name)

    if context.text in element.value:
        return True
    else:
        log.failed("Verify value contains? (multi-line)", element.value, value)


@step ("the [{element_name}] value matches pattern '{pattern}'")
def step_impl(context, element_name, pattern):
    element = world.find_element(element_name)
    if re.match(pattern, element.value):
        return True
    else:
        log.failed("Verify value match with pattern?", element.value, pattern)


@step ("the [{element_name}] value is more than '{value}'") ##->then
@step ("the [{element_name}] more than '{value}'")
def step_impl(context, element_name, value):
    element = world.find_element(element_name)

    if element.value |more_than| value:
        return True
    else:
        log.failed(
            "Verify value is more than?",
            "value = %s" % element.value,
            "value > %s" % value
        )


@step ("the [{element_name}] value is more than or equal '{value}'") ##->then
@step ("the [{element_name}] more than or equal '{value}'")
def step_impl(context, element_name, value):
    element = world.find_element(element_name)

    if element.value |more_than_or_equal| value:
        return True
    else:
        log.failed(
            "Verify value is more than or equal?",
            "value = %s" % element.value,
            "value >= %s" % value
        )


@step ("the [{element_name}] value is less than '{value}'") ##->then
@step ("the [{element_name}] less than '{value}'")
def step_impl(context, element_name, value):
    element = world.find_element(element_name)

    if element.value |less_than| value:
        return True
    else:
        log.failed(
            "Verify value is less than?",
            "value = %s" % element.value,
            "value < %s" % value
        )


@step ("the [{element_name}] value is less than or equal '{value}'") ##->then
@step ("the [{element_name}] less than or equal '{value}'")
def step_impl(context, element_name, value):
    element = world.find_element(element_name)

    if element.value |less_than_or_equal| value:
        return True
    else:
        log.failed(
            "Verify value is less than or equal?",
            "value = %s" % element.value,
            "value <= %s" % value
        )


@step ("the [{element_name}] value is between '{value1}' and '{value2}'") ##->then
def step_impl(context, element_name, value1, value2):
    element = world.find_element(element_name)

    if (element.value |more_than_or_equal| value1) and (element.value |less_than_or_equal| value2):
        return True
    elif (element.value |less_than_or_equal| value1) and (element.value |more_than_or_equal| value2):
        return True
    else:
        log.failed(
            "Verify value is between?",
            "value = %s" % element.value,
            "value is between %s and %s" % (value1, value2)
        )


@step ("the [{element_name}] value is empty") ##->then
@step ("the [{element_name}] is blank")
def step_impl(context, element_name):
    element = world.find_element(element_name)

    if element.value == "":
        return True
    else:
        log.failed("Verify value is empty?", element.value, "<blank>")


@step ("the [{element_name}] value is not empty") ##->then
@step ("the [{element_name}] has a value")
def step_impl(context, element_name):
    element = world.find_element(element_name)

    if element.value != "":
        return True
    log.failed("Verify value is not empty?", element.value, "<any value>")


@step ("the [{element_name}] exists") ##->then
def step_impl(context, element_name):
    element = world.find_element(element_name)

    if element.wait_for_exist():
        return True
    else:
        log.failed("Verify element '%s' exists?" % element.name, "not exists", "exists")


@step ("the [{element_name}] does not exist") ##->then
def step_impl(context, element_name):
    element = world.find_element(element_name)

    if element.wait_for_not_exist():
        return True
    else:
        log.failed("Verify element '%s' exists?" % element.name, "not exists", "exists")


@step ("the [{element_name}] is visible") ##->then
def step_impl(context, element_name):
    element = world.find_element(element_name)

    if element.wait_for_attribute('visible', True):
        return True
    else:
        log.failed("Verify element '%s' visible?" % element.name, "not visible", "visible")


@step ("the [{element_name}] is invisible") ##->then
def step_impl(context, element_name):
    element = world.find_element(element_name)

    if element.wait_for_attribute('visible', False):
        return True
    else:
        log.failed("Verify element '%s' not visible?" % element.name, "visible", "not visible")


@step ("the [{element_name}] is enabled") ##->then
def step_impl(context, element_name):
    element = world.find_element(element_name)

    if element.wait_for_attribute('enabled', True):
        return True
    else:
        log.failed("Verify element '%s' enabled?" % element.name, "disabled", "enabled")


@step ("the [{element_name}] is disabled") ##->then
def step_impl(context, element_name):
    element = world.find_element(element_name)

    if element.wait_for_attribute('enabled', False):
        return True
    else:
        log.failed("Verify element '%s' disabled?" % element.name, "enabled", "disabled")


@step ("the [{element_name}] is selected") ##->then
@step ("the [{element_name}] is checked") ##->then
def step_impl(context, element_name):
    element = world.find_element(element_name)

    if element.wait_for_attribute('selected', True):
        return True
    else:
        log.failed("Verify element '%s' checked?" % element.name, "unchecked", "checked")


@step ("the [{element_name}] is not selected") ##->then
@step ("the [{element_name}] is unchecked") ##->then
def step_impl(context, element_name):
    element = world.find_element(element_name)

    if element.wait_for_attribute('selected', False):
        return True
    else:
        log.failed("Verify element '%s' unchecked?" % element.name, "checked", "unchecked")


@step ("the popup message shows '{value}'") ##->then
@step ("the popup shows '{value}'")
def step_impl(context, value):
    alert = world.get_alert_when_exist()

    if alert is None:
        log.failed("The popup alert not visible")

    if alert.text == value:
        return True
    else:
        log.failed("Verify popup message is?", alert.text, value)


@step ("the page has '{amount}' items of [{element_name}]") ##->then
@step ("the system displays '{amount}' items of [{element_name}]")
def step_impl(context, amount, element_name):
    element = world.find_element(element_name)

    if element.count == int(amount):
        return True
    else:
        log.failed(
            "Verify amount of '%s' is?" % element.name,
            "amount = %s" % element.count,
            "amount = %s" % amount
        )


@step ("the [{element_name}] tooltip text is '{value}'") ##->then
@step ("the [{element_name}] tooltip is '{value}'")
def step_impl(context, element_name, value):
    element = world.find_element(element_name)

    if element.get_attribute('title') == value:
        return True
    else:
        log.failed("Verify tooltip text is?", element.title, value)


@step ("the [{element_name}] class contains '{value}'")
def step_impl(context, element_name, value):
    element = world.find_element(element_name)
    classes = element.get_attribute('class')
    if value in classes:
        return True
    else:
        log.failed("Verify class contains?", classes, value)
