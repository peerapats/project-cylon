# -*- coding: utf-8 -*-
import sys
import time

from urlparse import urlparse

from selenium.common.exceptions import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

import selenium.webdriver.support.ui as ui

from Logger import Logger as log


class Page:
    driver = None

    name = ""
    route = ""

    url = ""
    url_paths = {}

    urls = {}
    elements = {}

    def __init__(self, name="!!undefined", url="!!undefined"):
        self.name = name
        self.route = ""

        self.url = url
        self.url_paths = {}

        urls = {}
        self.elements = {}


    def find_element(self, name):
        if name in self.elements:
            element = self.elements[name]
            element.driver = self.driver

            return element
        else:
            return None


    def get_url(self, pathname=""):
        prefix = self.url
        middle = ""
        suffix = ""

        # get domain
        if '::' in self.url:
            prefix = self.url.split('::')[0]
            middle = self.url.split('::')[1]
            prefix = self.urls[prefix]

        # get path
        if pathname != "":
            if pathname in self.url_paths:
                suffix = self.url_paths[pathname]
            else:
                log.warning("Not found url path '%s' in '%s'" % (pathname, self.name))

        return "%s%s%s" % (prefix, middle, suffix)


    def go(self, pathname=""):
        url = self.get_url(pathname)
        try:
            self.driver.get(url)
        except TimeoutException:
            log.failed("Page load timeout (15 sec).")
        return True

    def wait_for_url(self, pathname="", timeout=15):
        self.driver.switch_to_window(self.driver.window_handles[-1])

        url = self.get_url(pathname)

        if "://" in url:
            uri = urlparse(url)
            url = uri.scheme + '://' + uri.hostname + uri.path

        ## wait until browser shows expected url
        wait = ui.WebDriverWait(self.driver, timeout)
        try:
            wait.until(lambda driver : self.driver.current_url.find(url) != -1)
            return True
        except TimeoutException:
            log.failed("Page load timeout (%s sec)." % timeout, self.driver.current_url, url)
            return False
