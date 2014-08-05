# -*- coding: utf-8 -*-
import sys
import time

from urlparse import urlparse
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

    elements = {}

    #site = ""
    #site_config = {}

    def __init__(self, name="!!undefined", url="!!undefined"):
        self.name = name
        self.route = ""

        self.url = url
        self.url_paths = {}

        self.elements = {}

        #self.site = "default"
        #self.site_config = {}


    # def switch_site(self, site):
    #     if self.site == "default":
    #         return True
    #
    #     if self.site in self.site_config:
    #         self.url = self.site_config[self.site]
    #     else:
    #         log.warning("Not found site config '%s' in '%s'" % (self.site, self.name))


    def find_element(self, name):
        #names = name.split("|")
        #for name in names:
        if name in self.elements:
            element = self.elements[name]
            element.driver = self.driver

            return element
        else:
            return None


    def get_url(self, pathname=""):
        url = ""

        if pathname == "":
            url = self.url
        elif pathname in self.url_paths:
            domain = self.url
            path = self.url_paths[pathname]

            if domain[-1] == '/': domain = domain[:-1]
            if path[0] == '/': path = path[1:]

            url = "%s/%s" % (domain, path)
        else:
            log.warning("Not found url path '%s' in '%s'" % (pathname, self.name))

        return url


    def go(self, pathname=""):
        url = self.get_url(pathname)
        self.driver.get(url)
        return True


    def wait_for_loading(self, pathname="", timeout=15):
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
        except:
            log.failed("Page load timeout (%s sec)." % timeout, self.driver.current_url, url)
            return False
