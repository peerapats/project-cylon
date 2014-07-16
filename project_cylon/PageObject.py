# -*- coding: utf-8 -*-
import sys
import time

from urlparse import urlparse
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

import selenium.webdriver.support.ui as ui

from Logger import *


class Element:
    name = ""
    identifier = ""
    driver = None

    def __init__(self, driver, identifier, name='noname'):
        self.driver = driver
        self.name = name
        self.identifier = identifier

    def __find_by_xpath(self):
        try: return self.driver.find_element_by_xpath(self.identifier)
        except: return None

    def __find_by_id(self):
        try: return self.driver.find_element_by_id(self.identifier)
        except: return None

    def __find_by_name(self):
        try: return self.driver.find_element_by_name(self.identifier)
        except: return None

    def __find_by_class_name(self):
        try: return self.driver.find_element_by_class_name(self.identifier)
        except: return None

    def __find_by_link_text(self):
        try: return self.driver.find_element_by_link_text(self.identifier)
        except: return None

    def __get_instance(self):
        element = None
        self.driver.implicitly_wait(0) ## set wait time to 0 in case not found

        if self.name == "noname":
            element = self.__find_by_id()
            if element is None: element = self.__find_by_name()
            if element is None: element = self.__find_by_class_name()
            if element is None: element = self.__find_by_link_text()
        else:
            element = self.__find_by_xpath()

        self.driver.implicitly_wait(15) ## set wait time back
        return element

    # def __get_element_value(self, element):
    #     if element.tag_name in ['input', 'button', 'textarea']:
    #         return element.get_attribute('value')
    #     elif element.tag_name == 'select':
    #         return Select(element).first_selected_option.get_attribute('value')
    #     else:
    #         return element.get_attribute('innerHTML')

    def __get_value(self):
        element = self.GetInstance()

        if element.tag_name in ['input', 'button', 'textarea']:
            return element.get_attribute('value')
        elif element.tag_name == 'select':
            return Select(element).first_selected_option.get_attribute('value')
        else:
            return element.get_attribute('innerHTML')

    def GetInstance(self):
        element = self.__get_instance()

        if not element is None:
            return element
        else:
            Log.Failed("The element '%s' not found at identifier '%s'" % (self.name, self.identifier))

        # element = None
        #
        # ## set wait time to 0 in case not found
        # self.driver.implicitly_wait(0)
        #
        # if self.name == "noname":
        #     element = self.__find_by_id()
        #     if element is None: element = self.__find_by_name()
        #     if element is None: element = self.__find_by_class_name()
        #     if element is None: element = self.__find_by_link_text()
        # else:
        #     element = self.__find_by_xpath()
        #
        # ## set wait time back
        # self.driver.implicitly_wait(15)
        #
        # if logError and element is None:
        #     Log.Failed("The element '%s' not found at identifier '%s'" % (self.name, self.identifier))
        # return element


    def GetItems(self):
        elements = self.driver.find_elements_by_xpath(self.identifier)
        return elements

    @property
    def Name(self):
        return self.name

    @property
    def Identifier(self):
        return self.identifier

    @property
    def Exists(self):
        element = self.__get_instance()
        if not element is None:
            return True
        else:
            return False

    @property
    def Enabled(self):
        element = self.GetInstance()
        return element.is_enabled()

    @property
    def Visible(self):
        element = self.GetInstance()
        return element.is_displayed()

    @property
    def Selected(self):
        element = self.GetInstance()
        return element.is_selected()

    @property
    def Value(self):
        return self.__get_value()

    @property
    def TooltipText(self):
        element = self.GetInstance()
        return element.get_attribute('title')

    @property
    def Count(self):
        return len(self.GetItems())


    def SendKeys(self, value):
        element = self.GetInstance()
        element.send_keys(value)
        return True

    def SendKeysByScript(self, value):
        element = self.GetInstance()
        script = "arguments[0].value = '" + value + "'"
        self.driver.execute_script(script, element)
        return True

    def Click(self):
        element = self.GetInstance()
        element.click()
        return True

    def Select(self, value):
        element = Select(self.GetInstance())
        element.select_by_visible_text(value)
        return True

    def MouseOver(self):
        element = self.GetInstance()
        action = ActionChains(self.driver).move_to_element(element)
        action.perform()
        return True

    def Check(self):
        if not self.Selected:
            self.Click()
        return True

    def Uncheck(self):
        if self.Selected:
            self.Click()
        return True

    ###
    ### !!Verification method will raise error when failed, don't use for condition logic
    ### (deprecated in v0.5.0 and will be remove in v1.0.0)
    ###

    def VerifyValueIs(self, value):
        if self.Value == value:
            return True

        Log.Failed("Verify value is?", self.Value, value)
        return False

    def VerifyValueIsNot(self, value):
        if self.Value != value:
            return True

        Log.Failed("Verify value is not?", self.Value, value)
        return False

    def VerifyValueContains(self, value):
        if value in self.Value:
            return True

        Log.Failed("Verify value contains?", self.Value, value)
        return False

    def VerifyValueMoreThan(self, value):
        actual = self.Value
        expect = value

        if actual |more_than| expect:
            return True

        Log.Failed(
            "Verify value is more than?",
            "value = %s" % actual,
            "value > %s" % expect
        )
        return False

    def VerifyValueMoreThanOrEqual(self, value):
        actual = self.Value
        expect = value

        if actual |more_than_or_equal| expect:
            return True

        Log.Failed(
            "Verify value is more than or equal?",
            "value = %s" % actual,
            "value >= %s" % expect
        )
        return False

    def VerifyValueLessThan(self, value):
        actual = self.Value
        expect = value

        if actual |less_than| expect:
            return True

        Log.Failed(
            "Verify value is less than?",
            "value = %s" % actual,
            "value < %s" % expect
        )
        return False

    def VerifyValueLessThanOrEqual(self, value):
        actual = self.Value
        expect = value

        if actual |less_than_or_equal| expect:
            return True

        Log.Failed(
            "Verify value is less than or equal?",
            "value = %s" % actual,
            "value <= %s" % expect
        )
        return False

    def VerifyValueBetween(self, value1, value2):
        actual = self.Value

        if (actual |more_than_or_equal| value1) and (actual |less_than_or_equal| value2):
            return True
        if (actual |less_than_or_equal| value1) and (actual |more_than_or_equal| value2):
            return True

        Log.Failed(
            "Verify value is between?",
            "value = %s" % actual,
            "value is between %s and %s" % (value1, value2)
        )
        return False

    def VerifyValueIsBlank(self):
        if self.Value == '':
            return True

        Log.Failed("Verify value is empty?", self.Value, "<blank>")
        return False

    def VerifyHasValue(self):
        if not self.Value == '':
            return True

        Log.Failed("Verify value is not empty?", self.Value, "<any value>")
        return False

    def VerifyExists(self):
        if self.Exists:
            return True

        Log.Failed("Verify element '%s' exists?" % self.name, "not exists", "exists")
        return False

    def VerifyNotExists(self):
        if not self.Exists:
            return True

        Log.Failed("Verify element '%s' not exists?" % self.name, "exists", "not exists")
        return False

    def VerifyEnabled(self):
        if self.Enabled:
            return True

        Log.Failed("Verify element '%s' enabled?" % self.name, "disabled", "enabled")
        return False

    def VerifyDisabled(self):
        if not self.Enabled:
            return True

        Log.Failed("Verify element '%s' disabled?" % self.name, "enabled", "disabled")
        return False

    def VerifyVisible(self):
        if self.Visible:
            return True

        Log.Failed("Verify element '%s' visible?" % self.name, "not visible", "visible")
        return False

    def VerifyNotVisible(self):
        if not self.Visible:
            return True

        Log.Failed("Verify element '%s' not visible?" % self.name, "visible", "not visible")
        return False

    def VerifyIsChecked(self):
        if self.Selected:
            return True

        Log.Failed("Verify element '%s' checked?" % self.name, "unchecked", "checked")
        return False

    def VerifyIsUnchecked(self):
        if not self.Selected:
            return True

        Log.Failed("Verify element '%s' unchecked?" % self.name, "checked", "unchecked")
        return False

    def VerifyItemsCount(self, count):
        if self.Count == int(count):
            return True

        Log.Failed(
            "Verify amount of '%s' is?" % self.name,
            "amount = %s" % self.Count,
            "amount = %s" % count
        )
        return False

    def VerifyTooltip(self, value):
        if self.Tooltip == value:
            return True

        Log.Failed("Verify tooltip text is?", self.Tooltip, value)
        return False

    # def VerifyValueSortedAscending(self):
    #     unsorted_values = []
    #     elements = self.GetItems()
    #
    #     for element in elements:
    #         unsorted_values.append(self.__get_element_value(element))
    #
    #     sorted_values = natural_sort(unsorted_values)
    #
    #     if unsorted_values == sorted_values:
    #         return True
    #
    #     Log.Failed(
    #         "Verify value sorted ascending?",
    #         "[%s]" % ','.join(unsorted_values),
    #         "[%s]" % ','.join(sorted_values)
    #     )
    #     return False

    # def VerifyValueSortedDescending(self):
    #     return False


