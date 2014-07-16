# -*- coding: utf-8 -*-
import sys
reload(sys); sys.setdefaultencoding('utf-8')

import glob
import yaml

from selenium import webdriver
from selenium.common.exceptions import *

from Logger import *
from Account import *
from PageObject import *


class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Other than that, there are
    no restrictions that apply to the decorated class.

    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.

    Limitations: The decorated class cannot be inherited from.

    """

    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)

@Singleton
class WorldContext:
    driver = None
    pages = {}
    accounts = {}

    current_page = None

    def OpenBrowser(self, browser="firefox"):
        if browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser.lower() == 'chrome':
            self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(15) ## set default wait time

    def CloseBrowser(self):
        for handle in self.driver.window_handles:
            self.driver.switch_to_window(handle)
            self.driver.close()

    def LoadPageObjects(self, path, site="default"):
        self.pages = {}

        for filename in glob.glob(path):
            content = open(filename, "r")
            docs = yaml.load_all(content)

            for doc in docs:
                page = Page(self.driver, doc, site)

                if not page.name in self.pages:
                    self.pages[page.name] = page
                else:
                    Log.Failed("Duplicate page name: '%s'" % page.name)

        return True

    def LoadAccounts(self, filename):
        self.accounts = {}

        content = open(filename, "r")
        doc = yaml.load(content)

        for acc in doc['accounts']:
            name = acc["name"]
            username = acc["username"]
            password = acc["password"]

            account = Account(name, username, password)
            self.accounts[name] = account

        return True


    def FindAccount(self, name):
        if name in self.accounts:
            return self.accounts[name]

        Log.Failed("Account not found in list: '%s'" % name)
        return None

    def FindPage(self, name):
        if name in self.pages:
            self.current_page = self.pages[name]
            return self.pages[name]

        Log.Failed("Page not found in list: '%s'" % name)
        self.current_page = None
        return None


    def FindElement(self, identifier):
        #element = self.CurrentPage.FindElement(identifier)
        element = self.current_page.__find_element(identifier)

        if element is not None:
            return element
        else:
            return Element(self.driver, identifier)


    def CreateDummyPage(self, url):
        pageobject = {}
        pageobject['page'] = {}
        pageobject['page']['name'] = 'noname'
        pageobject['page']['url'] = url

        page = Page(self.driver, pageobject)

        return page


    def VerifyURLIs(self, url):
        page = self.CreateDummyPage(url)
        page.WaitForPageLoaded()

        if url == self.driver.current_url:
            return True

        Log.Failed("Verify url is?", self.driver.current_url, url)
        return False


    def VerifyURLContains(self, url):
        page = self.CreateDummyPage(url)
        page.WaitForPageLoaded()

        if url in self.driver.current_url:
            return True

        Log.Failed("Verify url contains?", self.driver.current_url, url)
        return False


    @property
    def CurrentPage(self):
        return self.current_page

    def AcceptPopup(self):
        self.driver.switch_to_alert().accept()
        return True

    def DismissPopup(self):
        self.driver.switch_to_alert().dismiss()
        return True

    def SendKeysToPopup(self, value):
        self.driver.switch_to_alert().send_keys(value)
        return True

    def GetPopupMessage(self):
        popup = self.driver.switch_to_alert()
        return popup.text

    ## deprecated in v0.5.0
    def VerifyPopupMessage(self, message):
        popup = self.driver.switch_to_alert()
        if popup.text == message:
            return True

        Log.Failed("Verify popup message is?", popup.text, message)
        return False

World = WorldContext.Instance()
