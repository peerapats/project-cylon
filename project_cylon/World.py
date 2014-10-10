# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Element import *
from Logger import Logger as log


class World:

    driver = None
    pages = {}
    current_page = None

    @classmethod
    def open_browser(cls, browser="firefox"):
        if browser == "firefox":
            cls.driver = webdriver.Firefox()
        elif browser == "chrome":
            cls.driver = webdriver.Chrome()
        else:
            log.failed("The '%s' browser is not supported." % browser)

        cls.driver.maximize_window()

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
    def find_page_by_url(cls, url):
        for page in cls.pages:
            if url in page.url or page.url in url:
                page.driver = cls.driver
                cls.current_page = page

                log.warning("Current page was changed to: '%s'" % page.name)
                return page

        log.warning("Not found page match with url '%s'" % url)
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

    @classmethod
    def get_alert_when_exist(cls):
        wait = WebDriverWait(cls.driver, 10)

        try:
            wait.until(EC.alert_is_present())
            alert = cls.driver.switch_to_alert()
            return alert
        except:
            return None
