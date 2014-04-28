# -*- coding: utf-8 -*-
import sys
reload(sys); sys.setdefaultencoding('utf-8')

import glob
import yaml

from selenium import webdriver
from selenium.common.exceptions import *

from Logger import *
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

    current_page = None
    
    def OpenBrowser(self, browser="firefox"):
        if browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser.lower() == 'chrome':
            self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(15)

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
    
    def FindPage(self, name):
        if name in self.pages:
            self.current_page = self.pages[name]
            return self.pages[name]

        Log.Failed("Page not found in list: '%s'" % name)
        self.current_page = None
        return None

    # def VerifyURL(self, URL, match_query=False):
    #     self.driver.switch_to_window(self.driver.window_handles[-1])

    #     url = URL

    #     if match_query == False:
    #         uri = urlparse(URL)
    #         url = uri.scheme + '://' + uri.netloc + uri.path

    #     ## wait for page load
    #     wait = ui.WebDriverWait(self.driver, 15)
    #     try:
    #         wait.until(lambda driver : self.driver.current_url.lower().find(url.lower()) != -1)
    #         return True
    #     except:
    #         Log.Failed("URL not matched", self.driver.current_url.lower(), url.lower())
    #         return False

    def VerifyURLIs(self, URL):
        self.driver.switch_to_window(self.driver.window_handles[-1])
        url = URL

        ## wait for page load
        wait = ui.WebDriverWait(self.driver, 15)

        if url.lower() == self.driver.current_url.lower():
            return True

        Log.Failed("URL not matched", self.driver.current_url.lower(), url.lower())
        return False


    def VerifyURLContains(self, URL):
        self.driver.switch_to_window(self.driver.window_handles[-1])
        url = URL

        ## wait for page load
        wait = ui.WebDriverWait(self.driver, 15)

        if url.lower() in self.driver.current_url.lower():
            return True

        Log.Failed("URL not matched", self.driver.current_url.lower(), url.lower())
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

    def VerifyPopupMessage(self, message):
        popup = self.driver.switch_to_alert()
        if popup.text == message:
            return True

        Log.Failed("Value not matched", popup.text, message)
        return False

World = WorldContext.Instance()

