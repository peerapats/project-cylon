from WebElementMock import *


class WebDriverMock:

    def __init__(self):
        pass

    def __find_element_by_dummy(self, identifier):
        if identifier == None:
            return None

        element = WebElementMock()
        element.tag_name = identifier

        return element

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
