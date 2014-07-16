from AlertMock import *
from WebElementMock import *


class WebDriverMock:

    window_handles = []
    current_url = ""

    def __init__(self):
        self.window_handles = [1, 2, 3]
        pass

    def __find_element_by_dummy(self, identifier):
        if identifier == None:
            return None

        element = WebElementMock()
        element.tag_name = identifier

        return element

    def get(self, url):
        pass

    def switch_to_window(self, handle):
        pass

    def find_element_by_id(self, identifier):
        return self.__find_element_by_dummy(identifier)

    def find_element_by_xpath(self, identifier):
        return self.__find_element_by_dummy(identifier)

    def find_elements_by_xpath(self, identifier):
        element1 = WebElementMock()
        element2 = WebElementMock()

        elements = []
        elements.append(element1)
        elements.append(element2)

        return elements

    def execute(self, command, target):
        pass

    def execute_script(self, script, element):
        pass

    def implicitly_wait(self, timeout):
        pass

    def switch_to_alert(self):
        return AlertMock()
