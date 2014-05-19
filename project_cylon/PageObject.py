# -*- coding: utf-8 -*-
import sys
import time

from urlparse import urlparse
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

import selenium.webdriver.support.ui as ui

from Logger import *
from Parser import *


class Element:
    name = ""
    identifier = ""
    driver = None

    def __init__(self, driver, identifier, name='noname'):
        self.driver = driver
        self.name = name
        self.identifier = identifier

    def FindByXPath(self):
        try: return self.driver.find_element_by_xpath(self.identifier)
        except: return None

    def FindById(self):
        try: return self.driver.find_element_by_id(self.identifier)
        except: return None

    def FindByName(self):
        try: return self.driver.find_element_by_name(self.identifier)
        except: return None

    def FindByClassName(self):
        try: return self.driver.find_element_by_class_name(self.identifier)
        except: return None

    def FindByLinkText(self):
        try: return self.driver.find_element_by_link_text(self.identifier)
        except: return None

    def Get(self, logError=True):
        element = None

        ## set wait time to 0 in case not found
        self.driver.implicitly_wait(0)

        if self.name == "noname":
            element = self.FindById()
            if element is None: element = self.FindByName()
            if element is None: element = self.FindByClassName()
            if element is None: element = self.FindByLinkText()
        else:
            element = self.FindByXPath()

        ## set wait time back
        self.driver.implicitly_wait(15)

        if logError and element is None:
            Log.Failed("The element '%s' not found at identifier '%s'" % (self.name, self.identifier))
        return element


    def GetItems(self):
        elements = self.driver.find_elements_by_xpath(self.identifier)
        return elements


    @property
    def Exists(self):
        element = self.Get(False)
        if not element is None:
            return True
        return False

    @property
    def Enabled(self):
        element = self.Get()
        return element.is_enabled()

    @property
    def Visible(self):
        element = self.Get()
        return element.is_displayed()

    @property
    def Selected(self):
        element = self.Get()
        return element.is_selected()

    @property
    def Value(self):
        element = self.Get()
        if element.tag_name in ['input', 'button']:
            return element.get_attribute('value')
        else:
            return element.get_attribute('innerHTML')

    @property
    def Tooltip(self):
        element = self.Get()
        return element.get_attribute('title')

    @property
    def Count(self):
        return len(self.GetItems())


    def SendKeys(self, value):
        element = self.Get()
        element.send_keys(value)
        return True

    def SendKeysByScript(self, value):
        element = self.Get()
        script = "arguments[0].value = '" + value + "'"
        self.driver.execute_script(script, element)
        return True

    def Click(self):
        element = self.Get()
        element.click()
        return True

    def Select(self, value):
        element = Select(self.Get())
        element.select_by_visible_text(value)
        return True

    def MouseOver(self):
        element = self.Get()
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

    ##
    ## !!Verification method will raise error when failed, don't use for condition logic
    ##

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
        actual = Parser.Parse(self.Value)
        expect = Parser.Parse(value)

        if actual > expect:
            return True

        Log.Failed(
            "Verify value is more than?",
            "value = %s" % actual,
            "value > %s" % expect
        )
        return False

    def VerifyValueMoreThanOrEqual(self, value):
        actual = Parser.Parse(self.Value)
        expect = Parser.Parse(value)

        if actual >= expect:
            return True

        Log.Failed(
            "Verify value is more than or equal?",
            "value = %s" % actual,
            "value >= %s" % expect
        )
        return False

    def VerifyValueLessThan(self, value):
        actual = Parser.Parse(self.Value)
        expect = Parser.Parse(value)

        if actual < expect:
            return True

        Log.Failed(
            "Verify value is less than?",
            "value = %s" % actual,
            "value < %s" % expect
        )
        return False

    def VerifyValueLessThanOrEqual(self, value):
        actual = Parser.Parse(self.Value)
        expect = Parser.Parse(value)

        if actual <= expect:
            return True

        Log.Failed(
            "Verify value is less than or equal?",
            "value = %s" % actual,
            "value <= %s" % expect
        )
        return False

    def VerifyValueBetween(self, value1, value2):
        actual = Parser.Parse(self.Value)
        value1 = Parser.Parse(value1)
        value2 = Parser.Parse(value2)

        if (actual >= value1 and actual <= value2) or (actual <= value1 and actual >= value2):
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


class Page:
    name = ""
    url = ""
    driver = None

    elements = {}

    def __init__(self, driver, pageobject, site="default"):
        self.driver = driver
        self.name = pageobject['page']['name']
        self.url = pageobject['page']['url']

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

    def Go(self):
        self.driver.get(self.url)
        return True

    def FindElement(self, name):
        if name in self.elements:
            return self.elements[name]

        #Log.Failed("Element not found", None, name)
        return None

    def VerifyPage(self):
        self.driver.switch_to_window(self.driver.window_handles[-1])

        uri = urlparse(self.url)
        url = uri.scheme + '://' + uri.netloc + uri.path

        if url.lower() in self.driver.current_url.lower():
            return True

        Log.Failed("URL not matched", self.driver.current_url.lower(), url.lower())
        return False
