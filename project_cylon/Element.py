# -*- coding: utf-8 -*-
import time

from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Element:
    name = ""
    identifier = ""

    driver = None
    wait_timeout = 0

    def __init__(self, name="!!undefined", identifier="!!undefined"):
        self.name = name
        self.identifier = identifier
        self.wait_timeout = 8

    def get_instances(self):
        return self.driver.find_elements_by_xpath(self.identifier)

    def get_instance(self):
        instance = None

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

        return instance

    def get_instance_on_exist(self):
        self.wait_for_exist()
        return self.get_instance()

    def wait_for_exist(self):
        for n in range(0, self.wait_timeout * 2):
            element = self.get_instance()

            if element is not None: return True
            time.sleep(0.5)

        return False

    def wait_for_not_exist(self):
        for n in range(0, self.wait_timeout * 2):
            element = self.get_instance()

            if element is None: return True
            time.sleep(0.5)

        return False

    def wait_for_attribute(self, attr, expected):
        for n in range(0, self.wait_timeout * 2):
            element = self.get_instance()

            if element is not None:
                if attr == 'enabled' and element.is_enabled() == expected:
                    return True
                elif attr == 'visible' and element.is_displayed() == expected:
                    return True
                elif attr == 'selected' and element.is_selected() == expected:
                    return True
                elif element.get_attribute(attr) == expected:
                    return True

            time.sleep(0.5)

        return False

    @property
    def count(self):
        return len(self.get_instances())

    @property
    def title(self):
        element = self.get_instance_on_exist()
        return element.get_attribute('title')

    @property
    def value(self):
        element = self.get_instance_on_exist()

        if element is None: return ""

        if element.tag_name in ['input', 'button', 'textarea']:
            return element.get_attribute('value')
        elif element.tag_name == 'select':
            return Select(element).first_selected_option.get_attribute('innerHTML')
        else:
            return element.get_attribute('innerHTML')

    @property
    def exists(self):
        element = self.get_instance_on_exist()
        if element is None:
            return False
        else:
            return True

    @property
    def enabled(self):
        element = self.get_instance_on_exist()
        if element is None:
            return False
        else:
            return element.is_enabled()

    @property
    def visible(self):
        element = self.get_instance_on_exist()
        if element is None:
            return False
        else:
            return element.is_displayed()

    @property
    def selected(self):
        element = self.get_instance_on_exist()
        if element is None:
            return False
        else:
            return element.is_selected()


    def get_attribute(self, attr):
        element = self.get_instance_on_exist()
        if element is None:
            return ""
        else:
            return element.get_attribute(attr)

    def send_keys(self, value):
        if not self.wait_for_exist():
            return False
        if not self.wait_for_attribute('visible', True):
            return False
        if not self.wait_for_attribute('enabled', True):
            return False

        element = self.get_instance()
        element.send_keys(value)

        return True

    def send_keys_by_script(self, value):
        element = self.get_instance_on_exist()

        if element is None:
            return False

        script = "arguments[0].value = '" + value + "'"
        self.driver.execute_script(script, element)
        return True


    def click(self):
        if not self.wait_for_exist():
            return False
        if not self.wait_for_attribute('visible', True):
            return False
        if not self.wait_for_attribute('enabled', True):
            return False

        element = self.get_instance()
        element.click()

        return True

    def click_by_script(self):
        if not self.wait_for_exist():
            return False
        if not self.wait_for_attribute('visible', True):
            return False
        if not self.wait_for_attribute('enabled', True):
            return False

        element = self.get_instance()
        script = "document.evaluate('%s', document, null, 9, null).singleNodeValue.click();" % self.identifier
        self.driver.execute_script(script, element)

        return True

    def select(self, value):
        if not self.wait_for_exist():
            return False
        if not self.wait_for_attribute('visible', True):
            return False
        if not self.wait_for_attribute('enabled', True):
            return False

        element = Select(self.get_instance())
        element.select_by_visible_text(value)

        return True

    def check(self):
        if not self.selected: self.click()
        return True

    def uncheck(self):
        if self.selected: self.click()
        return True

    def move_mouse_over(self):
        element = self.get_instance_on_exist()
        action = ActionChains(self.driver).move_to_element(element)
        action.perform()
        return True
