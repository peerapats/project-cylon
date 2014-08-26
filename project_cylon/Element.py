# -*- coding: utf-8 -*-
import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class Element:
    name = ""
    identifier = ""

    driver = None

    def __init__(self, name="!!undefined", identifier="!!undefined"):
        self.name = name
        self.identifier = identifier

    def wait_for_present(self, timeout=8):
        for n in range(0, timeout):
            element = self.get_instance()

            if element is None:
                time.sleep(1)
                continue

        return element

    def wait_for_exist(self, timeout=8):
        for n in range(0, timeout):
            element = self.get_instance()

            if element is not None:
                return True
            time.sleep(1)

        return False

    def wait_for_not_exist(self, timeout=8):
        for n in range(0, timeout):
            element = self.get_instance()

            if element is None:
                return True
            time.sleep(1)

        return False

    def wait_for_visible(self, timeout=8):
        element = self.wait_for_present()

        if element is None:
            return False

        for n in range(0, timeout):
            if element.is_displayed():
                break
            time.sleep(1)

        return element.is_displayed()

    def wait_for_invisible(self, timeout=8):
        result = False
        element = self.wait_for_present()

        if element is None:
            return True

        for n in range(0, timeout):
            if not element.is_displayed():
                break
            time.sleep(1)

        return not element.is_displayed()

    def get_instance(self):
        instance = None
        #self.driver.implicitly_wait(0) ## set wait time to 0 in case not found

        if self.name == "!!undefined":
            if instance is None:
                try: instance = self.driver.find_element_by_id(self.identifier)
                except: pass

            if instance is None:
                try: instance = self.driver.find_element_by_name(self.identifier)
                except: pass

            if instance is None:
                try: instance = self.driver.find_element_by_class_name(self.identifier)
                except: pass

            if instance is None:
                try: instance = self.driver.find_element_by_link_text(self.identifier)
                except: pass
        else:
            try: instance = self.driver.find_element_by_xpath(self.identifier)
            except: pass

        #self.driver.implicitly_wait(15) ## set wait time back
        return instance

    def get_instances(self):
        return self.driver.find_elements_by_xpath(self.identifier)

    @property
    def title(self):
        #element = self.get_instance()
        element = self.wait_for_present()
        return element.get_attribute('title')

    @property
    def value(self):
        #element = self.get_instance()
        element = self.wait_for_present()

        if element is None:
            return ""

        if element.tag_name in ['input', 'button', 'textarea']:
            return element.get_attribute('value')
        elif element.tag_name == 'select':
            return Select(element).first_selected_option.get_attribute('value')
        else:
            return element.get_attribute('innerHTML')

    @property
    def exists(self):
        #element = self.get_instance()
        element = self.wait_for_present()
        if element is None:
            return False
        else:
            return True

    @property
    def enabled(self):
        #element = self.get_instance()
        element = self.wait_for_present()
        if element is None:
            return False
        else:
            return element.is_enabled()

    @property
    def visible(self):
        #element = self.get_instance()
        element = self.wait_for_present()
        if element is None:
            return False
        else:
            return element.is_displayed()

    @property
    def selected(self):
        #element = self.get_instance()
        element = self.wait_for_present()
        if element is None:
            return False
        else:
            return element.is_selected()

    @property
    def count(self):
        return len(self.get_instances())

    def send_keys(self, value):
        #element = self.get_instance()
        element = self.wait_for_present()
        element.send_keys(value)
        return True

    def send_keys_by_script(self, value):
        #element = self.get_instance()
        element = self.wait_for_present()
        script = "arguments[0].value = '" + value + "'"
        self.driver.execute_script(script, element)
        return True

    def click(self):
        #element = self.get_instance()
        element = self.wait_for_present()
        element.click()
        return True

    def select(self, value):
        #element = Select(self.get_instance())
        element = Select(self.wait_for_present())
        element.select_by_visible_text(value)
        return True

    def check(self):
        if not self.selected:
            self.click()
        return True

    def uncheck(self):
        if self.selected:
            self.click()
        return True

    def move_mouse_over(self):
        #element = self.get_instance()
        element = self.wait_for_present()
        action = ActionChains(self.driver).move_to_element(element)
        action.perform()
        return True
