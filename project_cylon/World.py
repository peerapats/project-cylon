# -*- coding: utf-8 -*-
from selenium import webdriver

from Element import *
from Logger import Logger as log


class World:

    driver = None
    pages = {}
    current_page = None

    @classmethod
    def open_browser(cls, browser="firefox"):
        if browser is "firefox":
            cls.driver = webdriver.Firefox()
        elif browser is "chrome":
            cls.driver = webdriver.Chrome()
        else:
            log.failed("The %s browser is not supported." % browser)

    @classmethod
    def close_browser(cls):
        if cls.driver is not None:
            for handle in cls.driver.window_handles:
                cls.driver.switch_to_window(handle)
                cls.driver.close()

    @classmethod
    def find_page(cls, name):
        if name in cls.pages:
            page = cls.pages[name]
            page.driver = cls.driver

            cls.current_page = page
            return page
        else:
            log.failed("Page not found in list: '%s'" % name)
            cls.current_page = None
            return None

    @classmethod
    def find_element(cls, identifier):
        element = cls.current_page.find_element(identifier)

        if element is not None:
            return element
        else:
            element = Element(identifier=identifier)
            element.driver = cls.driver
            return element

    @classmethod
    def get_alert(cls):
        return cls.driver.switch_to_alert()
