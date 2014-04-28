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
    xpath = ""
    page = None

    def __init__(self, page, element):  
        self.name = element['name']
        self.xpath = element['xpath']
        self.page = page

    def Get(self, logfail=True):
        wait = ui.WebDriverWait(self.page.driver, 3)
        try:
            element = self.page.driver.find_element_by_xpath(self.xpath)
            return element
        except:
            if logfail:
                Log.Failed("Element not found: '%s' at xpath '%s'" % (self.name, self.xpath))
            return None

    def GetItemsCount(self, logfail=True):
        wait = ui.WebDriverWait(self.page.driver, 3)
        elements = self.page.driver.find_elements_by_xpath(self.xpath)
        return len(elements)
        

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
        return self.GetItemsCount()
    

    def SendKeys(self, value):
        element = self.Get()
        element.send_keys(value)
        return True

    def SendKeysByScript(self, value):
        element = self.Get()
        script = "arguments[0].value = '" + value + "'"
        self.page.driver.execute_script(script, element)
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
        action = ActionChains(self.page.driver).move_to_element(element)
        action.perform()
        return True

    ##
    ## !!Verification method will raise error when failed, don't use for condition logic
    ##

    def VerifyValueIs(self, value):
        if self.Value == value:
            return True

        Log.Failed("Value not matched", self.Value, value)
        return False

    def VerifyValueContains(self, value):
        if value in self.Value:
            return True

        Log.Failed("Value not matched", self.Value, value)
        return False

    def VerifyValueMoreThan(self, value):
        if self.Value > value:
            return True

        Log.Failed("Value not matched", self.Value, value)
        return False

    def VerifyValueMoreThanOrEqual(self, value):
        if self.Value >= value:
            return True

        Log.Failed("Value not matched", self.Value, value)
        return False

    def VerifyValueLessThan(self, value):
        if self.Value < value:
            return True

        Log.Failed("Value not matched", self.Value, value)
        return False

    def VerifyValueLessThanOrEqual(self, value):
        if self.Value <= value:
            return True

        Log.Failed("Value not matched", self.Value, value)
        return False

    def VerifyValueIsBlank(self):
        if self.Value == '':
            return True

        Log.Failed("Value not matched", self.Value, "<blank>")
        return False

    def VerifyHasValue(self):
        if not self.Value == '':
            return True

        Log.Failed("Value not matched", self.Value, "<any value>")
        return False

    def VerifyExists(self):
        if self.Exists:
            return True

        Log.Failed("Verify element '%s' exists" % self.name, "Not exists", "Exists")
        return False

    def VerifyNotExists(self):
        if not self.Exists:
            return True

        Log.Failed("Verify element '%s' not exists" % self.name, "Exists", "Not exists")
        return False

    def VerifyEnabled(self):
        if self.Enabled:
            return True

        Log.Failed("Verify element '%s' enabled" % self.name, "Disabled", "Enabled")
        return False

    def VerifyDisabled(self):
        if not self.Enabled:
            return True

        Log.Failed("Verify element '%s' disabled" % self.name, "Enabled", "Disabled")
        return False

    def VerifyVisible(self):
        if self.Visible:
            return True

        Log.Failed("Verify element '%s' visible" % self.name, "Not visible", "Visible")
        return False

    def VerifyNotVisible(self):
        if not self.Visible:
            return True

        Log.Failed("Verify element '%s' not visible" % self.name, "Visible", "Not visible")
        return False

    def VerifyIsChecked(self):
        if self.Selected:
            return True

        Log.Failed("Verify element '%s' checked" % self.name, "Unchecked", "Checked")
        return False

    def VerifyIsUnchecked(self):
        if not self.Selected:
            return True

        Log.Failed("Verify element '%s' unchecked" % self.name, "Checked", "Unchecked")
        return False

    def VerifyAttribute(self, attr, value):
        pass

    def VerifyItemsCount(self, count):
        if self.Count == int(count):
            return True

        Log.Failed("Verify elements count '%s'" % self.name, self.Count, count)
        return False

    def VerifyTooltip(self, value):
        if self.Tooltip == value:
            return True

        Log.Failed("Value not matched", self.Tooltip, value)
        return False


class Page:
    name = ""
    #title = ""
    url = ""
    driver = None

    elements = {}

    def __init__(self, driver, pageobject, site="default"):
        self.driver = driver
        self.name = pageobject['page']['name']
        #self.title = pageobject['page']['title']
        self.url = pageobject['page']['url']
        
        self.elements = {}

        if "elements" in pageobject:
            for object in pageobject['elements']:
                element = Element(self, object)
                
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

        Log.Failed("Element not found", None, name)
        return None

    def VerifyPage(self):
        self.driver.switch_to_window(self.driver.window_handles[-1])

        uri = urlparse(self.url)
        url = uri.scheme + '://' + uri.netloc + uri.path

        ## wait for page load
        wait = ui.WebDriverWait(self.driver, 15)
        try:
            wait.until(lambda driver : self.driver.current_url.lower().find(url.lower()) != -1)
            return True
        except:
            Log.Failed("URL not matched", self.driver.current_url.lower(), url.lower())
            return False

    # def VerifyTitle(self):
    #     if self.title == self.driver.title:
    #         return True

    #     Log.Failed("Title not matched", self.driver.title, self.title)
    #     return False

    @property
    def URL(self):
        return self.url

    