# -*- coding: utf-8 -*-

from Element import *
from Logger import Logger as log


class World:

    driver = None
    pages = {}
    current_page = None


    @classmethod
    def find_page(cls, name):
        if name in cls.pages:
            cls.current_page = cls.pages[name]
            return cls.pages[name]

        log.failed("Page not found in list: '%s'" % name)
        cls.current_page = None
        return None

    @classmethod
    def find_element(cls, identifier):
        element = cls.current_page.find_element(identifier)

        if element is not None:
            return element
        else:
            return Element(identifier=identifier)

    @classmethod
    def get_alert(cls):
        return cls.driver.switch_to_alert()