class Page:
    name = ""
    url = ""
    url_paths = {}
    driver = None

    elements = {}

    def __init__(self, driver, pageobject, site="default"):
        self.driver = driver
        self.name = pageobject['page']['name']
        self.url = pageobject['page']['url']

        if "url_paths" in pageobject['page']:
            for item in pageobject['page']['url_paths']:
                name = item['name']
                path = item['path']

                if not name in self.url_paths:
                    self.url_paths[name] = path
                else:
                    Log.Warning("%s\nDuplicate url path name: '%s'" % (self.name, name))

        ## load elements
        self.elements = {}

        if "elements" in pageobject:
            for item in pageobject['elements']:
                element = Element(self.driver, item['xpath'], item['name'])

                if not element.name in self.elements:
                    self.elements[element.name] = element
                else:
                    Log.Warning("%s\nDuplicate element name: '%s'" % (self.name, element.name))

        if "site_url" in pageobject and site != "default":
            if site in pageobject['site_url']:
                self.url = pageobject['site_url'][site]
            else:
                Log.Warning("Not found site url '%s' in '%s'" % (site, self.name))


    def __find_element(self, name):
        names = name.split("|")
        for name in names:
            if name in self.elements:
                return self.elements[name]
        return None


    def GetURL(self, pathname=""):
        url = ""

        if pathname == "":
            url = self.url
        elif pathname in self.url_paths:
            domain = self.url
            path = self.url_paths[pathname]

            if domain[-1] == '/': domain = domain[:-1]
            if path[0] == '/': path = path[1:]

            url = domain + '/' + path
        else: Log.Warning("Not found url path '%s' in '%s'" % (pathname, self.name))

        return url


    def Go(self, pathname=""):
        url = self.GetURL(pathname)
        self.driver.get(url)
        return True

    def FindElement(self, name):
        element = self.__find_element(name)
        if element is not None:
            return element
        else:
            Log.Failed("Element not found in list: '%s'" % name)
        # names = name.split("|")
        # for name in names:
        #     if name in self.elements:
        #         return self.elements[name]
        # return None

    def VerifyPage(self, pathname=""):
        return self.WaitForPageLoaded(pathname)

    def WaitForPageLoaded(self, pathname="", timeout=15):
        self.driver.switch_to_window(self.driver.window_handles[-1])

        url = self.GetURL(pathname)

        if "://" in url:
            uri = urlparse(url)
            url = uri.scheme + '://' + uri.hostname + uri.path

        ## wait until browser shows expected url
        wait = ui.WebDriverWait(self.driver, timeout)
        try:
            wait.until(lambda driver : self.driver.current_url.find(url) != -1)
            return True
        except:
            Log.Failed("Page load timeout (%s sec)." % timeout, self.driver.current_url, url)
            return False
